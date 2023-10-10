import sqlite3

def connect_to_db():
    conn = sqlite3.connect('heroes.db')
    return conn

def crear_tabla():
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE heroe (
                heroe_id INTEGER PRIMARY KEY NOT NULL,
                nombre TEXT NOT NULL,
                poder TEXT NOT NULL,
                debilidad TEXT NOT NULL
            );
        ''')
        conn.commit()#confirmando
        print("tabla heroe creada satisfactoriamente")
        conn.close()
    except sqlite3.Error as e:
        print(e)
        print("error en la creacion de la tabla heroe")
    finally:
        conn.close()


crear_tabla()

#get heroes
def get_heroes(conn):
    iheroe={"codigo":"error"}
    try:
        cur=conn.cursor()
        c = conn.cursor()
        iheroe= c.execute('SELECT * FROM heroe').fetchall()
        conn.close()
        #iheroe={"codigo":"ok"}
    except Exception as error:
        print(error,"Error en la consulta de un heroes")
    return iheroe

def insert_heroe(conn, heroe):
    iheroe={"codigo":"error"}
    try:
        cur=conn.cursor()
        cur.execute('INSERT INTO heroe(nombre,poder,debilidad) VALUES (?,?,?)',[heroe['nombre'],heroe['poder'],heroe['debilidad']])
        conn.commit()
        conn.close()
        iheroe={"codigo":"ok"}
    except Exception as error:
        print(error,"Error en la consulta de un heroes")
    return iheroe

def actualizar_heroe(conn, heroe):
    iheroe={"codigo":"error"}
    try:
        cur=conn.cursor()
        cur.execute('INSERT INTO heroe(nombre,poder,debilidad) VALUES (?,?,?)',[heroe['nombre'],heroe['poder'],heroe['debilidad']])
        conn.commit()
        conn.close()
        iheroe={"codigo":"ok"}
    except Exception as error:
        print(error,"Error en la consulta de un heroes")
    return iheroe

def eliminar_heroe(conn,heroe):
    iheroe={"codigo":"error"}
    try:
        cur=conn.cursor()
        c = conn.cursor()
        c.execute("DELETE FROM table WHERE nombre=?",[heroe['nombre']])
        conn.close()
        iheroe={"codigo":"ok"}
    except Exception as error:
        print(error,"Error en la consulta de un heroes")
    return iheroe

from flask import Flask, request, jsonify #added to top of file
from flask_cors import CORS #added to top of file
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def hello_world():
    return "<h1><p>Hola, sebastian!</p></h1>"

@app.route('/heroe/eliminar', methods=['POST'])
def api_get_users():
    medi = request.get_json()
    conn=connect_to_db()
    return jsonify(eliminar_heroe(conn,medi))

@app.route('/heroes', methods=['GET'])
def api_medi():
    conn=connect_to_db()
    return jsonify(get_heroes(conn))

@app.route('/heroe/add',  methods = ['POST'])
def api_add_mediciones():
    heroe = request.get_json()
    conn= connect_to_db()
    return jsonify(insert_heroe(conn,heroe))

@app.route('/heroe/actualizar',  methods = ['POST'])
def api_add_mediciones2():
    medi = request.get_json()
    conn= connect_to_db()
    return jsonify(actualizar_heroe(conn,medi))


if __name__ == "__main__":
    #app.debug = True

    app.run() #run app