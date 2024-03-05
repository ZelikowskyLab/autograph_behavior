from PyQt6 import QtCore
from scipy import stats
import pandas as pd

class Tester(QtCore.QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.dfs = None

    def describe(self, data):
        try:
            data_df = pd.DataFrame(data)
            description = data_df.describe()
            nobs = len(data_df)
            variance = data_df.var()
            skewness = data_df.skew()
            kurtosis = data_df.kurtosis()

            description.loc['nobs'] = nobs
            description.loc['variance'] = variance
            description.loc['skewness'] = skewness
            description.loc['kurtosis'] = kurtosis

            return description
        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during describe: {e}")
            return None

    def ttest(self, grp1, grp2, ttest_type, measured_col_name, beh_col_name):
        try:
            description1 = self.describe(grp1)
            description2 = self.describe(grp2)
            overall_description = f"Measured Column: {measured_col_name}\nBehavior Column: {beh_col_name}\n\n"
            overall_description += f"Group 1 Description:\n{description1}\n\n"
            overall_description += f"Group 2 Description:\n{description2}\n\n"

            if ttest_type == "Independent T-test":
                t_statistic, p_value = stats.ttest_ind(grp1, grp2)
                overall_description += f"Independent T-test: t_statistic = {t_statistic}, p_value = {p_value}"
            elif ttest_type == "Dependent T-test":
                t_statistic, p_value = stats.ttest_rel(grp1, grp2)
                overall_description += f"Dependent T-test: t_statistic = {t_statistic}, p_value = {p_value}"
            else:
                overall_description += "Error: Invalid t-test type."

            self.main_window.append_prog_messages(overall_description)

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during t-test: {e}")

    def n_way_anova(self, *args):
        pass
