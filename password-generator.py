import random, string

f = open("password.txt","a")

print("Für ein starkes Passwort sind mindestens 20 Zeichen empfohlen!")
while True:
    try:
        length = int(input("Wie lang soll das Passwort sein?: "))
    except:
        print("Falsche Eingabe")
        continue
    break
while True:
    uppercase = input("Großbuchstaben? (Y/N): ").lower()
    if uppercase == "y":
        uppercase = string.ascii_uppercase
    elif uppercase == "n":
        uppercase = ""
    else:
        print("Y oder N!")
        continue
    punctuation = input("Sonderzeichen? (Y/N): ").lower()
    if punctuation == "y":
        punctuation = string.punctuation
        break
    elif punctuation == "n":
        punctuation = ""
        break
    else:
        print("Y oder N!")
        continue
pass_name = input("Notiz zum Merken: ")
password = "".join(random.SystemRandom().choice(uppercase + string.digits + string.ascii_lowercase + punctuation) for i in range(length))
f.writelines("\n" + pass_name + " : " + password)
print("Passwort für", pass_name, ":" , password)
