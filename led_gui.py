import tkinter as tk # biblioteca GUI pentru a face toata mini aplicatia grafica
import serial # librarie pentru a comunica cu HC 05(modul bluetooth)
import time # pentru delay uri

# Inițializează conexiunea cu HC-05 prin portul
# 🔌 Inițializează conexiunea Bluetooth prin port serial
try:
    bt = serial.Serial('/dev/rfcomm0', 9600)  # deschide conexiunea pe /dev/rfcomm0 la 9600 baud
    time.sleep(2)  # așteaptă 2 secunde ca modulul HC-05 să fie gata
except Exception as e:
    print("Eroare conexiune:", e)  # dacă nu merge conexiunea, afișează eroarea
    exit()  # și oprește programul


# Funcții pentru butoane
def aprinde_led():
    bt.write(b'1')  # trimite caracterul 1 prin bluetooth, si atunci arduibo aprinde ledul

def stinge_led():
    bt.write(b'0') # la 0 , stinge ledul

# Creează fereastra aplicatiei
root = tk.Tk()
root.title("Control LED prin Bluetooth") # setarea unui titlu
root.geometry("300x200") # marimea aplicatiei in pixeli

# 🔲 Creează butoanele GUI
btn_on = tk.Button(
    root, 
    text="APRINDE LED", # textul de pe buton
    command=aprinde_led,  # funcția apelată când apeși butonul
    bg="green",           # background verde
    fg="white",           # font alb
    font=("Arial", 14)    # font mai mare
)
btn_on.pack(pady=20)      # il adauga în fereastra și îi pune spațiu vertical

btn_off = tk.Button(
    root, 
    text="STINGE LED",  #textul
    command=stinge_led,   # funcția apelată când apeși
    bg="red",             # fundal roșu
    fg="white", 
    font=("Arial", 14)
)
btn_off.pack(pady=10)


# Rulează aplicația
root.mainloop()
