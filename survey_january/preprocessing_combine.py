import sys
fl = True
with open("combined_results.csv","w") as outfile:
    outfile.write("ID,diffuse,compact,merger,off_center,nearby,irregular,problematic\n")
    for line1, line2, line3, line4, line5 in zip(open(sys.argv[1]), open(sys.argv[2]), open(sys.argv[3]), open(sys.argv[4]), open(sys.argv[5])):
        if fl:
            fl = False
            continue

        res = [int(elem) for elem in line1.split(",")[:-1]]
        for i in range(1,8):
            res[i] += int(line2.split(",")[i])
            res[i] += int(line3.split(",")[i])
            res[i] += int(line4.split(",")[i])
            res[i] += int(line5.split(",")[i])
        
        res = [str(elem) for elem in res]
        outfile.write(",".join(res) + "\n")
