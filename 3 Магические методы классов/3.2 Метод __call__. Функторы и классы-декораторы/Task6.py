class RenderList:
    def __init__(self, type_list):
        self.type_list = 'ol' if type_list == 'ol' else 'ul'

    def __call__(self, lst):
        s = f'<{self.type_list}>\n'
        for i in lst:
            s += f'<li>{i}</li>\n'
        s += f'</{self.type_list}>'
        return s
