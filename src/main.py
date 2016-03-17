'''
  This file asks user to input a keyword, then searches it from database,
  and shows the results by charts.
'''
import WordCount
import TimeConversion
import csvFile
import ShowDate



def count(string='basic statistics',
          tBeg=TimeConversion.default_begin_time(),
          tEnd=TimeConversion.default_end_time()):
    '''
    Counts the number of scores of word string.
    '''

    # Get data.
    csvfile_list = csvFile.read_file()[1:]
    Ids = [each[0] for each in csvfile_list]
    reviews = [each[1] for each in csvfile_list]
    rates = [each[2] for each in csvfile_list]
    timeStamp = [each[3] for each in csvfile_list]
    if string == 'basic statistics' :
        return WordCount.basic_count(string, tBeg, tEnd, Ids,
                                     reviews, timeStamp, rates)
    else:
        return WordCount.word_count(string, tBeg, tEnd, Ids,
                                reviews, timeStamp, rates)


def result():
    '''
    Get user's input, and output it, then show the results.
    '''

    while 1:
        string = \
        raw_input("please input the type of reviews you want to cheak: ")
        string = string.split()
        # 4 means the number of input.
        if len(string) > 4:
            print "Too much input the number should 0 to 4"
            break
        if len(string) == 4:
            rate = string[-1]
            string = string[:-1]
            dic = count(*string)
            csvfile_list = csvFile.read_file()
            ShowDate.show_app(dic, csvfile_list, int(rate))
        else:
            dic = count(*string)
            ShowDate.show_data(dic)


if __name__ == '__main__':

    result()
