import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Funghi"
)
mycursor = mydb.cursor()

# Verifica se il database 'Funghi' esiste
mycursor.execute("SHOW DATABASES LIKE 'Funghi'")
result = mycursor.fetchone()

if result:
    print("Il database 'Funghi' è disponibile.")
else:
    print("Il database 'Funghi' non esiste.")
mycursor = mydb.cursor()
mycursor.execute("DESCRIBE Funghi")
print(mycursor.fetchall())

sql = "INSERT INTO Funghi (Nome_Comune, Famiglia, Commestibilità, Habitat, Stagione) VALUES (%s, %s, %s, %s, %s)"
dati_funghi = [
    ("Porcino", "Boletaceae", "Commestibile", "Boschi", "Autunno"),
    ("Chiodino", "Pholiotaceae", "Commestibile", "Legno morto", "Autunno"),
    ("Ovolo buono", "Amanitaceae", "Commestibile", "Boschi", "Autunno"),
    ("Gallinaccio", "Cantharellaceae", "Commestibile", "Boschi", "Autunno"),
    ("Amanita muscaria", "Amanitaceae", "Velenoso", "Boschi", "Autunno"),
    ("Lepiota cristata", "Lepiotaceae", "Velenoso", "Prati", "Estate"),
    ("Pleurotus ostreatus", "Pleurotaceae", "Commestibile", "Legno morto", "Autunno"),
    ("Macrolepiota procera", "Lepiotaceae", "Commestibile", "Prati", "Estate"),
    ("Boletus edulis", "Boletaceae", "Commestibile", "Boschi", "Autunno"),
    ("Russula emetica", "Russulaceae", "Velenoso", "Boschi","Estate")
]

mycursor.executemany(sql, dati_funghi)
mydb.commit()