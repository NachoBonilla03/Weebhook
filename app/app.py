def dibujar_cuadrado(tamano):
    for i in range(tamano):
        if i == 0 or i == tamano - 1:
            print("*" * tamano)
        else:
            print("*" + " " * (tamano - 2) + "*")

def dibujar_triangulo(tamano):
    for i in range(tamano):
        print(" " * (tamano - i - 1) + "*" * (2 * i + 1))

def dibujar_circulo(tamano):
    for i in range(tamano):
        for j in range(tamano):
            if (i - tamano // 2) ** 2 + (j - tamano // 2) ** 2 <= (tamano // 2) ** 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Dibujar figuras
print("Cuadrado:")
dibujar_cuadrado(5)
print("\nTriángulo:")
dibujar_triangulo(5)
print("\nCírculo:")
dibujar_circulo(10)
