__author__ = 'MarX'

from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Graphics.CFAbstractObjectUI import *
from CFMethods import *

def getListName(s):
    if isinstance(s, str):
        s = s.replace(' ', '')
        s = s.replace(',',';')
        return s.split(';')

class CFFindUserUI(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        uic.loadUi("Graphics\\CFFindUser.ui", self)

        self.FindUser.clicked.connect(self.find)

    def find(self):
        handle = self.Handle.text()

        if (len(handle) == 0):
            self.msg("Handle field is empty!")

        else:

            UserInfo = user_info(getListName(handle))
            print(UserInfo.url())

            data = UserInfo.get()
            if (isinstance(data, CFError)):
                self.msg(data.msg)

            else:
                self.curUserUIList = []
                for i in data:
                    cur_ui = CFAbstractObjectUI( i )
                    cur_ui.show()
                    self.curUserUIList.append( cur_ui )


    def msg(self, text, title = "Error"):
        self.mb = QMessageBox()

        self.mb.setWindowTitle(title)
        self.mb.setText(text)

        self.mb.show()