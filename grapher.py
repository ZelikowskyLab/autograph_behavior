import io
import random
from PySide6 import QtCore
from PySide6.QtGui import QImage
import matplotlib.pyplot as plt

class Grapher(QtCore.QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def graph_ttest(self, unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, test_type, t_statistic=None, p_value=None, describe1=None, describe2=None):
        try:
            fig, ax = plt.subplots(figsize=(9.6, 9.6))
            plt.subplots_adjust(top=0.9, bottom=0.35)

            # Set title and axis labels
            ax.set_title(beh_col_name, fontsize=18)
            if "Unspecified" in measured_col_name:
                ax.set_ylabel(beh_col_name, fontsize=16)
            else:
                ax.set_ylabel(measured_col_name, fontsize=16)
            ax.yaxis.grid(True)

            # Case where all key data is None, so no bars or points should be plotted
            if t_statistic is None and p_value is None and describe1 is None and describe2 is None:
                ax.set_xticks([])
                ax.set_yticks([])
                text = "All values in both groups were missing or removed.\n\n"
                text += f"{test_type} Results:\nNot performed\n\n"
                text += f"Group {unique_grp_col_names[0]} Describe results:\nNone\n\n"
                text += f"Group {unique_grp_col_names[1]} Describe results:\nNone"
                plt.figtext(0.05, 0.3, text, ha='left', va='top', fontsize=14, wrap=True, bbox=dict(boxstyle="square, pad=0.5", fc="white", ec="black", lw=0))

            else:
                # Set x axis ticks to the group names
                ax.set_xticks(range(len(unique_grp_col_names)))
                ax.set_xticklabels(unique_grp_col_names, fontsize=12)
                ax.tick_params(axis='y', labelsize=12)

                # Plot bars if means are valid, else plot "Invalid data for this group"
                if describe1 and describe2:
                    mean1 = describe1.get('mean')
                    mean2 = describe2.get('mean')
                    sem1 = describe1.get('sem')
                    sem2 = describe2.get('sem')
                elif describe1 is None:
                    mean1 = None
                    sem1 = None
                    mean2 = describe2.get('mean')
                    sem2 = describe2.get('sem')
                elif describe2 is None:
                    mean1 = describe1.get('mean')
                    sem1 = describe1.get('sem')
                    mean2 = None
                    sem2 = None
                else:
                    mean1 = None
                    sem1 = None
                    mean2 = None
                    sem2 = None

                missing_group_text = "Data missing for this group"

                # Plotting logic
                if mean1 and mean2 and grp1 and grp2:
                    all_data = grp1 + grp2
                    min_value = min(all_data)
                    max_value = max(all_data)
                    buffer_range = 0.1 * (max_value - min_value)
                    ax.set_ylim(min_value - buffer_range, max_value + buffer_range)

                    highest_bar_height = max(mean1, mean2)
                    if t_statistic and p_value:
                        ax.text(0.5, highest_bar_height, f"p-value: {p_value:.2f}", ha='center', va='bottom', fontsize=14)
                    else:
                        ax.text(0.5, highest_bar_height, "Invalid data, t-test not performed", ha='center', va='bottom', fontsize=14)

                    x_coords_grp1 = [random.uniform(-0.2, 0.2) for _ in range(len(grp1))]
                    ax.bar(0, mean1, align='center', yerr=sem1, label=unique_grp_col_names[0], capsize=5, color='lightblue')
                    ax.scatter(x_coords_grp1, grp1, color=(0.0, 0.0, 0.5, 0.5), s=100)

                    x_coords_grp2 = [random.uniform(0.8, 1.2) for _ in range(len(grp2))]
                    ax.bar(1, mean2, align='center', yerr=sem2, label=unique_grp_col_names[1], capsize=5, color='lightcoral')
                    ax.scatter(x_coords_grp2, grp2, color='#CD5B45', s=100)

                if not mean1 or not grp1:
                    all_data = grp2
                    min_value = min(all_data)
                    max_value = max(all_data)
                    buffer_range = 0.1 * (max_value - min_value)
                    ax.set_ylim(min_value - buffer_range, max_value + buffer_range)

                    x_coords_grp2 = [random.uniform(0.8, 1.2) for _ in range(len(grp2))]
                    ax.text(0, mean2, missing_group_text, fontsize=14, ha='center', va='center')
                    ax.bar(0, 0, align='center')
                    ax.bar(1, mean2, align='center', yerr=sem2, label=unique_grp_col_names[1], capsize=5, color='lightcoral')
                    ax.scatter(x_coords_grp2, grp2, color='#CD5B45', s=100)

                if not mean2 or not grp2:
                    all_data = grp1
                    min_value = min(all_data)
                    max_value = max(all_data)
                    buffer_range = 0.1 * (max_value - min_value)
                    ax.set_ylim(min_value - buffer_range, max_value + buffer_range)

                    x_coords_grp1 = [random.uniform(-0.2, 0.2) for _ in range(len(grp1))]
                    ax.bar(0, mean1, align='center', yerr=sem1, label=unique_grp_col_names[0], capsize=5, color='lightblue')
                    ax.text(1, mean1, missing_group_text, fontsize=14, ha='center', va='center')
                    ax.bar(1, 0, align='center')
                    ax.scatter(x_coords_grp1, grp1, color=(0.0, 0.0, 0.5, 0.5), s=100)

                # Add text below the plot with T-test results and additional information
                text = f"{test_type} Results:\nT-statistic={t_statistic}, p-value={p_value}\n\n"
                text += f"Group {unique_grp_col_names[0]} Describe results:\n{describe1}\n\n"
                text += f"Group {unique_grp_col_names[1]} Describe results:\n{describe2}"
                plt.figtext(0.05, 0.3, text, ha='left', va='top', fontsize=14, wrap=True, bbox=dict(boxstyle="square, pad=0.5", fc="white", ec="black", lw=0))

            # Convert plot to QImage PNG
            buffer = io.BytesIO()
            fig.savefig(buffer, format='png')
            buffer.seek(0)
            image = QImage()
            image.loadFromData(buffer.getvalue())
            plt.close(fig)
            return image

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during graph_ttest: {e}", message_type='err')
