import csv
import math

unique_rows = {}
id = 1
ARCSEC = 0.000277778

def search_radius(x1, y1, x2, y2, r = ARCSEC):
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if dist <= r:
        return True
    else:
        return False

def checkUnique(tup):
    for key in unique_rows.keys():
        if search_radius(float(tup[0]), float(tup[1]),float(unique_rows[key][1]),float(unique_rows[key][2])):
            return key
    return None
        
radecpairs = [] 

with open('catalogs1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    ra = 7
    dec = 8
    z = 6
    ew = 5
    cat = 1
   
    for row in spamreader:
        if checkUnique((row[ra], row[dec])) == None:
            unique_rows[(row[ra], row[dec])] = [id, row[ra], row[dec], row[z], row[ew], cat, 0]
            id += 1
        else:
            found_row = unique_rows[checkUnique((row[ra], row[dec]))]
            found_row[6] += 1
            found_row[5] = str(found_row[5]) + "//" + str(cat)
            if float(row[z]) > float(found_row[3]):
                found_row[3] = row[z]
            if float(row[ew]) > float(found_row[4]):
                found_row[4] = row[ew]
                
            unique_rows[checkUnique((row[ra], row[dec]))] = found_row
            
with open('catalogs2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    ra = 5
    dec = 6
    z = -1
    ew = 4
    cat = 2
    
    for row in spamreader:
        if checkUnique((row[ra], row[dec])) == None:
            unique_rows[(row[ra], row[dec])] = [id, row[ra], row[dec], -1, row[ew], cat,0]
            id += 1
        else:
            found_row = unique_rows[checkUnique((row[ra], row[dec]))]
            found_row[6] += 1
            found_row[5] = str(found_row[5]) + "//" + str(cat)
            if float(row[z]) > float(found_row[3]):
                found_row[3] = row[z]
            if float(row[ew]) > float(found_row[4]):
                found_row[4] = row[ew]
                
            unique_rows[checkUnique((row[ra], row[dec]))] = found_row
            
with open('catalogs3.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    ra = 7
    dec = 8
    z = 2
    ew = 4
    cat = 3
    for row in spamreader:
        if checkUnique((row[ra], row[dec])) == None:
            unique_rows[(row[ra], row[dec])] = [id, row[ra], row[dec], row[z], row[ew], cat,0]
            id += 1
        else:
            found_row = unique_rows[checkUnique((row[ra], row[dec]))]
            found_row[6] += 1
            found_row[5] = str(found_row[5]) + "//" + str(cat)
            if float(row[z]) > float(found_row[3]):
                found_row[3] = row[z]
            if float(row[ew]) > float(found_row[4]):
                found_row[4] = row[ew]
                
            unique_rows[checkUnique((row[ra], row[dec]))] = found_row
            
with open('catalogs4.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    ra = 8
    dec = 9
    z = 4
    ew = 6
    cat = 4
    
    for row in spamreader:
        if checkUnique((row[ra], row[dec])) == None:
            unique_rows[(row[ra], row[dec])] = [id, row[ra], row[dec], row[z], row[ew], cat,0]
            id += 1
        else:
            found_row = unique_rows[checkUnique((row[ra], row[dec]))]
            found_row[6] += 1
            found_row[5] = str(found_row[5]) + "//" + str(cat)
            if float(row[z]) > float(found_row[3]):
                found_row[3] = row[z]
            if float(row[ew]) > float(found_row[4]):
                found_row[4] = row[ew]
                
            unique_rows[checkUnique((row[ra], row[dec]))] = found_row
with open('catalogs5.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    ra = 43
    dec = 44
    z = 12
    ew = -1
    cat = 5
    
    for row in spamreader:
        if checkUnique((row[ra], row[dec])) == None:
            unique_rows[(row[ra], row[dec])] = [id, row[ra], row[dec], row[z], -1, cat,0]
            id += 1
        else:
            found_row = unique_rows[checkUnique((row[ra], row[dec]))]
            found_row[6] += 1
            found_row[5] = str(found_row[5]) + "//" + str(cat)
            if float(row[z]) > float(found_row[3]):
                found_row[3] = row[z]
            if float(row[ew]) > float(found_row[4]):
                found_row[4] = row[ew]
                
            unique_rows[checkUnique((row[ra], row[dec]))] = found_row
with open('catalogs6.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    ra = 7
    dec = 8
    z = 2
    ew = 3
    cat = 6
    
    for row in spamreader:
        if checkUnique((row[ra], row[dec])) == None:
            unique_rows[(row[ra], row[dec])] = [id, row[ra], row[dec], row[z], row[ew], cat,0]
            id += 1
        else:
            found_row = unique_rows[checkUnique((row[ra], row[dec]))]
            found_row[6] += 1
            found_row[5] = str(found_row[5]) + "//" + str(cat)
            if float(row[z]) > float(found_row[3]):
                found_row[3] = row[z]
            if float(row[ew]) > float(found_row[4]):
                found_row[4] = row[ew]
                
            unique_rows[checkUnique((row[ra], row[dec]))] = found_row

with open('res_catalog.csv', 'w+') as f:
    f.write("ID, RA, DEC, Z, EW, CatID, NumDuplicates\n")
    for key in unique_rows:
        str_inst = [str(x) for x in unique_rows[key]]
        f.write(",".join(str_inst) + "\n")
    
            
        
    
    