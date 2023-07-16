import sqlite3

connector = sqlite3.connect("data.db")
cursor = connector.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Products(name TEXT, price INTEGER, image_name TEXT)")

cursor.execute("INSERT INTO Products VALues('Hamburger', 1.79, 'Burger_1.png')")
cursor.execute("INSERT INTO Products VALues('Cheeseburger', 1.99, 'Burger_2.png')")
cursor.execute("INSERT INTO Products VALues('Double Cheeseburger', 2.99, 'Burger_3.png')")
cursor.execute("INSERT INTO Products VALues('Bacon Cheeseburger', 2.39, 'Burger_4.png')")

cursor.execute("INSERT INTO Products VALues('Classic Fries', 3.09, 'Side_1.png')")
cursor.execute("INSERT INTO Products VALues('Onion Rings', 3.09, 'Side_2.png')")
cursor.execute("INSERT INTO Products VALues('4 Pc. Chicken Nuggets', 1.49, 'Side_3.png')")
cursor.execute("INSERT INTO Products VALues('Mozzarella Sticks', 1.49, 'Side_4.png')")

cursor.execute("INSERT INTO Products VALues('Coca-Cola', 2.29, 'Drink_1.png')")
cursor.execute("INSERT INTO Products VALues('Fanta Orange', 2.29, 'Drink_2.png')")
cursor.execute("INSERT INTO Products VALues('Sprite', 2.29, 'Drink_3.png')")
cursor.execute("INSERT INTO Products VALues('Bottled Water', 2.19, 'Drink_4.png')")

cursor.execute("CREATE TABLE IF NOT EXISTS Billitems(bill_number INTEGER, name TEXT, price INTEGER, quantity INTEGER, total INTEGER)")

connector.commit()

