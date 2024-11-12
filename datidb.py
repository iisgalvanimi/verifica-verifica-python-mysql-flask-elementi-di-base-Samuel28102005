import mysql.connector

# Connessione al server MySQL senza selezionare il database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

# Verifica se il database 'Funghi' esiste già
mycursor.execute("SHOW DATABASES LIKE 'Funghi'")
result = mycursor.fetchone()

# Se il database non esiste, crealo
if not result:
    mycursor.execute("CREATE DATABASE Funghi")
    print("Database 'Funghi' creato.")
else:
    print("Il database 'Funghi' esiste già.")

# Ora seleziona il database
mydb.database = "Funghi"

# Creazione della tabella Funghi (se non esiste)
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Funghi (
        Id INT AUTO_INCREMENT PRIMARY KEY,
        Nome_Comune VARCHAR(255),
        Famiglia VARCHAR(255),
        Commestibilità VARCHAR(255),
        Habitat VARCHAR(255),
        Stagione VARCHAR(255)
    );
""")

# Esegui il commit delle modifiche
mydb.commit()

print("Tabella 'Funghi' creata o già esistente.")
