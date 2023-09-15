from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtPrintSupport import QPrinter
import sys
import sqlite3
import datetime

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
        self.settings_pushButton.clicked.connect(self.show_settings)
        self.modify_pushButton.clicked.connect(self.update_values)
        self.back_pushButton.clicked.connect(self.back2products)
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
        # connect combobox to its function
        self.itemlist_comboBox.currentIndexChanged.connect(self.show_values)

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


    def show_settings(self):
        self.main_tabWidget.setCurrentIndex(2)
        self.itemlist_comboBox.clear()
        # get data from database
        connector = sqlite3.connect("data.db")
        cursor = connector.execute("SELECT * FROM Products")
        result = cursor.fetchall()
        if result:
            for i in result:
                self.itemlist_comboBox.addItem(str(i[0]))


    # show item values in settings
    def show_values(self):
        # get data from database
        connector = sqlite3.connect("data.db")
        cursor = connector.execute("SELECT * FROM Products WHERE name = '"+ self.itemlist_comboBox.currentText()+"' ")
        result = cursor.fetchall()
        if result:
            for i in result:
                # show in fields
                self.item_name_lineEdit.setText(str(i[0]))
                self.item_price_lineEdit.setText(str(i[1]))
                self.item_picture_lineEdit.setText(str(i[2]))
                # show in sample label
                self.configure_name_label.setText(str(i[0]))
                self.configure_price_label.setText("$" + str(i[1]))
                # add pictures path to pixmap of the label
                filename = "./images/" + str(i[2])
                image = QImage(filename)
                pm = QPixmap.fromImage(image)
                self.configure_picture_label.setPixmap(pm)
        self.error_label_2.setText("")


    # update item values in settings
    def update_values(self):
        connector = sqlite3.connect("data.db")
        cursor = connector.execute( " UPDATE Products SET name = '"+ self.item_name_lineEdit.text() +"',"
                                                        " price = '"+ self.item_price_lineEdit.text() +"', "
                                                        " image_name = '"+ self.item_picture_lineEdit.text() +"' "
                                                        " WHERE name = '"+ self.itemlist_comboBox.currentText()+"' ")
        connector.commit()
        connector.close()
        # show in sample label
        self.configure_name_label.setText(self.item_name_lineEdit.text())
        self.configure_price_label.setText("$" + self.item_price_lineEdit.text())
        # add pictures path to pixmap of the label
        filename = "./images/" + self.item_picture_lineEdit.text()
        image = QImage(filename)
        pm = QPixmap.fromImage(image)
        self.configure_picture_label.setPixmap(pm)
        # get the items again on the second page and raise a message at the end
        self.get()
        self.error_label_2.setText("Item updated successfully")


    def back2products(self):
        self.main_tabWidget.setCurrentIndex(1)






def main():
    app = QApplication(sys.argv)            # Pass in sys.argv to allow command line arguments for your app
    window = MainApp()                      # Create a MainApp, which will be our window
    window.show()                           # Windows are hidden by default
    app.exec()                              # Start the event loop

if __name__ == "__main__":
    main()
