# Función y script mínimo que suma dos números
def add(a, b):
    return a + b

def main():
    print("Calculadora v1 — SUMA")
    a = float(input("Ingrese primer número: "))
    b = float(input("Ingrese segundo número: "))
    print(f"Resultado: {a} + {b} = {add(a, b)}")

if __name__ == "__main__":
    main()

# Añadimos resta
def sub(a, b):
    return a - b

# Añadimos multiplicación
def mul(a, b):
    return a * b

# Añadimos división con control de cero
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    return a / b

# Añadimos potencia
def power(a, b):
    return a ** b

# Menú interactivo con todas las operaciones
def main():
    print("Calculadora v6 — SUMA, RESTA, MULT, DIV, POTENCIA")
    op = input("Operación (add/sub/mul/div/pow): ").strip().lower()
    a = float(input("Ingrese primer número: "))
    b = float(input("Ingrese segundo número: "))

    try:
        if op == "add":
            print(f"{a} + {b} = {add(a, b)}")
        elif op == "sub":
            print(f"{a} - {b} = {sub(a, b)}")
        elif op == "mul":
            print(f"{a} * {b} = {mul(a, b)}")
        elif op == "div":
            print(f"{a} / {b} = {div(a, b)}")
        elif op == "pow":
            print(f"{a} ^ {b} = {power(a, b)}")
        else:
            print("Operación no soportada")
    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()
