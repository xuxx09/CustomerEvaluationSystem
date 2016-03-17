'''
  This file defines one function : show_data(dictionary), which is used to
show the customers' appreciations by ploting pie charts and bar charts.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import traceback
import multiprocessing
from csvFile import read_file
from ShowApp import show

def autolabel(rects):
    '''
    Add text for each bar.
    '''

    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x(), height, '%s' % float(height))


def show_data(dic):
    '''
    Plot a pie chart and a bar char for each item in dic based on its value.
    If star_num is equal to 1 ~ 5, print the customers' appreciations in
    csv_list with star_num stars about the key. If star_num is equal to 0,
    print the customers' appreciations which are not about the key.
    '''

    try:
        # For each item
        item = dic.items()[0]
        key = item[0]
        # Labels: 1 star to 5 stars.
        labels = [str(index) for index in range(len(item[1]))]
        # The count of each label.
        counts = [len(ids) for ids in item[1]]
        fig = plt.figure(1, figsize=(14, 6))
        # Set fig title
        plt.suptitle(key.upper(), fontsize=21)

        # On the left is a pie chart.
        ax1 = plt.subplot(121)
        ax1.pie(counts, labels=labels, autopct='%.2f%%')
        # Set the title.
        ax1.set_title("Percentage of each kind of customers' appreciations",
				  fontsize=11)
        # On the right is a bar chart.
        ax2 = plt.subplot(122)
        width = 0.4
        ind = np.linspace(0.5, 4.5, len(counts))
        rects = ax2.bar(ind - width / 2, counts, width, color='orange')

        # Set the ticks.
        ax2.set_xticks(ind)
        ax2.set_xticklabels(labels)
        ax2.set_yticks(np.linspace(0, round(max(counts) * 1.2), 5))
        # Set the labels.
        ax2.set_xlabel('Stars')
        ax2.set_ylabel('Counts')
        # Set the title.
        ax2.set_title("Counts of each kind of customers' appreciations",
				  fontsize=11)
        # Add texts.
        autolabel(rects)
	
        # At last, show the chart
        plt.show()
    except:
        plt.close()
        traceback.print_exc()


def show_app(dic, csv_list, star_num):
    '''
    Print the customers' appreciations.
    '''

    item = dic.items()[0]
    key = item[0]
    first_line = csv_list[0]
    texts = []
    if star_num == 1:
        texts.append("The customers' appreciations with {0} star about {1}:".format(
            star_num, key))
    elif star_num == 0:
        texts.append("The customers' appreciations which are not about {0}:".format(
            key))
    else:
        texts.append("The customers' appreciations with {0} stars about {1}:".format(
            star_num, key))
    texts.append(','.join(first_line))
    for line in csv_list[1:]:
        # Each line
        if (line[0]) in item[1][star_num]:
            texts.append(', '.join(line))
    show(texts)


if __name__ == '__main__':

    d = {'clean' : [[str(i) for i in range(1, 26)], ['1', '6', '11', '16', '21'],
                    {'2', '7', '12', '17', '22'}, {'3', '8', '13', '18', '23'}, {'24'}, {'25'}]}
    csv_list = read_file()
    show_data(d)
    show_app(d, csv_list, 1)
    
