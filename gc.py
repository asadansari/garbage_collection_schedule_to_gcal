import requests
from bs4 import BeautifulSoup
import csv
import datetime
year = str(datetime.datetime.now().year)
newDateTime = datetime.datetime.now() + datetime.timedelta(days=365)
newYear = str(newDateTime.year)

#Set your values below
startTime = "10:00 AM"
endTime = "11:00 PM"
address = "1234 Somewhere Cresecent, City, Province A3H 7Y7, Canada"
fileName = "garbage_collection_schedule_" + str(year) + ".csv"
collectionSchedCode = 'bm-cr-tue-a'
url = 'http://www.peelregion.ca/waste-scripts/when-does-it-go/nextCollectionHTML.asp?service=' + collectionSchedCode + '&days=365&date=' + str(year) + '-01-01&hidden=0'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
collectionDays = soup.find_all('div', class_='collectionDay')
listofcollectionDays = []

for day in collectionDays:
  listofcollectionDays.append(list(filter(str.strip, day.get_text().strip().split("\n"))))

# Removes " - Today" from the first date
def todayFix(lst):
  firstItem = lst[0]
  splitList = firstItem.split("-")
  lst[0] = splitList[0].strip()
  return lst

def getNumericDate(lst, newYearFix=0):
  if newYearFix == 0:
    date = lst[0] + ", " + year
  else:
    date = lst[0] + ", " + newYear
  dateTimeObject = datetime.datetime.strptime(date, '%A, %B %d, %Y')
  numericDate = datetime.datetime.strftime(dateTimeObject, '%m/%d/%Y')
  lst[0] = numericDate
  return lst

def addSubject(lst):
  subj = ["Garbage"]
  lst = subj + lst
  return lst

def addMissingValues(lst):
  sTime = startTime
  eDate = lst[1]
  eTime = endTime
  lst.insert(2, sTime)
  lst.insert(3, eDate)
  lst.insert(4, eTime)
  lst.insert(5, "True")
  lenofList = len(lst)
  lstFirst = lst[0:6]
  lstDescription = lst[6:lenofList]
  flatDescrip = mergeList(lstDescription)
  combinedList = lstFirst + flatDescrip
  combinedList.append(address)
  combinedList.append("True")
  return combinedList

def mergeList(lst):
  newlist = []
  flat = ''
  for item in lst:
    flat = flat + item + '\n'
  newlist.append(flat)
  return newlist

def removeLastElement(lst):
  return lst[:-1]

with open(fileName, "w", newline='') as csv_file:
  writer = csv.writer(csv_file, delimiter=',')
  headers = ["Subject","Start Date","Start Time","End Date","End Time","All Day Event","Description","Location","Private"]
  #print(headers)
  writer.writerow(headers)
  for counter, value in enumerate(listofcollectionDays):
    if counter  == 0:
      value = todayFix(value)
    value = removeLastElement(value)
    if counter == len(listofcollectionDays)-1:
      value = getNumericDate(value,1)
    else:
      value = getNumericDate(value)
    value = addSubject(value)
    value = addMissingValues(value)
    #value[6].split("\n")[0]
    #print(value)
    writer.writerow(value)
