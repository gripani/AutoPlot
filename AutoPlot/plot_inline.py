from AutoPlot.parser import Parser
from AutoPlot.control import Control 

def main():
    pars = Parser()
    fnct, x0, x1, style, plt_label, x_label, y_label, plt_title = pars.get_args()
    cntrl = Control(fnct, x0, x1, style, plt_label, x_label, y_label, plt_title)
    cntrl.run()

if __name__ == '__main__':
    main()