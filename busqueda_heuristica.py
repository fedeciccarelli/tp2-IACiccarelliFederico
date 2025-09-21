# Búsqueda heurística (A*)
# Simula la búsqueda de la posición A desde la posición B

B = 0.0         # posición inicial teórica (mm)
DELTA_H = 0.2   # paso de desplazamiento (mm)
H_MAX = 3.0     # límite máximo de búsqueda (mm)
TOL = 0.2       # tolerancia (mm)

A_REAL = -0.8   # meta real simulada

def heuristica(posicion, meta):
    """Distancia estimada a la meta (h)."""
    return abs(posicion - meta)

def alineado(posicion, meta, tolerancia):
    return abs(posicion - meta) <= tolerancia

def main():
    # Nodo representado como (posicion, g, f)
    abiertos = [(B, 0, heuristica(B, A_REAL))]
    cerrados = []
    palpados = []

    print("=== Busqueda heuristica A* ===")
    print(f"B={B} mm | ΔH={DELTA_H} mm | A_real={A_REAL} mm | tol={TOL} mm\n")

    while abiertos:
        # Tomo el nodo con menor f
        abiertos.sort(key=lambda x: x[2])
        pos, g, f = abiertos.pop(0)
        palpados.append(pos)
        print(f"Palpado #{len(palpados)} -> {pos:.3f} mm (f={f:.3f})")

        if alineado(pos, A_REAL, TOL):
            print("\n--- Resultado ---")
            print(f"ENCONTRADO en {pos:.3f} mm (palpados={len(palpados)})")
            return

        # Generar sucesores (vecinos: derecha e izquierda)
        for mov in [DELTA_H, -DELTA_H]:
            nuevo = pos + mov
            if abs(nuevo - B) <= H_MAX and nuevo not in cerrados:
                g_nuevo = g + DELTA_H
                h_nuevo = heuristica(nuevo, A_REAL)
                f_nuevo = g_nuevo + h_nuevo
                abiertos.append((nuevo, g_nuevo, f_nuevo))

        cerrados.append(pos)

    print("\n--- Resultado ---")
    print(f"NO ENCONTRADO dentro de ±{H_MAX} mm (palpados={len(palpados)})")

if __name__ == "__main__":
    main()
