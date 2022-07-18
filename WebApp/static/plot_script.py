from AutoPlot.control import Control

def getElementById(element_id):
    return Element(element_id)

def getElementValueById(element_id):
    return Element(element_id).value 

def sub(*args, **kwargs):
    output = getElementById("output")
    error = getElementById("error")
    fnct = getElementValueById("fnct")
    x0 = getElementValueById("x0")  
    x1 = getElementValueById("x1") 
    style = getElementValueById("style") 
    plt_label = getElementValueById("plt_label") 
    x_label = getElementValueById("x_label")
    y_label = getElementValueById("y_label")
    plt_title = getElementValueById("plt_title")
    try:
        cntrl = Control(fnct, x0, x1, style, plt_label, x_label, y_label, plt_title)
        html_plot = cntrl.run(html_render=True)
        error.write("")
        output.write(html_plot)
    except AssertionError as e:
        error = getElementById("error")
        error.write(e)