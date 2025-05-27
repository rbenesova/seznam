import random
def pozdrav():
    print("Ahoj, jak se mas")
def dnesni_den():
    print("Dnes je utery")
def vypis_cisla():
    cisla =[1, 2, 3, 4, 5]
    print(f"cislo:{random.choice(cisla)}")
def obdelnik():
    for i in range (5):
        print("*")
def nalada_dne():
    nalady =["stastna", "smutna", "vesela", "klidna"]
    print(f"dnesni nalada je {random.choice(nalady)}")