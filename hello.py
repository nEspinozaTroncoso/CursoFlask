from datetime import datetime  # Importa la clase datetime para manejar fechas y horas
from flask_wtf import FlaskForm  # Importa FlaskForm para crear formularios web seguros
from wtforms import StringField, PasswordField, SubmitField  # Campos para el formulario
from wtforms.validators import (
    DataRequired,
    Length,
)  # Validadores para los campos del formulario
from flask import (
    Flask,
    render_template,
)  # Importa Flask y la función para renderizar plantillas HTML

# Crea la instancia principal de la aplicación Flask
app = Flask(__name__)
# Configura la clave secreta necesaria para los formularios WTForms
app.config.from_mapping(SECRET_KEY="dev")


# =========================
# Filtro personalizado para plantillas
# =========================
@app.add_template_filter
def today(date):
    # Convierte un objeto datetime en un string con formato día/mes/año
    return date.strftime("%d/%m/%Y")


# =========================
# Función global personalizada para plantillas
# =========================
@app.add_template_global
def repeat(s, n):
    # Repite el string 's' 'n' veces
    return s * n


# =========================
# Rutas principales
# =========================
@app.route("/")
@app.route("/index")
def index():
    # Renderiza la plantilla 'index.html' con variables de ejemplo
    name = "Nicolas Espinoza"  # Nombre de usuario
    friends = ["Pata", "Peta", "Pita", "Pota"]  # Lista de amigos
    date = datetime.now()  # Fecha y hora actual
    return render_template(
        "index.html",
        name=name,
        friends=friends,
        date=date,
    )


# =========================
# Ruta /hello con parámetros opcionales
# =========================
@app.route("/hello")
@app.route("/hello/<name>")
@app.route("/hello/<name>/<int:age>/<email>")
def hello(name=None, age=None, email=None):
    # Renderiza la plantilla 'hello.html' con los datos recibidos por la URL
    my_data = {
        "name": name,
        "age": age,
        "email": email,
    }
    return render_template("hello.html", data=my_data)


# =========================
# Formulario de registro de usuario usando Flask-WTF
# =========================
class RegisterForm(FlaskForm):
    # Campo para el nombre de usuario, obligatorio y con longitud entre 4 y 25 caracteres
    username = StringField(
        "Nombre de usuario: ", validators=[DataRequired(), Length(min=4, max=25)]
    )
    # Campo para la contraseña, obligatorio y con longitud entre 6 y 40 caracteres
    password = PasswordField(
        "Contraseña: ", validators=[DataRequired(), Length(min=6, max=40)]
    )
    # Botón para enviar el formulario
    submit = SubmitField("Registrar")


# =========================
# Ruta para registrar usuario
# =========================
@app.route("/auth/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()  # Instancia el formulario

    if form.validate_on_submit():
        # Si el formulario es válido, obtiene los datos ingresados
        username = form.username.data
        password = form.password.data
        # Devuelve los datos ingresados como respuesta (solo para demostración)
        return f"Nombre de usuario : {username} Contraseña: {password}"

    # Si no se envió o no es válido, muestra el formulario en la plantilla
    return render_template("auth/register.html", form=form)
