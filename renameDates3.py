# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil
import os
import re

datePattern = re.compile(r"""^(.*?)       #all text before the date
    ((0|1)?\d)-                          #one or two digits for the month
    ((0|1|2|3)?\d)-                      #one or two digits for the day
    ((19|20)\d\d)                        #four digit for the year
    (.*?)$                               #all the text after the date
    """, re.VERBOSE)

#Loop over the files in the working directory
for filename in os.listdir(".\\DateFiles"):
    match = datePattern.search(filename)
    
    #Skip files withouta date
    if match == None:
        continue
    
    #Get the different parts of the file name
    beforePart = match.group(1)
    monthPart = match.group(2)
    dayPart = match.group(4)
    yearPart = match.group(6)
    afterPart = match.group(8)
    
    #Form European style fiel names
    newFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    
    #Get full aboslute file paths
    absWorkingDir = os.path.abspath('.\\DateFiles')
    amerFilename = os.path.join(absWorkingDir,filename)
    euroFilename = os.path.join(absWorkingDir,newFilename)
    
    #Rename the files
    print('Renaming "%s" to "%s" ...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)  #uncomment after testing