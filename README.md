# schedule-bot-template
> Telegram bot template that sends the lesson schedule

# demo 
![demo](https://github.com/Intercrus/schedule-bot-template/blob/master/demo-template.gif)

# Features

* **aiogram** as a framework
* **db gino** as a ORM
* **PostgreSQL** as a database

## Getting Started
1. Clone the repository
> If you have ubuntu - leave the ip the same (localhost)
2. Download PostgreSQL and pgAdmin4
3. In pgAdmin4 create a server with the following settings:
![](https://github.com/Intercrus/ScheduleBotTelegram/blob/master/Screenshot%20from%202020-11-12%2000-50-39.png)
4. Create a database on the server in PostgreSQL
5. Change the file .env (```/schedule-bot-template/.env```)
> The file has hints on what to change (this is your bot token, your id, etc.)
6. Install the modules that the bot uses. They are in the file requirements.txt ```/schedule-bot-template/requirements.txt```
7. Run the file app.py 
> After that the bot should work





