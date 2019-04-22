import sys

with open(sys.argv[1]) as infile, open(sys.argv[1][:-4] + "_formatted.csv", "a") as outfile:
    outfile.truncate(0)
    outfile.write("ID,diffuse,compact,merger,off_center,nearby,irregular,problematic,comment\n")
    for line in infile:
        keys = line.split(',')
        #escapes = ''.join([chr(char) for char in range(1, 32)])
        #keys = [key.translate(escapes) for key in keys]
        keys = [key[:-1].strip() for key in keys]
        res = []
        
        res.append(keys[0])
        
        if "diffuse" in keys:
            res.append("1")
        else:
            res.append("0")
            
        if "compact" in keys:
            res.append("1")
        else:
            res.append("0")
        
        if "merger" in keys:
            res.append("1")
        else:
            res.append("0")
            
        if "off_center" in keys:
            res.append("1")
        else:
            res.append("0")
            
        if "nearby" in keys:
            res.append("1")
        else:
            res.append("0")
        
        if "irregular" in keys:
            res.append("1")
        else:
            res.append("0")
            
        if "problematic" in keys:
            res.append("1")
        else:
            res.append("0")
            
        found = False
        for key in keys:
            if "Comment" in key:
                found = True
                res.append(key[9:])
                break
        if not found:
            res.append("")
            
        outfile.write(",".join(res) + "\n")
    print("Formatted file saved as " + sys.argv[1][:-4] + "_formatted.csv")
        