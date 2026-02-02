import sqlite3 as sql

Articles = [
        ("Banana", 3, 2.4, 0.6),
        ("Pomme De Terre",  4, 3.2, 0.8),
        ("Pomme", 3, 2.4, 0.6),
        ("Ananas", 17, 13.6, 3.4),
        ("Tomate", 2, 1.6, 0.4),
        ("Oreo", 3, 2.4, 0.6),
        ("Yogurt", 2, 1.6, 0.4),
        ("Sidi Ali", 5, 4, 1),
        ("Viande", 160, 128, 32),
        ("Poulet", 17, 13.6, 3.4),
        ("Poison", 20, 16, 4),
        ("Amidon", 5, 4, 1),
        ("Sucre", 5, 4, 1),
        ("Indomi", 3.5, 2.8, 0.7)
    ]

DBFile = sql.connect(r"C:\Users\Abdelaziz\OneDrive\Desktop\Rayane-Haouzi-Abdelaziz-Amine-Bakkari-Martil\ArticlesDataBase.db")
cursor = DBFile.cursor()
cursor.execute("CREATE TABLE articles(Article TEXT, TotalPrice INTEGER, PriceWithoutTVA INTEGER, TVA INTEGER)")
cursor.executemany("INSERT INTO articles VALUES(?,?,?,?)", Articles)


DBFile.commit()
DBFile.close()