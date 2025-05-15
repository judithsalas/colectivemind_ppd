# main.py
# Punto de entrada principal del proyecto CollectiveMind

from core.simulation import run_simulation

if __name__ == "__main__":
    import multiprocessing as mp
    mp.set_start_method("spawn")
    run_simulation()
