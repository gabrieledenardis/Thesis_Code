# -*- coding: utf-8 -*-
# !/usr/bin/env python

# PyQt4 imports
from PyQt4 import QtGui, QtCore

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

    ######################################################################
    # SECTION: MOUSE METHODS OVERRIDE (Application window drag and drop) #
    ######################################################################

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