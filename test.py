text = input("wiad: ")
print(text)
text = text.replace(" ", "")
print(text)
text = text.lower()
print(text)
letters = list(text)
print(letters)
if len(letters)>2:
    print("wiadomośc musi być w formacie litera cyfra np B3")
    

def get_idx(letter):
    letters = ["a","b","c","d","e","f","g","h","i","j"]
    idx = 1 + letters.index(letter)
    return idx

print(get_idx(letters[0]))