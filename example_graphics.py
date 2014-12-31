__author__ = 'MarX'

import sys
from Graphics.CFAbstractObjectUI import *
from Graphics.CFFindUser import *

def main():
    app = QApplication(sys.argv)

    win = CFFindUserUI()
    win.show()

    app.exec()

if __name__ == "__main__":
    main()
    