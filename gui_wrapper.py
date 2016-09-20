# -*- coding: utf-8 -*-
# !/usr/bin/env python

# PyQt4 imports
from PyQt4 import QtGui, QtCore

# Python imports
import platform

# Projects imports
from gui import python_converted_gui


class GuiWrapper(QtGui.QMainWindow, python_converted_gui.Ui_BrowserCacheAnalyzerGui):

    def __init__(self, parent=None):
        super(GuiWrapper, self).__init__(parent)
        self.setupUi(self)

        # Mouse cursor coordinates on left click over the application window
        self.mouse_press_event_position = None

    ##########################################
    # SECTION: SIGNALS AND SLOTS CONNECTIONS #
    ##########################################

        # Application "close" and "minimize" buttons
        self.btn_app_close.clicked.connect(self.close_application)
        self.btn_app_minimize.clicked.connect(self.showMinimized)

        # Other application elements
        self.btn_welcome_screen_next.clicked.connect(self.set_browser_choice_screen)

    ###########################
    # SECTION: WELCOME SCREEN #
    ###########################

        # Setting "welcome screen" as application start screen
        self.stackedWidget.setCurrentIndex(0)

        # If "welcome screen", "system info" and "selected browser info" group boxes are not visible
        if self.stackedWidget.currentIndex() == 0:
            self.groupBox_system_info.setVisible(False)
            self.groupBox_selected_browser_info.setVisible(False)

    ##################
    # SECTION: SLOTS #
    ##################

    def close_application(self):
        """
        Slot for application "close" button.
        A message box will ask to confirm before quitting.
        """

        # Confirmation before quitting
        msg_confirm_exit = QtGui.QMessageBox.question(QtGui.QMessageBox(), "Confirm",
                                                      "Are you sure you want to quit?",
                                                      QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                                      QtGui.QMessageBox.No)

        # If "yes" button clicked, quitting application
        if msg_confirm_exit == QtGui.QMessageBox.Yes:
            self.close()

        #####################################
        # SUBSECTION: BROWSER CHOICE SCREEN #
        #####################################

    def set_browser_choice_screen(self):
        """
        Slot for "next" button in "welcome screen".
        Setting stacked widget = 1, "system info" group box visible and retrieving system values
        """

        # Setting "browsers choice screen"
        self.stackedWidget.setCurrentIndex(1)

        # "Next" button not enabled (Yet no selected item from "found browsers table")
        self.btn_browser_choice_screen_next.setEnabled(False)

        # Setting "system info" group box visible
        self.groupBox_system_info.setVisible(True)

        # "System info" values
        self.lbl_sys_info.setText(platform.system())
        self.lbl_release.setText(platform.release())
        self.lbl_release_version.setText(platform.version())
        self.lbl_hostname.setText(platform.node())

    ######################################################################
    # SECTION: MOUSE METHODS OVERRIDE (Application window drag and drop) #
    #####################################################################

    def mousePressEvent(self, event):
        """
        Override for QtGui.QWidget.mousePressEvent to calculate mouse position at click.
        Event position is relative to the application window.
        :param event: QtGui.QMouseEvent
        """

        # Mouse cursor coordinates relative to the application window
        self.mouse_press_event_position = event.pos()

    def mouseMoveEvent(self, event):
        """
        Override for QtGui.QWidget.mouseMoveEvent to drag the application window.
        Event buttons indicates the button state when the event was generated.
        Event position is the global position of the mouse cursor at the time of the event.
        :param event: QtGui.QMouseEvent
        """

        # Application window move only with mouse left button
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.mouse_press_event_position)