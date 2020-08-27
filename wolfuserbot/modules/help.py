# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" WolfUserBot help command """

from wolfuserbot import CMD_HELP
from wolfuserbot.events import register
import asyncio

modules = CMD_HELP

@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**WolfUserBot Module doesn't exist or Module name is invalid**")
    else:
        await event.edit(f"**All WolfUserBot modules are listed below**\
            \nUsage: Type `.help <module name>` to know how it works\
            \nModules loaded: {len(modules)}")
        string = ""
        for i in sorted(CMD_HELP):
            string += "`" + str(i)
            string += "`  -  "
        await event.reply(string)
        await asyncio.sleep(300)
        await event.delete()