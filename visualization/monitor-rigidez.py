# Visualiza la evolución de la rigidez cognitiva de los agentes

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

class RigidityMonitor:
    def __init__(self, history_dict, config):
        self.history_dict = history_dict  # Diccionario compartido {id: [valores]}
        self.config = config
        self.fig, self.ax = plt.subplots()

    def animate(self, frame):
        self.ax.clear()
        for agent_id, rigidez in self.history_dict.items():
            if len(rigidez) > 0:
                self.ax.plot(rigidez, label=f"Agente {agent_id}")
        self.ax.set_ylim(0, 1)
        self.ax.set_title("Evolución de la rigidez cognitiva")
        self.ax.set_xlabel("Iteraciones")
        self.ax.set_ylabel("Rigidez")
        self.ax.legend()

    def start(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()
