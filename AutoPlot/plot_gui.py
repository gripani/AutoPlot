from wx import App

from .control import Control
from .widget import Widget

def control_run(**dict_values):
    control = Control(**dict_values)
    control.run()

if __name__ == '__main__':
    app = App(False)
    widget = Widget(None, 'AutoPlot', (400, 600), control_run)
    app.MainLoop()