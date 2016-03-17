import csv
import time


def build_file(tittle=['Id', 'reviews', 'rates', 'timeStamp']):
    '''
    generate a csv file to test.
    '''
    with open("coutomer_reviews.csv", "wb") as csvfile:
        csv_write = csv.writer(csvfile, dialect='excel')
        csv_write.writerow(tittle)
        for i in range(5):
            csv_write.writerow([1,"this is a great roon with cleaning", 1, 1449514742.0])
            csv_write.writerow([2,"this is a great roon with cleaning", 2, 1449514742.0])
            csv_write.writerow([2,"this is a great roon with cleaning", 3, 1449514742.0])
            csv_write.writerow([2,"this is a great roon with parking", 4, 1449514742.0])
            csv_write.writerow([2,"this is a great roon with parking", 5, 1449514742.0])
            

def read_file(file_name="coutomer_reviews.csv"):
    '''
    read the csv file to a list
    '''
   
    with open(file_name, 'rb') as csvfile:
        csv_iter = csv.reader(csvfile)
        csv_list = [each for each in csv_iter]
    return csv_list

    
if __name__=="__main__":
    #build_file()
    print  read_file()

    
