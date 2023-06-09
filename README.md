# Docker-Discord-Bot
Discort music bot Dockerized

## What does it do?
This is a Python script that uses the Discord API to create a bot that can join a voice channel in a Discord server, play a song, pause, resume or stop the song, list all the members and channels in the server, move a member to a random voice channel, spam a member with messages, and clear the chat. The script also includes a command to disconnect a member from the server.

The script uses the discord and dotenv modules to interact with the Discord API and load the token and server name from a .env file. It also uses the commands module from the discord.ext package to define the commands that the bot can respond to.

To use this script, you will need to create a Discord bot and obtain a token from the Discord Developer Portal. You will also need to set up a .env file with the token and server name. Then, you can run the script and use the commands in the Discord server to interact with the bot.

## Creating a Docker Image for a Python-based Discord Bot
This Dockerfile creates a Docker image for a Python 3.10.6 runtime environment and sets the working directory to "/app". It then copies all the contents of the current directory to the "/app" directory in the Docker image.

The "requirements.txt" file is then installed using pip3, which contains all the necessary dependencies required to run the main.py script. Finally, the Docker container is started and the command "python3 main.py" is executed to run the Discord bot implemented in main.py.
