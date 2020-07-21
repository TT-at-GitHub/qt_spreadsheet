import sys
import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PySide2.QtWidgets import (QTableWidget, QApplication,
                               QMainWindow, QTableWidgetItem)


class Table(QTableWidget):

    def __init__(self, rows, columns, data=None, headers=None, parent=None):
        super().__init__(rows, columns, parent)
        self.data = data
        self.headers = None
        self.update_headers(headers)
        self.setup_ui()
        self.setup_signals()

    def setup_ui(self):
        self.setMinimumWidth(720)
        self.setMinimumHeight(480)
        
    def setup_signals(self):
        self.cellChanged.connect(self.on_cellChanged)

    def update_headers(self, headers):
        self.headers = headers
        if self.headers is None:
            return
        
        self.setHorizontalHeaderLabels(self.headers)

    def on_cellChanged(self):
        row = self.currentRow()
        col = self.currentColumn()
        val = self.item(row, col).text()
        
        print(f'cellChanged: Cell({row}, {col}).value = {val}')
        
    def set_data(self, data):
        self.data = data

    def set_headers(self, headers):
        self.update_headers(headers)


class Sheet(QMainWindow):

    def __init__(self, table: QTableWidget, parent=None):
        super().__init__(parent)
        self.table = table
        self.setCentralWidget(table)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sheet = Sheet(table=Table(rows=10, columns=5, headers=['A', 'B', 'C', 'D', 'E']))
    sheet.show()
    sys.exit(app.exec_())