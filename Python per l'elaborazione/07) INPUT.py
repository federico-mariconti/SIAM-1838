nome=input("come ti chiami? ")
annonascita=int(input("in che anno sei nato? "))
eta=2024-annonascita
peso=int(int(input("quanto pesi?"))*0.5)

print("Ciao", nome,",", eta, "anni",end=", ")
print("sulla luna peseresti", peso)
print(f"Ciao, {nome} la tua età è di {eta} anni e sulla luna peseresti {peso} Kg")
