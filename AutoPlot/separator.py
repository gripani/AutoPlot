class Separator:
    def __init__(self, fnct, style, label):
        self.fnct = fnct 
        self.style = style 
        self.label = label  
    
    def separate(self):
        if ';' in self.fnct:
            self.fnct = self.fnct.split(';')
            self.style = self.style.split(';')
            self.label = self.label.split(';')
            assert len(self.fnct) == len(self.style) == len(self.label), 'Semicolumn separated values (function, style and label) must have the same lengths'
        else:
            self.fnct = [self.fnct]
            self.style = [self.style]
            self.label = [self.label]
        return self.fnct, self.style, self.label  