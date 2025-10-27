from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

def conectar_db(usuario, password, database):
    return pymysql.connect(
        host='localhost',
        user=usuario,
        password=password,
        database=database
    )

@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        database = request.form.get('database')
        
        try:
            conexion = conectar_db('root', '', database)
            cursor = conexion.cursor()
            query = f"SELECT * FROM users WHERE username = '{usuario}' AND password = '{password}'"
            cursor.execute(query)
            result = cursor.fetchone()
            conexion.close()
            
            if result:
                return render_template('tablas.html', usuario=usuario, password=password, database=database)
            else:
                return render_template('inicio_sesion.html', error="Error de autentificación")
        except:
            return render_template('inicio_sesion.html', error="Error de autentificación")
    
    return render_template('inicio_sesion.html', error=None)

@app.route('/tablas', methods=['POST'])
def tablas():
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    database = request.form.get('database')
    
    try:
        conexion = conectar_db(usuario, password, database)
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        conexion.close()
        return render_template('tablas.html', tablas=tablas, usuario=usuario, password=password, database=database)
    except:
        return render_template('inicio_sesion.html', error="La tabla indicada no existe para el usuario introducido.")

@app.route('/registros', methods=['POST'])
def registros():
    tabla = request.form.get('tabla')
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    database = request.form.get('database')
    
    try:
        conexion = conectar_db(usuario, password, database)
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM `{tabla}`")
        registros = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]
        conexion.close()
        return render_template('registros.html', tabla=tabla, registros=registros, columnas=columnas, 
                             usuario=usuario, password=password, database=database)
    except Exception as err:
        return render_template('inicio_sesion.html', error=f"Error al consultar la tabla: {str(err)}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
