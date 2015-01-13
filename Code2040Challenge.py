#author: Nicole Daniels
#github: https://www.github.com/ComicStix/Code2040Challenge

import requests
import dateutil.parser
import datetime

#PART 1

getString = requests.post('http://challenge.code2040.org/api/getstring',json={"token":"Q0CvICZIad"})
#Gets JSON representation of getString
getStringJSON = getString.json()
stringToBeReversed = getStringJSON['result']
#Uses extended slice syntax to reverse string
stringReverse = stringToBeReversed[::-1]
#Posts results to API
reversedStringPost = requests.post('http://challenge.code2040.org/api/validatestring',json={"token":"Q0CvICZIad","string":stringReverse})

#PART 2

haystack = requests.post('http://challenge.code2040.org/api/haystack',json={"token":"Q0CvICZIad"})
#Gets JSON representation of haystack
haystackJSON = haystack.json()
needle = haystackJSON['result']['needle']
#Find the index of the needle
findIndex = haystackJSON['result']['haystack'].index(needle)
#Posts results to API
needlePost = requests.post('http://challenge.code2040.org/api/validateneedle',json={"token":"Q0CvICZIad","needle":findIndex})

#PART 3

prefixRequest = requests.post('http://challenge.code2040.org/api/prefix',json={"token":"Q0CvICZIad"})
#Gets JSON representation of prefixRequest
prefixRequestJSON = prefixRequest.json()
#Assigns prefix to variable
prefix = prefixRequestJSON['result']['prefix']
#Assigns array of words to search through to find needle
searchArray = prefixRequestJSON['result']['array']
#Array that only contains words that do not contain the prefix
notContainsPrefixList = []
#Searches through search array and if any item does not contain prefix, add it to the notContainsPrefixList array
for item in searchArray:
    if item.find(prefix) == -1:
        notContainsPrefixList.append(item)
#Post results to the API
prefixPost = requests.post('http://challenge.code2040.org/api/validateprefix',json={"token":"Q0CvICZIad","array":notContainsPrefixList})

#PART 4
dateRequest = requests.post('http://challenge.code2040.org/api/time',json={"token":"Q0CvICZIad"})
#Gets JSON representation of dateRequest
dateRequestJSON = dateRequest.json()
#Assigns ISO 8601 string to dateStamp
dateStamp = dateRequestJSON['result']['datestamp']
#Assigns interval in seconds to intervalInSeconds
intervalInSeconds = dateRequestJSON['result']['interval']
#Coverts dateStamp to a datetime object
date = dateutil.parser.parse(dateStamp)
#Adds intervalInSeconds to date in order to obtain finalDate
finalDate = date + datetime.timedelta(seconds=intervalInSeconds)
#Converts the finalDate datetime object back to a string that can be processed by the API
finalDateString = finalDate.isoformat()
#Posts results to the API
datePost = requests.post('http://challenge.code2040.org/api/validatetime',json={"token":"Q0CvICZIad","datestamp":finalDateString})

#Check results
answer = requests.post('http://challenge.code2040.org/api/status',json={"token":"Q0CvICZIad"})
checkResults = answer.json()
print (checkResults)
