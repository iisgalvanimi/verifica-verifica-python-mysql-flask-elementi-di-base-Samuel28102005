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

# Endpoint per eliminare un fungo
@app.route('/api/funghi/<int:id>', methods=['DELETE'])
def elimina_fungo(id):
    conn = connessione_db()
    cursor = conn.cursor()

    # Controlla se il fungo con questo id esiste
    cursor.execute("SELECT * FROM Funghi WHERE Id = %s", (id,))
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return jsonify({"messaggio": "Fungo non trovato"}), 404

    # Esecuzione dell'operazione di DELETE
    query = "DELETE FROM Funghi WHERE Id = %s"
    cursor.execute(query, (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"messaggio": "Fungo eliminato con successo!"}), 200

if __name__ == '_main_':
    app.run(debug=True)