import base64
import requests #this module will need to be installed
import json
import os.path
import datetime

base64str = ''
filePath = 'cv.docx'
#open the file, encode the bytes to base64, then decode that to a UTF-8 string
with open(filePath, 'rb') as f:
    base64str = base64.b64encode(f.read()).decode('UTF-8')

epochSeconds = os.path.getmtime(filePath)
lastModifiedDate = datetime.datetime.fromtimestamp(epochSeconds).strftime("%Y-%m-%d") 

#use https://eu-rest.resumeparsing.com/v10/parser/resume if your account is in the EU data center
url = "https://rest.resumeparsing.com/v10/parser/resume"
payload = {
    'DocumentAsBase64String': base64str,
    'DocumentLastModified': lastModifiedDate
    #other options here (see http://docs.sovren.com/API/Rest/Parsing)
}

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'sovren-accountid': "12345678",
    'sovren-servicekey': "eumey7feY5zjeWZW397Jks6PBj2NRKSH",
}

#make the request, NOTE: the payload must be serialized to a json string
response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
responseJson = json.loads(response.content)

#grab the ResumeData
resumeData = responseJson['Value']['ResumeData']

#access the ResumeData properties with simple JSON syntax:
print(resumeData['ContactInformation']['CandidateName']['FormattedName'])
#for response properties and types, see http://docs.sovren.com/API/Rest/Parsing
