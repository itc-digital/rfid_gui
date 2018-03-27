import htmlPy
from .keyboard_alike import reader

ID_VENDOR = 0xffff
ID_PRODUCT = 0x0035


class RFIDreader(reader.Reader):
    pass

class TestClass(htmlPy.Object):
    def __init__(self, app):
        super(TestClass, self).__init__()
        self.app = app
        self.template = "index.html"
        self.vars = {
            "h1": None
        }

    @htmlPy.Slot()
    def say_hello_world(self):
        reader = RFIDreader(
            vendor_id=ID_VENDOR,
            product_id=ID_PRODUCT,
            data_size=84,
            chunk_size=16,
            should_reset=False
        )
        reader.initialize()
        rfid = reader.read().strip()
        reader.disconnect()
        self.vars["h1"] = rfid
        self.app.template = (self.template, self.vars)

    
