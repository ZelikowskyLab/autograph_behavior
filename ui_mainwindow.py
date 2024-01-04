# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1027, 829)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 415, 343))
        self.input_params = QGridLayout(self.gridLayoutWidget)
        self.input_params.setObjectName(u"input_params")
        self.input_params.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.input_params.setHorizontalSpacing(5)
        self.input_params.setContentsMargins(0, 0, 0, 0)
        self.num_ind_vars = QLabel(self.gridLayoutWidget)
        self.num_ind_vars.setObjectName(u"num_ind_vars")

        self.input_params.addWidget(self.num_ind_vars, 3, 0, 1, 1)

        self.in_format = QLabel(self.gridLayoutWidget)
        self.in_format.setObjectName(u"in_format")

        self.input_params.addWidget(self.in_format, 6, 0, 1, 1)

        self.in_location_button = QPushButton(self.gridLayoutWidget)
        self.in_location_button.setObjectName(u"in_location_button")

        self.input_params.addWidget(self.in_location_button, 5, 0, 1, 1)

        self.num_groups = QLabel(self.gridLayoutWidget)
        self.num_groups.setObjectName(u"num_groups")

        self.input_params.addWidget(self.num_groups, 1, 0, 1, 1)

        self.grp_names_text = QPlainTextEdit(self.gridLayoutWidget)
        self.grp_names_text.setObjectName(u"grp_names_text")

        self.input_params.addWidget(self.grp_names_text, 2, 1, 1, 1)

        self.in_location = QLabel(self.gridLayoutWidget)
        self.in_location.setObjectName(u"in_location")

        self.input_params.addWidget(self.in_location, 5, 1, 1, 1)

        self.analysis_type_combo_2 = QComboBox(self.gridLayoutWidget)
        self.analysis_type_combo_2.addItem("")
        self.analysis_type_combo_2.addItem("")
        self.analysis_type_combo_2.addItem("")
        self.analysis_type_combo_2.setObjectName(u"analysis_type_combo_2")

        self.input_params.addWidget(self.analysis_type_combo_2, 6, 1, 1, 1)

        self.ind_var_names_text = QPlainTextEdit(self.gridLayoutWidget)
        self.ind_var_names_text.setObjectName(u"ind_var_names_text")

        self.input_params.addWidget(self.ind_var_names_text, 4, 1, 1, 1)

        self.ind_var_names = QLabel(self.gridLayoutWidget)
        self.ind_var_names.setObjectName(u"ind_var_names")

        self.input_params.addWidget(self.ind_var_names, 4, 0, 1, 1)

        self.num_ind_vars_combo = QComboBox(self.gridLayoutWidget)
        self.num_ind_vars_combo.addItem("")
        self.num_ind_vars_combo.addItem("")
        self.num_ind_vars_combo.addItem("")
        self.num_ind_vars_combo.setObjectName(u"num_ind_vars_combo")

        self.input_params.addWidget(self.num_ind_vars_combo, 3, 1, 1, 1)

        self.num_groups_combo = QComboBox(self.gridLayoutWidget)
        self.num_groups_combo.addItem("")
        self.num_groups_combo.addItem("")
        self.num_groups_combo.addItem("")
        self.num_groups_combo.setObjectName(u"num_groups_combo")

        self.input_params.addWidget(self.num_groups_combo, 1, 1, 1, 1)

        self.grp_names = QLabel(self.gridLayoutWidget)
        self.grp_names.setObjectName(u"grp_names")

        self.input_params.addWidget(self.grp_names, 2, 0, 1, 1)

        self.analysis_type_combo = QComboBox(self.gridLayoutWidget)
        self.analysis_type_combo.addItem("")
        self.analysis_type_combo.addItem("")
        self.analysis_type_combo.addItem("")
        self.analysis_type_combo.addItem("")
        self.analysis_type_combo.setObjectName(u"analysis_type_combo")

        self.input_params.addWidget(self.analysis_type_combo, 0, 1, 1, 1)

        self.analysis_type = QLabel(self.gridLayoutWidget)
        self.analysis_type.setObjectName(u"analysis_type")

        self.input_params.addWidget(self.analysis_type, 0, 0, 1, 1)

        self.images = QTabWidget(self.centralwidget)
        self.images.setObjectName(u"images")
        self.images.setGeometry(QRect(520, 10, 471, 551))
        self.images.setTabPosition(QTabWidget.North)
        self.images.setTabShape(QTabWidget.Rounded)
        self.images.setElideMode(Qt.ElideNone)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.display_pngs = QLabel(self.tab)
        self.display_pngs.setObjectName(u"display_pngs")
        self.display_pngs.setGeometry(QRect(90, 20, 121, 121))
        self.display_pngs.setFrameShape(QFrame.Box)
        self.images.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.images.addTab(self.tab_2, "")
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(540, 570, 431, 141))
        self.save_graph_options = QGridLayout(self.gridLayoutWidget_2)
        self.save_graph_options.setObjectName(u"save_graph_options")
        self.save_graph_options.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.gridLayoutWidget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.save_graph_options.addWidget(self.line, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.save_graph_options.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.save_graph_options.addWidget(self.label_2, 3, 1, 1, 1)

        self.out_ppt_location_button = QPushButton(self.gridLayoutWidget_2)
        self.out_ppt_location_button.setObjectName(u"out_ppt_location_button")

        self.save_graph_options.addWidget(self.out_ppt_location_button, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.save_graph_options.addWidget(self.pushButton, 1, 0, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.save_graph_options.addWidget(self.line_2, 2, 1, 1, 1)

        self.out_png_location_button = QPushButton(self.gridLayoutWidget_2)
        self.out_png_location_button.setObjectName(u"out_png_location_button")

        self.save_graph_options.addWidget(self.out_png_location_button, 0, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.save_graph_options.addWidget(self.label, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.save_graph_options.addWidget(self.pushButton_3, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1027, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.images.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.num_ind_vars.setText(QCoreApplication.translate("MainWindow", u"Number of independent variables:", None))
        self.in_format.setText(QCoreApplication.translate("MainWindow", u"Input data format:", None))
        self.in_location_button.setText(QCoreApplication.translate("MainWindow", u"Choose input file location:", None))
        self.num_groups.setText(QCoreApplication.translate("MainWindow", u"Number of groups:", None))
        self.in_location.setText(QCoreApplication.translate("MainWindow", u"No file chosen", None))
        self.analysis_type_combo_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose Format . . .", None))
        self.analysis_type_combo_2.setItemText(1, QCoreApplication.translate("MainWindow", u"program1", None))
        self.analysis_type_combo_2.setItemText(2, QCoreApplication.translate("MainWindow", u"program2", None))

        self.ind_var_names.setText(QCoreApplication.translate("MainWindow", u"Ind var names:", None))
        self.num_ind_vars_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose Value . . .", None))
        self.num_ind_vars_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.num_ind_vars_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.num_groups_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose Value . . .", None))
        self.num_groups_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.num_groups_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.grp_names.setText(QCoreApplication.translate("MainWindow", u"Group names:", None))
        self.analysis_type_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose Test Type . . .", None))
        self.analysis_type_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Independent T-test", None))
        self.analysis_type_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Dependent T-test", None))
        self.analysis_type_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Anova", None))

        self.analysis_type.setText(QCoreApplication.translate("MainWindow", u"Stat analysis type:", None))
        self.display_pngs.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.images.setTabText(self.images.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Image 1", None))
        self.images.setTabText(self.images.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Image 2", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save all images", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"No path chosen", None))
        self.out_ppt_location_button.setText(QCoreApplication.translate("MainWindow", u"Choose ppt save location:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save this image only", None))
        self.out_png_location_button.setText(QCoreApplication.translate("MainWindow", u"Choose image save location:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"No path chosen", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save all images to power point", None))
    # retranslateUi

