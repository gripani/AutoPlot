from AutoPlot.control import Control

def getElementById(element_id):
    return Element(element_id)

def sub(*args, **kwargs):
    output = getElementById("output")
    fnct = getElementById("fnct").value
    x0 = getElementById("x0").value  
    x1 = getElementById("x1").value 
    style = getElementById("style").value 
    plt_label = getElementById("plt_label").value 
    x_label = getElementById("x_label").value 
    y_label = getElementById("y_label").value 
    plt_title = getElementById("plt_title").value
    cntrl = Control(fnct, x0, x1, style, plt_label, x_label, y_label, plt_title)
    html_plot = cntrl.run(html_render=True)
    output.write(html_plot)