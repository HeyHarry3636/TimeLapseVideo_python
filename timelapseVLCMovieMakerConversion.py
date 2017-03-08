import os, sys, subprocess, datetime
import xml.etree.cElementTree as ET

#Set the folder/directory locations using user input for the file locations
print "\n"
tlvFolder = raw_input("Enter the Folder of the TLV files:\nPlease enter exactly as this example format... J:\TimelapseCameras\Knife\KnifeTLV \n")
print "\n"
frameFolderLoc = raw_input("Enter the Folder where the frames will be saved:\nPlease enter exactly as this example format... J:\TimelapseCameras\Knife\KnifeFrames \n")
##tlvFolder = r"J:\TimelapseCameras\Knife\KnifeTLV"
##frameFolderLoc = r"J:\TimelapseCameras\Knife\KnifeFrames"

#create empty dateList to store the dates for which the videos span
dateList = []

#Change the directory of where the frames from the TLV videos will be saved
os.chdir(frameFolderLoc)
currentDirectory = os.getcwd()

#Ask the user for the start and end dates of the duration of the timelapse videos in the field (day you dropped off, day you picked up)
print "\n"
startDateCamera = str(raw_input("What is the START date for the most recent time-lapse video files?\n(Please enter in YYYYMMDD format): \n"))
print "\n"
endDateCamera = str(raw_input("What is the END date for the most recent time-lapse video files?\n(Please enter in YYYYMMDD format): \n"))
##startDateCamera = "20160505" #Hard-coded for testing
##endDateCamera = "20160616" #Hard-coded for testing

#Convert the string user input to date format
dtStart = datetime.datetime.strptime(startDateCamera, '%Y%m%d')
dtEnd = datetime.datetime.strptime(endDateCamera, '%Y%m%d')

#Save only the date and NOT the time from the user input (saves in YYYY-MM-DD format)
dtStartDate = datetime.datetime.date(dtStart)
dtEndDate = datetime.datetime.date(dtEnd)

#Create _A & _B directories for the dates that you picked up and dropped off the SD cards for the camera.
stDte_B = (str(dtStartDate) + "_B")
endDte_A = (str(dtEndDate) + "_A")
os.mkdir(stDte_B)
os.mkdir(endDte_A)

#compute the difference in dates from start to end; print the difference in dates
delta = dtEndDate - dtStartDate
print "\n" + "There are " + str(delta.days) + " days between the Start Date and End Date."

#add the _A, _B names to the list
dateList.append(stDte_B)
dateList.append(endDte_A)

#for every day between the start and end dates, create a new folder in the user inputted directory
for i in range(delta.days + 1):
    dateList.append(str(dtStartDate + datetime.timedelta(days = i)))
    os.mkdir(str(dtStartDate + datetime.timedelta(days = i)))

#remove non _A, _B names from list
dateList.remove(str(dtStartDate))
dateList.remove(str(dtEndDate))

#remove empty directory for the start and end dates without the _A & _B suffixes
os.rmdir(str(dtStartDate))
os.rmdir(str(dtEndDate))

#Variables used for command line prompt for VLC
vlcFull = r"C:\Progra~1\VideoLAN\VLC\vlc.exe"
vF = "--video-filter=scene"
vO = "--vout=dummy"
sR = "--scene-ratio=1"
sPre = "--scene-prefix=kn_"
sPath1 = "--scene-path="
vlcQuit = "vlc://quit"

#Create the TLV file names and run the VLC command prompt script for the scene filter
for flNme in dateList:
    #Using the StartDate Folder, remove the _B and assign appropriate TLV extension
    if flNme[-2:] == "_B":
        newFlNme = flNme.replace("_B", "")
        newFlNme = newFlNme.replace("-", "")
        newFlNmeShort = newFlNme[2:]
        tlvFileName = newFlNmeShort + "AB.TLV"
    elif flNme[-2:] == "_A":
        newFlNme = flNme.replace("_A", "")
        newFlNme = newFlNme.replace("-", "")
        newFlNmeShort = newFlNme[2:]
        tlvFileName = newFlNmeShort + "AA.TLV"
    else:
        newFlNme = flNme.replace("-", "")
        newFlNmeShort = newFlNme[2:]
        tlvFileName = newFlNmeShort + "AA.TLV"
    tlvPath = r"{0}\{1}".format(tlvFolder, tlvFileName)
    sPath2 = r"{0}\{1}".format(frameFolderLoc, flNme)
    prmpt = "{0} {1} {2} {3} {4} {5} {6}{7} {8}".format(vlcFull, tlvPath, vF, vO, sR, sPre, sPath1, sPath2, vlcQuit)
    os.system("cd c:")
    os.system(prmpt)

