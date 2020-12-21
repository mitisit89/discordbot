const { prefix } = require("../config.json");

module.exports = (bot, aliases, callback) => {
  if (typeof aliases === "string") {
    aliases = [aliases];
  }
  bot.on("message", (message) => {
    const { content } = message;
    for (const alias of aliases) {
      const cmd = `${prefix}${alias}`;

      if (content.startsWith(`${cmd}`) || content === cmd) {
        console.log(`running the command ${cmd}`);
        callback(message);
      }
    }
  });
};
