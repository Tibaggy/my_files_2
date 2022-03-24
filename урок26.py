# text = '"Ура!", - вопите, дети, повару!'
text = 'nsjgkbsjgdz'
def word(t):
    words = ''
    banned = ['"', '!', ' ', '-', ',']
    for i in t.lower():
        if i not in banned:
            words += i
    return words
def palidrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s [-1] and palidrome(s[1:-1])
                 
print(palidrome(word(text)))