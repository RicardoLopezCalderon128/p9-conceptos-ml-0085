# Ricardo Lopez 0085
import pandas as pd
print(pd.__version__) # Output: 1.5.2
datos3 = {
    'distancia_km': [0.8, 7.5, 2.0, 3.5, 5.2],
    'trafico_nivel': [1, 3, 2, 1, 3],
    'edad_repartidor': [20, 38, 27, 33, 42],
    'tiempo_entrega_min': [8, 68, 18, 20, 48]
}
df = pd.DataFrame(datos3)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))
print("programa echo por Ricardo Antonio Lopez NC = 0085")