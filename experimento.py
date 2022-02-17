def cambia(cadena,basura):
    for c in basura:
        cadena.replace(c,'*')
    return cadena


basura = ',;.:!¡¿?-_'
cadena = 'hola,.:paco'

print(cambia(cadena,basura))

# Python3 program to demonstrate the
# use of replace() method

string = "geeks for geeks geeks geeks geeks"

# Prints the string by replacing all
# geeks by Geeks
print(string.replace("geeks", "Geeks"))

# Prints the string by replacing only
# 3 occurrence of Geeks
print(string.replace("geeks", "GeeksforGeeks", 3))
