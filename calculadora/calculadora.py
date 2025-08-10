# Función suma dos números

def add(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def main():
    print("Calculadora v1 — SUMA")
    try:
        a = float(input("Ingrese primer número: "))
        b = float(input("Ingrese segundo número: "))
    except ValueError:
        print("Entrada inválida. Usa números.")
        return
    print(f"Resultado: {a} + {b} = {add(a, b)}")


if __name__ == "__main__":
    main()


def add(a, b):
    return a + b


def sub(a, b):
    return a - b

#resta
def main():
    print("Calculadora v2 — SUMA y RESTA")
    op = input("Operación (add/sub): ").strip().lower()
    try:
        a = float(input("Ingrese primer número: "))
        b = float(input("Ingrese segundo número: "))
    except ValueError:
        print("Entrada inválida. Usa números.")
        return

    if op == "add":
        print(f"{a} + {b} = {add(a,b)}")
    elif op == "sub":
        print(f"{a} - {b} = {sub(a,b)}")
    else:
        print("Operación no soportada. Usa 'add' o 'sub'.")


if __name__ == "__main__":
    main()


# multiplicacion

def add(a, b):
# Añadimos división con control de división por cero (cuarto commit: dividir)

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    """Devuelve a / b. Lanza ZeroDivisionError si b == 0."""
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    return a / b


def main():
    print("Calculadora v4 — SUMA, RESTA, MULT, DIV")
    op = input("Operación (add/sub/mul/div): ").strip().lower()
    try:
        a = float(input("Ingrese primer número: "))
        b = float(input("Ingrese segundo número: "))
    except ValueError:
        print("Entrada inválida. Usa números.")
        return

    try:
        if op == "add":
            print(f"{a} + {b} = {add(a,b)}")
        elif op == "sub":
            print(f"{a} - {b} = {sub(a,b)}")
        elif op == "mul":
            print(f"{a} * {b} = {mul(a,b)}")
        elif op == "div":
            print(f"{a} / {b} = {div(a,b)}")
        else:
            print("Operación no soportada. Usa 'add', 'sub', 'mul' o 'div'.")
    except ZeroDivisionError as e:
        print(e)


if __name__ == "__main__":
    main()

# funcion dividir

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    """Devuelve a / b. Lanza ZeroDivisionError si b == 0."""
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    return a / b


def main():
    print("Calculadora v4 — SUMA, RESTA, MULT, DIV")
    op = input("Operación (add/sub/mul/div): ").strip().lower()
    try:
        a = float(input("Ingrese primer número: "))
        b = float(input("Ingrese segundo número: "))
    except ValueError:
        print("Entrada inválida. Usa números.")
        return

    try:
        if op == "add":
            print(f"{a} + {b} = {add(a,b)}")
        elif op == "sub":
            print(f"{a} - {b} = {sub(a,b)}")
        elif op == "mul":
            print(f"{a} * {b} = {mul(a,b)}")
        elif op == "div":
            print(f"{a} / {b} = {div(a,b)}")
        else:
            print("Operación no soportada. Usa 'add', 'sub', 'mul' o 'div'.")
    except ZeroDivisionError as e:
        print(e)


if __name__ == "__main__":
    main()


# 

