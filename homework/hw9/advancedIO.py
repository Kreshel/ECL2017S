#!/usr/bin/env python

import urllib.request as ur

def parseTable(html):
    #Each "row" of the HTML table will be a list, and the items
    #in that list will be the TD data items.
    ourTable = []

    #We keep these set to NONE when not actively building a
    #row of data or a data item.
    ourTD = None    #Stores one table data item
    ourTR = None    #List to store each of the TD items in.


    #State we keep track of
    inTable = False
    inTR = False
    inTD = False

    #Start looking for a start tag at the beginning!
    tagStart = html.find("<", 0)

    while( tagStart != -1):
        tagEnd = html.find(">", tagStart)

        if tagEnd == -1:    #We are done, return the data!
            return ourTable

        tagText = html[tagStart+1:tagEnd]

        #only look at the text immediately following the <
        tagList = tagText.split()
        tag = tagList[0]
        tag = tag.lower()

        #Watch out for TABLE (start/stop) tags!
        if tag == "table":      #We entered the table!
            inTable = True
        if tag == "/table":     #We exited a table.
            inTable = False

        #Detect/Handle Table Rows (TR's)
        if tag == "tr":
            inTR = True
            ourTR = []      #Started a new Table Row!

        #If we are at the end of a row, add the data we collected
        #so far to the main list of table data.
        if tag == "/tr":
            inTR = False
            ourTable.append(ourTR)
            ourTR = None

        #We are starting a Data item!
        if tag== "td":
            inTD = True
            ourTD = ""      #Start with an empty item!
            
        #We are ending a data item!
        if tag == "/td":
            inTD = False
            if ourTD != None and ourTR != None:
                cleanedTD = ourTD.strip()   #Remove extra spaces
                ourTR.append( ourTD.strip() )
            ourTD = None
            

        #Look for the NEXT start tag. Anything between the current
        #end tag and the next Start Tag is potential data!
        tagStart = html.find("<", tagEnd+1)
        
        #If we are in a Table, and in a Row and also in a TD,
        # Save anything that's not a tag! (between tags)
        #
        #Note that this may happen multiple times if the table
        #data has tags inside of it!
        #e.g. <td>some <b>bold</b> text</td>
        #
        #Because of this, we need to be sure to put a space between each
        #item that may have tags separating them. We remove any extra
        #spaces (above) before we append the ourTD data to the ourTR list.
        if inTable and inTR and inTD:
            ourTD = ourTD + html[tagEnd+1:tagStart] + " "
            #print("td:", ourTD)   #for debugging


    #If we end the while loop looking for the next start tag, we
    #are done, return ourTable of data.
    return(ourTable)

def fetchHtmlTable(link,outputPath):

    # saves html file
    ur.urlretrieve(link, filename=outputPath)

    # opens and creates a list of html code
    with ur.urlopen(link) as webfile:
        webcontent = [line.decode("utf-8") for line in webfile.readlines()]

    # converts html to string and parses
    webcontent = str(webcontent)
    parsed = parseTable(webcontent)
   
    # writes parsed code to a file
    outFile = open('data.txt','w')
    for ele in parsed:
        outFile.write('{:>30}'.format(ele[0])); outFile.write('{:>30}'.format(ele[1])); outFile.write('{:>30}'.format(ele[2])); outFile.write('{:>30}'.format(ele[3])); outFile.write('{:>30}'.format(ele[4])); outFile.write('{:>30}'.format(ele[5])); outFile.write('{:>30}'.format(ele[6])); outFile.write('{:>30}'.format(ele[7])); outFile.write('{:>30}'.format(ele[8])); outFile.write('{:>30}'.format(ele[9])); outFile.write('{:>30}'.format(ele[10]));  outFile.write('{:>30}'.format(ele[11])); outFile.write('{:>30}'.format(ele[12])); outFile.write('{:>30}'.format(ele[13])); outFile.write('{:>30}'.format(ele[14]));outFile.write('\n');  
    outFile.close()
    
def event_id(dataFile):
    data = open(dataFile,'r')
    
    # strips first line
    data.readline()
    
    for line in data:
        url = 'http://butler.lab.asu.edu/swift/' + line[21:29] + '/bat/ep_flu.txt'
        out = './swift/GRB' + line[21:29] + '_ep_flu.txt'
        try:
            print('Saving',url,'to',out)
            ur.urlretrieve(url, filename=out)
        except ur.HTTPError:
            print(url,'does not exist/contain data. Moving onto next line.')
        
    data.close()
    
    # to signify end of files
    #testFile = open('./swift/cool.txt','w')
    #testFile.close()

    
def plotBatFiles(inPath,figFile):
    import os
    import numpy as np, os
    import matplotlib.pyplot as plt
    plt.clf()
    ax = plt.gca()  # generate a plot handle
    ax.set_xlabel('Fluence [ ergs/cm^2 ]') # set X axis title
    ax.set_ylabel('Epeak [ keV ]')  # set Y axis title
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.axis([1.0e-8, 1.0e-1, 1.0, 1.0e4]) # set axix limits [xmin, xmax, ymin, ymax]
    plt.hold('on')  # add all data files to the same plot
    counter = 0     # counts the number of events
    
    for file in os.listdir(inPath):
        if file.endswith("ep_flu.txt"):
            data = np.loadtxt(os.path.join(inPath, file), skiprows=1)
            if data.size !=0 and all(data[:,1]<0.0):
                data[:,1] = np.exp(data[:,1])
                ax.scatter(data[:,1],data[:,0],s=1,alpha=0.05,c='r',edgecolors='none')
                counter += 1

                
    ax.set_title('Plot of Epeak vs. Fluence for {} Swift GRB events'.format(counter))
    plt.savefig(figFile)




fetchHtmlTable('http://www.shahmoradi.org/ECL2017S/homework/9/swift/bat_time_table.html','batTimeTable.html')
event_id('data.txt')
plotBatFiles('./swift','SwiftGRB.png')
