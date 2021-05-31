# personal_bot
A bot to figure out the basics of discord bots and the api. Has quite a few random commands, including a timer, a google image search, and just saying bob.

# Libraries/Modules

discord.py 

Excellent guide on starting to make a discord bot:
https://realpython.com/how-to-make-a-discord-bot-python/#what-is-discord

Uses hardikvasa's google image download, https://github.com/hardikvasa/google-images-download

//install this using pip install google_images_download ----do not use unless it has been updated recently, date of this note: 5/13/21

Instead: patched version here, use these commands in your site-packages folder in python folders
(navigate here using %appdata% and going to local for windows)

git clone https://github.com/Joeclinton1/google-images-download.git

cd google-images-download THEN do python setup.py install


# Using this bot

This bot has a bunch of random features that I'm trying my hand at implementing, such as a timer, simple text file reading and outputting, etc.
Feel free to take the file and run it in your own server, you'll simply have to follow the guide to make your own .env file with your own token that
discord should provide. 

You'll also want to change the text file, although the command to load it should be able to take in different names.
