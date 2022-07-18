import matplotlib.pyplot as plt 
import matplotlib as mpl
import base64
from io import BytesIO

def convert_fig_to_html(fig):
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html_plot = "<img src='data:image/png;base64,{}'>".format(encoded)
    return html_plot

class Plotter:

    mpl.rcParams['text.color'] = 'darkred'
    mpl.rcParams['axes.labelcolor'] = 'darkred'

    font_dict = { 
        'family': 'serif',
        'weight': 'normal',
        'size': 16,
    }

    def __init__(self, x, ys, styles, plt_labels, x_label, y_label, plt_title):
        if len(plt.get_fignums()) > 0:
            plt.close()
        self.x = x 
        self.ys = ys 
        self.styles = styles 
        self.labels = plt_labels 
        _, self.ax = plt.subplots()
        self.ax.set_xlabel(x_label, fontdict=self.font_dict)
        self.ax.set_ylabel(y_label, fontdict=self.font_dict) 
        self.ax.set_title(plt_title, fontdict=self.font_dict)

    def plot(self):
        for y, style, label in zip(self.ys, self.styles, self.labels):
            self.ax.plot(self.x, y, style.strip(), label=label.strip())
        self.ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1.), prop=self.font_dict)
        plt.tight_layout()

    def show(self):
        plt.show()
    
    def render(self):
        fig = plt.gcf()
        return convert_fig_to_html(fig)

    def save(self, fname):
        plt.savefig(fname, dpi=600)
    
    def close(self):
        plt.close()
        