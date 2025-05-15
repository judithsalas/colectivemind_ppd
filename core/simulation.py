# Debate coordinado entre filósofos con interacción estructurada

import multiprocessing as mp
import time
from agents import Agent
from utils.config import get_default_config


def create_philosophers(config, manager):
    names_positions = [
        ("Sócrates", [0.9, 0.4, 0.1]),
        ("Nietzsche", [0.2, 0.9, 0.4]),
        ("Kant", [0.6, 0.6, 0.9]),
        ("Simone de Beauvoir", [0.7, 0.3, 0.8]),
        ("Confucio", [0.4, 0.8, 0.2])
    ]
    n = len(names_positions)
    inboxes = {i: mp.Queue() for i in range(n)}
    barrier = mp.Barrier(n)
    shared_data = manager.dict({i: names_positions[i][1][:] for i in range(n)})
    agents = []
    for i, (name, pos) in enumerate(names_positions):
        outboxes = {j: inboxes[j] for j in inboxes if j != i}
        agent = Agent(
            agent_id=i,
            name=name,
            position_vector=pos,
            inbox=inboxes[i],
            outboxes=outboxes,
            config=config,
            barrier=barrier,
            shared_data=shared_data
        )
        agents.append(agent)
    return agents, inboxes, names_positions, shared_data


def start_agents(agents):
    for agent in agents:
        agent.start()


def stop_agents(agents, inboxes):
    for q in inboxes.values():
        q.put("TERMINATE")
    for agent in agents:
        agent.join()


def determine_winner(shared_data, names):
    avg = [
        sum(shared_data[i][j] for i in shared_data) / len(shared_data)
        for j in range(len(shared_data[0]))
    ]
    distances = [
        (names[i], sum(abs(a - b) for a, b in zip(shared_data[i], avg)))
        for i in shared_data
    ]
    distances.sort(key=lambda x: x[1])
    print(f"\n[Resultado] El pensador más influyente ha sido: {distances[0][0]}\n")


def run_simulation():
    config = get_default_config()
    manager = mp.Manager()
    agents, inboxes, names_positions, shared_data = create_philosophers(config, manager)
    start_agents(agents)

    try:
        rounds = config.get("rounds", 5)
        for r in range(rounds):
            print(f"\n🗣️ Ronda {r+1}")
            for i, (name, _) in enumerate(names_positions):
                print(f"\n👉 {name} toma la palabra")
                for q in inboxes.values():
                    q.put({"speaker": i})
                time.sleep(1)
    except KeyboardInterrupt:
        print("\n[Simulación] Detenida manualmente.")
    finally:
        stop_agents(agents, inboxes)
        print("[Simulación] Debate finalizado.")
        determine_winner(shared_data, [name for name, _ in names_positions])


if __name__ == "__main__":
    mp.set_start_method("spawn")
    run_simulation()
