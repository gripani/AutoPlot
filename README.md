Description:

AutoPlot is a simple tool that allows you to plot functions.
In WebApp there is also an example of usage with pyscript.

Installation:

```
python readme.py bdist_wheel
python readme.py build
python readme.py install
```
move the wheel file into the static folder of WebApp

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
python WebApp.my_server.py
``` 