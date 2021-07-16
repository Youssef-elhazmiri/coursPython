"""
#Variabes

nom = "Youssef"
age = "20"
ville_Orig = "El kelaa des Sraghna"
ville_Hab = "Rabat"
University = "ENS Rabat"

#mon_premier_programme:

print("Je suis "+nom+", j'ai "+age+" ans, ma ville d'origine est "+ville_Orig+", mais j'habite dans "+ville_Hab+" à cause de mes études dans l'"+University+".")

print("\n")
#ecrire_l'egillemet_dans_print:

print("youssef \"Elhazmiri\"")

print("\n")

#fonctions:_var.lower()_et_var.islower()_et_var.upper()_et_var.isupper():
#var.upper(): changer la forme du variable à Majuscule
#var.isupper(): voir es-ce-qu'il y a des majuscule dans le contenue de la variable si oui le programme donne "TRUE" si non il donne " FALSE"

print(nom.lower().islower())
print(nom.isupper())
print(nom.upper())

print("\n")

#fonction: len(var): //donner la taille de le contenue d'une variable
print(len(nom))

print("\n")

#fonction: nom[]: //Donner le contenue d'une adresse

print(nom[0])
print(nom[1])
print(nom[2])
print(nom[3])

print("\n")

#fonction:_nom.index(""): // Donner l'adresse d'une valeur

print(nom.index("o"))
print(nom.index("Y"))
print(nom.index("s"))
print(University.index("Rabat"))

print("\n")
#fonction:_nom.replace("","")

print(nom.replace("ou","az"))
print(nom)

#inserer_un_element_par_l'utilisateur:

#Variables:
nom1 = input("Donner votre nom: ")
prenom1 = input("Donner votre prenom: ")
age1 = input("Donner votre age: ")
University1 = input("Donner votre Universite: ")

#code:
print("votre nom complet est "+nom1+" "+prenom1+", vous avez "+age1+" ans, vous etudiez dans l'"+University1+".")


#variables:
num1 = input("Donner le nombre 1: ")
num2 = input("Donner le nombre 2: ")
print( num1 + num2 )

#La_somme_de_deux_variables (int):
num1 = input("Donner le nombre 1: ")
num2 = input("Donner le nombre 2: ")
result = int(num1) + int(num2)
print(result)

#La_somme_de_deux_variables (float):
num1 = input("Donner le nombre 1: ")
num2 = input("Donner le nombre 2: ")
result = float(num1) + float(num2)
print(result)

#Donner_les_variables:
cars = ["audi","bmw","mercedes","renault","ferrari"]

print(cars[0])
print(cars[1])
print(cars[2])

print(cars[-1])
print(cars[-2])
print(cars[-3])

#Donner les valeurs qu'ils sont avant et apres:
print("les valeurs avant bmw :\n")
print(cars[:1])

print("\n")

print("les valeurs apres bmw :\n")
print(cars[1:])

#Donner les valeurs de ... à :

print(cars[1:3])

#changer les valeurs:
print(cars)

cars[2] = "kia"

print(cars)


cars = ["renault","mercedes","bmw","Audi","Ferrari"]
speed = [14 , 1 , 100 , 13 , 300]

#fonction de var.extend(): // combiner deux groupes 
print(cars)

#fonction de var.append(): ajouter une valeur dans une variable
cars.append("kia")
print(cars)

#fonction var.insert(,''): // ajouter une valeur dans une adresse
cars.insert(2,"kia")
print(cars)

#fonction var.remove(): //supprimer une valeur 
cars.remove("renault")
print(cars)

#fonction var.clear(): //supprimer tous le contenue du variable
cars.clear()
print(cars)

#fonction var.pop(): // supprimer la derniere valeur
cars.pop()
print(cars)

#fonction var.count(): //calculer la repition de la valeur
count = cars.count("renault")
print(count)

#fonction de var.sort(): //grouper les valeurs d'une variables de Maj à Mun et de a à z :
cars.sort()
print(cars)

speed.sort()
print(speed)

#fonction var.reverse(): // sert de reverser l'ordre du contenue d'une variable:
cars.reverse()
print(cars)

speed.reverse()
print(speed)

#fonction var.copy(): //copier les valeurs d'une variable dans une autre variable:
cars2 = cars.copy()
print(cars2)

#Tuples: on ne peut pas modifier sur tuple 

color = ("red" , "black" , "blue")
color[0] = "yellow"
print(color[0])






#-----------------------Fonctions-------------------------

#la fonction:
def salma(name, poste , age):
    print("bonjour "+name+", vous etes un "+poste+", vous avez "+str(age)+" ans.")

#tester
salma("Youssef" , "Developpeur de web" , 20)
"""