# Discord update bot
Small bot for Discord integration. It listens on Github webhook posts in configured 
discord channels to trigger scripts on a remote server.

# Quick start
1. Install the discord module with ``pip install discord``.
2. Then run ```python run.py```

# Config
Configure the bot with a json file named ``dc_bot.cfg`` (see ``sample.cfg`` for structure).

In a list specify each trigger to listen on Github web hook posts in a channel. For each
trigger configure:
* ``repo``: The name of the Github repository.
* ``branch``: The branch to listen on, e.g. master
* ``channel_id``: The id of the discord channel to listen on. You find this ID by right clicking on a text channel
* ``script``: The commands to trigger as a list e.g. ``["explorer", "."]`` or ``["./path/to/script"]``