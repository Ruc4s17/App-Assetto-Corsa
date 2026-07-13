import json
import matplotlib.pyplot as plt
import numpy as np

# -------- CONFIG --------
lap1_file = "laps/lap_1.json"
lap2_file = "laps/lap_2.json"


# -------- FUNÇÃO PARA CARREGAR --------
def load_lap(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data["samples"]


# -------- CARREGAR DADOS --------
lap1 = load_lap(lap1_file)
lap2 = load_lap(lap2_file)


# -------- EXTRAIR DADOS --------
def extract(lap):
    lap_ordenada = sorted(lap, key=lambda x: x["position"])

    pos = [p["position"] for p in lap_ordenada]
    speed = [p["speed"] for p in lap_ordenada]
    throttle = [p["throttle"] for p in lap_ordenada]
    brake = [p["brake"] for p in lap_ordenada]
    gear = [p["gear"] for p in lap_ordenada]
    time = [p["time"] for p in lap_ordenada]
    rpm = [p["rpm"] for p in lap_ordenada]
    cut_present = [p["cut_present"] for p in lap_ordenada]
    steer = [p["steer"] for p in lap_ordenada]
    return pos, speed, throttle, brake, gear, time, rpm, cut_present, steer


pos1, speed1, throttle1, brake1, gear1, time1, rpm1, cut_present1, steer1 = extract(lap1)
pos2, speed2, throttle2, brake2, gear2, time2, rpm2, cut_present2, steer2 = extract(lap2)

plt.figure(figsize=(16, 24))
# -------- GRÁFICO VELOCIDADE --------
plt.subplot(8,1,1)
plt.plot(pos1, speed1, label="Lap 1")
plt.plot(pos2, speed2, label="Lap 2")
plt.title("Comparação de Velocidade")
plt.xlabel("Posição na pista (0 → 1)")
plt.ylabel("Velocidade (km/h)")
plt.legend()
plt.grid()
# -------- GRÁFICO THROTTLE --------
plt.subplot(8,1,2)
plt.plot(pos1, throttle1, label="Lap 1")
plt.plot(pos2, throttle2, label="Lap 2")
plt.title("Throttle")
plt.xlabel("Posição")
plt.ylabel("Throttle")
plt.legend()
plt.grid()
# -------- GRÁFICO BRAKE --------
plt.subplot(8,1,3)
plt.plot(pos1, brake1, label="Lap 1")
plt.plot(pos2, brake2, label="Lap 2")
plt.title("Brake")
plt.xlabel("Posição")
plt.ylabel("Brake")
plt.legend()
plt.grid()
#-------- GRÁFICO RPM --------
plt.subplot(8,1,4)
plt.plot(pos1, rpm1, label="Lap 1")
plt.plot(pos2, rpm2, label="Lap 2")
plt.title("RPM")
plt.xlabel("Posição")
plt.ylabel("RPM")
plt.legend()
plt.grid()
#------- GRÁFICO CUT PRESENT --------
plt.subplot(8,1,5)
plt.plot(pos1, cut_present1, label="Lap 1")
plt.plot(pos2, cut_present2, label="Lap 2")
plt.title("Corte na Pista")
plt.xlabel("Posição")
plt.ylabel("Corte Presente")
plt.legend()
plt.grid()
plt.legend()
plt.grid()
#-------- GRÁFICO DELTA ------------
delta1 = [t - time1[0] for t in time1]
delta2 = [t - time2[0] for t in time2]
pos_comum = np.linspace(0, 1, 1000)
time1_interp = np.interp(pos_comum, pos1, delta1)
time2_interp = np.interp(pos_comum, pos2, delta2)
delta_tempo = time2_interp - time1_interp

plt.subplot(8, 1, 6)

plt.plot(pos_comum, delta_tempo, color="purple", linewidth=2, label="Delta (L2 - L1)")
plt.axhline(0, color="black", linestyle="--", alpha=0.6)

plt.title("Delta de Tempo Real (Segundos)")
plt.xlabel("Posição")
plt.ylabel("Diferença (s)")
plt.ylim(-5, 5)
plt.legend()
plt.grid(True)

plt.text(0.02, max(delta_tempo)*0.7 if max(delta_tempo) > 0 else 0.5, "↑ Lap 1 Mais Rápida", color="blue", fontsize=9)
plt.text(0.02, min(delta_tempo)*0.7 if min(delta_tempo) < 0 else -0.5, "↓ Lap 2 Mais Rápida", color="orange", fontsize=9)
#-------- GRÁFICO GEAR ------------
plt.subplot(8,1,7)
plt.plot(pos1, gear1, label="Lap 1")
plt.plot(pos2, gear2, label="Lap 2")
plt.title("Gear")
plt.xlabel("Posição")
plt.ylabel("Gear")
plt.legend()
plt.grid()
#-------- GRÁFICO STEER ------------
plt.subplot(8,1,8)
plt.plot(pos1, steer1, label="Lap 1")
plt.plot(pos2, steer2, label="Lap 2")
plt.title("Steer")
plt.xlabel("Posição")
plt.ylabel("Steer")
plt.legend()
plt.grid()

plt.subplots_adjust(hspace=0.6, top=0.95, bottom=0.05)
plt.show()
