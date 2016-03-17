'''
    This file defines 5 subject patterns to match the customers' appreciations
  and get_patterns() function to return these patterns. A pattern is composed
  of some typical words.
'''

bathroom = "bathroom|washroom"

cleanliness = "cleanliness|sheet|sanitation|bedclothes|\
bedspread|flat|floor|toilet|bathroom|washroom|restroom|lavatory|cleaning|clean"

parking = "parking|sparking"

decoration = "fixtures|trim|fit\sup|decoration|decorate |renovation|chair|\
table|desk |der\stisch|television|TV|teevee|video|closestool|nightstool|\
commode|toilet|maxthon|shower|needle\sbath|electric\skettle|kettle|hardware"

service = "service|receptionist|foreground|water"

price = "money|cash|fund|price|cost|spend|expenses|expend|economical|\
substantial|solid|pricey"


def get_patterns():
    '''
    Returns the defined patterns.
    '''

    default_patterns = [bathroom, cleanliness, parking, decoration, service, price]
    return default_patterns


if __name__=="__main__":
    
    print get_patterns
