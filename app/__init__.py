import discord


class Bot(discord.Client):

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content == '!привет':
            await message.channel.send(f'Привет,я рад тебя видеть {message.author.mention} !')
        if message.content == 'карп':
            await  message.channel.send(f"Карпа убиль @Mestro ,но это не точно  {message.author.mention}!")


bot = Bot()

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
