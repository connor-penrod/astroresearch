import sys
import scipy.stats as stat
import numpy as np
import matplotlib.pyplot as plt   
from matplotlib.ticker import MultipleLocator
import itertools      
import math
import statistics 
from matplotlib.backends.backend_pdf import PdfPages

class hist_model(object):
    def __init__(self):
        self.parameters = []
        self.enableLog = False
        self.sample1 = []
        self.sample2 = []
        self.title = "<Title>"
        self.labels = ("label1", "label2")
        self.targetQuantity = None
    
    def addTargetQuantity(self, quantity):
        self.targetQuantity = quantity
    def addParameter(self, group, params, condition):
        c = condition.__code__.co_argcount
        self.parameters.append((group, params, condition, c))
    
    def changeLog(self,b):
        self.enableLog = b
    
    def changeTitle(self,s):
        self.title = s
        
    def changeLabels(self, tup):
        self.labels = tup


class hist_stats(object):

    def __init__(self, filename):
        self.filename = filename
        self.header = True
        self.all_data = []
        self.objList = []
        self.indices = []
            
    def addHistObject(self, obj):
        self.objList.append(obj)
 
    def convertfloat(self, value):
      try:
        return float(value)
      except ValueError:
        return float(-1)

    def create_2hist(self,sample1,sample2, title, log = False, pdf = None, labels = ('compact', 'noncompact')):

        
        fig = plt.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.hist(x=sample1, bins=500, alpha=0.5, range=(min(min(sample1), min(sample2)),max(max(sample1), max(sample2))), density=True, cumulative=True, label=labels[0], color="xkcd:blue")
        plt.hist(x=sample2, bins=500, alpha=0.5, range=(min(min(sample1), min(sample2)),max(max(sample1), max(sample2))), density=True, cumulative=True, label=labels[1], color="xkcd:light blue")
        plt.legend(loc='lower right')
        plt.grid()
        ml = MultipleLocator(50)
        plt.axes().xaxis.set_minor_locator(ml)
        plt.axes().set_title(title)
        
        kstest = stat.ks_2samp(sample1, sample2)
        plt.figtext(0.5,0.3, "KS-Test -> Statistic = " + str(round(kstest[0], 4)) + ", P-Value = " + str(round(kstest[1], 4)), fontsize='large')
        
        if log:
            plt.axes().set_xscale('log')
        if pdf is not None:
            pdf.savefig(fig)

    def execute(self):
        with open(self.filename, "r") as infile:
            for line in infile:
                if self.header:
                    labels = line.split(',')
                    for idx,label in enumerate(labels):
                        self.indices.append((label,idx))
                    self.header = False
                else:
                    data = line.split(',')
                    data = [self.convertfloat(elem) for elem in data]
                    
                    for hist_obj in self.objList:
                        targetIdx = None
                        for pair in self.indices:
                            if pair[0] == hist_obj.targetQuantity:
                                targetIdx = pair[1]
                                
                        for parameter in hist_obj.parameters:
                            desired_values = []
                            for curr_id in range(parameter[3]):
                                for idxGroup in self.indices:
                                    if idxGroup[0] == parameter[1][curr_id]:
                                        desired_values.append(data[idxGroup[1]])
                            
                            if parameter[2](*desired_values):
                                if parameter[0] == 0:
                                    hist_obj.sample1.append(data[targetIdx])
                                elif parameter[0] == 1:
                                    hist_obj.sample2.append(data[targetIdx])

        pp = PdfPages("statistics.pdf")
        
        for hist_obj in self.objList:
            self.create_2hist(hist_obj.sample1, hist_obj.sample2, hist_obj.title + " " + hist_obj.targetQuantity, pdf=pp, labels=hist_obj.labels, log=hist_obj.enableLog)
                    
        pp.close()
        print("Histograms saved to PDF.")
    
if __name__ == "__main__":
    h = hist_stats("results_with_data.csv")
    
    obj1 = hist_model()
    obj1.changeTitle("Test2")
    obj1.changeLabels(("EW < 800", "EW > 800"))
    obj1.changeLog(True)
    obj1.addParameter(0,["problematic", "irregular"],lambda y, z : y <= 2 and z < 3)
    obj1.addParameter(1,["problematic", "irregular"],lambda y, z : y <= 2 and z >= 3)
    obj1.addTargetQuantity("EW_rest")
    
    obj2 = hist_model()
    obj2.changeTitle("test3")
    obj2.addParameter(0,["compact", "problematic", "EW_rest"], lambda x, y, z: (x >= 3 ) and (y <= 2) and (z < 5000))
    obj2.addParameter(1,["compact", "problematic", "EW_rest"], lambda x, y, z: (x < 3 ) and (y <= 2) and (z < 5000))
    obj2.changeLabels(("compact","noncompact"))
    obj2.addTargetQuantity("EW_rest")
    obj2.changeLog(True)
    
    h.addHistObject(obj1)
    h.addHistObject(obj2)
    h.execute()
#print("Compact")
#print(sw_compact)
#print("Noncompact")
#print(sw_noncompact)