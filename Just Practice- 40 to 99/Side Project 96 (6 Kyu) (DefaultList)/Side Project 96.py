class DefaultList (list):
    def __init__ (self, array):
        super().__init__(array)          
    def __getitem__ (self, item):
        try:
            return super().__getitem__(item)
        except IndexError:               
            return 'No'        