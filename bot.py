# bot.py
import os,time,asyncio,random
from twitchio.ext import commands
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token='IRC TOKEN HERE', client_id='CLIENT ID HERE', nick='BOT NAME HERE', prefix='PREFIX HERE',
                         initial_channels=['twitchverse'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')
        task = asyncio.create_task(feed_channel(self))

async def feed_channel(self):
    emotes = ["Kappa","DansGame"]
    stream = self.get_channel('twitchverse')
    while True:
        command = "!feed CHANNELNAMEHERE"
        for x in range(15):
            command = command + " " + random.choice(emotes)
        await stream.send(command)
        await asyncio.sleep(5)



bot = Bot()
bot.run()