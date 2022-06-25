import re 

class NumpyizeException(Exception):

    def __init__(self, string, cases):
        message = f"""Cannot trasform string with numpy:
'{string}' not available. cases available are:
{cases}, 
mathematical operations, parentheses, integers and floating numbers
        """
        super().__init__(message)

cases = (
    'e',
    'pi',
    'exp',
    'cos',
    'sin',
    'tan',
    'arcsin',
    'arccos',
    'arctan',
    'sinh',
    'cosh',
    'tanh',
    'arcsinh',
    'arccosh',
    'arctanh',
    'log',
    'log10',
    'log2',
    'sqrt',
    'cbrt'
) 

var = (
    'x',
)

delimiters = '+', '*', ')', '(', '/'

def is_float(x):
    try:
        float(x)
        return True 
    except ValueError:
        return False 

def numpyize(strn):

    reptrn = '|'.join(map(re.escape, delimiters))
    splitted_string = re.split(reptrn, strn)
    for obj in splitted_string:
        if not (obj in cases + var or is_float(obj) or obj == ''):
            raise NumpyizeException(obj, cases + var)

    for case in cases:
        if case in strn:
            strn = re.sub(case, f'np.{case}', strn)

    return strn