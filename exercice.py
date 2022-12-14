#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return (voltage**2)/resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
    scal=0
    if (v1[0]==0 * v1[1]==0)+(v2[0]==0 * v2[1]==0):
        return True
    if len(v1)>len(v2):
        v1,v2=v2,v1
    for i in range(len(v1)):
        scal+=v1[i]*v2[i]
    if scal==0:
        return True
    else:
        return False

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
    c=0
    S=0
    for v in values:
        if v>0:
            S+=v
            c+=1
    return S/c
		 # La variable v contient une valeur de la liste.

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	pass

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value>base:
		result+=digit_letters[abs_value%base]
        abs_value=abs_value//base    
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
        result+="-"
    result=result[::-1]
    return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
