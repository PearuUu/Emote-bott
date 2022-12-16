import discord

TOKEN = 'MTAzMjIyNDAxMTc0NjI3OTQ0NQ.GJM9pQ.x74J3TnHdJGGujUIp0dgObA_1Bac8u1fs78isk'



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        isAnimated = False
        userMessage = message.content
        userName = message.author

        emote = userMessage.split(":")
        emoteId = emote[2][:-1]

        if len(emote[0]) > 1:
            isAnimated = True

        if message.author != self.user:
            if isAnimated:
                await message.channel.send(f'https://cdn.discordapp.com/emojis/{emoteId}.gif?size=128&quality=lossless')
            else:
                await message.channel.send(f'https://cdn.discordapp.com/emojis/{emoteId}.webp?size=128&quality=lossless')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)

