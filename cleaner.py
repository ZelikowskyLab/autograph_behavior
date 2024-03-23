import os
import pandas as pd
import re
from PyQt6 import QtCore
from tester import Tester
from grapher import Grapher
import datetime
import numpy as np

class Cleaner(QtCore.QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    # Main method
    def main(self, path, mice_cols, grp_cols, beh_cols, measured_cols):
        try:
            # Convert file to df
            df = self.file_to_df(path)
            self.main_window.append_prog_messages("File loaded successfully.")
            self.main_window.update_progress_bar(10)

            # Clean all column entries
            cleaned_mice_cols, cleaned_grp_cols, cleaned_beh_cols, cleaned_measured_cols = self.clean_col_names(df, mice_cols, grp_cols, beh_cols, measured_cols)
            self.main_window.append_prog_messages("Columns cleaned successfully.")
            self.main_window.update_progress_bar(25)

            # Reformat
            self.main_window.cleaned_dfs, mice_col_names, grp_col_names, unique_beh_col_names, self.main_window.measured_col_names = self.reformat(df, cleaned_mice_cols, cleaned_grp_cols, cleaned_beh_cols, cleaned_measured_cols)
            self.main_window.append_prog_messages("Dataframes reformatted succesfully.")
            self.main_window.set_unique_beh_col_names(unique_beh_col_names)
            self.main_window.update_progress_bar(50)

            # Get groups data to run tests on then display graphs
            self.main_window.add_graphs(self.get_grp_data(self.main_window.get_test_type(), self.main_window.get_cleaned_dfs(), mice_col_names, grp_col_names, unique_beh_col_names, self.main_window.measured_col_names))
            self.main_window.append_prog_messages("Tests run succesfully.")
            self.main_window.update_progress_bar(100)

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred while cleaning: {e}")

    # Converts file to DataFrame
    def file_to_df(self, path):
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

            self.main_window.update_progress_bar(5)

            self.main_window.append_prog_messages("Converted file to DataFrame.")
            self.main_window.append_prog_messages(f"DataFrame size: {df.size} elements")
            self.main_window.append_prog_messages(f"DataFrame shape: {df.shape[0]} rows, {df.shape[1]} columns")
            return df

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred while reading file: {e}")
            return None

    # Clean column names
    def clean_col_names(self, df, mice_cols, grp_cols, beh_cols, measured_cols):
        try:
            # Clean each list of columns
            self.main_window.append_prog_messages("Cleaning columns.")
            cleaned_mice_cols     = self.clean_col_list(df, mice_cols)
            cleaned_grp_cols      = self.clean_col_list(df, grp_cols)
            cleaned_beh_cols      = self.clean_col_list(df, beh_cols)
            cleaned_measured_cols = -1 if not measured_cols else self.clean_col_list(df, measured_cols)
            return cleaned_mice_cols, cleaned_grp_cols, cleaned_beh_cols, cleaned_measured_cols

        except Exception as e:
            self.main_window.append_prog_messages(f"Error cleaning column names: {e}")
            return None, None, None

    # Helper method to clean one list of columns
    def clean_col_list(self, df, col_list):
        cleaned_cols = []
        for col in col_list:
            col = col.strip()
            cleaned_cols.extend(self.clean_col_name(df, col))
        return cleaned_cols

    # Helper to match names to regex
    def clean_col_name(self, df, col_name):
        # Range of column names surrounded by "" with - or :
        if re.match(r'^\s*"(.*?)"\s*[-:]\s*"(.*?)"\s*$', col_name):
            start_col = self.get_col_index_from_name(df, re.split(r'[-:]', col_name)[0].strip()[1:-1])
            end_col = self.get_col_index_from_name(df, re.split(r'[-:]', col_name)[1].strip()[1:-1])
            return list(range(start_col, end_col + 1))

        # Number
        if re.match(r'^\s*\d+\s*$', col_name):
            return [int(col_name.strip())]

        # Letter(s)
        if re.match(r'^\s*[a-zA-Z]+\s*$', col_name):
            return [self.alpha_to_num(col_name.strip().lower())]

        # Column name surrounded by ""
        if re.match(r'^\s*"(.*?)"\s*$', col_name):
            return [self.get_col_index_from_name(df, col_name.strip()[1:-1])]

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
    def get_col_index_from_name(self, df, col_name):
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

    # Unstack data
    def reformat(self, df, cleaned_mice_cols, cleaned_grp_cols, cleaned_beh_cols, cleaned_measured_cols):
        try:
            # Convert column indexes to column names
            mice_col_names = [df.columns[i] for i in cleaned_mice_cols]
            grp_col_names = [df.columns[i] for i in cleaned_grp_cols]
            beh_col_names = [df.columns[i] for i in cleaned_beh_cols]
            if cleaned_measured_cols == -1:
                measured_col_names = ["Unspecified"]
            else:
                measured_col_names = [df.columns[i] for i in cleaned_measured_cols]

            # Check if cleaned columns have only one value and are valid
            if len(mice_col_names) == 1 and len(grp_col_names) == 1 and len(beh_col_names) == 1:
                if (0 <= cleaned_mice_cols[0] < df.shape[1]) and (0 <= cleaned_grp_cols[0] < df.shape[1]) and (0 <= cleaned_beh_cols[0] < df.shape[1]):
                    mice_col_name = mice_col_names[0]
                    grp_col_name = grp_col_names[0]
                    beh_col_name = beh_col_names[0]

                    unique_beh_col_names = df[beh_col_name].unique()
                    dfs = []
                    for measured_col_name in measured_col_names:
                        # Create a new DataFrame with unique_beh_col_names as columns
                        new_df = pd.DataFrame(columns=[grp_col_name, mice_col_name] + list(unique_beh_col_names))  # Include grp_col_name and mice_col_name at the front
                        for idx, beh_val in enumerate(df[beh_col_name]):
                            new_df.loc[idx, grp_col_name] = df[grp_col_name][idx]  # Assign grp_col_name value
                            new_df.loc[idx, mice_col_name] = df[mice_col_name][idx]  # Assign mice_col_name value
                            new_df.loc[idx, beh_val] = df[measured_col_name][idx]  # Assign measured values to corresponding behavior columns

                        # Collapse the DataFrame to have only one row for each unique value in mice_col_name
                        new_df = new_df.groupby([grp_col_name, mice_col_name]).first().reset_index()

                        # Fill missing values with 0
                        # pd.set_option('future.no_silent_downcasting', True)
                        # new_df.fillna(0, inplace=True)
                        dfs.append(new_df)

                    # Return array of DataFrames and measured_col_names
                    return dfs, mice_col_names, grp_col_names, unique_beh_col_names, measured_col_names

            # This means that one of the cleaned columns has more than one value (more than one behavior column)
            else:
                dfs = [df]
                return dfs, mice_col_names, grp_col_names, beh_col_names, measured_col_names

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during reformatting: {e}")
            return None, None

    # Method to get groups and perform statistical tests based on the selected test type
    def get_grp_data(self, test_type, cleaned_dfs, mice_col_names, grp_col_names, unique_beh_col_names, measured_col_names):
        try:
            images = []
            if test_type == "Independent T-test":

                percent_increment = 50 / len(cleaned_dfs)
                target_percent = 50 + percent_increment

                for i, df in enumerate(cleaned_dfs):
                    unique_grp_col_names = df[grp_col_names[0]].unique()
                    if len(unique_grp_col_names) == 2:
                        for beh_col_name in unique_beh_col_names:
                            grp1 = df[df[grp_col_names[0]] == unique_grp_col_names[0]][beh_col_name].tolist()
                            grp2 = df[df[grp_col_names[0]] == unique_grp_col_names[1]][beh_col_name].tolist()

                            # Convert value to seconds if it is a datetime.time datatype and is not None.
                            grp1 = [(val.hour * 3600 + val.minute * 60 + val.second + round(val.microsecond / 10**6, 1)) if isinstance(val, datetime.time) and val is not None else val for val in grp1]
                            grp2 = [(val.hour * 3600 + val.minute * 60 + val.second + round(val.microsecond / 10**6, 1)) if isinstance(val, datetime.time) and val is not None else val for val in grp2]

                            # Perform ttests and graph
                            tester = Tester(self.main_window)
                            grapher = Grapher(self.main_window)
                            unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, t_statistic, p_value, describe1, describe2 = tester.ttest(grp1, grp2, test_type, unique_grp_col_names, measured_col_names[i], beh_col_name)
                            image = grapher.graph_ttest(unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, t_statistic, p_value, describe1, describe2)
                            images.append(image)
                    else:
                        self.main_window.append_prog_messages("Error: Wrong number of groups for Independent T-test.")

                    percent_increment += percent_increment
                    self.main_window.update_progress_bar(target_percent)
            else:
                self.main_window.append_prog_messages("Error: Wrong test type.")

            return np.array(images)

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during get_grp_data: {e}")
