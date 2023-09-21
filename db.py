import sqlite3

connector = sqlite3.connect("data.db")
cursor = connector.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Billitems(bill_number INTEGER, name TEXT, price INTEGER, quantity INTEGER, total INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS Products(name TEXT, price INTEGER, image_name TEXT)")

cursor.execute("INSERT INTO Products VALUES ('Whopper', 5.39, 'Burger_1.png')")
cursor.execute("INSERT INTO Products VALUES ('Imposible Whopper', 6.39, 'Burger_2.png')")
cursor.execute("INSERT INTO Products VALUES ('Double Whopper', 6.59, 'Burger_3.png')")
cursor.execute("INSERT INTO Products VALUES ('Triple Whopper', 7.79, 'Burger_4.png')")
cursor.execute("INSERT INTO Products VALUES ('Bacon king', 6.49, 'Burger_5.png')")
cursor.execute("INSERT INTO Products VALUES ('Single Quarter Pound King', 5.49, 'Burger_6.png')")
cursor.execute("INSERT INTO Products VALUES ('Single Impossible King', 6.49, 'Burger_7.png')")
cursor.execute("INSERT INTO Products VALUES ('BBQ Bacon Whopper Jr.', 3.89, 'Burger_8.png')")
cursor.execute("INSERT INTO Products VALUES ('Whopper Jr.', 3.29, 'Burger_9.png')")
cursor.execute("INSERT INTO Products VALUES ('Big King', 4.19, 'Burger_10.png')")
cursor.execute("INSERT INTO Products VALUES ('Bacon Double Cheeseburger', 3.59, 'Burger_11.png')")
cursor.execute("INSERT INTO Products VALUES ('Bacon Cheeseburger', 2.49, 'Burger_12.png')")
cursor.execute("INSERT INTO Products VALUES ('Double Cheeseburger', 2.99, 'Burger_13.png')")
cursor.execute("INSERT INTO Products VALUES ('Cheeseburger', 1.99, 'Burger_14.png')")
cursor.execute("INSERT INTO Products VALUES ('Rodeo Burger', 1.79, 'Burger_15.png')")
cursor.execute("INSERT INTO Products VALUES ('Hamburger', 1.79, 'Burger_16.png')")

cursor.execute("INSERT INTO Products VALUES ('BK Royal Crispy Chicken', 5.39, 'Chicken_1.png')")
cursor.execute("INSERT INTO Products VALUES ('Spicy BK Royal Crispy Chicken', 5.89, 'Chicken_2.png')")
cursor.execute("INSERT INTO Products VALUES ('Bacon and Swiss BK Royal Crispy Chicken', 6.79, 'Chicken_3.png')")
cursor.execute("INSERT INTO Products VALUES ('Honey Mustard BK Royal Crispy Chicken', 6.79, 'Chicken_4.png')")
cursor.execute("INSERT INTO Products VALUES ('Original Chicken Sandwich', 4.99, 'Chicken_5.png')")
cursor.execute("INSERT INTO Products VALUES ('Chicken Jr.', 1.59, 'Chicken_6.png')")
cursor.execute("INSERT INTO Products VALUES ('Big Fish', 4.69, 'Chicken_7.png')")
cursor.execute("INSERT INTO Products VALUES ('Classic BK Royal Crispy Wrap.', 2.99, 'Chicken_8.png')")
cursor.execute("INSERT INTO Products VALUES ('Spicy BK Royal Crispy Wrap', 2.99, 'Chicken_9.png')")
cursor.execute("INSERT INTO Products VALUES ('Honey Mustard BK Royal Crispy Wrap', 2.99, 'Chicken_10.png')")

# cursor.execute("INSERT INTO Products VALUES"
#                                 "('Classic Fries', 3.19, 'Side_1.png'),"
#                                 "('Onion Rings', 3.19, 'Side_2.png'),"
#                                 "('4 Pc. Chicken Fries', 1.99, 'Side_3.png'),"
#                                 "('8 Pc. Chicken Fries', 3.59, 'Side_4.png'),"
#                                 "('12 Pc. Chicken Fries', 4.99, 'Side_5.png'),"
#                                 "('4 Pc. Chicken Nuggets', 1.49, 'Side_6.png'),"
#                                 "('8 Pc. Chicken Nuggets', 2.49, 'Side_7.png'),"
#                                 "('16 Pc. Chicken Nuggets', 4.49, 'Side_8.png'),"
#                                 "('Mozzarella Sticks', 2.59, 'Side_9.png'),"
#                                 "('MOTTS Applesauce', 1.99, 'Side_10.png')")

# cursor.execute("INSERT INTO Products VALUES"
#                                 "('Coca-Cola', 2.29, 'Drink_1.png'),"
#                                 "('Diet Coke', 2.29, 'Drink_2.png'),"
#                                 "('Dr Pepper', 2.29, 'Drink_3.png'),"
#                                 "('Sprite', 2.29, 'Drink_4.png'),"
#                                 "('Fanta Orange', 2.29, 'Drink_5.png'),"
#                                 "('Bottled Water', 2.19, 'Drink_6.png')"
#                                 "('Sweetened Iced Tea', 2.29, 'Drink_7.png'),"
#                                 "('Unsweetened Iced Tea', 2.29, 'Drink_8.png'),"
#                                 "('Frozen Coke', 1.69, 'Drink_9.png'),"
#                                 "('Frozen Fanta Wild Cherry', 1.69, 'Drink_10.png',)"
#                                 "('BK Café', 1.89, 'Drink_11.png',)"
#                                 "('BK Café Decaf', 1.89, 'Drink_12.png',)"
#                                 "('BK Café Iced Coffee', 1.89, 'Drink_13.png',)"
#                                 "('Fat Free Milk', 1.99, 'Drink_14.png',)"
#                                 "('Simply Orange Juice', 2.49, 'Drink_15.png',)"
#                                 "('Capri Sun Apple Juice', 1.59, 'Drink_16.png')")


# cursor.execute("INSERT INTO Products VALUES"
#                                 "('HERSHEY'S Sundae Pie', 1.99, 'Sweet_1.png'),"
#                                 "('Classic Oreo Shake', 3.59, 'Sweet_2.png'),"
#                                 "('Chocolate Oreo Shake', 3.59, 'Sweet_3.png'),"
#                                 "('Chocolate Shake', 3.39, 'Sweet_4.png'),"
#                                 "('Vanilla Shake', 3.39, 'Sweet_5.png'),"
#                                 "('Soft Serve Cup', 1.00, 'Sweet_6.png')"
#                                 "('Soft Serve Cone', 1.00, 'Sweet_7.png'),"
#                                 "('2 Chocolate Chip Cookies', 1.00, 'Sweet_8.png')")


connector.commit()

