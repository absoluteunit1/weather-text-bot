Weather Text Bot

I wanted to create a simple program that I would use. 

I created this weather-updater using the following tools:

- Python, OpenWeatherAPI, Twilio API, AWS EC2, crontab (a linux time based job scheduler), and the keys I saved in my EC2 instance for the APIs.

This python scripts executes everyday at 10pm on my EC2 Ubuntu instance. When it executes, I receive a text forecasting tomorrow's weather conditions (temp, wind speend, 'feels like..' and a general description) for 9am and 3pm. 

Having the bot text me the weather for the next day is quite convenient as I often forget to check the weather in the morning when I'm rushing out the door.  




