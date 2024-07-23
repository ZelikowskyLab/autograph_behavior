from PySide6 import QtCore
from scipy import stats
from scipy.stats import describe, sem
import math

class Tester(QtCore.QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.dfs = None

    def get_description(self, data):
        try:
            if not data:
                return None
            description = describe(data)._asdict()
            sem_value = sem(data)
            description['sem'] = sem_value
            return description

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during describe: {e}")
            return None

    def ttest(self, grp1, grp2, ttest_type, unique_grp_col_names, measured_col_name, beh_col_name):
        try:            
            # Identify missing values before removing them (used to determine whether or not to do a dep ttest)
            grp1_missing_indexes = [i for i, value in enumerate(grp1) if value is None or math.isnan(value)]
            grp2_missing_indexes = [i for i, value in enumerate(grp2) if value is None or math.isnan(value)]

            # Remove missing values
            grp1 = [value for value in grp1 if (value is not None and not math.isnan(value))]
            grp2 = [value for value in grp2 if (value is not None and not math.isnan(value))]

            # Check if an entire group is missing
            grp1_all_none = all(((value is None or math.isnan(value)) or not grp1) for value in grp1)
            grp2_all_none = all(((value is None or math.isnan(value)) or not grp2) for value in grp2)

            # If both groups are missing, dont perform tests and return nones
            if grp1_all_none and grp2_all_none:
                return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, None, None

            describe1 = self.get_description(grp1)
            describe2 = self.get_description(grp2)
            print(f"grp1: {grp1}\ngrp1 describe: {describe1}")
            print(f"grp2: {grp2}\ngrp2 describe: {describe2}")

            if grp1_all_none:
                return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, None, describe2
            if grp2_all_none:
                return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, describe1, None

            if ttest_type == "Independent T-test":
                t_statistic, p_value = stats.ttest_ind(grp1, grp2)
            elif ttest_type == "Dependent T-test":
                # Proceed with the dependent t-test only if missing indexes of both groups are the same (the same mouse is missing from each group)
                if grp1_missing_indexes == grp2_missing_indexes:
                    t_statistic, p_value = stats.ttest_rel(grp1, grp2)
                else:
                    t_statistic = None
                    p_value = None
            else:
                t_statistic = None
                p_value = None

            return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, t_statistic, p_value, describe1, describe2

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during t-test: {e}")

    def n_way_anova(self, *args):
        pass
