from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
productos = {}
@app.route('/')
def index():
    return render_template("index.html")

def agregar_producto():
    print(request)
    print(request.args)
    nombre = request.args.get('p1')
    precio = request.args.get('p2')
    cantidad = request.args.get('p3')
    
    #Validar datos ingresados 
    if not nombre or not precio or not cantidad:
        return "Error: Por favor, ingrese todos los datos del producto"
    try:
        precio = float(precio)
        cantidad = int(cantidad)
    except ValueError:
        return "Error, el precio y la cantidad del producto deben ser valores numericos"
    
    #Agregar el producto al diccionario
    productos[nombre]={'precio': precio, 'cantidad': cantidad}
    return "Producto agregado correctamente"

@app.route('/mostrar_productos')
def mostrar():
    return render_template("mostrar.html", productos = productos)


def error_404(error):
    #return render_template('error_404.html'), 404 en caso de direccionar a otra vista donde indique que no existe
    return redirect(url_for('index'))#No coloca el punto html, se hace referencia a la vista no a la url





if __name__ == '__main__':
    app.add_url_rule('/agregar_producto', view_func=agregar_producto)
    #Manejador de errores que recibe la función
    app.register_error_handler(404, error_404)
    app.run(debug=True, port=9999)