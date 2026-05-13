text = input("wiad: ")
print(text)
text = text.replace(" ", "")
print(text)
text = text.lower()
print(text)
letters = list(text)
print(letters)
if len(letters)>2:
    print("wiadomośc za długa, wiadomość musi być w formacie litera cyfra np B3")
    

def letter2number(letter):
    letters = ["a","b","c","d","e","f","g","h","i","j"]
    idx = 1 + letters.index(letter)
    return idx

print(letter2number("a"))

def get_idx(text):
    text = text.replace(" ", "")
    text = text.lower()
    letters = list(text)
    if len(letters)>2:
        print("wiadomośc za długa, wiadomość musi być w formacie litera cyfra np B3")
    else:
        if(letters[0].isalpha() and letters[1].isdigit()):
            i = letter2number(letters[1])
            j = letters[0]
        elif(letters[0].isdigit() and letters[1].isalpha()):
            i = letter2number(letters[0])
            j = letters[1]
        else:
            i = 0
            j = 0
            print("wiadomość musi być w formacie litera cyfra np. D6")
    return i,j
            
            