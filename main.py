import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.db")
        self.pushButton.clicked.connect(self.add)
        self.printing()

    def printing(self):
        self.cur = self.con.cursor()
        result = self.cur.execute("Select * from Coffee").fetchall()
        self.id = result[-1][0] + 1
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]) - 1)
        self.titles = [description[0] for description in self.cur.description]

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def add(self):
        cost = int(self.cost.text())
        count = int(self.count.text())
        fry = self.fry.text()
        mol = self.mol.text()
        name = self.name.text()
        plot = self.plot.text()

        self.cur.execute(f'''INSERT INTO Coffee VALUES({self.id}, "{name}", "{fry}", 
"{mol}", "{plot}", {cost}, {count})''')
        self.con.commit()
        self.printing()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
