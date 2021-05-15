import enum

class Comparison(enum.Enum):
   EQ = 1
   NEQ = 2
   GT = 3
   GTE = 4
   LT = 5
   LTE = 6

class Logical(enum.Enum):
    AND = 1
    OR = 2

class FilterTriplet:

    #Constructor for a filter triplet
    #Parameters
    #----------
    #comparison : Comparison
    #    Comparison type based on the enum Comparison
    #field : string
    #   The field for the filter e.g. name
    #criteria: multiple
    #   The criteria for the filter e.g. 6 or test
    def __init__(self, comparison, field, criteria):
        if not isinstance(comparison, Comparison):
            raise TypeError("comparison parameter has to be of type enum Comparison")

        self._comparison = comparison
        self._field = field
        self._criteria = criteria
    
    def to_filter_string(self):
        return "filter[{0}][{1}]={2}".format(self._field, self._comparison.name, self._criteria)

class Filter:

    #Constructor for the filter
    #Parameters
    #----------
    #logical : Logical
    #    The logical connector. Must be of enum Logical
    #criteria : list
    #   List of criterias of FilterTriplet
    def __init__(self, logical, criteria):
        if not isinstance(logical, Logical):
            raise TypeError("logical parameter has to be of type enum Logical")

        self._logical = logical
        self._criteria = criteria
    
    def to_filter_string(self):
        criteria_string = ""
        for c in self._criteria:
            criteria_string = "&{0}".format(c.to_filter_string())

        return "filter[operator]={0}{1}".format(self._logical.name, criteria_string)