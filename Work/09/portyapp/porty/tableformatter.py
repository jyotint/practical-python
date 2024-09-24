
class TableFormatter:
    '''
    Overwrite in the concrete implementaion with the formatter type name.
    '''
    formatter_name = "(NoName)"

    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()
