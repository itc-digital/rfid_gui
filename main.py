import os
import htmlPy
from PySide import QtCore, QtGui

# Initial confiurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# GUI initializations
app = htmlPy.AppGUI(
    title=u"RFID Read", 
    maximized=False, 
    plugins=True, 
    width=768,
    height=512,
    x_pos=300,
    y_pos=100
)

# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")

# GUI minimum size
app.web_app.setMinimumWidth(768)
app.web_app.setMinimumHeight(512)

# GUI icon
app_icon = QtGui.QIcon()
app_icon.addFile(BASE_DIR + "/static/img/icon.png", QtCore.QSize(110, 110))
app.window.setWindowIcon(app_icon)

# Import back-end functionalities
from back_end.back import TestClass

# Register back-end functionalities
app.bind(TestClass(app))

# GUI template
app.template = ("index.html", {"h1": "**********"})

if __name__ == "__main__":
    app.start()

