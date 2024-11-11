# эти строчки не менять
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


# здесь продолжайте программу
class StringText:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)
    
    def __gt__(self, st):
        return len(self.lst) > len(st.lst)
    
    def __ge__(self, st):
        return len(self.lst) > len(st.lst)
    
    def __lt__(self, st):
        return len(self.lst) < len(st.lst)
    
    def __le__(self, st):
        return len(self.lst) <= len(st.lst)

def get_words(line):
    words = []
    for i in line.split():
        i_new = i.strip('–?!,.;')
        if i_new:
            words.append(i_new)
    return words

lst_text = [StringText(get_words(line)) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [str(' '.join(i.lst)) for i in lst_text_sorted]
