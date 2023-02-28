##########################################
#                                        #
######       PAGE GRABBER V1      ########
#                                        #
##########################################

##########################################
#                                        #
# Functionality of page grabber v1       #
#                                        #
# Download user specified web page       #
# with all its js,css and image files    #
#                                        #
##########################################

#Module to change file system and directories - for v2 update 
import os

#Modules to access webpage 
import urllib.request, urllib.error, urllib.parse

###
#
#   Function definitions
#
###

def getRoot(url):
    #the beginning of the url
    crawler1 = 0
    #After  or 
    #012345678
    #https://w
    #012345678
    #http://ww
    crawler2 = 9

    rootURL = url[crawler1:crawler2]

    #url ending
    urlEnding = url[-5:-1]+""+url[-1]

    #crawler2 value in url
    crawler2Value = url[(crawler2-1):crawler2]

    #crawler2 location tester
    crawler2Location = url[str(url).__len__()-crawler2-6:str(url).__len__()-crawler2-1]+""+url[str(url).__len__()-crawler2-1]

    #While the crawler has not hit a slash or the end of the url 
    # Continue looping
    while(not crawler2Value=="/" or crawler2Location==urlEnding):
        rootURL = url[crawler1:crawler2]

        #url ending
        urlEnding = url[-5:-1]+""+url[-1]

        #crawler2 value in url
        crawler2Value = url[(crawler2-1):crawler2]

        #crawler2 location tester
        crawler2Location = url[str(url).__len__()-crawler2-6:str(url).__len__()-crawler2-1]+""+url[str(url).__len__()-crawler2-1]

        crawler2 = crawler2 + 1

    return rootURL

def findExt(rootURL, walkerDict, fileDict, line, k, j):
    if walkerDict["midWalker1"] == "j" and walkerDict["midWalker2"] =="p" and walkerDict["midWalker3"] =="e" and walkerDict["backWalker"] =="g":
        print("jpeg file found")
        ###
        #
        #   JPEG Image download
        #
        ###

        #Get the full link/path - j+4 would exclude a character the full extension
        fileURL = line[k:j+5]

        print("without root URL = ", fileURL)

        if(fileURL[0] == "." and fileURL[1] == "/"):
            #Add the web address / root directory to the file path
            fileURL = rootURL + fileURL[2:j+5]

            print(fileURL)

            #Get image by requesting it
            response = urllib.request.urlopen(fileURL)

            #Save file as 
            file = open("newImage" , fileDict["jpeg"], ".jpeg", "w")
            file.write(response)
            file.close

            #Take note of number
            fileDict["jpeg"] = fileDict["jpeg"] + 1
            print("jpeg file downloaded")


    if walkerDict["midWalker2"] =="j" and walkerDict["midWalker3"] =="p" and walkerDict["backWalker"] =="g":
        print("JPG Image file found")
        ###
        #
        #   JPG Image download
        #
        ###

        fileURL = line[k:j+5]

        print("without root URL = ", fileURL)

        if(fileURL[0] == "." and fileURL[1] == "/"):
            #Add the web address / root directory to the file path
            fileURL = rootURL + fileURL[2:j+5]

            print(fileURL)

    if walkerDict["midWalker2"] =="p" and walkerDict["midWalker3"] =="n" and walkerDict["backWalker"] =="g":
        print("png Image file found")
        ###
        #
        #   PNG Image download
        #
        ###

        fileURL = line[k:j+5]

        print("without root URL = ", fileURL)

        if(fileURL[0] == "." and fileURL[1] == "/"):
            #Add the web address / root directory to the file path
            fileURL = rootURL + fileURL[2:j+5]

            print(fileURL)

    if walkerDict["midWalker2"] =="c" and walkerDict["midWalker3"] =="s" and walkerDict["backWalker"] =="s":
        print("css file found")
        ###
        #
        #   CSS download
        #
        ###

        fileURL = line[k:j+5]

        print("without root URL = ", fileURL)

        if(fileURL[0] == "." and fileURL[1] == "/"):
            #Add the web address / root directory to the file path
            fileURL = rootURL + fileURL[2:j+5]

            print(fileURL)

    if walkerDict["midWalker2"] =="." and walkerDict["midWalker3"] =="j" and walkerDict["backWalker"] =="s":
        print("js file found")
        ###
        #
        #   js download
        #
        ###

        fileURL = line[k:j+5]

        print("without root URL = ", fileURL)

        if((fileURL[0] == "." and fileURL[1] == "/") or (fileURL[0] == "/")):
            #Add the web address / root directory to the file path
            fileURL = rootURL + fileURL[2:j+5]
            #Get image by requesting it
            response = urllib.request.urlopen(fileURL)

            print(fileURL)

            #Save image as 
            #file = open("newJSfile" , fileDict["js"], ".js", "w")
            #file.write(response)
            #file.close
            #fileDict["js"] = fileDict["js"] + 1
            #print("js file downloaded")

