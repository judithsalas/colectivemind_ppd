
# Proceso central que introduce eventos o alteraciones externas en la red de agentes

import asyncio
import random
import time
from communication.messaging import send_message

class Oracle:
    def __init__(self, agent_queues, config):
        self.agent_queues = agent_queues  # Diccionario {agent_id: queue}
        self.config = config
        self.event_interval = config.get("event_interval", 5)  # segundos

    async def start(self):
        """Inicia el ciclo de eventos del oráculo."""
        while True:
            await asyncio.sleep(self.event_interval)
            await self.dispatch_event()

    async def dispatch_event(self):
        """Genera un evento aleatorio y lo envía a uno o varios agentes."""
        event_type = random.choice(["rumor", "shock", "insight"])
        affected = random.sample(list(self.agent_queues.keys()), k=1)

        for agent_id in affected:
            queue = self.agent_queues[agent_id]
            message = self.generate_event_message(event_type)
            send_message(queue, message)
            print(f"[Oracle] Evento '{event_type}' enviado a {agent_id}")

    def generate_event_message(self, event_type):
        """Crea un mensaje que represente un evento del oráculo."""
        if event_type == "rumor":
            return {"type": "event", "event": "rumor", "opinion": [random.random() for _ in range(3)]}
        elif event_type == "shock":
            return {"type": "event", "event": "shock", "amplify": True}
        elif event_type == "insight":
            return {"type": "event", "event": "insight", "boost": 0.2}
        else:
            return {"type": "event", "event": "unknown"}