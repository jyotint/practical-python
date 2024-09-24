
from .tableformatter import TableFormatter

class TextTableFormatter(TableFormatter):
    formatter_name = 'text'

    '''
    Emits a table in plain-text format
    '''

    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        for data in rowdata:
            match data:
                case int():
                    print(f'{data:>10d}', end=' ')
                case float():
                    print(f'{data:>10.2f}', end=' ')
                case _:
                    print(f'{str(data):>10s}', end=' ')
        print()
