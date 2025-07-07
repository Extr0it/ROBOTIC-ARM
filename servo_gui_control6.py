import tkinter as tk
from tkinter import ttk
import serial
import time

# Deschide conexiunea cu HC-05
try:
    bt = serial.Serial('/dev/rfcomm0', 9600)
    time.sleep(2)
except Exception as e:
    print("Eroare conexiune Bluetooth:", e)

# Trimite comenzi la servo
def trimite_comanda(canal, unghi):
    unghi = max(0, min(180, unghi))
    try:
        bt.write(bytes([canal, unghi]))
    except Exception as e:
        print(f"Eroare trimitere pe canal {canal}: {e}")

def slider_miscare(canal):
    def update(val):
        trimite_comanda(canal, int(float(val)))
    return update

# GUI
root = tk.Tk()
root.title("🎮 Control Servo-uri Bluetooth")
root.geometry("700x700")  # fereastră mai mare
root.configure(bg="#1e1e2e")

# Titlu mare
title = tk.Label(root, text="🎛️ Panou Control Servo (10-15)", font=("Helvetica", 20, "bold"), fg="white", bg="#1e1e2e")
title.pack(pady=30)

# Stil modern + slider mare
style = ttk.Style()
style.theme_use('clam')
style.configure("TScale",
    background="#1e1e2e",
    troughcolor="#44475a",
    sliderthickness=40,     # grosime slider
    sliderlength=60,        # lungime cursor
)

# Creează slidere mari
for canal in range(10, 16):
    frame = tk.Frame(root, bg="#1e1e2e")
    frame.pack(pady=20)

    label = tk.Label(frame, text=f"🛠️ Servo {canal}", font=("Arial", 14, "bold"), fg="#8be9fd", bg="#1e1e2e")
    label.pack(anchor="center")

    slider = ttk.Scale(frame, from_=0, to=180, orient='horizontal', command=slider_miscare(canal), length=500)
    slider.set(90)
    slider.pack(pady=10)

root.mainloop()

