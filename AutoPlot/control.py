from AutoPlot.plotter import Plotter 
from AutoPlot.execute import Execute 
from AutoPlot.separator import Separator

class Control:

    def __init__(self, fnct, x0, x1, style, plt_label, x_label, y_label, plt_title):

        self.fnct = fnct 
        self.x0 = x0 
        self.x1 = x1 
        self.style = style 
        self.plt_label = plt_label 
        self.x_label = x_label 
        self.y_label = y_label 
        self.plt_title = plt_title 
    
    def run(self, html_render=False):

        sep = Separator(self.fnct, self.style, self.plt_label)
        fncts, styles, plt_labels = sep.separate()

        ys = []
        for fnct in fncts:
            exc = Execute(fnct, self.x0, self.x1)
            x, y = exc.exc()
            ys.append(y)

        plttr = Plotter(x, ys, styles, plt_labels, self.x_label, self.y_label, self.plt_title)
        plttr.plot()

        if html_render:
            return plttr.render()
        else:
            plttr.show()
            return None 
            
    
    