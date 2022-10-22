
somme = 0 

for entiers in range(101):
    somme += entiers

solution = somme


print(f"{solution} est la bonne valeur de la somme !" if solution == (100 * 101) / 2 else "Raté")
