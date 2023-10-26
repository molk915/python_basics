haslo = input("Podaj haslo: ")
 
def szyfrowanie(haslo):
    for i in haslo:
        if i == " ":
            print(" ", end="")
        elif i == "z":
            print("a", end="")
        elif i == "Z":
            print("A", end="")
        else:
            print(chr(ord(i)+1), end="")
szyfrowanie(haslo)