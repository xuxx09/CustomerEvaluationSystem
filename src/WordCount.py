'''
    This file defines one function:
    word_count(string2search, time_begin, time_end, reviews, timeStamp, rates)
    (str, str, str, list of strs, list of strs, list of ints) --> dict.
    This function search string2search from reviews with timeStamp and
    the number of stars(rates), from the time_begin of time to the time_end.
    Returns a dictory containing only one item, whose key is string2search,
    and value is a list of counts of the each score(the number of stars).
'''
import re
import time
import TimeConversion
import Pattern


def word_count(string2search, time_begin, time_end, Ids, reviews, timeStamp, rates):
    '''
    (str, str, str, list of ints, list of strs, list of strs, list of ints) --> dict.
    time formate should be YYYY-MM-DD.
    This function search string2search from reviews with timeStamp and
    the number of stars(rates), from the time_begin of time to the time_end.
    Returns a dictory containing only one item, whose key is string2search,
    and value is a list of counts of the each score(the number of stars).
    '''

    time_begin = TimeConversion.time2stamp(time_begin)
    time_end = TimeConversion.time2stamp(time_end)
    pattern = string2search
    # Search from each pattern.
    for each in Pattern.get_patterns():
        if re.search(string2search, each):
            pattern = each
            break
    counts = [[] for i in range(6)]
    if str(time_begin) > str(time_end):
        time_begin, time_end = time_end, time_begin
    
    for i in range(len(reviews)):
        Id = Ids[i]
        review = reviews[i]
        rate = int(rates[i])
        timestamp = timeStamp[i]
        if timestamp < str(time_begin) or timestamp >= str(time_end):
            continue
        if re.search(pattern,review):
            counts[rate].append(Id)
        else:
            counts[0].append(Id)
    return {string2search: counts}


def basic_count(string2search, time_begin, time_end, Ids, reviews, timeStamp, rates):
    '''
    This  function return the basic statistic of the records.
    it only return the distribution of the rates. 
    '''
    time_begin = TimeConversion.time2stamp(time_begin)
    time_end = TimeConversion.time2stamp(time_end)
    
    #this number 6 represent the stars from 0 to 5,
    #modify this function again.
    counts = [[] for i in range(6)]
    if str(time_begin) > str(time_end):
        time_begin, time_end = time_end, time_begin
    for i in range(len(rates)):
        Id = Ids[i]
        review = reviews[i]
        rate = int(rates[i])
        timestamp = timeStamp[i]
        if timestamp < str(time_begin) or timestamp >= str(time_end):
            continue
        counts[rate].append(Id)     
    return {string2search: counts}
    
    

if __name__ == "__main__":

    reviews = ['this is a great room with clean',
               'this is a great room with clean',
               'this is a great room with dirty']
    timeStamp = ['1449514742', '1449514742', '1449514742']
    rates = [4, 3, 2]
    print word_count("clean", '2015-11-12', '2015-12-15',
                     reviews, timeStamp, rates)
