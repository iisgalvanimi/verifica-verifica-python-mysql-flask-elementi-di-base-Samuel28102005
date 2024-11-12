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

@app.route('/api/funghi/<int:id>', methods=['PUT'])
def aggiorna_fungo(id):
    dati = request.get_json()

    # Controlla che i campi richiesti siano presenti
    if not all(campo in dati for campo in ('Nome_Comune', 'Famiglia', 'Commestibilita', 'Habitat', 'Stagione')):
        return jsonify({"errore": "Dati incompleti"}), 400

    nome_comune = dati['Nome_Comune']
    famiglia = dati['Famiglia']
    commestibilita = dati['Commestibilita']
    habitat = dati['Habitat']
    stagione = dati['Stagione']

    # Connessione e aggiornamento nel database
    conn = connessione_db()
    cursor = conn.cursor()

    query = "UPDATE Funghi SET Nome_Comune = %s, Famiglia = %s, Commestibilita = %s, Habitat = %s, Stagione = %s WHERE Id = %s"
    valori = (nome_comune, famiglia, commestibilita, habitat, stagione, id)
    cursor.execute(query, valori)
    conn.commit()

    righe_modificate = cursor.rowcount
    cursor.close()
    conn.close()

    if righe_modificate == 0:
        return jsonify({"messaggio": "Fungo non trovato"})

    return jsonify({"messaggio": "Fungo aggiornato con successo!"})