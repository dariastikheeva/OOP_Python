# здесь объявляйте класс
class Morph:
    def __init__(self, *args):
        self.words = [i.lower() for i in args]
    
    def add_word(self, word):
        self.words.append(word.lower())
    
    def get_words(self):
        return tuple(self.words)
    
    def __eq__(self, other):
        return other.lower() in self.words  

text = input()   # эту строчку не менять

# здесь создавайте объекты класса и обрабатывайте строку text
dict_words = [
    Morph("связь", "связи", "связью", "связей", "связям", "связями", "связях"),
    Morph("формула", "формулы", "формуле", "формулу", "формулой", "формул", "формулам", "формулами", "формулах"),
    Morph("вектор", "вектора", "вектору", "вектором", "векторе", "векторы", "векторов", "векторам", "векторами", "векторах"),
    Morph("эффект", "эффекта", "эффекту", "эффектом", "эффекте", "эффекты", "эффектов", "эффектам", "эффектами", "эффектах"),
    Morph("день", "дня", "дню", "днем", "дне", "дни", "дням", "днями", "днях")
]

text = text.strip()

punctuation = '–?!,.;:"'
text_new = ''.join(i.lower() if i not in punctuation else ' ' for i in text)
words_in_text = text_new.split()

count = 0
for word in words_in_text:
    if any(mw == word for mw in dict_words):
        count += 1

print(count)
