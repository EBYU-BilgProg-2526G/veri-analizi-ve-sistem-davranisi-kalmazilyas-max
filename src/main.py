# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 18:03:18 2026

@author: İLYAS
"""

import csv
import os
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = "data/sample_signal.csv"
REPORT_PATH = "report/report.md"
FIG_PATH = "report/figures/time_signal.png"

# -------------------- Görev 1 — Veri Okuma --------------------
import csv
import numpy as np
def load_signal_csv(path):
    t = []
    x = []

    with open(path, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # başlığı geç
        for row in reader:
            if len(row) >= 2:
                t.append(float(row[0]))
                x.append(float(row[1]))
    return np.array(t), np.array(x)
t, x = load_signal_csv("kayit.csv")
print(load_signal_csv("kayit.csv")) 

# -------------------- Görev 2 — Temel Analiz --------------------
def compute_basic_stats(x):
    return {
        "mean": float(np.mean(x)),
        "std": float(np.std(x)),
        "rms": float(np.sqrt(np.mean(x**2))),
        "min": float(np.min(x)),
        "max": float(np.max(x)),
    }

# -------------------- Görev 3 — Örnekleme Frekansı --------------------
def compute_sampling_frequency(t):
    dt = t[1] - t[0]
    fs = 1.0 / dt
    return fs, dt

# -------------------- Görev 4 — Hareketli Ortalama Filtresi --------------------
def moving_average(x, window=5):
    y = np.zeros_like(x)
    for i in range(len(x)):
        start = max(0, i - window + 1)
        y[i] = np.mean(x[start:i+1])
    return y

# -------------------- Görev 5 — Grafik Çizimi --------------------
def plot_signals(t, x, y, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    plt.figure()
    plt.plot(t, x, label="Ham Sinyal")
    plt.plot(t, y, label="Filtreli Sinyal")
    plt.xlabel("Zaman (s)")
    plt.ylabel("Genlik")
    plt.title("Zaman Bölgesi Sinyal Grafiği")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

# -------------------- Rapor Yazma --------------------
def write_report(stats, fs, dt):
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("# Sinyal Analizi Raporu\n\n")
        f.write("## Temel İstatistikler\n")
        for k, v in stats.items():
            f.write(f"- **{k}**: {v:.6f}\n")
        f.write("\n## Örnekleme Bilgisi\n")
        f.write(f"- Δt = {dt:.6f} s\n")
        f.write(f"- fs = {fs:.2f} Hz\n")
        f.write("\n## Grafik\n- report/figures/time_signal.png\n")
"""
# -------------------- Ana Program --------------------
def main():
    t, x = read_csv_signal(DATA_PATH)

    stats = compute_basic_stats(x)
    fs, dt = compute_sampling_frequency(t)

    y = moving_average(x, window=5)

    plot_signals(t, x, y, FIG_PATH)
    write_report(stats, fs, dt)

    print("✔ İşlem tamamlandı. Rapor ve grafik üretildi.")

if __name__ == "__main__":
    main()
"""
