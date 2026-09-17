import time
import concurrent.futures

N = 20 # Número de Fibonacci a calcular

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def calcular_fibonacci_paralelo(n_elementos, executor_type):
    #Inicio tiempo para medir el tiempo de ejecución
    inicio = time.time()

    # Crear un pool de hilos o procesos para calcular Fibonacci en paralelo
    resultados = [0] * n_elementos

    # Usar un contexto para manejar el pool de hilos o procesos
    with executor_type() as executor:
        # Crear una lista de futuros para cada cálculo de Fibonacci
        futures = [executor.submit(fibonacci, i) for i in range(n_elementos)]

        # Esperar a que todos los futuros se completen y almacenar los resultados
        for future in concurrent.futures.as_completed(futures):
            # Obtener el índice del futuro completado y almacenar el resultado correspondiente
            i = futures.index(future)
            # Almacenar el resultado en la lista de resultados segun el índice )
            resultados[i] = future.result()
            
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    
    print(f"Fibonacci ({n_elementos}): {resultados}")
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")

if __name__ == "__main__":
    calcular_fibonacci_paralelo(N, concurrent.futures.ThreadPoolExecutor) # o ProcessPoolExecutor