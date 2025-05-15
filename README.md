# CollectiveMind: Debate Filosófico Paralelo y Distribuido

Este proyecto simula un debate entre cinco filósofos clásicos utilizando técnicas de **programación paralela y distribuida** con Python. Cada filósofo es un agente que defiende una postura ideológica, interactúa por turnos, y puede modificar su opinión dependiendo de su nivel de convicción.

## Participantes del debate
- **Sócrates** – Mayéutica, ética
- **Nietzsche** – Nihilismo, voluntad de poder
- **Kant** – Deontología, razón pura
- **Simone de Beauvoir** – Existencialismo, feminismo
- **Confucio** – Armonía, tradición

## Tecnologías y conceptos usados
- `multiprocessing.Process` para ejecutar agentes en paralelo.
- `multiprocessing.Queue` para comunicación entre agentes.
- `multiprocessing.Barrier` para sincronizar turnos.
- `Manager().dict()` para compartir el estado global.
- Turnos estructurados y control centralizado (moderador).

## Objetivo del sistema
Simular un entorno en el que cada filósofo:
- Toma la palabra por turnos.
- Expone su postura (vector de ideas).
- Influye o es influido por los demás dependiendo de su nivel de convicción.
- Modifica su pensamiento según la lógica del debate.

Al final, se calcula automáticamente quién fue el **más influyente** del debate.

## Ejecución
Asegúrate de tener Python 3.10+ instalado.

```bash
python main.py
```

## Requisitos (puedes crear un entorno virtual)
```bash
pip install -r requirements.txt
```

## Mejores extensiones posibles
- Visualización en tiempo real de opiniones y convicciones.
- Logs detallados por agente.
- Exportación de resultados a archivo.


Proyecto para la asignatura **Programación Paralela y Distribuida (PPD)**
