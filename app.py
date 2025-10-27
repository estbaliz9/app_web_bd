from flask import Flask, request, render_template, redirect, url_for
import pymysql

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        database = request.form.get('database')
        try:
            conexion = pymysql.connect(
                host='localhost',
                user='root',  # Credenciales predeterminadas para la conexión
                password='',  # Ajusta si tu MariaDB tiene contraseña
                database=database
            )
            cursor = conexion.cursor()
            # Consulta vulnerable - inyecta directamente la entrada del usuario (riesgo de inyección SQL)
            query = f"SELECT * FROM users WHERE username = '{usuario}' AND password = '{password}'"
            cursor.execute(query)
            result = cursor.fetchone()
            conexion.close()
            if result:
                return render_template('tablas.html', usuario=usuario, password=password, database=database)
            else:
                error_msg = "Error de autentificación"
                return render_template('inicio_sesion.html', error=error_msg)
        except pymysql.Error:
            error_msg = "Error de autentificación"
            return render_template('inicio_sesion.html', error=error_msg)
    return render_template('inicio_sesion.html', error=None)

@app.route('/tablas', methods=['POST'])
def tablas():
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    database = request.form.get('database')
    try:
        conexion = pymysql.connect(
            host='localhost',
            user=usuario,
            password=password,
            database=database
        )
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        conexion.close()
        return render_template('tablas.html', tablas=tablas, usuario=usuario, password=password, database=database)
    except pymysql.Error as err:
        error_msg = f"La tabla indicada no existe para el usuario introducido."
        return render_template('inicio_sesion.html', error=error_msg)

@app.route('/registros', methods=['POST'])
def registros():
    tabla = request.form.get('tabla')
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    database = request.form.get('database')
    try:
        conexion = pymysql.connect(
            host='localhost',
            user=usuario,
            password=password,
            database=database
        )
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM `{tabla}`")
        registros = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]
        conexion.close()
        return render_template('registros.html', tabla=tabla, registros=registros, columnas=columnas, usuario=usuario, password=password, database=database)
    except pymysql.Error as err:
        error_msg = f"Error al consultar la tabla: {str(err)}"
        return render_template('inicio_sesion.html', error=error_msg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
