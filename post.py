from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Funzione per stabilire una connessione al database
def connessione_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Funghi"  # Nome del database per i funghi
    )

@app.route('/api/funghi', methods=['POST'])
def aggiungi_fungo():
    dati = request.get_json()  # Riceve i dati JSON dal client

    # Controlla che i campi richiesti siano presenti
    if not all(campo in dati for campo in ('Nome_Comune', 'Famiglia', 'Commestibilita', 'Habitat', 'Stagione')):
        return jsonify({"errore": "Dati incompleti"})

    nome_comune = dati['Nome_Comune']
    famiglia = dati['Famiglia']
    commestibilita = dati['Commestibilita']
    habitat = dati['Habitat']
    stagione = dati['Stagione']

    # Connessione al database e inserimento
    conn = connessione_db()
    cursor = conn.cursor()

    query = "INSERT INTO Funghi (Nome_Comune, Famiglia, Commestibilita, Habitat, Stagione) VALUES (%s, %s, %s, %s, %s)"
    valori = (nome_comune, famiglia, commestibilita, habitat, stagione)
    cursor.execute(query, valori)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"messaggio": "Fungo aggiunto con successo!"})