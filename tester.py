from PyQt6 import QtCore
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
            #     df = pd.DataFrame(data)
            description = describe(data)._asdict()
            sem_value = sem(data)

            #     nobs = len(df)
            #     variance = df.var()
            #     skewness = df.skew()
            #     kurtosis = df.kurtosis()
                # sem = description.sem()
            description['sem'] = sem_value

            # print(description)
            #     # Add additional statistics to the DataFrame
            #     description.loc['nobs'] = nobs
            #     description.loc['variance'] = variance
            #     description.loc['skewness'] = skewness
            #     description.loc['kurtosis'] = kurtosis
                # description.loc['sem'] = sem

            #     # Convert DataFrame to dictionary
            #     describe_dict = description.to_dict()
                # describe_dict = describe_dict[0]

                # return describe_dict
            return description

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during describe: {e}")
            return None

    def ttest(self, grp1, grp2, ttest_type, unique_grp_col_names, measured_col_name, beh_col_name):
        try:
            grp1_all_none = all((value is None or math.isnan(value)) for value in grp1)
            grp2_all_none = all((value is None or math.isnan(value)) for value in grp2)
            grp1_some_none = any((value is not None or math.isnan(value)) for value in grp1) and any((value is None or not math.isnan(value)) for value in grp1)
            grp2_some_none = any((value is not None or math.isnan(value)) for value in grp2) and any((value is None or not math.isnan(value)) for value in grp2)

            # Remove Nones if there are some real values
            if grp1_some_none:
                grp1 = [value for value in grp1 if (value is not None and not math.isnan(value))]
            if grp2_some_none:
                grp2 = [value for value in grp2 if (value is not None and not math.isnan(value))]

            # If any group is all None, return it as is
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
                t_statistic, p_value = stats.ttest_rel(grp1, grp2)
            else:
                t_statistic = None
                p_value = None

            # self.main_window.append_prog_messages(
            #     f"T-Test Results for {measured_col_name} and {beh_col_name}:\n"
            #     f"Group {unique_grp_col_names[0]}: {grp1}\n"
            #     f"Group {unique_grp_col_names[1]}: {grp2}\n"
            #     f"T-Statistic: {t_statistic}\n"
            #     f"P-Value: {p_value}\n"
            #     f"Describe {unique_grp_col_names[0]}: {describe1}\n"
            #     f"Describe {unique_grp_col_names[1]}: {describe2}"
            # )
            return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, t_statistic, p_value, describe1, describe2

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during t-test: {e}")

    def n_way_anova(self, *args):
        pass
