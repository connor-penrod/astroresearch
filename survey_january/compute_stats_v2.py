import sys
import scipy.stats as stat
import numpy as np
import matplotlib.pyplot as plt   
from matplotlib.ticker import MultipleLocator
import itertools      
import math
import statistics 
from matplotlib.backends.backend_pdf import PdfPages
 
def convertfloat(value):
  try:
    return float(value)
  except ValueError:
    return float(-1)

def create_2hist(sample1,sample2, title, log = False, pdf = None, labels = ('compact', 'noncompact')):

    
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
        
def display_graphs(sample1, sample2, type = "", pdf = None, labels = ('compact', 'noncompact')):
    ew_compact = [elem[EW_col] for elem in sample1 if elem[EW_col] <= EW_limit]
    ew_noncompact = [elem[EW_col] for elem in sample2 if elem[EW_col] <= EW_limit]
    ew_abnormal = [elem[EW_col] for elem in itertools.chain(sample1, sample2) if elem[EW_col] > EW_limit]
    sw_compact = [elem[spatial_col] for elem in sample1]# if elem[spatial_col] <= 5000]
    sw_noncompact = [elem[spatial_col] for elem in sample2]# if elem[spatial_col] <= 5000]
    sw_abnormal = [elem[spatial_col] for elem in itertools.chain(sample1, sample2)]# if elem[spatial_col] > 5000]
    flux_compact = [elem[flux_col] for elem in sample1]
    flux_noncompact = [elem[flux_col] for elem in sample2]
    


    create_2hist(ew_compact, ew_noncompact, type + ' Cumulative histogram (EW)', pdf=pdf, labels=labels)
    create_2hist(ew_compact, ew_noncompact, type + ' Cumulative histogram (EW) (logarithmic)', log=True, pdf=pdf, labels=labels)
    create_2hist(sw_compact, sw_noncompact, type + ' Cumulative histogram (SpatialWeight)', pdf=pdf, labels=labels)
    create_2hist(flux_compact, flux_noncompact, type + ' Cumulative histogram (Flux)', pdf=pdf, labels=labels)
    create_2hist(flux_compact, flux_noncompact, type + ' Cumulative histogram (Flux) (logarithmic)', log=True, pdf=pdf, labels=labels)

    ew_compact_log = [math.log(elem,10) for elem in ew_compact]
    ew_noncompact_log = [math.log(elem,10) for elem in ew_noncompact]


header = True
EW_col = -1
problem_col = -1
compact_col = -1
spatial_col = -1
offcenter_col = -1
irregular_col = -1
merger_col = -1
flux_col = -1
compact_data = []
noncompact_data = []
irregular_data = []
regular_data = []
irregular_compact_data = []
irregular_noncompact_data = []
regular_compact_data = []
regular_noncompact_data = []
EW_limit = 1200
all_data = []
with open("results_with_data.csv", "r") as infile:
    for line in infile:
        if header:
            labels = line.split(',')
            for idx,label in enumerate(labels):
                if label == "EW_rest":
                    EW_col = idx
                elif label == "problematic":
                    problem_col = idx
                elif label == "compact":
                    compact_col = idx
                elif label == "SpatialWeight":
                    spatial_col = idx
                elif label == "off_center":
                    offcenter_col = idx
                elif label == "F_Lya":
                    flux_col = idx
                elif label == "merger":
                    merger_col = idx
                elif label == "irregular":
                    irregular_col = idx
            header = False
        else:
            data = line.split(',')
            data = [convertfloat(elem) for elem in data]
            all_data.append(data)
            if data[problem_col] > 2 or data[offcenter_col] > 2:
                continue
            if data[irregular_col] >= 3 or data[merger_col] >= 3:
                irregular_data.append(data)
                if data[compact_col] >= 3:
                    compact_data.append(data)
                    irregular_compact_data.append(data)
                else:
                    noncompact_data.append(data)
                    irregular_noncompact_data.append(data)
            if data[irregular_col] < 3 and data[merger_col] < 3:
                regular_data.append(data)
                if data[compact_col] >= 3:
                    compact_data.append(data)
                    regular_compact_data.append(data)
                else:
                    noncompact_data.append(data)
                    regular_noncompact_data.append(data)
            #print(data)

pp = PdfPages("statistics.pdf")
            
# ALL SAMPLES
            
display_graphs(compact_data, noncompact_data, "All Samples (Compact vs Noncompact)", pdf=pp)


# IRREGULAR

display_graphs(irregular_data, regular_data, "All Samples (Irregular vs Regular)", pdf=pp, labels=('irregular', 'regular'))


ews = [elem[EW_col] for elem in all_data if elem[EW_col] <= EW_limit]
ew_greater_sample = [elem for elem in all_data if elem[EW_col] >= statistics.median(ews)]
ew_lesser_sample = [elem for elem in all_data if elem[EW_col] < statistics.median(ews)]


#print(ew_greater_sample)
#print(ew_lesser_sample)
display_graphs(ew_greater_sample, ew_lesser_sample, "EW Split", pdf=pp, labels=('EW >= median', 'EW < median'))



pp.close()
#print("Compact")
#print(sw_compact)
#print("Noncompact")
#print(sw_noncompact)