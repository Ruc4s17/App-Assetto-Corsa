import time
import json
import os
from sim_info import info

ac = info

# Criar pasta se não existir
if not os.path.exists("laps"):
    os.makedirs("laps")

print("Sistema de gravação de voltas iniciado...\n")

current_lap = ac.graphics.completedLaps
lap_data = []
lap_valid = True
start_time = time.time()

try:
    while True:
        # Ler dados
        speed = ac.physics.speedKmh #Feito
        gear = ac.physics.gear
        throttle = ac.physics.gas #Feito
        brake = ac.physics.brake #Feito
        rpm = ac.physics.rpms
        position = ac.graphics.normalizedCarPosition

        # Tempo relativo
        timestamp = time.time() - start_time

        # Verificar validade
        if ac.physics.numberOfTyresOut >= 3:
            lap_valid = False

        # Guardar ponto
        lap_data.append({
            "time": timestamp,
            "speed": speed,
            "gear": gear,
            "throttle": throttle,
            "brake": brake,
            "rpm": rpm,
            "position": position
        })

        # Detectar nova volta
        if ac.graphics.completedLaps != current_lap:
            print(f"Volta {current_lap} terminada! A guardar...")

            lap_info = {
                "lap_number": current_lap,
                "valid": lap_valid,
                "samples": lap_data
            }

            filename = f"laps/lap_{current_lap}.json"

            with open(filename, "w") as f:
                json.dump(lap_info, f, indent=2)

            print(f"Guardado em {filename} | Válida: {lap_valid}\n")

            # Reset
            current_lap = ac.graphics.completedLaps
            lap_data = []
            lap_valid = True
            start_time = time.time()

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nParado.")