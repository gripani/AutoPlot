from AutoPlot.control import Control
from AutoPlot.widget import mainApp

def control_run(**dict_values):
    control = Control(**dict_values)
    control.run()

if __name__ == '__main__':
    mainApp('AutoPlot', (400, 600), control_run)