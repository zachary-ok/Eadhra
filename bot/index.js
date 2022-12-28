require('dotenv').config()
DISCORD_TOKEN = process.env.DISCORD_TOKEN;
DISCORD_CLIENT_ID = process.env.DISCORD_CLIENT_ID

const { REST, Routes } = require('discord.js');

const commands = [
  {
    name: 'ping',
    description: 'Replies with Pong!',
  },
  {
    name: 'wodl',
    description: 'Replies with Wodl!',
  },
  {
    name: 'thot',
    description: 'Replies with Thot!',
  },
  {
    name: 'bueno',
    description: 'Replies with Bueno!',
  },
  {
    name: 'flatfuck',
    description: 'Replies with Flat Fuck!',
  },
  {
    name: 'willsmith',
    description: 'Replies with Will Smith!',
  },
];

const rest = new REST({ version: '10' }).setToken(DISCORD_TOKEN);

(async () => {
  try {
    console.log('Started refreshing application (/) commands.');

    await rest.put(Routes.applicationCommands(DISCORD_CLIENT_ID), { body: commands });

    console.log('Successfully reloaded application (/) commands.');
  } catch (error) {
    console.error(error);
  }
})();

const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('interactionCreate', async interaction => {
  if (!interaction.isChatInputCommand()) return;

  if (interaction.commandName === 'ping') {
    await interaction.reply('Pong!');
  }
  if (interaction.commandName === 'wodl') {
    await interaction.reply('https://i.imgur.com/9G7fL7l');
  }
  if (interaction.commandName === 'thot') {
    await interaction.reply('https://i.imgur.com/RoJ9IYz');
  }
  if (interaction.commandName === 'bueno') {
    await interaction.reply('https://i.imgur.com/a4pQcxn');
  }
  if (interaction.commandName === 'flatfuck') {
    await interaction.reply('https://imgur.com/a/Z4lHs7r');
  }
  if (interaction.commandName === 'willsmith') {
    await interaction.reply('https://tenor.com/view/will-smith-doom-eternal-gif-18735959');
  }
});

client.login(DISCORD_TOKEN);