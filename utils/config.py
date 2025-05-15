# config.py
# Configuración por defecto para la simulación CollectiveMind

def get_default_config():
    return {
        "n_agents": 5,               # Número de agentes
        "opinion_dim": 3,           # Dimensión del vector de opinión
        "influence_factor": 0.1,    # Grado de influencia externa
        "event_interval": 5         # Intervalo en segundos entre eventos del oráculo
    }
