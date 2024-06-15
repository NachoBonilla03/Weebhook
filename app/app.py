from flask import Flask, request, jsonify

app = Flask(__name__)

# Define functions to draw shapes
def draw_square(size):
    output = ""
    for i in range(size):
        if i == 0 or i == size - 1:
            output += "*" * size + "\n"
        else:
            output += "*" + " " * (size - 2) + "*" + "\n"
    return output

def draw_triangle(size):
    output = ""
    for i in range(size):
        output += " " * (size - i - 1) + "*" * (2 * i + 1) + "\n"
    return output

def draw_circle(size):
    output = ""
    for i in range(size):
        for j in range(size):
            if (i - size // 2) ** 2 + (j - size // 2) ** 2 <= (size // 2) ** 2:
                output += "*"
            else:
                output += " "
        output += "\n"
    return output

# Define routes to handle shape drawing requests
@app.route("/draw-square/<int:size>")
def draw_square_api(size):
    square_output = draw_square(size)
    return jsonify({"square": square_output})

@app.route("/draw-triangle/<int:size>")
def draw_triangle_api(size):
    triangle_output = draw_triangle(size)
    return jsonify({"triangle": triangle_output})

@app.route("/draw-circle/<int:size>")
def draw_circle_api(size):
    circle_output = draw_circle(size)
    return jsonify({"circle": circle_output})

@app.route("/work-progress")
def print_work_in_progress():
    return jsonify({"Proximamente esto": "Trabajo en proceso..."})

@app.route("/")
def drawall():
    circle_output = draw_circle(5)
    triangle_output = draw_triangle(5)
    square_output = draw_square(5)
    return jsonify({"circle": circle_output, "triangle": triangle_output, "square": square_output, "proximamente":"prueba con el tigre"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
