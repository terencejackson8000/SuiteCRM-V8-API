class FilterTriplet:
    #EQ = '=';
    #NEQ = '<>';
    #GT = '>';
    #GTE = '>=';
    #LT = '<';
    #LTE = '<=';
    def __init__(self, comparison, field, criteria):
        self._comparison = comparison
        self._field = field
        self._criteria = criteria
    
    def to_filter_string(self):
        return "filter[{0}][{1}]={2}".format(self._field, self._comparison, self._criteria)

class Filter:

    #Constructor for the filter
    #Parameters
    #----------
    #logical : string
    #    The logical connector. Must be OR or AND
    #criteria : list
    #   List of criterias of FilterTriplet
    def __init__(self, logical, criteria):
        self._logical = logical
        self._criteria = criteria
    
    def to_filter_string(self):
        #filter[operator]=and&filter[account_type][eq]=Customer
        criteria_string = ""
        for c in self._criteria:
            criteria_string = "&{0}".format(c.to_filter_string())

        return "filter[operator]={0}{1}".format(self._logical, criteria_string)