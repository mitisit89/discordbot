import discord
TOKEN = 'NzgzNDQwNjExNDc0MDE0MjU4.X8ax7Q.1BEfVEju3N5RzEk1OU4QHopT_Pk'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!привет'):
        await message.channel.send('Привет,я рад тебя читать!')
    if message.content.startswith('!about'):
        await message.channel.send('Привет ,я бот. Пока я ничего не умею ,но я буду учится ,что бы стать лучше ')
    if message.content.startswith('!команды'):
        await message.channel.send('!привет\n !about\n !команды')
    if message.content.startswith('!карп'):
        await message.channel.send('Карпа убиль @Mestro ,но это не точно ')

    if message.content.startswith('!бот подайте стол'):
        await message.channel.send('┬─┬ノ( º _ ºノ) пожалуйста')
    if message.content.startswith('!бот переверни стол'):
        await message.channel.send('( ╯°□°)╯ ┻━━┻')
    if message.content.startswith('!спасибо бот'):
        await message.channel.send('ат души, братан')
    if message.content.startswith('!Бот дай прогноз'):
        await message.channel.send('Для успеха нужно построить Зиккурат')
