# This Python file uses the following encoding: utf-8
import os
import re
from PyQt6 import QtCore, QtWidgets
import pandas as pd

class Cleaner(QtCore.QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    # Main method
    def main(self, path, mice_cols, grp_cols, beh_cols, measured_cols):
        df = self.csv_to_df(path)
        if df is not None:
            self.main_window.append_prog_messages(str(df))

            cleaned_mice_cols, cleaned_grp_cols, cleaned_beh_cols, cleaned_measured_cols = self.clean_col_names(mice_cols, grp_cols, beh_cols, measured_cols, df)
            if cleaned_mice_cols is not None and cleaned_grp_cols is not None and cleaned_beh_cols is not None and cleaned_measured_cols is not None:
                self.main_window.append_prog_messages("Cleaned MiceID Columns: {}".format(cleaned_mice_cols))
                self.main_window.append_prog_messages("Cleaned Group Columns: {}".format(cleaned_grp_cols))
                self.main_window.append_prog_messages("Cleaned Behavior Columns: {}".format(cleaned_beh_cols))
                self.main_window.append_prog_messages("Cleaned Measured Columns: {}".format(cleaned_measured_cols))
            else:
                self.main_window.append_prog_messages("Error occurred while cleaning column names.")

    # Converts file to DataFrame
    def csv_to_df(self, path):
        self.main_window.append_prog_messages("Converting file to DataFrame...")
        try:
            _, file_extension = os.path.splitext(path)
            if file_extension.lower() == '.csv':
                df = pd.read_csv(path)
            elif file_extension.lower() == '.xlsx':
                df = pd.read_excel(path)
            else:
                self.main_window.append_prog_messages("Unsupported file format.")
                return None

            self.main_window.append_prog_messages("Converted file to DataFrame.")
            self.main_window.append_prog_messages(f"DataFrame size: {df.size} elements")
            self.main_window.append_prog_messages(f"DataFrame shape: {df.shape[0]} rows, {df.shape[1]} columns")
            return df

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred while reading file: {e}")
            return None

    # Clean column names
    def clean_col_names(self, mice_cols, grp_cols, beh_cols, measured_cols, df):
        try:
            # Clean each list of columns
            self.main_window.append_prog_messages("Cleaning columns.")
            cleaned_mice_cols     = self.clean_col_list(mice_cols, df)
            cleaned_grp_cols      = self.clean_col_list(grp_cols, df)
            cleaned_beh_cols      = self.clean_col_list(beh_cols, df)
            cleaned_measured_cols = self.clean_col_list(measured_cols, df)
            return cleaned_mice_cols, cleaned_grp_cols, cleaned_beh_cols, cleaned_measured_cols

        except Exception as e:
            self.main_window.append_prog_messages(f"Error cleaning column names: {e}")
            return None, None, None

    # Helper method to clean one list of columns
    def clean_col_list(self, col_list, df):
        cleaned_cols = []
        for col in col_list:
            col = col.strip()
            cleaned_cols.extend(self.clean_col_name(col, df))
        return cleaned_cols

    # Helper to match names to regex
    def clean_col_name(self, col_name, df):
        # Range of column names surrounded by "" with - or :
        if re.match(r'^\s*"(.*?)"\s*[-:]\s*"(.*?)"\s*$', col_name):
            start_col = self.get_col_index_from_name(re.split(r'[-:]', col_name)[0].strip()[1:-1], df)
            end_col = self.get_col_index_from_name(re.split(r'[-:]', col_name)[1].strip()[1:-1], df)
            return list(range(start_col, end_col + 1))

        # Number
        if re.match(r'^\s*\d+\s*$', col_name):
            return [int(col_name.strip())]

        # Letter(s)
        if re.match(r'^\s*[a-zA-Z]+\s*$', col_name):
            return [self.alpha_to_num(col_name.strip().lower())]

        # Column name surrounded by ""
        if re.match(r'^\s*"(.*?)"\s*$', col_name):
            return [self.get_col_index_from_name(col_name.strip()[1:-1], df)]

        # Range of numbers with - or :
        if re.match(r'^\s*(\d+)\s*[-:]\s*(\d+)\s*$', col_name):
            start, end = map(int, re.split(r'[-:]', col_name.strip()))
            return list(range(start, end + 1))

        # Range of letters with - or :
        if re.match(r'^\s*([a-zA-Z]+)\s*[-:]\s*([a-zA-Z]+)\s*$', col_name):
            start, end = map(self.alpha_to_num, re.split(r'[-:]', col_name.strip().lower()))
            return list(range(start, end + 1))

        return []

    # Helper method to get column index based on the column name
    def get_col_index_from_name(self, col_name, df):
        try:
            col_index = list(df.columns).index(col_name)
            return col_index

        except ValueError:
            self.main_window.append_prog_messages(f"Column '{col_name}' not found.")
            return []

    # Convert alphabetic characters to numeric value (0-based)
    def alpha_to_num(self, alpha):
        num = 0
        for char in alpha:
            num = num * 26 + (ord(char) - ord('a')) + 1
        return num - 1
