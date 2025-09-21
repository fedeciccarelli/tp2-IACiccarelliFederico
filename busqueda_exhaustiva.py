# Búsqueda exhaustiva
# Probamos: B, B+ΔH, B-ΔH, B+2ΔH, B-2ΔH, ...

B = 0.0        # posición teórica inicial (mm)
DELTA_H = 0.2  # paso de búsqueda (mm)
H_MAX = 3.0    # límite ±H_max (mm)
TOL = 0.2      # tolerancia (mm)

A_REAL = 1.4   # meta real simulada

def alineado(posicion, meta, tolerancia):
    """True si posicion está dentro de tolerancia respecto a meta."""
    return abs(posicion - meta) <= tolerancia

def main():
    palpados = []
    k = 0
    encontrado = None

    print("=== Busqueda exhaustiva ===")
    print(f"B={B} mm | ΔH={DELTA_H} mm | H_max=±{H_MAX} mm | tol={TOL} mm | A_real={A_REAL} mm\n")

    while k * DELTA_H <= H_MAX:
        if k == 0:
            pos = B
            palpados.append(pos)
            print(f"Palpado #{len(palpados)} -> {pos:.3f} mm")
            if alineado(pos, A_REAL, TOL):
                encontrado = pos
                break
            k = 1
            continue

        # lado derecho
        pos = B + k * DELTA_H
        if abs(pos - B) <= H_MAX:
            palpados.append(pos)
            print(f"Palpado #{len(palpados)} -> {pos:.3f} mm")
            if alineado(pos, A_REAL, TOL):
                encontrado = pos
                break

        # lado izquierdo
        pos = B - k * DELTA_H
        if abs(pos - B) <= H_MAX:
            palpados.append(pos)
            print(f"Palpado #{len(palpados)} -> {pos:.3f} mm")
            if alineado(pos, A_REAL, TOL):
                encontrado = pos
                break

        k += 1

    print("\n--- Resultado ---")
    if encontrado is not None:
        print(f"ENCONTRADO en {encontrado:.3f} mm (palpados={len(palpados)})")
    else:
        print(f"NO ENCONTRADO dentro de ±{H_MAX} mm (palpados={len(palpados)})")

if __name__ == "__main__":
    main()
