"""Grafo mínimo: leer documentos -> comparar palabras -> mostrar resultado."""

from pathlib import Path


RAIZ = Path(__file__).resolve().parents[2]
TEMAS = ("perfiles", "créditos", "calificaciones")


def leer(estado):
    estado["mvp"] = (RAIZ / "docs/mvp.md").read_text(encoding="utf-8")
    estado["wbs"] = (RAIZ / "docs/wbs.md").read_text(encoding="utf-8")


def comparar(estado):
    estado["resultados"] = {}
    for tema in TEMAS:
        estado["resultados"][tema] = (
            tema in estado["mvp"].casefold(),
            tema in estado["wbs"].casefold(),
        )


def mostrar(estado):
    print("\nPresencia de palabras (no valida la coherencia del alcance):")
    for tema, (en_mvp, en_wbs) in estado["resultados"].items():
        print(f"  {tema}: MVP={'sí' if en_mvp else 'no'}, "
              f"WBS={'sí' if en_wbs else 'no'}")


# Nodos: cada nombre identifica una función que realiza un paso.
NODOS = {"leer": leer, "comparar": comparar, "mostrar": mostrar}

# Aristas: indican a qué nodo pasar después. None significa terminar.
ARISTAS = {"leer": "comparar", "comparar": "mostrar", "mostrar": None}


def ejecutar():
    estado = {}  # Memoria compartida por los nodos durante esta ejecución.
    actual = "leer"
    while actual is not None:
        print(f"Nodo: {actual}")
        NODOS[actual](estado)
        actual = ARISTAS[actual]


if __name__ == "__main__":
    ejecutar()
