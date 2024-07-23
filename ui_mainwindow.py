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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 786)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 351, 491))
        self.input_params = QGridLayout(self.gridLayoutWidget)
        self.input_params.setObjectName(u"input_params")
        self.input_params.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.input_params.setHorizontalSpacing(5)
        self.input_params.setContentsMargins(0, 0, 0, 0)
        self.prog_msgs_label = QLabel(self.gridLayoutWidget)
        self.prog_msgs_label.setObjectName(u"prog_msgs_label")

        self.input_params.addWidget(self.prog_msgs_label, 18, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.analysis_type_2 = QLabel(self.gridLayoutWidget)
        self.analysis_type_2.setObjectName(u"analysis_type_2")

        self.horizontalLayout_2.addWidget(self.analysis_type_2)

        self.analysis_type_combo_2 = QComboBox(self.gridLayoutWidget)
        self.analysis_type_combo_2.addItem("")
        self.analysis_type_combo_2.addItem("")
        self.analysis_type_combo_2.addItem("")
        self.analysis_type_combo_2.setObjectName(u"analysis_type_combo_2")

        self.horizontalLayout_2.addWidget(self.analysis_type_combo_2)


        self.input_params.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.grp_cols_label = QLabel(self.gridLayoutWidget)
        self.grp_cols_label.setObjectName(u"grp_cols_label")

        self.input_params.addWidget(self.grp_cols_label, 3, 0, 1, 1)

        self.grp_cols_input = QPlainTextEdit(self.gridLayoutWidget)
        self.grp_cols_input.setObjectName(u"grp_cols_input")

        self.input_params.addWidget(self.grp_cols_input, 4, 0, 1, 1)

        self.beh_cols_label = QLabel(self.gridLayoutWidget)
        self.beh_cols_label.setObjectName(u"beh_cols_label")

        self.input_params.addWidget(self.beh_cols_label, 7, 0, 1, 1)

        self.in_location_text = QTextBrowser(self.gridLayoutWidget)
        self.in_location_text.setObjectName(u"in_location_text")

        self.input_params.addWidget(self.in_location_text, 16, 0, 1, 1)

        self.confirm_col_info_button = QPushButton(self.gridLayoutWidget)
        self.confirm_col_info_button.setObjectName(u"confirm_col_info_button")

        self.input_params.addWidget(self.confirm_col_info_button, 14, 0, 1, 1)

        self.beh_cols_input = QPlainTextEdit(self.gridLayoutWidget)
        self.beh_cols_input.setObjectName(u"beh_cols_input")

        self.input_params.addWidget(self.beh_cols_input, 8, 0, 1, 1)

        self.measured_cols_input = QPlainTextEdit(self.gridLayoutWidget)
        self.measured_cols_input.setObjectName(u"measured_cols_input")

        self.input_params.addWidget(self.measured_cols_input, 12, 0, 1, 1)

        self.in_location_button = QPushButton(self.gridLayoutWidget)
        self.in_location_button.setObjectName(u"in_location_button")

        self.input_params.addWidget(self.in_location_button, 15, 0, 1, 1)

        self.measured_cols_label = QLabel(self.gridLayoutWidget)
        self.measured_cols_label.setObjectName(u"measured_cols_label")

        self.input_params.addWidget(self.measured_cols_label, 10, 0, 1, 1)

        self.run_button = QPushButton(self.gridLayoutWidget)
        self.run_button.setObjectName(u"run_button")

        self.input_params.addWidget(self.run_button, 17, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.analysis_type = QLabel(self.gridLayoutWidget)
        self.analysis_type.setObjectName(u"analysis_type")

        self.horizontalLayout.addWidget(self.analysis_type)

        self.analysis_type_combo = QComboBox(self.gridLayoutWidget)
        self.analysis_type_combo.addItem("")
        self.analysis_type_combo.addItem("")
        self.analysis_type_combo.addItem("")
        self.analysis_type_combo.addItem("")
        self.analysis_type_combo.setObjectName(u"analysis_type_combo")

        self.horizontalLayout.addWidget(self.analysis_type_combo)


        self.input_params.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.mice_cols_label = QLabel(self.gridLayoutWidget)
        self.mice_cols_label.setObjectName(u"mice_cols_label")

        self.input_params.addWidget(self.mice_cols_label, 5, 0, 1, 1)

        self.mice_cols_input = QPlainTextEdit(self.gridLayoutWidget)
        self.mice_cols_input.setObjectName(u"mice_cols_input")

        self.input_params.addWidget(self.mice_cols_input, 6, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(370, 538, 521, 111))
        self.save_graph_options = QGridLayout(self.gridLayoutWidget_2)
        self.save_graph_options.setObjectName(u"save_graph_options")
        self.save_graph_options.setContentsMargins(0, 0, 0, 0)
        self.save_all_ppt = QPushButton(self.gridLayoutWidget_2)
        self.save_all_ppt.setObjectName(u"save_all_ppt")

        self.save_graph_options.addWidget(self.save_all_ppt, 2, 1, 1, 1)

        self.save_one_image = QPushButton(self.gridLayoutWidget_2)
        self.save_one_image.setObjectName(u"save_one_image")

        self.save_graph_options.addWidget(self.save_one_image, 1, 0, 1, 1)

        self.save_all_dfs = QPushButton(self.gridLayoutWidget_2)
        self.save_all_dfs.setObjectName(u"save_all_dfs")

        self.save_graph_options.addWidget(self.save_all_dfs, 3, 1, 1, 1)

        self.save_one_ppt = QPushButton(self.gridLayoutWidget_2)
        self.save_one_ppt.setObjectName(u"save_one_ppt")

        self.save_graph_options.addWidget(self.save_one_ppt, 2, 0, 1, 1)

        self.out_png_location_button = QPushButton(self.gridLayoutWidget_2)
        self.out_png_location_button.setObjectName(u"out_png_location_button")

        self.save_graph_options.addWidget(self.out_png_location_button, 0, 0, 1, 1)

        self.save_all_images = QPushButton(self.gridLayoutWidget_2)
        self.save_all_images.setObjectName(u"save_all_images")

        self.save_graph_options.addWidget(self.save_all_images, 1, 1, 1, 1)

        self.out_png_location_text = QTextBrowser(self.gridLayoutWidget_2)
        self.out_png_location_text.setObjectName(u"out_png_location_text")

        self.save_graph_options.addWidget(self.out_png_location_text, 0, 1, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(370, 10, 521, 521))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(10, 650, 351, 4))
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setOrientation(Qt.Horizontal)
        self.progress_bar.setInvertedAppearance(False)
        self.progress_bar.setTextDirection(QProgressBar.TopToBottom)
        self.color_options = QPushButton(self.centralwidget)
        self.color_options.setObjectName(u"color_options")
        self.color_options.setGeometry(QRect(780, 530, 111, 31))
        self.prog_msgs_text = QTextBrowser(self.centralwidget)
        self.prog_msgs_text.setObjectName(u"prog_msgs_text")
        self.prog_msgs_text.setGeometry(QRect(10, 500, 351, 151))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 932, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.prog_msgs_label.setText(QCoreApplication.translate("MainWindow", u"Program Messages:", None))
        self.analysis_type_2.setText(QCoreApplication.translate("MainWindow", u"Program that input data is from:", None))
        self.analysis_type_combo_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose program . . .", None))
        self.analysis_type_combo_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Observer", None))
        self.analysis_type_combo_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Ethovision", None))

        self.grp_cols_label.setText(QCoreApplication.translate("MainWindow", u"Group column(s) *", None))
        self.beh_cols_label.setText(QCoreApplication.translate("MainWindow", u"Behavior column(s) *", None))
        self.in_location_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No path chosen</p></body></html>", None))
        self.confirm_col_info_button.setText(QCoreApplication.translate("MainWindow", u"Confirm all column info", None))
        self.in_location_button.setText(QCoreApplication.translate("MainWindow", u"Choose input file location:", None))
        self.measured_cols_label.setText(QCoreApplication.translate("MainWindow", u"Measured column(s)", None))
        self.run_button.setText(QCoreApplication.translate("MainWindow", u"Run ->", None))
        self.analysis_type.setText(QCoreApplication.translate("MainWindow", u"Statistical analysis type:", None))
        self.analysis_type_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose Test Type . . .", None))
        self.analysis_type_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Independent T-test", None))
        self.analysis_type_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Dependent T-test", None))
        self.analysis_type_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Anova", None))

        self.mice_cols_label.setText(QCoreApplication.translate("MainWindow", u"MiceID column(s) *", None))
        self.save_all_ppt.setText(QCoreApplication.translate("MainWindow", u"Save all images to power point", None))
        self.save_one_image.setText(QCoreApplication.translate("MainWindow", u"Save this image only", None))
        self.save_all_dfs.setText(QCoreApplication.translate("MainWindow", u"Save all cleaned dataframes to exel", None))
        self.save_one_ppt.setText(QCoreApplication.translate("MainWindow", u"Save this image only to power point", None))
        self.out_png_location_button.setText(QCoreApplication.translate("MainWindow", u"Choose output save location:", None))
        self.save_all_images.setText(QCoreApplication.translate("MainWindow", u"Save all images", None))
        self.out_png_location_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No path chosen</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Graphs will appear here after tests tun", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.color_options.setText(QCoreApplication.translate("MainWindow", u"Color Options", None))
    # retranslateUi

