import discord
from  discord.utils import get
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
roles=[role.name for role in bot.guilds.roles]
print(roles)

#719928773230985286

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
@bot.command(name='test')
async def _test(context):
    await context.channel.send(f"Я работаю  и с мной все в проядке  {context.message.author.mention}! ")
    '''
    context.message.author.mention для обращения к пользователью 
    '''

@bot.command(name='карп')
async  def on_karp_reaction(message):
    if message.content=='карп':
        await  message.channel.send(f'карпа нет его убиль стример')

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
    if message.content.startswith('!спасибо бот'):
        await message.channel.send('ат души, братан')
    if message.content.startswith('!Бот дай прогноз'):
        await message.channel.send('Для успеха нужно построить Зиккурат')
    if message.content.startswith('!карп велик')=='!карп велик':
        await message.channel.send('Да,конечно он карп велик')
    if message.content.startswith('!покушать'):
        await message.channel.send('Я бот ,я не умею готовить')'''