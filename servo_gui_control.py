import tkinter as tk
from tkinter import ttk
import serial
import time

# Configurare conexiune serială cu HC-05 (asigură-te că rfcomm0 e conectat)
bt = serial.Serial('/dev/rfcomm0', 9600)
time.sleep(2)  # așteaptă conexiunea

# Canalul pe care e conectat servo-ul (ex: canalul 15)
CANAL_SERVO = 15

# Trimite comanda la Arduino prin Bluetooth
def trimite_comanda(canal, unghi):
    unghi = max(0, min(180, unghi))  # limitează unghiul între 0-180
    bt.write(bytes([canal, unghi]))

# Funcții pentru butoane

def rotire_stanga():
    trimite_comanda(CANAL_SERVO, 30)  # ex: unghi stânga

def rotire_dreapta():
    trimite_comanda(CANAL_SERVO, 150)  # ex: unghi dreapta

# Funcție slider

def slider_miscare(val):
    trimite_comanda(CANAL_SERVO, int(float(val)))

# GUI setup
root = tk.Tk()
root.title("Control Servo Minimal")
root.geometry("300x250")

btn_stanga = tk.Button(root, text="⟲ Stânga", command=rotire_stanga, bg="lightblue", font=("Arial", 12))
btn_stanga.pack(pady=10)

btn_dreapta = tk.Button(root, text="Dreapta ⟳", command=rotire_dreapta, bg="lightgreen", font=("Arial", 12))
btn_dreapta.pack(pady=10)

slider = ttk.Scale(root, from_=0, to=180, orient='horizontal', command=slider_miscare)
slider.set(90)
slider.pack(pady=20, fill='x', padx=20)

root.mainloop()
