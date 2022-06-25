from .numpy_strings import numpyize 

class Execute:

    def __init__(self, funct, x0, x1, n=10000):
        self.funct = funct 
        self.x0 = x0 
        self.x1 = x1 
        self.n = n 
    
    def exc(self):
        kw = {}
        self.funct = numpyize(self.funct)
        try :
            self.x0 = str(float(self.x0))
        except ValueError:
            self.x0 = numpyize(self.x0)
        try:
            self.x1 = str(float(self.x1))
        except ValueError:
            self.x1 = numpyize(self.x1) 
        src = f"xi = np.linspace({self.x0}, {self.x1}, {self.n}); yi = np.array([{self.funct} for x in xi])"
        import numpy as np 
        exec(src, {'np': np}, kw)  
        x, y = kw['xi'], kw['yi']
        return x, y 