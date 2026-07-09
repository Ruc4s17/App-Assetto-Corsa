import json
import matplotlib.pyplot as plt

# -------- CONFIG --------
lap1_file = "laps/lap_0.json"
lap2_file = "laps/lap_1.json"


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
    pos = [p["position"] for p in lap]
    speed = [p["speed"] for p in lap]
    throttle = [p["throttle"] for p in lap]
    brake = [p["brake"] for p in lap]
    return pos, speed, throttle, brake


pos1, speed1, throttle1, brake1 = extract(lap1)
pos2, speed2, throttle2, brake2 = extract(lap2)


# -------- GRÁFICO VELOCIDADE --------
plt.figure()
plt.title("Comparação de Velocidade")
plt.plot(pos1, speed1, label="Lap 1")
plt.plot(pos2, speed2, label="Lap 2")
plt.xlabel("Posição na pista (0 → 1)")
plt.ylabel("Velocidade (km/h)")
plt.legend()
plt.grid()

# -------- GRÁFICO THROTTLE --------
plt.figure()
plt.title("Throttle")
plt.plot(pos1, throttle1, label="Lap 1")
plt.plot(pos2, throttle2, label="Lap 2")
plt.xlabel("Posição")
plt.ylabel("Throttle")
plt.legend()
plt.grid()

# -------- GRÁFICO TRAVÃO --------
plt.figure()
plt.title("Brake")
plt.plot(pos1, brake1, label="Lap 1")
plt.plot(pos2, brake2, label="Lap 2")
plt.xlabel("Posição")
plt.ylabel("Brake")
plt.legend()
plt.grid()

plt.show()