import random

def harommal_oszthatok():
    print("20 véletlen szám [1; 12] intervallumból")

    szamok = [random.randint(1, 12) for _ in range(20)]
    print(f"Összes szám: {szamok}")

    oszthatok = [szam for szam in szamok if szam % 3 == 0]
 
    print(f"\n3-mal osztható számok: {oszthatok}")
    print(f"Darabszám: {len(oszthatok)}")

harommal_oszthatok()