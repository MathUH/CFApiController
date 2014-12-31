__author__ = 'MarX'

from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from CFMethods import *
from CFObject import *

class CFAbstractObjectUI(QWidget):
    def __init__(self, obj, parent = None):
        super().__init__(parent)

        uic.loadUi("Graphics\\CFAbstractObject.ui", self)
        self.obj = obj

        self.CFClassName.setText( class_name(self.obj)[2:].capitalize() )

        layout = QVBoxLayout()
        for i, j in self.obj.get_all():
            cur_layout = QHBoxLayout()

            nam = QLabel( str(i) )
            dat = QLabel( str(j) )

            cur_layout.addWidget(nam)
            cur_layout.addWidget(dat)

            layout.addLayout(cur_layout)

        self.CFUserFrame.setLayout(layout)
