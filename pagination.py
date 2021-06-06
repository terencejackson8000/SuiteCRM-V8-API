class Pagination:
    #Construct a Pagination object
    #Parameters
    #----------
    #page_size : int
    #    The intended page size. Default is 50
    #page_number : int
    #   The page number to look at. 
    def __init__(self, page_size = 50, page_number = None):
        if not isinstance(page_size, int):
            raise TypeError("page_size has to be of type int")
        if page_number != None and not isinstance(page_number, int):
            raise TypeError("page_number has to be of type int")
        self.page_size = page_size
        self.page_number = page_number