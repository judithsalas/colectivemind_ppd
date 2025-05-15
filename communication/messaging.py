# Funciones auxiliares para la comunicación entre procesos

import multiprocessing as mp

def send_message(queue: mp.Queue, message):
    """Envía un mensaje a través de una cola."""
    try:
        queue.put(message)
    except Exception as e:
        print(f"[send_message] Error al enviar mensaje: {e}")

def receive_message(queue: mp.Queue):
    """Recibe un mensaje de una cola (bloqueante)."""
    try:
        return queue.get()
    except Exception as e:
        print(f"[receive_message] Error al recibir mensaje: {e}")
        return None
