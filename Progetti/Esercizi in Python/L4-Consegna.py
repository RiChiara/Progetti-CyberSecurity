import turtle
import math

window = turtle.Screen()
window.bgcolor("pink")

def quadrato(lato:int):
    perimetro = 4 * lato
    for i in range(4):
        turtle.forward(lato)
        turtle.left(90)
    return perimetro

def cerchio(raggio):
    perimetro = 2 * math.pi * raggio
    turtle.circle(raggio)
    return perimetro

def rettangolo(base, altezza):
    perimetro = 2 * (base + altezza)
    for i in range(2):
        turtle.forward(base)
        turtle.left(90)
        turtle.forward(altezza)
        turtle.left(90)
    return perimetro

print("Scegli una figura geometrica da disegnare e calcolare il perimetro:")
print("1) Quadrato")
print("2) Cerchio")
print("3) Rettangolo")

a =(input("Inserisci la tua scelta (1-3): "))

if a == "1":
    lato = int (input("Inserisci la lunghezza del lato del quadrato: "))
    p = quadrato(lato)
    print(f"Perimetro del quadrato: {p}")

elif a == "2":
    raggio = float(input("Inserisci il raggio del cerchio: "))
    p = cerchio(raggio)
    print(f"Circonferenza del cerchio: {p}")

elif a == "3":
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    p = rettangolo(base, altezza)
    print(f"Perimetro del rettangolo: {p}")

else:
    print("Scelta non valida. Devi inserire un numero tra 1 e 3.")

turtle.done()
