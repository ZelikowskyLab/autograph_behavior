import os
import sys
from datetime import datetime
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from cleaner import Cleaner

# Important:
# You need to run the following command to generate the ui_mainwindow.py file
#     pyside6-uic mainwindow.ui -o ui_mainwindow.py, or
#     pyside2-uic mainwindow.ui -o ui_mainwindow.py
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cleaner = Cleaner(self)

        # Used to save the cleaned dataframes
        self.cleaned_dfs = None
        self.measured_col_name = None

        # These variables will be set by the user input
        self.in_path = ""
        self.out_path = ""
        self.mice_cols = []
        self.grp_cols = []
        self.beh_cols = []
        self.measured_cols = []
        self.valid_formats = ['.csv', '.xlsx']

        # Connect buttons to methods
        self.ui.in_location_button.clicked.connect(self.open_file_dialog)
        self.ui.out_png_location_button.clicked.connect(self.open_file_dialog)
        self.ui.run_button.clicked.connect(self.run)
        self.ui.confirm_col_info_button.clicked.connect(self.assign_column_names)
        self.ui.save_all_dfs.clicked.connect(self.save_all_dfs)

    # Depending on which button is pressed, save file/folder location to variable
    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)

        # Determine which button was pressed
        sender_button = self.sender()

        if sender_button == self.ui.in_location_button:
            file_path, _ = file_dialog.getOpenFileName(self, "Select Input File", "", "All Files (*);;CSV Files (*.csv)")
            if file_path:
                if self.check_file_format(file_path):
                    self.set_in_path(file_path)
                    self.ui.in_location_text.setText(file_path)
                    self.append_prog_messages("Input file selected.")
                else:
                    self.append_prog_messages("Error: Unsupported file format.")
        else:
            folder_path = file_dialog.getExistingDirectory(self, "Select Output Folder")
            if folder_path:
                self.set_out_path(folder_path)
                self.ui.out_png_location_text.setText(folder_path)
                self.append_prog_messages("Output folder selected.")

    # Checks for valid file format
    def check_file_format(self, file_path):
        ext = os.path.splitext(file_path)[-1].lower()
        return ext in self.valid_formats

    # Assigns column names based on user input
    def assign_column_names(self):
        try:
            mice_cols_input     = self.ui.mice_cols_input.toPlainText()
            grp_cols_input      = self.ui.grp_cols_input.toPlainText()
            beh_cols_input      = self.ui.beh_cols_input.toPlainText()
            measured_cols_input = self.ui.measured_cols_input.toPlainText()

            # Split the comma-separated values
            mice_cols     = [col.strip() for col in      mice_cols_input.split(",") if col.strip()]
            grp_cols      = [col.strip() for col in      grp_cols_input.split(",") if col.strip()]
            beh_cols      = [col.strip() for col in      beh_cols_input.split(",")  if col.strip()]
            measured_cols = [col.strip() for col in measured_cols_input.split(",") if col.strip()]

            # Assign columns to variables
            self.set_mice_cols(mice_cols)
            self.set_grp_cols(grp_cols)
            self.set_beh_cols(beh_cols)
            self.set_measured_cols(measured_cols)

            self.append_prog_messages("Column information confirmed.")
        except Exception as e:
            self.append_prog_messages(f"Error: {e}")

    # Appends to the program messages text box
    def append_prog_messages(self, message):
        current_datetime = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        self.ui.prog_msgs_text.append(f"[{current_datetime}] {message}")

    # Runs the data cleaner
    def run(self):
        try:
            in_path = self.get_in_path()
            if in_path:
                if self.mice_cols and self.grp_cols and self.beh_cols and self.measured_cols:
                    self.append_prog_messages("Running...")
                    self.cleaner.main(in_path, self.mice_cols, self.grp_cols, self.beh_cols, self.measured_cols)
                else:
                    self.append_prog_messages("Error: Please enter and confirm all column info.")
            else:
                self.append_prog_messages("Error: No input file selected.")
        except Exception as e:
            self.append_prog_messages(f"Error: {e}")

    # Save cleaned DataFrames to specified directory
    def save_all_dfs(self):
        try:
            if self.cleaned_dfs:
                if self.out_path:
                    output_filename = "_".join(datetime.now().strftime("%m_%d_%Y %H_%M_%S").split()) + "_cleaned_output.xlsx"
                    output_path = os.path.join(self.out_path, output_filename)
                    if os.path.exists(output_path):
                        if not self.overwrite_popup(output_path):
                            return  # Save operation canceled by user
                    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
                        for idx, (reformatted_df, measured_col_name) in enumerate(zip(self.cleaned_dfs, self.measured_col_name)):
                            # Truncate sheet name if greater than or equal to 31 characters
                            if len(measured_col_name) >= 31:
                                measured_col_name = measured_col_name[:31]
                                self.append_prog_messages(f"Sheet name '{measured_col_name}' truncated.")
                            reformatted_df.to_excel(writer, sheet_name=measured_col_name, index=False)
                    self.append_prog_messages("All reformatted DataFrames saved.")
                else:
                    self.append_prog_messages("Error: Please select an output folder.")
            else:
                self.append_prog_messages("Error: No reformatted DataFrames to save.")
        except Exception as e:
            self.append_prog_messages(f"Error: {e}")

    # User confirm overwrite file if already exists
    def overwrite_popup(self, output_path):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText("The file already exists.")
        msg_box.setInformativeText("Do you want to replace it?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)

        result = msg_box.exec()
        if result == QMessageBox.Yes:
            return True  # User wants to overwrite the file
        else:
            self.append_prog_messages("Save operation canceled.")
            return False  # User canceled the save operation

    # Getters
    def get_in_path(self):
        return self.in_path

    def get_out_path(self):
        return self.out_path

    def get_mice_cols(self):
        return self.mice_cols

    def get_grp_cols(self):
        return self.grp_cols

    def get_beh_cols(self):
        return self.beh_cols

    def get_measured_cols(self):
        return self.measured_cols

    # Setters
    def set_in_path(self, path):
        self.in_path = path

    def set_out_path(self, path):
        self.out_path = path

    def set_mice_cols(self, columns):
        self.mice_cols = columns

    def set_grp_cols(self, columns):
        self.grp_cols = columns

    def set_beh_cols(self, columns):
        self.beh_cols = columns

    def set_measured_cols(self, columns):
        self.measured_cols = columns


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
