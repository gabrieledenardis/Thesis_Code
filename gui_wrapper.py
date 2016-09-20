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
