import argparse 

class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--fnct', type=str, help='inline function of x to plot, separate multiple values with semicolumn')
        self.parser.add_argument('--x0', type=str, help='lower limit of x-axis')
        self.parser.add_argument('--x1', type=str, help='upper limit of x-axis')
        self.parser.add_argument('--style', type=str, help='linestyle for plot function, separate multiple values with semicolumn')
        self.parser.add_argument('--plt_label', type=str, help='label for plot function, separate multiple values with semicolumn')
        self.parser.add_argument('--x_label', type=str, help='label for x-axis')
        self.parser.add_argument('--y_label', type=str, help='label for y-axis')
        self.parser.add_argument('--plt_title', type=str, help='plot title')
    
    def get_args(self):
        args = self.parser.parse_args()
        fnct = args.fnct 
        x0 = args.x0 
        x1 = args.x1 
        style = args.style 
        plt_label = args.plt_label 
        x_label = args.x_label 
        y_label = args.y_label 
        plt_title = args.plt_title 
        return fnct, x0, x1, style, plt_label, x_label, y_label, plt_title