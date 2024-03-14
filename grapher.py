from PyQt6 import QtCore
import matplotlib.pyplot as plt
import numpy as np
import io
from PySide6.QtGui import QImage
import random

class Grapher(QtCore.QObject):
    def __init__(self, main_window):
        self.main_window = main_window

    def graph_ttest(self, unique_grp_col_names, measured_col_name, beh_col_name, grp1, grp2, t_statistic=None, p_value=None, describe1=None, describe2=None):
        try:
            fig, ax = plt.subplots()

            # Set title and axis labels
            ax.set_title(beh_col_name)
            if "Unspecified" in measured_col_name:
                ax.set_ylabel(beh_col_name)
            else:
                ax.set_ylabel(measured_col_name)
            ax.yaxis.grid(True)

            # Set x axis ticks to the group names
            ax.set_xticks(range(len(unique_grp_col_names)))
            ax.set_xticklabels(unique_grp_col_names)

            # Plot bars if means are valid, else plot "No valid data to graph"
            mean1 = describe1.get('mean', None)
            mean2 = describe2.get('mean', None)
            sem1 = describe1.get('sem', None)
            sem2 = describe2.get('sem', None)
            no_data_text = "No valid data to graph"

            # Find min and max values from all_data to set y axis ticks
            if p_value and mean1 and mean2 and grp1 and grp2:
                all_data = grp1 + grp2
                min_value = min(all_data)
                max_value = max(all_data)
                buffer_range = 0.1 * (max_value - min_value) # Buffer so that points aren't cut off
                ax.set_ylim(min_value - buffer_range, max_value + buffer_range)

                # Plot p-value text, mean bars, and individual points
                self.main_window.append_prog_messages("truee")
                highest_bar_height = max(mean1, mean2)
                ax.text(0.5, highest_bar_height, f"p-value: {p_value:.2f}", ha='center', va='bottom', fontsize=12)

                # Individual values
                x_coords_grp1 = [random.uniform(-0.2, 0.2) for _ in range(len(grp1))]
                ax.bar(0, mean1, align='center', yerr=sem1, label=unique_grp_col_names[0], capsize=5)
                ax.scatter(x_coords_grp1, grp1, color='blue', alpha=0.5)  # Scatter plot for grp1

                x_coords_grp2 = [random.uniform(0.8, 1.2) for _ in range(len(grp2))]
                ax.bar(1, mean2, align='center', yerr=sem2, label=unique_grp_col_names[1], capsize=5)
                ax.scatter(x_coords_grp2, grp2, color='orange', alpha=0.5)  # Scatter plot for grp2

            elif not mean1 or not grp1:
                ax.text(0, 0, no_data_text, ha='center', va='center')

            elif not mean2 or not grp2:
                ax.text(1, 0, no_data_text, ha='center', va='center')

            # Add text below the plot with T-test results and additional information
            text = f"T-test Results: T-statistic={t_statistic}, p-value={p_value}\n\n"
            text += f"{unique_grp_col_names[0]} Describe results: {describe1}\n\n"
            text += f"{unique_grp_col_names[1]} Describe results: {describe2}"
            plt.figtext(0.5, 0.1, text, ha='center', va='top', fontsize=10, wrap=True)

            # Convert plot to QImage PNG
            buffer = io.BytesIO()
            fig.savefig(buffer, format='png')
            buffer.seek(0)
            image = QImage()
            image.loadFromData(buffer.getvalue())
            plt.close(fig)

            return image

        except Exception as e:
            self.main_window.append_prog_messages(f"Error occurred during graph_ttest: {e}")
