import statistics as stat
import matplotlib.pyplot as plt


print("Statistika čísel")

while True:
    vstup = input("Zadej čísla oddělená čárkou (např. 1, 2.5, 3): ") #Načtu čísla od uživatele

    try:
        cisla_jako_text = vstup.split(",") #Rozdělím řetězec na jednotlivá čísla/texty a vloží do seznamu
        muj_seznam = [float(i.strip()) for i in cisla_jako_text] #Comprehension, očistím o neviditelné znaky + převedu na float + nový seznam

        if len(muj_seznam) < 2: # True vrací uživatele na začátek
            print("Zadejde alespoň dvě čísla.")
        else:
            print(f"Načteno {len(muj_seznam)} čísel.")
            print(muj_seznam)

            print("\n--- Statistická analýza ---")
            print(f"Součet: {sum(muj_seznam)}")
            print(f"Průměr: {stat.mean(muj_seznam)}")
            print(f"Medián: {stat.median(muj_seznam)}")
            print(f"Minimum: {min(muj_seznam)}")
            print(f"Maximum: {max(muj_seznam)}")
            print(f"Rozptyl: {stat.variance(muj_seznam)}")
            print(f"Směrodatná odchylka: {stat.stdev(muj_seznam)}")

            # --- VIZUALIZACE ---
            plt.bar(range(len(muj_seznam)), muj_seznam)
            plt.title("Sloupcový graf hodnot")
            plt.xlabel("Index")
            plt.ylabel("Hodnota")
            plt.axhline(stat.mean(muj_seznam), color='red', linestyle='--', label='Průměr')
            plt.legend()
            plt.show()

            break

    except ValueError:
        print("Chybný vstup! Zadej pouze čísla oddělená čárkami.")

input("\nStiskněte Enter pro ukončení...")

