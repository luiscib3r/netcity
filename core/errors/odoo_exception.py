class OdooException(Exception):
    def __init__(self, message):
        super(OdooException).__init__()

        self.message = message