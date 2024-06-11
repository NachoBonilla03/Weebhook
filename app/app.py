from flask import Flask, render_template_string

app = Flask(__name__)

def dibujar_cuadrado(tamano):
    square = ""
    for i in range(tamano):
        if i == 0 or i == tamano - 1:
            square += "*" * tamano + "\n"
        else:
            square += "*" + " " * (tamano - 2) + "*" + "\n"
    return square

def dibujar_triangulo(tamano):
    triangle = ""
    for i in range(tamano):
        triangle += " " * (tamano - i - 1) + "*" * (2 * i + 1) + "\n"
    return triangle

def dibujar_circulo(tamano):
    circle = ""
    for i in range(tamano):
        for j in range(tamano):
            if (i - tamano // 2) ** 2 + (j - tamano // 2) ** 2 <= (tamano // 2) ** 2:
                circle += "*"
            else:
                circle += " "
        circle += "\n"
    return circle

@app.route('/')
def home():
    return '''
    <h1>Choose a shape to draw</h1>
    <ul>
        <li><a href="/cuadrado/5">Draw 5x5 Square</a></li>
        <li><a href="/triangulo/5">Draw 5-row Triangle</a></li>
        <li><a href="/circulo/10">Draw 10x10 Circle</a></li>
    </ul>
    '''

@app.route('/cuadrado/<int:tamano>')
def cuadrado(tamano):
    square = dibujar_cuadrado(tamano)
    return render_template_string('<pre>{{ square }}</pre>', square=square)

@app.route('/triangulo/<int:tamano>')
def triangulo(tamano):
    triangle = dibujar_triangulo(tamano)
    return render_template_string('<pre>{{ triangle }}</pre>', triangle=triangle)

@app.route('/circulo/<int:tamano>')
def circulo(tamano):
    circle = dibujar_circulo(tamano)
    return render_template_string('<pre>{{ circle }}</pre>', circle=circle)

if __name__ == '__main__':
    app.run(debug=True)
