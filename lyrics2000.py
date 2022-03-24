with open('lyrics.txt', encoding="utf8") as f:
    lyrics = f.read()
# print(lyrics) 
# print(type(lyrics))
lyrics_list = []
banned = [' ', '.', ',','!', '(', ')', '\n', '«', '»', '—']
lyrics_word = ''    
for w in lyrics:
    w = w.lower()
    if w in banned:
        if lyrics_word:
            lyrics_list.append(lyrics_word)
            lyrics_word = ''
    elif w not in banned:
        lyrics_word = lyrics_word + w 
# lyrics_list = lyrics.replace('(', '').replace(')', '').replace('!', '').lower().split()
# print(lyrics_list)
check_dupes = {}
for w in lyrics_list:
    w = w.lower()
    if w not in check_dupes:
        check_dupes[w] = 1
    else:
        check_dupes[w] += 1 


two = 0
for i in check_dupes:
    if check_dupes[i] > two:
        two = check_dupes[i]
#Находим самое большое число


dict_2 = {}

for i in check_dupes:
    if check_dupes[i] == two:
        dict_2[i] = check_dupes[i]
def words_often(freq, times):
    dict_ = {}
    for i in freq:
        if freq[i] >= times:
            dict_[i] = freq[i]
    return dict_
lyrics_2000 = words_often(check_dupes, 6)
print(lyrics_2000)