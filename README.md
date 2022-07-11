Will add proper readme file later....


Pre-requisites:

Install git & python & pip

Install discord-py-interactions: python -m pip install -U discord-py-interactions

Install dotenv: python -m pip install python-dotenv

Clone application and cd into directory

Copy .env.sample to .env

Step 3) Visit the discord developer portal to create a bot, store token in .env file, replace all other environment variables with production values

Step 4) Enable privileged 'Message Content Intent' from Bot section of the portal. No other privileged intents are required.

Step 5) Generate URL to invite the bot to your server. Enable the 'bot' scope and then assign only the following permissions:

    NOTE: Depending on your server's configuration, you may need to manually move the bot's role up the list, or change channel/category/role permissions in order to allow the bot access to a specific channel.

    a) manage messages
    b) read messages/view channels


Step 6) Invite the bot to your server by visiting the URL.

Step 7) On your server, make the bot run in the background by issuing the command `python main.py &` (or use nohup) from the project root directory.
