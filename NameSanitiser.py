#!/usr/bin/env python
import csv



inFile = open("names.csv",'rb')
outf = open("./cleaned.csv","w")
data = csv.reader(inFile, delimiter = ",")
NamePrepends = ["von", "dos", "van", "de"]


def capitilisation(string = [str,str]):
    prependsIdx = []
    # for first name string.title() works fine because we don't have to
    # consider the vons, de's etc
    # convert everything to lower case. Do the title on the first name
    first = string[0].rstrip().lower().title()
    # second name set up for parsing.
    second = string[1].rstrip().lower()
    mc,prepend = False, False
    # check for special cases: mc, von, de etc, list can be added to in time
    if second[:2] == "mc": mc = True
    
    if len(second.split(" ")) > 1:
        for i,word in enumerate(second.split(" ")):
            if word in NamePrepends: 
                prepend = True
                prependsIdx.append(i)
                
                
    
    if mc:
        second = "Mc" + second[2:].title()
        
    if prepend :
       sec_split = second.split(" ")
       second = ""
       for i,word in enumerate(sec_split):
           if i in prependsIdx:
               second = second.join(word)
           else:
               second += (" "+word.title())
               
    else:    
        second = second.title()
    return first +","+second+"\n"

def main():
    for line in data:
        print capitilisation(line)
        outf.write(capitilisation(line))
    outf.close()



if __name__ == "__main__":
    main()