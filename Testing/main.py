import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client()
client = discord.Client(intents=intents)


@client.event
async def on_member_join(member):
    await member.edit(nick= "Fern")


client.run('OTc2MDk4MDU4OTgwOTU4MjY5.GWcoi4.V7RNj3M2OWs3Kbs0qrAgBJlVgK7FawOURR1VWk')




