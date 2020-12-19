const Discord = require('discord.js');
const bot=new Discord.Client()
const commands = require('./commands/command.js')
const fs = require('fs');
const config =require('./config.json')

const TOKEN = config.token;
let prefix=config.prefix


bot.on('ready',()=>{
    console.log(`ready ${bot.user.tag} to working`);
})
bot.on('message',(msg)=>{
    if(msg.content==='ping'){
       msg.channel.send('pong');
    }
})
bot.login(TOKEN)