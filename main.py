
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
def salma():
    name = input("donner votre nom: ")
    poste = input("donner votre poste: ")
    age = input("donner votre age: ")
    print("bonjour "+name+", vous etes un "+poste+", vous avez "+str(age)+" ans.")

#tester
salma()


#return:

def cub(num):
    print(num*num*num)

cub(2)

#la meme chose quand on utilise return:

def cube(num):
    return num*num*num

print(cube(2))

#-----------if Statements---------------

homme = True
muslim = False

if homme and muslim:
    print("vous etes un homme et muslim")
elif homme and not muslim:
    print("vous etes un homme mais vous n'etes pas muslim")
elif not homme  and muslim:
    print ("vous etes une femme muslime")
else:
    print("vous etes une femme non muslime")

#comparaison:

#fonction max():
def max( num1 , num2 , num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max(4 , 945 , 5))

#fonction min():

def min( num1 , num2 , num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

print(min(456 , 1 , 6 ))


#exercice de faire une simple calculatrice:

num1 = float(input("Donner le premier nombre: "))
op = input("Donner l'operation: ")
num2 = float(input("Donner le deuxieme nombre: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Svp donner une operation")




#---------------------Dectionnaire--------------------

week = {
    1:"lundi",
    2:"Mardi",
    3:"Mercredi",
    4:"Jeudi",
    5:"Vendredi",
    6:"Samedi",
    7:"Dimanche",
}

print(week[3])
print(week.get(3,"try again"))


#-------while--------:

i = 0
while i <= 20:
    print(i)
    i = i + 1   #ou bien i += 1
    if i > 20 :
        print("Terminer")



#------for------------:

for letter in "Youssef El Hazmiri":
    print(letter)

cars2 = ["honda" , "mercides", "audi" , "bmw"]

for car in cars2:
    print(car)

for num in range(5):
    print(num)

for num in range(5,11):
    print(num)

print("\n")

for num in range(len(cars2)):
    print(num)

for num in range(len(cars2)):
    print(cars2[num])




#exercice : LOG IN BANQUE
password = "2420"
mots = ""
count = 0
limit = 3
out = False

while mots != password and not out:
    if count < limit :
        mots = input("Le mots de passe: ")
        count = count + 1
    else:
        out = True

if out:
    print("vous avez echoué dans les 3 fois, votre carte banquaire est blocké")
else:
    print("Vous êtes connecté, Bonjour Youssef")




