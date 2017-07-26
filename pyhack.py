import discord
import aiohttp
import asyncio
import keyboard as k 
from discord.ext.commands import Bot
bot = Bot(';', pm_help=False)

@bot.command(pass_context=True)
async def nethack(ctx):
    m = ctx.message
    mc = m.content[9:]
    try:
        arg = mc.split(' ')[0]
    except:
        return
    try:
        secondarg = mc.split(' ')[1]
    except:
        secondarg = ''
    try:
        thirdarg = mc.split(' ')[2]
    except:
        thirdarg = ''
    if arg == '': await bot.send_message(m.channel, 'Invalid command. Not passing.')
    elif arg == 'up':
        k.send('k')
    elif arg == 'left':
        k.send('h')
    elif arg == 'right':
        k.send('l')
    elif arg == 'down':
        k.send('j')
    elif arg == 'upleft':
        k.send('y')
    elif arg == 'upright':
        k.send('u')
    elif arg == 'downleft':
        k.send('b')
    elif arg == 'downright':
        k.send('n')
    elif arg == 'inventory':
        k.send('i')
    elif arg == 'opendoor':
        k.send('o')
    elif arg == 'closedoor':
        k.send('c')
    elif arg == 'pickup':
        k.send('comma')
    elif arg == 'drop':
        k.send('d')
    elif arg == 'eat':
        k.send('e')
    elif arg == 'yes':
        k.send('y')
    elif arg == 'no':
        k.send('n')
    elif arg == 'wear':
        k.send('shift+w')
    elif arg == 'takeoff':
        k.send('shift+t')
    elif arg == 'equipamulet':
        k.send('shift+p')
    elif arg == 'removeamulet':
        k.send('shift+r')
    elif arg == 'weapon':
        if secondarg != '':
            k.send('w')
            k.send(secondarg)
    elif arg == 'throwweapon':
        if secondarg != '' and thirdarg != '':
            k.send('t')
            k.send(secondarg)
            k.send(thirdarg)
    elif arg == 'quiverselect':
        if secondarg != '':
            k.send('shift+q')
            k.send(secondarg)
    elif arg == 'fire':
        k.send('f')
    elif arg == 'usewand':
        if secondarg != '':
            k.send('z')
            k.send(secondarg)
    elif arg == 'scroll':
        if secondarg != '':
            k.send('r')
            k.send(secondarg)
    elif arg == 'memoryspell':
        if secondarg != '':
            k.send('shift+z')
            k.send(secondarg)
    elif arg == 'potion':
        if secondarg != '':
            if ', ' in mc:
                aaa = mc[16:]
                k.send('q')
                k.send(aaa)
            else:
                k.send('q')
                k.send(secondarg)
    elif arg == 'tool':
        k.send('a')

bot.run('TOKEN')