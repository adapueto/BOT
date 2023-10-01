import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$random-name'):
        await message.channel.send("Amanda")
    elif message.content.startswith('$supercalifagilistico...'):
        await message.channel.send("...espialidoso!!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("MTE1ODA1MzAxOTg2NzQxODcwNA.G-oI6W.FQQnPdeKWxfH7Ja4OlmkK_yJpIIPlaTA8oMlPY")