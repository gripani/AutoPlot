import sys 
import traceback

from .numpy_strings import numpyize 


class InterpreterError(Exception):

    pass 

def my_exec(src, globals, locals, description):
    try:
        exec(src, globals, locals)
    except SyntaxError as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        line_number = err.lineno
    except Exception as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
    else:
        return
    raise InterpreterError(f"{error_class} at line {line_number} of {description}: {detail}")

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
        my_exec(src=src, globals={'np': np}, locals=kw, description='apply numpy call of x and y')
        x, y = kw['xi'], kw['yi']
        return x, y 