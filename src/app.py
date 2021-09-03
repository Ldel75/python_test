#import re 

#nom = input("Indiquer le mot que vous voulez saisir: ")
#solution = re.findall('([A-Z])',nom)
#print ("les lettres en majuscules sont : ",solution)

def majuscule(phrase):
    maj = phrase.capitalize()
    print (maj)

phrase = input("Indiquez une phrase : ")
rep= majuscule(phrase)
