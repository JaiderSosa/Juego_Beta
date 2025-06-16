
import tkinter as tk
from tkinter import messagebox
import random

# Clase base Personaje
class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.__vida = 0
        self.__ataque = ataque
        self.__defensa = defensa
        self.set_vida(vida)

    def get_vida(self):
        return self.__vida

    def set_vida(self, nueva_vida):
        self.__vida = max(0, min(100, nueva_vida))

    def get_ataque(self):
        return self.__ataque

    def get_defensa(self):
        return self.__defensa

    def esta_vivo(self):
        return self.__vida > 0

    def atacar(self, objetivo):
        pass

    def __str__(self):
        return f"{self.nombre} - Vida: {self.get_vida()}"

# Clases hijas
class Guerrero(Personaje):
    def atacar(self, objetivo):
        danio = self.get_ataque() * 1.2 - objetivo.get_defensa()
        danio = max(0, danio)
        objetivo.set_vida(objetivo.get_vida() - danio)
        return f"{self.nombre} ataca con fuerza a {objetivo.nombre} causando {danio:.1f} de daño."

class Mago(Personaje):
    def atacar(self, objetivo):
        danio = self.get_ataque()
        objetivo.set_vida(objetivo.get_vida() - danio)
        return f"{self.nombre} lanza un hechizo a {objetivo.nombre} causando {danio:.1f} de daño (ignora defensa)."

class Arquero(Personaje):
    def atacar(self, objetivo):
        if self.get_ataque() > objetivo.get_defensa():
            danio = (self.get_ataque() - objetivo.get_defensa()) * 2
        else:
            danio = self.get_ataque() - objetivo.get_defensa()
        danio = max(0, danio)
        objetivo.set_vida(objetivo.get_vida() - danio)
        return f"{self.nombre} dispara una flecha a {objetivo.nombre} causando {danio:.1f} de daño."

# Funcionalidad del juego con interfaz
class JuegoBatalla:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Guardians of the Ancient Kingdom")

        # Crear personajes
        self.p1 = Guerrero("Thoran el Guerrero", 100, 30, 20)
        self.p2 = Mago("Elyra la Maga", 80, 40, 10)

        self.label_estado = tk.Label(ventana, text="", justify="left")
        self.label_estado.pack(pady=10)

        self.boton_turno = tk.Button(ventana, text="Siguiente Turno", command=self.turno)
        self.boton_turno.pack(pady=5)

        self.mostrar_estado()

    def mostrar_estado(self):
        estado = f"{self.p1}\n{self.p2}"
        self.label_estado.config(text=estado)

    def turno(self):
        if not (self.p1.esta_vivo() and self.p2.esta_vivo()):
            ganador = self.p1 if self.p1.esta_vivo() else self.p2
            messagebox.showinfo("Fin del juego", f"El ganador es {ganador.nombre} con {ganador.get_vida():.1f} de vida.")
            self.boton_turno.config(state="disabled")
            return

        atacante = random.choice([self.p1, self.p2])
        defensor = self.p2 if atacante == self.p1 else self.p1

        resultado = atacante.atacar(defensor)
        messagebox.showinfo("Ataque", resultado)
        self.mostrar_estado()

# Iniciar interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoBatalla(root)
    root.mainloop()
