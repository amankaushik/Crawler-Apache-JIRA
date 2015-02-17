__author__ = 'chanakya'

import csv
import os
import urllib


class CSVReader:
    def __init__(self, filename):
        self.file_name = filename
        self.bug_id = []

    def get_bug_ID_from_CSV(self):                                                   # takes the csv file(which contains bug info) as input and saves bug id(column 3) from it to a list
        with open(self.file_name, 'rb') as csvfile:
            csv_read = csv.reader(csvfile)
            csv_read.next()
            i = 0
            for row in csv_read:
                    self.bug_id.append(row[2])
        return self.bug_id


class WordFileSaver:
    def __init__(self, bug_list):
        self.base_url = 'https://issues.apache.org/jira/si/jira.issueviews:issue-word/'
        self.url_ext = '.doc'
        #https://issues.apache.org/jira/si/jira.issueviews:issue-word/HAMA-895/HAMA-895.doc
        self.bug_list = bug_list

    def save_as_word_files(self):                                                             # saves the csv response(gotten by opening search_URL) to a file
        search_URL = {}
        for bug_id in self.bug_list:
            bid = bug_id.strip()
            if not bid is '':
                search_URL[bug_id.strip()] = self.base_url+bid+'/'+bid+self.url_ext

        #pprint.pprint(search_URL.items())
        dir_path = 'BugReports/'
        try:
            os.makedirs('BugReports/')
        except OSError:
            pass
        for bid, url in search_URL.items():
            #response = urllib2.urlopen(url)
            urllib.urlretrieve(url, dir_path+bid+'.doc')

if __name__ == '__main__':
    bug_id = []
    cr = CSVReader('ASF JIRA.csv')
    bug_id = cr.get_bug_ID_from_CSV()
    #print len(bug_id)
    #pprint(bug_id)
    wfs = WordFileSaver(bug_id)
    wfs.save_as_word_files()