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