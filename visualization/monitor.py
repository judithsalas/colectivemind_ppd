# monitor.py
# Visualización en tiempo real del estado de los agentes

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

class OpinionMonitor:
    def __init__(self, inboxes, config):
        self.inboxes = inboxes
        self.config = config
        self.opinion_dim = config["opinion_dim"]
        self.data = {i: [0.5] * self.opinion_dim for i in inboxes.keys()}

    def update_data(self):
        for agent_id, q in self.inboxes.items():
            while not q.empty():
                msg = q.get()
                if isinstance(msg, dict) and "opinion" in msg:
                    self.data[agent_id] = msg["opinion"]

    def animate(self, frame):
        self.update_data()
        plt.clf()
        for i, vec in self.data.items():
            plt.plot(range(len(vec)), vec, label=f"Agent {i}")
        plt.ylim(0, 1)
        plt.title("Evolución de Opiniones")
        plt.xlabel("Dimensiones")
        plt.ylabel("Valor de Opinión")
        plt.legend(loc='upper right')

    def start(self):
        fig = plt.figure()
        ani = animation.FuncAnimation(fig, self.animate, interval=1000)
        plt.show()
