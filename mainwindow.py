# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

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

        self.ui.in_location_button.clicked.connect(self.open_input_file_dialog)

        # These variables will be set by the user input
        self._input_file_path = ""
        self._output_file_path = ""
        self._group_columns = []
        self._behavior_columns = []
        self._time_columns = []

    def open_input_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)

        # Display select file dialog
        file_path, _ = file_dialog.getOpenFileName(self, "Select Input File", "", "All Files (*);;CSV Files (*.csv)")

        # If file is selected, update the input file path and the QLabel text
        if file_path:
            self.set_input_file_path(file_path)
            self.ui.in_location_label.setText(file_path)

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

# write all variables to hold params from user entered values
# Other classes will use these values from setter and getter methods
