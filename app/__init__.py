import discord
from discord.ext import commands


class Bot(discord.Client):
    list_of_commands = ['!привет', '!команды', '!Дай прогноз', '!спасибо']

    # bot_id='<@783440611474014258>'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


    async def on_message(self, message, ):
        mestro = '<@447491112823685140>'  # формат id
        if message.author.id == self.user.id:
            return
        if message.content == f'привет':
            await message.channel.send(f'Привет,я рад тебя видеть {message.author.mention} !')
        if message.content == 'карп':
            await  message.channel.send(f"Карпа убиль {mestro},но это не точно  {message.author.mention}!")
        if message.content.startswith('Дай прогноз'):
            await message.channel.send(f'Для успеха нужно построить Зиккурат,{message.author.mention}')
        if message.content == '!спасибо':
            await message.channel.send(f'ат души {message.author.mention}, братан')
        if message.content == 'команды':
            for command in self.list_of_commands:
                await  message.channel.send(command)


bot = Bot(command_prefix='!')

'''
client.event
async def on_message(message):
   

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
   
    if message.content.startswith('!карп велик')=='!карп велик':
        await message.channel.send('Да,конечно он карп велик')
    if message.content.startswith('!покушать'):
        await message.channel.send('Я бот ,я не умею готовить')'''
