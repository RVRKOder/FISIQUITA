import numpy as np
import matplotlib.pyplot as plt

g = 9.81 

def tiro_parabolico(v0, angulo, interval):
    angulo_rad = np.radians(angulo)
    
    h_max = (v0**2 * np.sin(angulo_rad)**2) / (2 * g)
    
    t_total = (2 * v0 * np.sin(angulo_rad)) / g
    
    t = np.linspace(0, t_total, num=500)
    
    x = v0 * np.cos(angulo_rad) * t
    y = v0 * np.sin(angulo_rad) * t - 0.5 * g * t**2
    
    t_puntos = np.arange(0, t_total + interval, interval)
    x_puntos = v0 * np.cos(angulo_rad) * t_puntos
    y_puntos = v0 * np.sin(angulo_rad) * t_puntos - 0.5 * g * t_puntos**2
    
    return x, y, h_max, x_puntos, y_puntos, t_total, t_puntos

while True:
    plt.figure(figsize=(12, 8))
    colores = ['blue', 'orange', 'green', 'red', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'gray']
    i = 0


    while True:
        print(f"Disparo {i + 1}:")
        v0 = float(input("Ingrese la velocidad inicial (m/s): "))
        angulo = float(input("Ingrese el ángulo de disparo (grados): "))
        
        intervalo = float(input("Ingrese el intervalo de tiempo para los puntos (en segundos): "))
        
        x, y, h_max, x_puntos, y_puntos, t_total, t_puntos = tiro_parabolico(v0, angulo, intervalo)
        

        print(f"Altura máxima: {h_max:.2f} m")
        print(f"Distancia horizontal máxima: {x[-1]:.2f} m")
        print(f"Tiempo total de vuelo: {t_total:.2f} s\n")
        
        color = colores[i % len(colores)]  
        plt.plot(x, y, label=f"Disparo {i + 1}", color=color)
        plt.scatter(x_puntos, y_puntos, color=color, s=50, zorder=5)



        for j, (px, py, pt) in enumerate(zip(x_puntos, y_puntos, t_puntos)):
            offset_x = 8 if j % 2 == 0 else -5  
            offset_y = 10 if j % 2 == 0 else -10  
            plt.text(px + offset_x, py + offset_y, f"t={pt:.2f}s\nx={px:.2f}m\ny={py:.2f}m", fontsize=8, color='black', ha='center')

        i += 1
        
        continuar = input("¿Desea realizar otro disparo? (si/no): ").strip().lower()
        if continuar != 'si':
            break



    plt.title("Simulación de Tiro Parabólico con Puntos en Intervalos y Etiquetas Desplazadas")
    plt.xlabel("Distancia horizontal (m)")
    plt.ylabel("Altura (m)")
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.legend()
    plt.grid()
    plt.show()


    reiniciar = input("¿Desea reiniciar la simulación completa? (si/no): ").strip().lower()
    if reiniciar != 'si':
        print("¡Gracias por usar el simulador de tiro parabólico!")
        break
