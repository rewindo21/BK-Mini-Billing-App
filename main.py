from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtPrintSupport import QPrinter
import sys
import sqlite3
import datetime

# try:
#     ui, _ = loadUiType('billing.ui')
# except Exception as e:
#     print("Error loading UI file:", e)
ui, _ = loadUiType('billing.ui')        # import ui file

class MainApp(QMainWindow, ui):

    Products = ["0"]
    prices = ["0"]

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)                          # make ui file an attribute
        self.main_tabWidget.setCurrentIndex(0)      # show tab 0 initially
        # connect buttons to their function
        self.login_pushButton.clicked.connect(self.login)
        self.logout_pushButton.clicked.connect(self.logout)
        self.print_pushButton.clicked.connect(self.print_items)
        self.reset_pushButton.clicked.connect(self.reset_table)
        self.settings_pushButton.clicked.connnect(self.show_settings)
        # connect Products add button to add function
        self.burger_add_pushButton_1.clicked.connect(lambda: self.add(1))
        self.burger_add_pushButton_2.clicked.connect(lambda: self.add(2))
        self.burger_add_pushButton_3.clicked.connect(lambda: self.add(3))
        self.burger_add_pushButton_4.clicked.connect(lambda: self.add(4))
        self.side_add_pushButton_1.clicked.connect(lambda: self.add(5))
        self.side_add_pushButton_2.clicked.connect(lambda: self.add(6))
        self.side_add_pushButton_3.clicked.connect(lambda: self.add(7))
        self.side_add_pushButton_4.clicked.connect(lambda: self.add(8))
        self.drink_add_pushButton_1.clicked.connect(lambda: self.add(9))
        self.drink_add_pushButton_2.clicked.connect(lambda: self.add(10))
        self.drink_add_pushButton_3.clicked.connect(lambda: self.add(11))
        self.drink_add_pushButton_4.clicked.connect(lambda: self.add(12))


    def login(self):
        username = self.username_lineEdit.text()     # collect username
        password = self.password_lineEdit.text()     # collect password
        if (username == "admin" and password == "admin"):
            self.username_lineEdit.setText("")
            self.password_lineEdit.setText("")
            self.error_label.setText("")
            self.bill()                             # create a new bill
            self.main_tabWidget.setCurrentIndex(1)  # go to tab 1 after login
        else:
            self.error_label.setText("Invalid Username or Password")


    def logout(self):
       self.main_tabWidget.setCurrentIndex(0)       # back to tab 0


    # generate a new bill
    def bill(self):
        try:
            connector = sqlite3.connect("data.db")
            cursor = connector.execute("SELECT MAX(bill_number) FROM billitems")
            temp = cursor.fetchall()
            if temp:
                    for i in temp:
                        n = int(i[0] + 1)
            self.bill_number_label.setText(str(n))                  # specify bill number
        except:
            n = 1
            self.bill_number_label.setText(str(n))
        self.bill_date_label.setText(str(datetime.datetime.now()))  # specify bill date
        self.get()


    # get Products from database
    def get(self):
        self.Products = ["0"]
        self.prices = [0]
        connector = sqlite3.connect("data.db")
        cursor = connector.execute("SELECT * FROM Products")
        temp = cursor.fetchall()
        if temp:
            for i in temp:
                self.Products.append(str(i[0]))
                self.prices.append(str(i[1]))
        # print(self.Products)
        # print(self.prices)


    # add item to database
    def add(self, id):
        billnumber = self.bill_number_label.text()
        itemname = self.Products[id]
        itemprice = self.prices[id]
        quantity = "1"
        connector = sqlite3.connect("data.db")
        cursor = connector.execute("SELECT * FROM Billitems WHERE name = '"+itemname+"' and bill_number = "+billnumber+" ")
        temp = cursor.fetchall()
        # duplicate item
        if temp:
            connector.execute(" UPDATE Billitems SET quantity = quantity + 1, total = total + "+itemprice+" "
                              " WHERE name = '"+itemname+"' and bill_number = "+billnumber+" ")
            connector.commit()
        # new item
        else:
            connector.execute(" INSERT INTO Billitems(bill_number, name, price, quantity, total) "
                              " VALUES("+billnumber+", '"+itemname+"', "+itemprice+", "+quantity+", "+itemprice+") ")
            connector.commit()
        self.show_items()


    # show items in table
    def show_items(self):
        # if there is anything in table, remove them
        self.bill_tableWidget.setRowCount(0)   
        self.bill_tableWidget.clear()
        # get data from database
        connector = sqlite3.connect("data.db")
        cursor = connector.execute(" SELECT name, price, quantity, total FROM Billitems "
                                   " WHERE bill_number = "+self.bill_number_label.text()+" ")
        temp = cursor.fetchall()
        # number of rows and columns
        r = 0
        c = 0
        for row_number, row_data in enumerate(temp):
            r += 1
            c = 0
            for column_number, data in enumerate(row_data):
                    c += 1
        self.bill_tableWidget.setColumnCount(c)
        # insert data to rows
        for row_number, row_data in enumerate(temp):
            self.bill_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.bill_tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        # hide headers
        self.bill_tableWidget.verticalHeader().setVisible(False)
        self.bill_tableWidget.horizontalHeader().setVisible(False)
        # bill total price
        total = 0
        cursor = connector.execute("SELECT * FROM Billitems WHERE bill_number = "+str(self.bill_number_label.text())+" ")
        temp = cursor.fetchall()
        if temp:
            for i in temp:
                total = total + int(i[4])   # total price of each item is 4th
        self.bill_total_label.setText("%.2f" % (total))
        # bill tax (5%)
        self.bill_tax_label.setText("%.2f" % (total * .05))
        # grand total
        self.grand_total_label.setText("%.2f" % (total + ((total * .05))))


    def reset_table(self):
        if (self.grand_total_label.text() != 0):
            self.bill()         # generate new bill
            self.show_items()   # remove last items


    def print_items(self):
        if (self.grand_total_label.text() != 0):
            printer = QPrinter()
            painter = QPainter()
            painter.begin(printer)
            screen = self.bill_groupBox.grab()
            painter.drawPixmap(10, 10, screen)
            painter.end()
            self.bill()         # generate new bill
            self.show_items()   # remove last items





# pyside6-rcc resources.qrc -o resources_rc.py


def main():
    app = QApplication(sys.argv)            # Pass in sys.argv to allow command line arguments for your app
    window = MainApp()                      # Create a MainApp, which will be our window
    window.show()                           # Windows are hidden by default
    app.exec()                              # Start the event loop

if __name__ == "__main__":
    main()
