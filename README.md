# Genie - SBHacks 2019  ![build passing](https://img.shields.io/circleci/project/github/badges/shields/master.svg)
### Code developed by: Jerry Lee, Kyle Semelka, Jeffrey Wong, Brandon Lam  
## Platform that allows access to specific, important information that are typically difficult to find
## Customer Usage:  
Customers have either the option of texting the business phone number information or using our mobile application to find/select the business and message from there.
Customers can use Natural Language in the text messages to ask for specific information. 
Our server will process the request, fetch the correct information, and send a reply text with the information. This makes it convenient for customers to find specific information that could otherwise take some time to look up or be difficult to find. Also,because the response is by our server and database, the business being inquired about is not interrupted by repeated questions.  
Example: "Are you open today and if so, what are the store hours?"  
Response from our server: "Yes, we are open today from 9am to 5pm."
## Business Usage:
For our platform, we specifically built it to be used by restaurants, just to serve as one specific example of the use cases. 
We built a web application specifically for restaurants to be able to log in and easily input their information. 
They could enter things such as their menu items, location, etc. Here we also integrated the Google Calendar API. 
The resutaurants are given an option to integrate their Google Calendar into our database so if they have their business schedule set up on a calendar with what days they're open, the specific hours of each day, daily specials and special events, all of the data would be automatically stored by our database. Once there, the restaurant does not have to worry about it anymore because our software will automatically provide this information to customers when asked.

## Technologies Used:  
### Google Cloud Platform:  
Google Cloud SQL  
Google Cloud App Engine  
Google Calendar API
### Twilio  
Twilio SMS text API
