from flask import Flask, render_template, request

app = Flask(__name__)
#ruta
"""
def suma():
    s_1 = 3+4
    return s_1
"""
@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    numero_a = request.form['numero_a']
    numero_b = request.form['numero_b']
    numero_a=float(numero_a)
    numero_b=float(numero_b)
    suma= numero_a+numero_b
    return suma

"""
@app.route("/", methods=['GET', 'POST'])
def ind():
  numero_b = " "
  if request.method == 'POST'and '"numero_b"' in request.form:
      # Aquí puedes agregar el código que se ejecutará cuando se presione el botón
      numero_b= numero_b
      #"Opcion A seleccionada"
      print (numero_b)
      print('El botón ha sido presionado')
  return render_template ("index.html",  numero_b= numero_b)
"""

@app.route("/", methods=['GET', 'POST'])
def index():
  output = " "
  if request.method == 'POST'and 'button' in request.form:
      # Aquí puedes agregar el código que se ejecutará cuando se presione el botón
      output =procesar_formulario()
      #"Opcion A seleccionada"
      print (output)
      print('El botón ha sido presionado')
  return render_template ("index.html", output=output)
#"<h1>Hello World!</h1>"
##render_template ("index.html")

#ruta
@app.route('/saludos')
def saludos():
    return "<h1>Hola a todos!</h1>"



if __name__ =="__main__":
    app.run(debug=True)
    