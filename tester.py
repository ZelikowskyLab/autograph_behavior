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
            self.main_window.append_prog_messages(f"Error occurred during describe: {e}", message_type='err')
            return None

    def ttest(self, grp1, grp2, ttest_type, mice_IDs, grp_names, unique_grp_col_names, measured_col_name, beh_col_name):
        try:
            if ttest_type == "Independent T-test":
                return self.ind_ttest(grp1, grp2, ttest_type, mice_IDs, grp_names, unique_grp_col_names, measured_col_name, beh_col_name)
            elif ttest_type == "Dependent T-test":
                return self.dep_ttest(grp1, grp2, ttest_type, mice_IDs, grp_names, unique_grp_col_names, measured_col_name, beh_col_name)
            else:
                self.main_window.append_prog_messages(f"Invalid t-test type: {ttest_type}.", message_type='err')
        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during t-test: {e}", message_type='err')

    def ind_ttest(self, grp1, grp2, ttest_type, mice_IDs, grp_names, unique_grp_col_names, measured_col_name, beh_col_name):
        try:
            # Remove missing values
            grp1 = [value for value in grp1 if (value is not None and not math.isnan(value))]
            grp2 = [value for value in grp2 if (value is not None and not math.isnan(value))]

            # Check if an entire group is missing
            grp1_all_none = all((value is None or math.isnan(value)) for value in grp1)
            grp2_all_none = all((value is None or math.isnan(value)) for value in grp2)

            if grp1_all_none and grp2_all_none:
                return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, None, None

            describe1 = self.get_description(grp1)
            describe2 = self.get_description(grp2)

            if grp1_all_none:
                return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, None, describe2
            if grp2_all_none:
                return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, describe1, None

            t_statistic, p_value = stats.ttest_ind(grp1, grp2)
            return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, t_statistic, p_value, describe1, describe2

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during independent t-test: {e}", message_type='err')

    def dep_ttest(self, grp1, grp2, ttest_type, mice_IDs, grp_IDs, unique_grp_col_names, measured_col_name, beh_col_name):
        try:
            # Check if an entire group is missing
            grp1_all_none = all((value is None or math.isnan(value)) for value in grp1)
            grp2_all_none = all((value is None or math.isnan(value)) for value in grp2)

            if self.main_window.is_remove_mice_checked():
                if grp1_all_none and grp2_all_none:
                    return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, None, None

                if grp1_all_none:
                    grp2 = [value for value in grp2 if (value is not None and not math.isnan(value))]
                    describe2 = self.get_description(grp2)
                    return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, None, describe2

                if grp2_all_none:
                    grp1 = [value for value in grp1 if (value is not None and not math.isnan(value))]
                    describe1 = self.get_description(grp1)
                    return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, describe1, None

                filtered_pairs = [(g1, g2) for g1, g2 in zip(grp1, grp2) if g1 is not None and g2 is not None and not math.isnan(g1) and not math.isnan(g2)]
                if filtered_pairs:
                    grp1, grp2 = zip(*filtered_pairs)
                else:
                    return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, None, None

            else:
                grp1_missing_indexes = [i for i, value in enumerate(grp1) if value is None or math.isnan(value)]
                grp2_missing_indexes = [i for i, value in enumerate(grp2) if value is None or math.isnan(value)]

                grp1 = [value for value in grp1 if (value is not None and not math.isnan(value))]
                grp2 = [value for value in grp2 if (value is not None and not math.isnan(value))]

                if grp1_all_none and grp2_all_none:
                    return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, None, None

                describe1 = self.get_description(grp1)
                describe2 = self.get_description(grp2)

                if grp1_all_none:
                    return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, None, describe2
                if grp2_all_none:
                    return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, describe1, None

                if grp1_missing_indexes == grp2_missing_indexes:
                    t_statistic, p_value = stats.ttest_rel(grp1, grp2)
                else:
                    t_statistic = None
                    p_value = None

                return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, t_statistic, p_value, describe1, describe2

            if self.main_window.is_remove_mice_checked():
                grp1_IDs = []
                grp2_IDs = []
                unique_group_IDs = list(set(grp_IDs))
                for idx, grp_ID in enumerate(grp_IDs):
                    if grp_ID == unique_group_IDs[0]:
                        grp1_IDs.append(mice_IDs[idx])
                    else:
                        grp2_IDs.append(mice_IDs[idx])

                common_mice_ids = set(grp1_IDs) & set(grp2_IDs)
                if common_mice_ids:
                    grp1 = [grp1[i] for i in range(len(grp1)) if grp1[i] in common_mice_ids]
                    grp2 = [grp2[i] for i in range(len(grp2)) if grp2[i] in common_mice_ids]

                describe1 = self.get_description(grp1)
                describe2 = self.get_description(grp2)

                t_statistic, p_value = stats.ttest_rel(grp1, grp2)
                return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, t_statistic, p_value, describe1, describe2

            else:
                return unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, None, None, describe1, describe2

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during dependent t-test: {e}", message_type='err')

    def n_way_anova(self, *args):
        pass
