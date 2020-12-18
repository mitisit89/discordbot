from  app import bot

file=open("token.txt")
TOKEN=file.read()
file.close()
if __name__ == '__main__':
    bot.run(TOKEN)
