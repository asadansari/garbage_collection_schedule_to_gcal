## Project is now deprecated.
## Generate you schedule at http://www.peelregion.ca/waste/calendar/
## garbage_collection_schedule_to_gcal

This script will scrape the http://www.peelregion.ca/waste/ and generate a csv file that can be imported into Google Calendar.
Previously Peel Region used to provide an ics file with the garbage collection schedule but they no longer do so.

What is needed?

The script requires your collection schedule code to retrieve your complete garbage collection schedule.

To do this follow the steps below:

01. Go to http://www.peelregion.ca/waste.
02. In Google Chrome or Mozilla FireFox open up Dev Tools by hitting the Ctrl + Shift + I shortcut.
03. Type your home address under "When Does It Go".
04. Click the "Find" button.
05. About four weeks of your schedule will be displayed on a new page.
06. At the bottom of this page click the "Show More of Collection Schedule" button.
07. In Dev Tools go to the Network Tab and look for XHR.
08. You should find an XHR request that looks similar to the one shown below. 
http://www.peelregion.ca/waste-scripts/when-does-it-go/nextCollectionHTML.asp?service=bm-cr-tue-a&days=4&date=2019-02-05&hidden=1
09. Copy the code for your collection schedule from the url in step 8. This is everything after "service=" and before "&days". In my case it is "bm-cr-tue-a".
10. Replace the exisiting collection code in the "collectionSchedCode" variable with the code in step 9.
11. Change the address variable with your address (this is used to populate the location field in Google Calendar).
12. You can also change the start time and end time if you desire.
13. Personally I have created a new calendar called "Garbage Collection" and imported the CSV file into that calendar so my main calendar remains uncluttered.
14. Do not forget to set the default reminder for the calendar under "All Day Events".
15. For more information on importing a CSV to Google Calendar please see https://support.google.com/calendar/answer/37118?hl=en.
16. I am certain that I have done something stupid so my apologies in advance for any issues. If there are any fixes or suggestions I would be more than happy to implement.
17. Comments and criticisms are always welcome.
18. Enjoy!
