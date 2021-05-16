class Pagination:
    #Construct a Pagination object
    #Parameters
    #----------
    #page_size : int
    #    The intended page size. Default is 50
    #page_number : int
    #   The page number to look at. 
    def __init__(self, page_size = 50, page_number = None):
        self.page_size = page_size
        self.page_number = page_number