# garbage_collection_schedule_to_gcal

This script will scrape the http://www.peelregion.ca/waste/ and generate a csv file that can be imported into Google Calendar.
Previously Peel Region used to provide an ics file with the garbage collection schedule but they no longer do so.

What is needed?

Depending on where you live you need to get the url for your complete garbage collection schedule.
To do this follow the steps below:
01. Go to http://www.peelregion.ca/waste
02. If using Google Chrome or Mozilla FireFox open up Dev Tools by hitting the Ctrl + Shift + I shortcut
03. Type your home address under "When Does It Go"
04. Click the "Find" button
05. About four weeks of your schedule will be displayed to you on a new page
06. At the bottom of this page click the "Show More of Collection Schedule"
07. In Dev Tools go to the Network Tab and look for XHR
08. You should find an XHR request that looks similar to the one shown below. 
http://www.peelregion.ca/waste-scripts/when-does-it-go/nextCollectionHTML.asp?service=bm-cr-tue-a&days=4&date=2019-02-05&hidden=1
09. Modify the request so it matches the request shown below.
http://www.peelregion.ca/waste-scripts/when-does-it-go/nextCollectionHTML.asp?service=bm-cr-tue-a&days=365&date=2019-01-01&hidden=0
10. Replace the url variable in the script with the modified url above
11. Change the address variable with your address (this is used to populate the location field in Google Calendar)
12. You can also change the start time and end time if you desire
13. Personally I have created a new calendar called "Garbage Collection" and imported the CSV file into that calendar so my main calendar remains uncluttered.
14. Also don't forget to set the default reminder for the calendar under "All Day Events"
15. For more information on importing a CSV to Google Calendar please see https://support.google.com/calendar/answer/37118?hl=en
16. I am certain I have likely done something stupid so my apologies in advance for any issues. If there are any fixes, suggestions, or anything else for that matter I am happy to implement.