#create empty list to store new updated and ordered list
newDateList = []

#Create new list that has the dates in the correct order with _B starting followed by others, then lastly by _A
for value in dateList:
    if value[-2:] == "_B":
        newDateList.insert(0, value)
    elif value[-2:] == "_A":
        pass
    else:
        newDateList.append(value)
for val in dateList:
    if val[-2:] == "_A":
        newDateList.append(val)

#create empty list to save image path names within each directory 
files = []
filesNew = []

#save contents of the directory as a list, append the full path name
#For every date, create a list with the full path name to the images within each directory folder
for dt in newDateList:
    fileStringShort = frameFolderLoc + "\\" + dt
    files = os.listdir(fileStringShort)
    for fles in files:
        fileStringFull = fileStringShort + "\\" + fles
        filesNew.append(fileStringFull)

#I'm sure this can be done in a loop, but can't figure out how to do it for the life of me... come back to later.
#Set empty lists corresponding the months for which the files will be saved
filesJan_A = []
filesFeb_A = []
filesMar_A = []
filesApr_A = []
filesMay_A = []
filesJun_A = []
filesJul_A = []
filesAug_A = []
filesSep_A = []
filesOct_A = []
filesNov_A = []
filesDec_A = []
filesJan_B= []
filesFeb_B= []
filesMar_B= []
filesApr_B= []
filesMay_B= []
filesJun_B= []
filesJul_B= []
filesAug_B= []
filesSep_B= []
filesOct_B= []
filesNov_B= []
filesDec_B= []

##monthList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
##monthFileList = []
##
##for stuff in monthList:
##    listMonthA = "files" + stuff + "_A"
##    listMonthB = "files" + stuff + "_B"
##    nameMonthA = "name" + stuff + "_A"
##    nameMonthB = "name" + stuff + "_B"
##    monthFileList.append(listMonthA)
##    monthFileList.append(listMonthB)
##    
##for stuff in monthFileList:
##    monthVar = list(stuff)

#assign names for the XML documents
nameJan_A = "Jan_A"
nameFeb_A = "Feb_A"
nameMar_A = "Mar_A"
nameApr_A = "Apr_A"
nameMay_A = "May_A"
nameJun_A = "Jun_A"
nameJul_A = "Jul_A"
nameAug_A = "Aug_A"
nameSep_A = "Sep_A"
nameOct_A = "Oct_A"
nameNov_A = "Nov_A"
nameDec_A = "Dec_A"
nameJan_B = "Jan_B"
nameFeb_B = "Feb_B"
nameMar_B = "Mar_B"
nameApr_B = "Apr_B"
nameMay_B = "May_B"
nameJun_B = "Jun_B"
nameJul_B = "Jul_B"
nameAug_B = "Aug_B"
nameSep_B = "Sep_B"
nameOct_B = "Oct_B"
nameNov_B = "Nov_B"
nameDec_B = "Dec_B"


