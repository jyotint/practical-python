
from .tableformatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    formatter_name = "csv"

    '''
    Emits a table in plain-text format
    '''

    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        print(','.join(headers))
    
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        rowdatastr = [ self._convert_(data) for data in rowdata] 
        print(','.join(rowdatastr))

    def _convert_(self, data):
        match data:
            case int():
                return str(data)
            case float():
                return f'{data:>.2f}'
            case _:
                return str(data) 
