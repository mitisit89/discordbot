const { Client } = require("discord.js");
const bot = new Client();
const command = require("./commands/command.js");
const fs = require("fs");
const { token } = require("./config.json");

bot.on("ready", () => {
  console.log(`ready ${bot.user.tag} to working`);
  command(bot, ["ping"], (message) => {
    message.channel.send("pong");
  });
  command(bot, ["servers"], (message) => {
    bot.guilds.cache.forEach((guild) => {
      message.channel.send(
        `$ У сервера  ${guild.name} всего ${guild.memberCount} участников `
      );
    });
  });
  command(bot, ["cc", "clearchannel"], (message) => {
    if (message.member.hasPermission("ADMINISTRATOR")) {
      message.channel.messages.fetch().then((result) => {
        message.channel.bulkDelete(result);
      });
    }
  });
  command(bot, "status", (message) => {
    const content = message.content.replace("!status", "");
    bot.user.setPresence({
      activity: {
        name: content,
        type: 0,
      },
    });
  });
  command(bot,"карп",(message)=>{
    message.channel.send(`Карп жив и велик как никогда ${message.author},его никто убивал , это все враки`)
  })

});

bot.login(token).catch((e) => console.error(e));
