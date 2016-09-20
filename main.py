# -*- coding: utf-8 -*-
# !/usr/bin/env python

# PyQt4 imports
from PyQt4 import QtGui, QtCore

# Python imports
import sys

# Project imports
import gui_wrapper

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = gui_wrapper.GuiWrapper()
    main_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    main_window.show()
    sys.exit(app.exec_())
