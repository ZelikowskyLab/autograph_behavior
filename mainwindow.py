# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
import os
from datetime import datetime
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

        # These variables will be set by the user input
        # columns can either be one column with many groups/behaviors/durations
        # or many columns with the times under each column
        # time columns only needed if there is only one behavior column
        self.in_path = ""
        self.out_path = ""
        self.grp_cols = []
        self.beh_cols = []
        self.measured_cols = []
        self.valid_formats = ['.csv', '.xlsx']

        # Connect buttons to methods
        self.ui.in_location_button.clicked.connect(self.open_file_dialog)
        self.ui.out_png_location_button.clicked.connect(self.open_file_dialog)
        self.ui.run_button.clicked.connect(self.run)
        self.ui.confirm_col_info_button.clicked.connect(self.assign_column_names)

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
                    self.append_prog_messages("File path saved: " + file_path)
                    self.set_in_path(file_path)
                    self.ui.in_location_label.setText(file_path)
                else:
                    self.append_prog_messages("File type not supported: " + file_path)
        else:
            folder_path = file_dialog.getExistingDirectory(self, "Select Output Folder")
            if folder_path:
                self.set_out_path(folder_path)
                self.ui.out_png_location_label.setText(folder_path)
                self.append_prog_messages("Output path saved: " + folder_path)

    # Checks for valid file format
    def check_file_format(self, file_path):
        ext = os.path.splitext(file_path)[-1].lower()
        return ext in self.valid_formats

    # Assigns column names based on user input
    def assign_column_names(self):
        try:
            grp_cols_input      = self.ui.grp_cols_input.toPlainText()
            beh_cols_input      = self.ui.beh_cols_input.toPlainText()
            measured_cols_input = self.ui.measured_cols_input.toPlainText()

            # Split the comma-separated values
            grp_cols      = [col.strip() for col in      grp_cols_input.split(",") if col.strip()]
            beh_cols      = [col.strip() for col in      beh_cols_input.split(",")  if col.strip()]
            measured_cols = [col.strip() for col in measured_cols_input.split(",") if col.strip()]

            # Assign columns to variables
            self.set_grp_cols(grp_cols)
            self.set_beh_cols(beh_cols)
            self.set_measured_cols(measured_cols)

            self.append_prog_messages("Column numbers assigned successfully.")
        except Exception as e:
            self.append_prog_messages(f"Error assigning column names: {e}")

    # Appends to the program messages text box
    def append_prog_messages(self, message):
        current_datetime = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        self.ui.prog_msgs_text.append(f"[{current_datetime}] {message}")

    # Runs the data cleaner
    def run(self):
        # try:
            in_path = self.get_in_path()
            if in_path:
                self.append_prog_messages("Running...")
                self.cleaner.main(in_path, self.grp_cols, self.beh_cols, self.measured_cols)
            else:
                self.append_prog_messages("No file path selected.")
        # except Exception as e:
        #     self.append_prog_messages(f"Error occurred while running: {e}")

    # Getters
    def get_in_path(self):
        return self.in_path

    def get_out_path(self):
        return self.out_path

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
