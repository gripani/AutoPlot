from AutoPlot.plotter import Plotter 
from AutoPlot.execute import Execute 
from AutoPlot.parser import Parser
from AutoPlot.separator import Separator

def main():
    pars = Parser()

    fnct, x0, x1, style, plt_label, x_label, y_label, plt_title = pars.get_args()

    sep = Separator(fnct, style, plt_label)
    n, fnct, style, plt_label = sep.separate()


    for i in range(n):
        exc = Execute(fnct[i], x0, x1)
        x, y = exc.exc()
        plttr = Plotter(x, y, style[i], plt_label[i], x_label, y_label, plt_title)
        plttr.plot()

    plttr.plot()
    plttr.show()

if __name__ == '__main__':
    main()