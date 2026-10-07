This is the folder that will contained everything for the backend


Backend - Python/FastAPI for Data Processing and AI Logic

To do: 


- Write out skeleton (allocate ports/terminal to modules (ex. Temperature, moisture, etc)) 

- Using Open Ai and connect to it - for AI prompts

- Figure out a way to store data for all the modules, for each plant, for each user - PostgreSQL for database storage and proceessing 

- Build a pathway from that database 
→ Prototype - database + Ai - our decision making (BRAIN CENTER) - user interface (“advice”)

- Use “best” from internet, and like adjust it with our trained Ai model (later)
	→ Use Color coding to establish “Good, Okay, Bad” 



How the Data Flows (Step-by-Step)

User presses a button in the mobile app.

The App sends a request over the internet to your custom Backend.

Your Backend wakes up and does three things internally:

It pulls the user's history from the Database.
It runs the Web Scraper to grab fresh internet data.It bundles that data together and sends it to the AI Model.

The AI Model sends the prompt/response back to your Backend.

Your Backend cleans up the answer and sends it back to the Mobile App.