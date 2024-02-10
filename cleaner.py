# This Python file uses the following encoding: utf-8
from PyQt6 import QtCore
from PyQt6 import QtWidgets
import pandas as pd
import os

class Cleaner(QtCore.QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    # Main run method
    def run(self, file_path):
        df = self.csv_to_df(file_path)
        if df is not None:
            print(df)

    # Converts file to DataFrame
    def csv_to_df(self, file_path):
        self.main_window.append_prog_messages("Converting file to DataFrame...")
        try:
            _, file_extension = os.path.splitext(file_path)
            if file_extension.lower() == '.csv':
                df = pd.read_csv(file_path)
            elif file_extension.lower() == '.xlsx':
                df = pd.read_excel(file_path)
            else:
                self.main_window.append_prog_messages("Unsupported file format.")
                return None

            self.main_window.append_prog_messages("Converted file to DataFrame.")
            self.main_window.append_prog_messages(f"DataFrame size: {df.size} elements")
            self.main_window.append_prog_messages(f"DataFrame shape: {df.shape}")
            return df
        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred while reading file: {e}")
            return None

