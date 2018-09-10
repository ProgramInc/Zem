# -*- coding: utf-8 -*-

import csv
import os


fileLocation = r'C:\\Users\\User\\Documents\\Orban Audio Loudness Meter\\'
relevant = []


class Reader:

    goodCount = 0
    badCount = 0

    @staticmethod
    def fileOpener():
        filetoscan = os.listdir(fileLocation)
        print(filetoscan)
        for f in filetoscan:
            with open(fileLocation+f, encoding='utf-8') as csvfile:
                for line in csvfile.readlines():
                    column = line.split(', ')
                    newcolumn = list(column[14:15])
                    for t in newcolumn:
                        if float(t) == -200:
                            pass
                        # elif not -2 < float(t) < 2:
                        #     # print("File is NOT approved for broadcast!")
                        #     Reader.badCount += 1
                        #     break
                        else:
                            relevant.append(t)
                # print(relevant)

    @staticmethod
    def final_check():
        all_good = True
        for r in relevant:
            if not -2.1 < float(r) < 2.1:
                all_good = False
                break
                # Reader.badCount += 1
                # print("File is NOT approved for broadcast!")
            else:
                pass
                # Reader.goodCount += 1
                # print("File Is OK For Broadcast")
        if all_good != True:
            print("File is NOT approved for broadcast!")
            Reader.badCount += 1
            relevant.clear()
        else:
            print("File Is OK For Broadcast")
            Reader.goodCount += 1
            relevant.clear()

    @staticmethod
    def total_tally():
        # print(Reader.goodCount, "File/s Approved for Broadcast")
        # print(Reader.badCount, "File/s Rejected")
        pass

if __name__ == '__main__':
    # fileOpen = Reader()
    # fileOpen.fileOpener()
    # fileOpen.final_check()
    # fileOpen.total_tally()
    pass


