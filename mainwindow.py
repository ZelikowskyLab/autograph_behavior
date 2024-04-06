import os
import sys
import time
from datetime import datetime
import pandas as pd
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox,
                               QVBoxLayout, QLabel, QWidget, QSizePolicy, QColorDialog)
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
        self.measured_col_names = None
        self.unique_beh_col_names = None

        # These variables will be set by the user input
        self.test_type = ""
        self.in_path = ""
        self.out_path = ""
        self.mice_cols = []
        self.grp_cols = []
        self.beh_cols = []
        self.measured_cols = []

        self.valid_formats = ['.csv', '.xlsx']

        # Names to save images as
        self.graph_names = []
        # Stores the images of all graphs
        self.all_graphs = []

        # Connect ui elements to methods
        self.ui.analysis_type_combo.currentTextChanged.connect(self.update_test_type)
        self.ui.in_location_button.clicked.connect(self.open_file_dialog)
        self.ui.out_png_location_button.clicked.connect(self.open_file_dialog)
        self.ui.run_button.clicked.connect(self.run)
        self.ui.confirm_col_info_button.clicked.connect(self.assign_column_names)
        self.ui.save_all_dfs.clicked.connect(self.save_all_dfs)
        self.ui.save_all_images.clicked.connect(self.save_graphs)
        self.ui.save_one_image.clicked.connect(self.save_graph)
        self.ui.color_options.clicked.connect(self.color_popup)

        self.initialize_tabs()

    def update_progress_bar(self, target_percent):
        if target_percent == 0:
            self.ui.progress_bar.setValue(0);

        else:
            while self.ui.progress_bar.value() < target_percent:
                time.sleep(0.00001)
                self.ui.progress_bar.setValue(self.ui.progress_bar.value() + 1)

    def initialize_tabs(self):
        # Remove all existing tabs
        while self.ui.tabWidget.count() > 0:
            self.ui.tabWidget.removeTab(0)

        initial_tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Graphs will display here after tests run")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        initial_tab.setLayout(layout)
        self.ui.tabWidget.addTab(initial_tab, "")

    def add_graphs(self, images):
           # Remove all existing tabs and clear graph_names
           while self.ui.tabWidget.count() > 0:
               self.ui.tabWidget.removeTab(0)

           self.graph_names.clear()
           self.all_graphs = []

           for measured_idx, measured_name in enumerate(self.measured_col_names):
               for beh_idx, beh_name in enumerate(self.unique_beh_col_names):
                   tab = QWidget()
                   layout = QVBoxLayout()
                   label = QLabel()

                   # Set alignment properties
                   label.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
                   pixmap = QPixmap.fromImage(images[measured_idx * len(self.unique_beh_col_names) + beh_idx])

                   # Scale pixmap to fit label
                   pixmap = pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                   label.setPixmap(pixmap)
                   label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                   layout.addWidget(label)
                   tab.setLayout(layout)
                   tab_name = f"{measured_name}_{beh_name}"
                   self.ui.tabWidget.addTab(tab, tab_name)

                   self.graph_names.append(tab_name)
                   self.all_graphs.append(pixmap)

    # Save the graph corresponding to the currently focused tab
    def save_graph(self):
        if not self.all_graphs:
            self.append_prog_messages("Error: No graphs to save.")
            return

        if not self.out_path:
            self.append_prog_messages("Error: Please select an output folder.")
            return

        try:
            current_tab_index = self.ui.tabWidget.currentIndex()

            if current_tab_index is not None:
                image = self.all_graphs[current_tab_index]
                graph_name = self.graph_names[current_tab_index]
                image_path = os.path.join(self.out_path, f"{graph_name}.png")
                self.update_progress_bar(50)
                if os.path.exists(image_path):
                    if not self.overwrite_popup(image_path):
                        return
                    else:
                        image.save(image_path, "PNG")
                else:
                    image.save(image_path, "PNG")
            else:
                self.append_prog_messages("Error: No tab selected.")
            self.append_prog_messages(f"Graph '{graph_name}' saved.")

            self.update_progress_bar(100)
            self.update_progress_bar(0)
        except Exception as e:
            self.append_prog_messages(f"Error: {e}")

    # Save all images from all_graphs to out_path
    def save_graphs(self):
        if not self.all_graphs:
            self.append_prog_messages("Error: No graphs to save.")
            return

        if not self.out_path:
            self.append_prog_messages("Error: Please select an output folder.")
            return

        try:
            for idx, (image, graph_name) in enumerate(zip(self.all_graphs, self.graph_names)):
                image_path = os.path.join(self.out_path, f"{graph_name}.png")
                self.update_progress_bar(50)
                if os.path.exists(image_path):
                    if not self.overwrite_popup(image_path):
                        continue
                    else:
                        image.save(image_path, "PNG")

                else:
                    image.save(image_path, "PNG")

            self.append_prog_messages("Graphs saved.")
            self.update_progress_bar(100)
            self.update_progress_bar(0)

        except Exception as e:
            self.append_prog_messages(f"Error: {e}")

    def color_popup(self):
        color_dialog = QColorDialog(self)


    # Update the statistical analysis type
    def update_test_type(self, text):
        self.set_test_type(text)
        self.append_prog_messages(f"Test type updated: {text}")
        self.update_progress_bar(100)
        self.update_progress_bar(0)

    # Depending on which button is pressed, save file/folder location to variable
    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)

        # Determine which button was pressed
        sender_button = self.sender()

        # Select input path
        if sender_button == self.ui.in_location_button:
            self.update_progress_bar(50)
            file_path, _ = file_dialog.getOpenFileName(self, "Select Input File", "", "All Files (*);;CSV Files (*.csv)")
            if file_path:
                if self.check_file_format(file_path):
                    self.set_in_path(file_path)
                    self.ui.in_location_text.setText(file_path)
                    self.append_prog_messages("Input file selected.")
                    self.update_progress_bar(100)
                else:
                    self.append_prog_messages("Error: Unsupported file format.")

        # Select output path
        else:
            self.update_progress_bar(50)
            folder_path = file_dialog.getExistingDirectory(self, "Select Output Folder")
            if folder_path:
                self.set_out_path(folder_path)
                self.ui.out_png_location_text.setText(folder_path)
                self.append_prog_messages("Output folder selected.")
                self.update_progress_bar(100)

        self.update_progress_bar(0)

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
            self.update_progress_bar(50)

            # Assign columns to variables
            self.set_mice_cols(mice_cols)
            self.set_grp_cols(grp_cols)
            self.set_beh_cols(beh_cols)
            self.set_measured_cols(measured_cols)

            self.append_prog_messages("Column information confirmed.")
            self.update_progress_bar(100)
            self.update_progress_bar(0)
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
                if self.test_type and self.test_type != "Choose Test Type":
                    if self.mice_cols and self.grp_cols and self.beh_cols:
                        self.cleaner.main(in_path, self.mice_cols, self.grp_cols, self.beh_cols, self.measured_cols)
                    else:
                        self.append_prog_messages("Error: Please enter and confirm all column info.")
                else:
                    self.append_prog_messages("Error: Please choose a test type to perform.")
            else:
                self.append_prog_messages("Error: No input file selected.")
            self.update_progress_bar(0)
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
                        self.update_progress_bar(50)
                        for idx, (reformatted_df, measured_col_name) in enumerate(zip(self.cleaned_dfs, self.measured_col_names)):
                            # Truncate sheet name if greater than or equal to 31 characters
                            if len(measured_col_name) >= 31:
                                measured_col_name = measured_col_name[:31]
                                self.append_prog_messages(f"Sheet name '{measured_col_name}' truncated.")
                            reformatted_df.to_excel(writer, sheet_name=measured_col_name, index=False)
                    self.append_prog_messages("All reformatted DataFrames saved.")
                    self.update_progress_bar(100)
                    self.update_progress_bar(0)
                else:
                    self.append_prog_messages("Error: Please select an output folder.")
                    self.update_progress_bar(0)
            else:
                self.append_prog_messages("Error: No reformatted DataFrames to save.")
                self.update_progress_bar(0)
        except Exception as e:
            self.append_prog_messages(f"Error: {e}")

    # User confirm overwrite file if already exists
    def overwrite_popup(self, output_path):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText(f"The file {output_path} already exists.")
        msg_box.setInformativeText("Do you want to replace it?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)

        result = msg_box.exec()
        if result == QMessageBox.Yes:
            self.append_prog_messages(f"File {output_path} overwritten")
            return True  # User wants to overwrite the file
        else:
            self.append_prog_messages("Save operation canceled.")
            return False  # User canceled the save operation

    # Getters
    def get_cleaned_dfs(self):
        return self.cleaned_dfs

    def get_measured_col_names(self):
        return self.measured_col_names

    def get_unique_beh_col_names(self):
        return self.unique_beh_col_names

    def get_test_type(self):
        return self.test_type

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
    def set_cleaned_dfs(self, cleaned_dfs):
        self.cleaned_dfs = cleaned_dfs

    def set_measured_col_names(self, measured_col_names):
        self.measured_col_names = measured_col_names

    def set_unique_beh_col_names(self, unique_beh_col_names):
        self.unique_beh_col_names = unique_beh_col_names

    def set_test_type(self, test_type):
        self.test_type = test_type

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