#pull out the months for which the videos are occuring, set them to separate lists
#movie maker can only handle less than 1000 photos added per instance, so I have to divide the files into half-months
for fl in filesNew:
    #search the filepath name for the index of the start of the year 2015, 2016, 2017, etc... thus \\20 
    yearIndex = fl.index("\\20")
    #for the fileTypes of the cameras that we have, the month is 6 places to the right of the year value for the pathname
    monthIndex = yearIndex + 6
    #for the fileTypes of the cameras that we have, the month is 9 places to the right of the year value for the pathname
    dayIndex = yearIndex + 9
    #there would be a function or loop for this, but it works for now
    if fl[monthIndex:monthIndex+2] == '01':
        #Movie maker only accepts importing less than 1000 files at a time, must divide months into first half/second half
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesJan_A.append(fl)
        else:
            filesJan_B.append(fl)
    elif fl[monthIndex:monthIndex+2] == '02':
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesFeb_A.append(fl)
        else:
            filesFeb_B.append(fl)
    elif fl[monthIndex:monthIndex+2] == '03':
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesMar_A.append(fl)
        else:
            filesMar_B.append(fl)
    elif fl[monthIndex:monthIndex+2] == '04':
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesApr_A.append(fl)
        else:
            filesApr_B.append(fl)
    elif fl[monthIndex:monthIndex+2] == '05':
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesMay_A.append(fl)
        else:
            filesMay_B.append(fl)
    elif fl[monthIndex:monthIndex+2] == '06':
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesJun_A.append(fl)
        else:
            filesJun_B.append(fl)
    elif fl[monthIndex:monthIndex+2] == '07':
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesJul_A.append(fl)
        else:
            filesJul_B.append(fl)
    elif fl[monthIndex:monthIndex+2] == '08':
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesAug_A.append(fl)
        else:
            filesAug_B.append(fl)
    elif fl[monthIndex:monthIndex+2] == '09':
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesSep_A.append(fl)
        else:
            filesSep_B.append(fl)
    elif fl[monthIndex:monthIndex+2] == '10':
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesOct_A.append(fl)
        else:
            filesOct_B.append(fl)
    elif fl[monthIndex:monthIndex+2] == '11':
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesNov_A.append(fl)
        else:
            filesNov_B.append(fl)
    elif fl[monthIndex:monthIndex+2] == '12':
        if int(fl[dayIndex:dayIndex+2]) >= 1 and int(fl[dayIndex:dayIndex+2]) <=15:
            filesDec_A.append(fl)
        else:
            filesDec_B.append(fl)
    else:
        print "ERROR in filesNew"

#Set list of XML files that will be used to create the movie maker files
xmlNameList = []

#creating function to create XML files for each month args(month list of paths to img files)
def createXML(month, name):
    mviMk = ET.Element("MovieMk")
    contnt = ET.SubElement(mviMk, "Content")
    for fl in month:
        ET.SubElement(contnt, "ContentFile", Filename=fl)
    ET.SubElement(mviMk, "AutoEdit", Style="FadeReveal")
    ET.SubElement(mviMk, "DeleteOnClose")
    tree = ET.ElementTree(mviMk)
    createXML.xmlSaveName = name + ".xml"
    xmlNameList.append(createXML.xmlSaveName)
    tree.write(createXML.xmlSaveName, encoding="utf-8", xml_declaration=True)

#if the list is empty then skip, if not run the createXML function
def existXML(month, name):
    if len(month) == 0:
        pass
    else:
        createXML(month, name)

existXML(filesJan_A, nameJan_A)
existXML(filesJan_B, nameJan_B)
existXML(filesFeb_A, nameFeb_A)
existXML(filesFeb_B, nameFeb_B)
existXML(filesMar_A, nameMar_A)
existXML(filesMar_B, nameMar_B)
existXML(filesApr_A, nameApr_A)
existXML(filesApr_B, nameApr_B)
existXML(filesMay_A, nameMay_A)
existXML(filesMay_B, nameMay_B)
existXML(filesJun_A, nameJun_A)
existXML(filesJun_B, nameJun_B)
existXML(filesJul_A, nameJul_A)
existXML(filesJul_B, nameJul_B)
existXML(filesAug_A, nameAug_A)
existXML(filesAug_B, nameAug_B)
existXML(filesSep_A, nameSep_A)
existXML(filesSep_B, nameSep_B)
existXML(filesOct_A, nameOct_A)
existXML(filesOct_B, nameOct_B)
existXML(filesNov_A, nameNov_A)
existXML(filesNov_B, nameNov_B)
existXML(filesDec_A, nameDec_A)
existXML(filesDec_B, nameDec_B)

#Variables used for command line prompt for VLC
mviMkFull = r"C:\Progra~2\wic4a1~1\photog~1\MovieMaker.exe"

#Create new FOR loop that adds the xml files for each new MONTH to a separate movie maker file
for files in xmlNameList:
    xmlSaveLoc = frameFolderLoc + "\\" + files
    prompt = "{0} {1} {2}".format(mviMkFull, xmlSaveLoc, " & exit")
    os.system(prompt)

quitCMD = "exit"
os.system(quitCMD)


