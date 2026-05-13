




def get_idx(text):
    text = text.replace(" ", "")
    text = text.lower()
    tab = letters = ["a","b","c","d","e","f","g","h","i","j"]
    letters = list(text)
    if len(letters) ==0:
        i = 0
        j = 0
        print("proszę mnie nie denerwować pustymi frazesami")
    elif len(letters)>2:
        i = 0
        j = 0
        print("wiadomośc za długa, wiadomość musi być w formacie litera cyfra np B3")
    else:
        if(letters[0].isalpha() and letters[1].isdigit()):
            if letters[0] not in tab:
                i = 0
                j = 0
                print("zakres liter od A do J")
            else:
                i = 1 +tab.index(letters[0])
                j = letters[1]
        elif(letters[0].isdigit() and letters[1].isalpha()):
            if letters[1] not in tab:
                i = 0
                j = 0
                print("zakres liter od A do J")
            else:
                i = 1 +tab.index(letters[1])
                j = letters[0]
        else:
            i = 0
            j = 0
            print("wiadomość musi być w formacie litera cyfra np. D6")
    return i,j

while True:
    wiad = input("podaj: ")
    print(get_idx(wiad))
            
            