# agent.py
# Filósofo que participa en un debate por turnos, escuchando y reaccionando a argumentos

import multiprocessing as mp
import random
import time
from datetime import datetime
from communication.messaging import receive_message

class Agent(mp.Process):
    def __init__(self, agent_id, name, position_vector, inbox, outboxes, config, barrier, shared_data):
        super().__init__()
        self.agent_id = agent_id
        self.name = name
        self.position = position_vector
        self.inbox = inbox
        self.outboxes = outboxes
        self.config = config
        self.conviction = random.uniform(0.0, 1.0)
        self.barrier = barrier
        self.shared_data = shared_data

    def run(self):
        print(f"[{self.name}] se une al debate con convicción inicial: {self.conviction:.2f}")
        while True:
            message = receive_message(self.inbox)
            if message == "TERMINATE":
                print(f"[{self.name}] abandona el foro filosófico.")
                break

            speaker_id = message.get("speaker")
            if speaker_id == self.agent_id:
                print(f"[{self.name}] expone su argumento.")
            else:
                other_position = self.shared_data[speaker_id]
                ts = datetime.now().strftime("%H:%M:%S")
                dist = sum(abs(a - b) for a, b in zip(self.position, other_position))
                openness = 1 - self.conviction
                if random.random() < openness:
                    alpha = self.config.get("influence_factor", 0.2)
                    self.position = [
                        (1 - alpha) * a + alpha * b
                        for a, b in zip(self.position, other_position)
                    ]
                    self.conviction = max(0.0, self.conviction - 0.05)
                    print(f"[{ts}] {self.name} reconsidera tras escuchar a su colega.")
                else:
                    self.conviction = min(1.0, self.conviction + 0.02)
                    print(f"[{ts}] {self.name} permanece firme ante el argumento contrario.")

            self.shared_data[self.agent_id] = self.position[:]
            self.barrier.wait()
