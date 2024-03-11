<h1 align="center">Cheap Flight Deals</h1>
Run this project and follow the comments/steps and use your own API Keys if you want it to work.


<h2>Step 1</h2> 
You need to create a google spreadsheet with 3 columns with name "City", "IATA Code", "Lowest Price". 

Something like this:-
<br>
![Screenshot 2024-03-11 232108](https://github.com/VishalRaj0/CHEAP_FLIGHT_DEALS/assets/108023331/f6ae1423-c89b-484b-aeb3-270a3ade45da)
<br>
You only need to fill the "City" and "Lowest Price" columns.

<h2>Step 2</h2>
Use the "iata_code_finder" method under "flight_search.py" to get the IATA code for the city in column and use the "update_destination_codes" method under "data_manager.py" to fill the spreadsheet with all the 
IATA codes.

<h2>How to run</h2>
After following the above steps, all you need to do is run "main.py" and messages regarding cheap flights to your destination will be sent to your phone number via your twilio account.

<h2>Important points</h2>
1. Don't do typo in writing the city names in the google spreadsheet.<br>
2. Each json file used for commiting POST request needs to have specific keys, don't change them. <br>
3. Read the <a href="https://tequila.kiwi.com/portal/docs/tequila_api">TEQUILA API DOCS</a> and <a href="https://sheety.co/docs/requests.html">SHEETY.CO_API_DOCS</a> for better understanding of how these API work.
