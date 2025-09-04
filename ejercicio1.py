import math

def calcular_descuento(cantidad):
    precio_base = 50
    if cantidad >= 5:
        descuento = 0.30
    elif cantidad >= 3:
        descuento = 0.20
    else:
        descuento = 0.0
    precio_final = precio_base * (1 - descuento)
    total = precio_final * cantidad
    return total

def calcular_volumen_esfera(radio):
    pi = 3.1416
    volumen = (4/3) * pi * (radio ** 3)
    return volumen
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Calcular descuento en compras de software")
        print("2. Calcular volumen de una esfera")
        print("3. Salir del programa")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            try:
                cantidad = int(input("Ingrese la cantidad de licencias a comprar: "))
                if cantidad <= 0:
                    print("Debe ingresar una cantidad positiva.")
                    continue
                total_pagar = calcular_descuento(cantidad)
                print(f"El total a pagar por {cantidad} licencias es: ${total_pagar:.2f}")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        elif opcion == "2":
            try:
                radio = float(input("Ingrese el radio de la esfera: "))
                if radio <= 0:
                    print("El radio debe ser un número positivo.")
                    continue
                volumen = calcular_volumen_esfera(radio)
                print(f"El volumen de la esfera con radio {radio} es: {volumen:.2f}")
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
        elif opcion == "3":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida. Intente con 1, 2 o 3.")

if __name__ == "__main__":
    menu()
