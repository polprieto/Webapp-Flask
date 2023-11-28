from flask import Flask, render_template, request
app = Flask(__name__)

#----------------------------------------------------------------------------------------------

@app.route('/')
def home():
    return '''
    <p>Bienvenido a la página de Pol!</p>
    <p>Entra en <a href="/formulari">/formulari</a>.</p>
    '''

#----------------------------------------------------------------------------------------------

# Diccionario global con nombres de usuario y contraseñas válidos
usuarios_validos = {
    'pol': '1234',
    'joel': '1234',
    'enric': '1234'
}

#----------------------------------------------------------------------------------------------

# Formulario para ingresar usuario y contraseña
@app.route('/formulari', methods=['GET'])
def mostrar_formulario():
    return """
    <form method='post' action='/formulari'>
        Usuario:
        <input name='usuario' type='text' />
        <br>
        Contraseña:
        <input name='contrasenya' type='password' />
        <br>
        <input type='submit' value='Iniciar sesión'>
    </form>
    """
#----------------------------------------------------------------------------------------------

# Página que responde al formulario de usuario y contraseña
@app.route('/formulari', methods=['POST'])
def verificar_credenciales():
    usuario_ingresado = request.form["usuario"]
    contrasenya_ingresada = request.form["contrasenya"]

    # Verificar si las credenciales son válidas
    if usuario_ingresado in usuarios_validos and usuarios_validos[usuario_ingresado] == contrasenya_ingresada:
        return "OK: Credenciales válidas"
    else:
        return "ERROR: Credenciales incorrectas"
#----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
