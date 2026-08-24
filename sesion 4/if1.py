#Lees la nota de un estudiante
from colorama import Fore, Style
grade = int(input("Ingrese la nota:"))
if grade >= 70:
    print(Fore.GREEN + "Usted a aprobado.")
else: 
    print(Fore.RED "Su aprendizaje es inicial")
Style.RESET_ALL

