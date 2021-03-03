# Discord Bot 

A Python based bot using Discord API to UwU-ify a person's text message and add gifs to a Server.

* Stores a Token in a separate file to pull from for security.
* Use of the random module to determine a random gif to post on command.
* On command will replace all "l" and "r" characters in a selected message with "w" and mention the original poster.
* Deletes the command message.

## Things to consider:
* Additional gifs
* Removal of unnecessary commands - creating a channel with the server for example.
* Editing the welcome message - Could either not DM an individual upon joining, could edit to be more UwU on sending, or could send an UwU message to the whole server when the bot is invited to the server.
* Fixing how replacements are made - currently has the potential to be hard to read with double letters and certain words such as "lol" would lose their meaning.

### Lessons:
* Reading documention thoroughly is an incredibly useful skill.
* Discord API and how to interact with it if something is not functioning appropriately or as expected.
* Intents!! 