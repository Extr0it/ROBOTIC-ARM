Am realizat un braț robotic cu 6 grade de libertate, proiectat
parțial de mine în Fusion 360 și controlat printr-o interfață
grafică personalizată. 

Structura mecanică este construită
modular, iar mișcarea este asigurată de 6 servo-motoare: 3
MG996R (pentru articulațiile care necesită cuplu mare) și 3
MG90S (pentru poziționări fine). 

Controlul servo-urilor este
realizat cu un driver PCA9685 conectat la un Arduino Uno.
Alimentarea se face printr-un adaptor de 5V 3A, suficient pentru
a susține simultan toate cele 6 servo-uri. 

Comanda brațului se
face wireless, printr-un modul HC-05 Bluetooth, conectat la
Arduino.

Am dezvoltat o aplicație desktop cu interfață grafică (GUI) în
Python folosind biblioteca Tkinter, care permite controlul
intuitiv al fiecărui servo prin slidere individuale. Aplicația
comunică prin comenzi seriale Bluetooth trimise de pe Linux,
întrucât suportul HC-05 nu funcționează corect pe macOS fără
drivere speciale.


Proiectul demonstrează integrarea eficientă a hardware-ului cu
software-ul, de la nivel electric și mecanic, până la controlul prin
interfață grafică, și evidențiază capacitatea de a dezvolta sisteme
embedded interactive, adaptabile și ușor de extins.
