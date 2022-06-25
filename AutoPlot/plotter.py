import matplotlib.pyplot as plt 
import matplotlib as mpl

class Plotter:

    mpl.rcParams['text.color'] = 'darkred'
    mpl.rcParams['axes.labelcolor'] = 'darkred'

    font_dict = { 
        'family': 'serif',
        'weight': 'normal',
        'size': 16,
    }

    def __init__(self, x, ys, styles, plt_labels, x_label, y_label, plt_title):
        self.x = x 
        self.ys = ys 
        self.styles = styles 
        self.labels = plt_labels 
        plt.xlabel(x_label, fontdict=self.font_dict)
        plt.ylabel(y_label, fontdict=self.font_dict) 
        plt.title(plt_title, fontdict=self.font_dict)

    def plot(self):
        for y, style, label in zip(self.ys, self.styles, self.labels):
            plt.plot(self.x, y, style, label=label)
    
    def show(self):
        plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1.), prop=self.font_dict)
        plt.tight_layout()
        plt.show()
    
    def save(self, fname):
        plt.savefig(fname, dpi=600)
    
    def close(self):
        plt.close()
        