from wx import App

from .widget import Widget

if __name__ == '__main__':
    app = App(False)
    widget = Widget(None, 'AutoPlot', (400, 600))
    app.MainLoop()