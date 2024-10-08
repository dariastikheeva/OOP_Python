# здесь объявляются все необходимые классы
class Graph:
    def __init__(self, data):
        self.data = data.copy()
        self.is_show = True

    def set_data(self, data):
        self.data = data.copy()

    def show_data(self):
        return ' '.join(map(str, self.data))
    
    def dec(func):
        def wrapper(self):
            if self.is_show:
                return func(self)
            else:
                print('Отображение данных закрыто')
        return wrapper
    
    @dec
    def show_table(self):
        print(self.show_data())

    @dec
    def show_graph(self):
        print(f'Графическое отображение данных: {self.show_data()}')
        
    @dec
    def show_bar(self):
        print(f'Столбчатая диаграмма: {self.show_data()}')

    def set_show(self, fl_show):
        self.is_show = fl_show
        
# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()
