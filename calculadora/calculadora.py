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