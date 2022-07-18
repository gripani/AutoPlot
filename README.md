Description:

AutoPlot is a simple tool that allows you to plot functions.
In WebApp there is also an example of usage with pyscript.

Installation:

```
python setup.py bdist_wheel
python setup.py build
python setup.py install
```
move the wheel file into the static folder in WebApp

Usage:

inline interface
``` 
python -m AutoPlot.plot_inline --fnct="sin(2*x)+.5*cos(3*x)" --x0="-2*pi" --x1="2*pi" --style="-" --plt_label="Sin(2x)+.5Cos(3x)" --x_label="x (rad)" --ylabel="y (au)" --plt_title="Plot"
```

GUI interface 
``` 
python -m AutoPlot.plot_gui
```

Web App
``` 
python ./WebApp/my_server.py
``` 