import csv
from Entry import *

class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.entries = []
        self.disks = dict()

    def parseFile(self):
        with open(self.filename, newline='', errors='ignore') as catalog:
            catalog_reader = csv.reader(catalog, delimiter='\t')
            i = 0
            key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for c in catalog_reader:
                if i == 0:
                    i = 1
                else:
                    if len(c) == 2: # disk
                        if not key in c[0]:
                            key = c[0]
                            self.disks[key] = []
                            #print(key, disks[key])
                    elif len(c) == 5: # file
                        l = self.disks.get(key)
                        l.append(Entry(c[0],c[1],c[2],c[3],c[4]))
                        self.disks[key] = l
                    else:
                        print(c)

    def getKeys(self):
        keys = self.disks.keys()
        list = []
        for k in keys:
            list.append(k)
        return list
