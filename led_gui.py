import tkinter as tk
import serial
import time

# Inițializează conexiunea cu HC-05
try:
    bt = serial.Serial('/dev/rfcomm0', 9600)
    time.sleep(2)
except Exception as e:
    print("Eroare conexiune:", e)
    exit()

# Funcții pentru butoane
def aprinde_led():
    bt.write(b'1')

def stinge_led():
    bt.write(b'0')

# Creează fereastra
root = tk.Tk()
root.title("Control LED prin Bluetooth")
root.geometry("300x200")

# Butoane
btn_on = tk.Button(root, text="APRINDE LED", command=aprinde_led, bg="green", fg="white", font=("Arial", 14))
btn_on.pack(pady=20)

btn_off = tk.Button(root, text="STINGE LED", command=stinge_led, bg="red", fg="white", font=("Arial", 14))
btn_off.pack(pady=10)

# Rulează aplicația
root.mainloop()
