
class TableFormatterException(Exception):
    def __init__(self, formatter: str):
        self.formatter = formatter

    def __str__(self):
        return f'  EXCEPTION: Unknown formatter "{self.formatter}"'