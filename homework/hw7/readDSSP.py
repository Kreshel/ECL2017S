#!/usr/bin/env python

import sys
import os

#######
if len(sys.argv) != 2:
   print('\n\nUsage:')
   print('\t./readDSSP.py <input dssp file> <output summary file>')
   print('\nProgram Aborted.')
else:
   # strips the file extension from protein name
   pdb = sys.argv[1]
   pdb = pdb[:pdb.rfind('.')]

   # initiate empty list
   AA = []
   ACC = []
   RSA = []
   weights = {'A':129.0,'R':274.0,'N':195.0,'D':193.0,'C':167.0,'Q':225.0,'E':223.0,'G':104.0,'H':224.0,'I':197.0,
              'L':201.0,'K':236.0,'M':224.0,'F':240.0,'P':159.0,'S':155.0,'T':172.0,'W':285.0,'Y':263.0,'V':174.0}


   #### Read Data ####
   fileIn = open(sys.argv[1],'r')
   # skips the first 25 lines
   for i in range(25):
      fileIn.readline()

   # reads in data from useful lines
   for line in fileIn:
      # skips lines with no amino acid information
      if line[13] == '!':
         continue
      # appends information on AA and ACC to respective lists
      AA.append(line[13])
      ACC.append(int(line[35:38]))

   fileIn.close()

   # computes fraction of exposed surface
   for i in range(len(AA)):
      RSA.append( ACC[i] / weights[AA[i]])


   #### Write Data ####
   # appends if file already exists
   if os.path.isfile(sys.argv[2]):
      fileOut = open(sys.argv[2],'a')
      
      # writes data
      for i in range(len(AA)):
         string = pdb + '\t' + AA[i] + '\t' + str(ACC[i]) + '\t' + str(RSA[i])
         fileOut.write(string)
         fileOut.write('\n')

   # else creates and writes to a new file
   else:
      fileOut = open(sys.argv[2],'w')
      fileOut.write('pdb\t');fileOut.write('Name\t');fileOut.write('ACC\t');fileOut.write('RSA\n')

      # writes data
      for i in range(len(AA)):
         string = pdb + '\t' + AA[i] + '\t' + str(ACC[i]) + '\t' + str(RSA[i])
         fileOut.write(string)
         fileOut.write('\n')

   fileOut.close()
