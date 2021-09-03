#import re 

#nom = input("Indiquer le mot que vous voulez saisir: ")
#solution = re.findall('([A-Z])',nom)
#print ("les lettres en majuscules sont : ",solution)

def capital_case(v):
    """
    permet de passer la première lettre en majuscule
    """
    return v.capitalize()


def test_capital_case():
    resultat = capital_case("adrien")
    assert resultat == "Adrien"
