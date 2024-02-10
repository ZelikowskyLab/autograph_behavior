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
        self._input_file_path = ""
        self._output_file_path = ""
        self._group_columns = []
        self._behavior_columns = []
        self._time_columns = []
        self.valid_formats = ['.csv', '.xlsx']

        # Connect buttons to methods
        self.ui.in_location_button.clicked.connect(self.open_file_dialog)
        self.ui.out_png_location_button.clicked.connect(self.open_file_dialog)
        self.ui.run_button.clicked.connect(self.run_cleaner)

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
                    self.set_input_file_path(file_path)
                    self.ui.in_location_label.setText(file_path)
                else:
                    self.append_prog_messages("File type not supported: " + file_path)
        else:
            folder_path = file_dialog.getExistingDirectory(self, "Select Output Folder")
            if folder_path:
                self.set_output_file_path(folder_path)
                self.ui.out_png_location_label.setText(folder_path)
                self.append_prog_messages("Output path saved: " + folder_path)

    # Checks for valid file format
    def check_file_format(self, file_path):
        ext = os.path.splitext(file_path)[-1].lower()
        return ext in self.valid_formats

    # Appends to the program messages text box
    def append_prog_messages(self, message):
        current_datetime = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        self.ui.prog_msgs_text.append(f"[{current_datetime}] {message}")

    # Runs the data cleaner
    def run_cleaner(self):
        try:
            input_file_path = self.get_input_file_path()
            if input_file_path:
                self.append_prog_messages("Running...")
                self.cleaner.run(input_file_path)
            else:
                self.append_prog_messages("No file path selected.")
        except Exception as e:
            self.append_prog_messages(f"Error occurred while running: {e}")


    # Getters
    def get_input_file_path(self):
        return self._input_file_path

    def get_output_file_path(self):
        return self._output_file_path

    def get_group_columns(self):
        return self._group_columns

    def get_behavior_columns(self):
        return self._behavior_columns

    def get_time_columns(self):
        return self._time_columns

    # Setters
    def set_input_file_path(self, path):
        self._input_file_path = path

    def set_output_file_path(self, path):
        self._output_file_path = path

    def set_group_columns(self, columns):
        self._group_columns = columns

    def set_behavior_columns(self, columns):
        self._behavior_columns = columns

    def set_time_columns(self, columns):
        self._time_columns = columns


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
