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

# Endpoint per ottenere tutti i funghi presenti nella tabella
@app.route('/api/funghi', methods=['GET'])
def ottieni_funghi():
    conn = connessione_db()
    cursor = conn.cursor(dictionary=True)
    
    # Query per recuperare tutti i funghi
    cursor.execute("SELECT * FROM Funghi")
    elenco_funghi = cursor.fetchall()
    
    # Chiusura della connessione
    cursor.close()
    conn.close()
    
    # Restituisce i dati come JSON
    return jsonify(elenco_funghi)