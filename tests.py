# Fonctions utilisées pour tester les réponses dans les différents ateliers d\'introduction.
# Je vous conseille de ne pas les modifier, mais vous avez tout à fait le droit de les regarder.

import ast, inspect, random

def introduction(une_chaine, un_entier, un_flottant):
    # Fonction de test pour le premier fichier
    if type(une_chaine) is str : # On vérifie le type de la variable "une_chaine" en utilisant la fonction built-in "type"
        print("Chaîne : OK")
    else :
        raise TypeError("La variable une_chaine doit être du type string.")
    if type(un_entier) is int : # De la même manière, on vérifie le type de la variable "un_entier"
        print("Entier : OK")
    else :
        raise TypeError("La variable un_entier doit être du type int.")
    if type(un_flottant) is float : # De la même manière, on vérifie le type de la variable "un_flottant"
            print("Flottant : OK")
    else :
        raise TypeError("La variable un_flottant doit être du type float.")

    print("Parfait ! Vous pouvez passer au fichier suivant, qui portera sur les listes.")

def listes(chiffres, noms):
    # Fonction de test pour le deuxième fichier
    if chiffres == [x for x in range(1,5)] : # On utilise ici une compréhension de liste afin de générer celle demandée.
                                             # C'est une fonctionnalité qui sera abordée dans le fichier 7, car celle-ci demande de connaître les boucles.
        print("Chiffres : OK")
    else :
        raise BaseException("Vérifie ce qu'il y a dans la liste \"chiffres\".")
    if noms == ["Lovelace", "Hamilton", "Van Rossum", "Ritchie"] :
        print("Noms : OK")
    else :
        raise BaseException("Vérifie ce qu'il y a dans la liste \"noms\".")

    print("Parfait ! Vous pouvez passer au fichier suivant, qui portera sur les opérateurs.")

def operateurs(three_list, pattern_list):
    # Fonction de test pour le quatrième fichier
    if three_list == [3 for x in range(10)] : # On utilise encore une compréhension !
        print("three_list : OK")
    else :
        raise BaseException("Vérifie ce qu'il y a dans la liste \"3_list\".")
    if pattern_list == ["abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"] : # Ce n'est pas une manière élégante de présenter cette liste, mais je n'allais pas donner la réponse comme ça :)
        print("pattern_list : OK")
    else :
        raise BaseException("Vérifie ce qu'il y a dans la liste \"pattern_list : OK\".")

    print("Parfait ! Vous pouvez passer au fichier suivant, qui portera sur les conditions.")

# Quelques fonctions de test pour le sixième fichier

def uses_for(func):
    # Vérifie si une fonction contient "for" dans son code source
    if not (inspect.isfunction(func)) :
        raise TypeError("La variable func doit être une fonction.")
    nodes = ast.walk(ast.parse(inspect.getsource(func)))
    return any(isinstance(node, ast.For) for node in nodes)

def uses_while(func):
    # Vérifie si une fonction contient "while" dans son code source
    if not (inspect.isfunction(func)) :
        raise TypeError("La variable func doit être une fonction.")
    nodes = ast.walk(ast.parse(inspect.getsource(func)))
    return any(isinstance(node, ast.While) for node in nodes)

def boucles_while(func):
    
    if not (inspect.isfunction(func)) :
        raise TypeError("La variable func doit être une fonction.")
    if not uses_while(func):
        raise BaseException("Vous devez utiliser la boucle while.")
    
    r_func = func(9)
    
    if any(x<0 for x in r_func):
        raise ValueError("La liste de retour ne doit comporter que des entiers positifs.")
    
    test_1 = list(range(9)[1::2])
    
    if r_func != test_1:
        raise ValueError("La liste de retour est erronée. La valeur attendue pour n = 9 est : " + str(test_1))
    
    # Tests avec des valeurs aléatoires, pour s'assurer que la fonction est correcte
    
    for i in range(10):
        rng = random.randint(-100, 100)
        rng_test = list(range(rng)[1::2])
        if func(rng) != rng_test:
            raise ValueError("La liste de retour est erronée. La valeur attendue pour n = "+ str(rng) + " est : " + str(rng_test))
        
    print("Parfait ! Vous pouvez passer à la fonction qui utilise la boucle for !")

def boucles_for(func):
    
    if not (inspect.isfunction(func)) :
        raise TypeError("La variable func doit être une fonction.")
    if not uses_for(func):
        raise BaseException("Vous devez utiliser la boucle for.")
    
    r_func = func(9)
    
    if any(x<0 for x in r_func):
        raise ValueError("La liste de retour ne doit comporter que des entiers positifs.")
    
    test_1 = list(range(9)[1::2])
    
    if r_func != test_1:
        raise ValueError("La liste de retour est erronée. La valeur attendue pour n = 9 est : " + str(test_1))
    
    # Tests avec des valeurs aléatoires, pour s'assurer que la fonction est correcte
    
    for i in range(10):
        rng = random.randint(-100, 100)
        rng_test = list(range(rng)[1::2])
        if func(rng) != rng_test:
            raise ValueError("La liste de retour est erronée. La valeur attendue pour n = "+ str(rng) + " est : " + str(rng_test))
        
    print("Parfait ! Vous pouvez passer au fichier suivant, qui portera sur les compréhensions de liste.")