def searchLink(loopDict, walkerDict, line, j, k, webContent, fileDict, rootURL):

    #While extension not found and link has not been cut
    extStartLocation = j
    loopDict["lineLength"] = (int(str(line).__len__()))

    while(j<loopDict["lineLength"] - 5):

        # Declare walkers
        walkerDict = {
            "frontWalker":line[k],
            "midWalker1": line[j+1],
            "midWalker2": line[j+2],
            "midWalker3": line[j+3],
            "backWalker": line[j+4]
        }

        findExt(rootURL, walkerDict, fileDict, line, k, j)

        #Push walkers through the file to find extension
        j = j+1

        #If we have reached the end of the line, no exension found
        if(j==loopDict["lineLength"] - 6):
            #Link cut, so extend line variable
            line = webContent[i:i+200]

            if(loopDict["lineLength"] < 200):
                j = extStartLocation

            loopDict["lineLength"] = (int(str(line).__len__()))

###
#
#   Main crawler
#
###

#URL of the webpage
#url = "file:///C:/Users/CURBY-LEE%20WILLIAMS/OneDrive/Desktop/Downloading%20Web%20Pages%20with%20Python%20_%20Programming%20Historian.html"
#url = "https://programminghistorian.org/en/lessons/working-with-web-pages"
url = input("Please enter the url of the website you'd like to download:\n", )

fileName = input("\nWhat would you like to name the HTML file:\n")

#Get the root of the url 
rootURL = getRoot(url)

#Get the webpage by requesting it
response = urllib.request.urlopen(url)

#Decode the file to get the information
webContent = response.read().decode("utf-8")

###
#
#   Sub files crawler
#
###

### Loop variables
#HTML Characters crawling iterator
i = 0
#url front crawling iterator
k = 0
#url mid and back crawler iterator
j = 0
#Looper variable
loopDict = {"continueLoop" : True, "lineLength" : 0}
#walkerDict used to keep track of link crawlers 
# - keep their changed state even outside local scope
walkerDict = {}
#fileDict used to make sure to not override download files
fileDict = {}

while(loopDict["continueLoop"]):

    line = webContent[i:i+100]
    # Declare walkers
    walkerDict = {
        "frontWalker":line[k],
        "midWalker1": line[j+1],
        "midWalker2": line[j+2],
        "midWalker3": line[j+3],
        "backWalker": line[j+4]
    }

    # Declare file types
    fileDict = {
        "jpeg": 0,
        "jpg": 0,
        "png": 0,
        "css": 0,
        "js": 0
    }

    loopDict["lineLength"] = (int(str(line).__len__()))

    #Loop through characters in line variable
    #while extension has not been found and walkerDict["backWalker"] is not at the end of the line
    while(j < loopDict["lineLength"] - 5):

        loopDict["lineLength"] = (int(str(line).__len__()))

        #Give walkers new definition inside loop
        # Declare walkers
        walkerDict = {
            "frontWalker":line[k],
            "midWalker1": line[j+1],
            "midWalker2": line[j+2],
            "midWalker3": line[j+3],
            "backWalker": line[j+4]
        }
        
        #Check for http or https
        protocol = walkerDict["frontWalker"] + walkerDict["midWalker1"] + walkerDict["midWalker2"] + walkerDict["midWalker2"] + walkerDict["backWalker"]

        # Check if file has been found
        #if(walkerDict["frontWalker"]=="." and walkerDict["midWalker1"]=="/"):
            
        #    searchLink(loopDict, walkerDict, line, j, k, webContent, fileDict, rootURL)

        #if(walkerDict["frontWalker"]=="." and not walkerDict["midWalker1"]=="<" and not walkerDict["midWalker1"]=="0" and walkerDict["midWalker2"]=="/"):
            
        #    searchLink(loopDict, walkerDict, line, j, k, webContent, fileDict, rootURL)
            
        #if(walkerDict["frontWalker"]=='"' and walkerDict["midWalker1"]=="/"):
            
            #searchLink(loopDict, walkerDict, line, j, k, webContent, fileDict, rootURL)
            
        #if(protocol == "http:" or protocol == "https"):
            
            #searchLink(loopDict, walkerDict, line, j, k, webContent, fileDict, rootURL)
            
        k= k + 1
        j= j + 1
    
    i = i+100
    k = 0
    j = 0

    cut=False

    #Image download
    #jpg, jpeg and png extension

    #Use to determine if the end of the file has been reached
    #Find (the ending body tag </body>)
    # returns -1 if value not found
    # returns +number if found
    if(line.find("</html>")>1):
        loopDict["continueLoop"] =False
        print("")
        print("HTML File downloaded -------------------------------------------------")

    ###
    #   Main HTML file link editor + Final download
    ###


###
#
#   Final download
#
###

# Save main webpage (html) file
file = open(fileName+".html", "w")
file.write(webContent)
file.close
