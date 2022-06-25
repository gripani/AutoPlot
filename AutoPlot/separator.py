class Separator:
    def __init__(self, y, style, label):
        self.y = y 
        self.style = style 
        self.label = label  
    
    def separate(self):
        if ';' in self.y:
            self.y = self.y.split(';')
            self.style = self.style.split(';')
            self.label = self.label.split(';')
            assert len(self.y) == len(self.style) == len(self.label)
        else:
            self.y = [self.y]
            self.style = [self.style]
            self.label = [self.label]
        return self.y, self.style, self.label  