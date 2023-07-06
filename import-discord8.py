import discord
from discord.ext import commands
import csv

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    print('Pronto para salvar as threads em threads.csv!')
    await bot.wait_until_ready()  # Aguarda o bot carregar todas as informações
    await salvar_threads()

async def salvar_threads():
    guild_id = 000  # Substitua pelo ID do seu servidor
    guild = bot.get_guild(guild_id)

    if guild is None:
        print('Servidor não encontrado.')
        return

    channels = await guild.fetch_channels()

    threads = [channel for channel in channels if isinstance(channel, discord.Thread)]

    if threads:
        with open('threads.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'ID', 'Conteúdo'])
            for thread in threads:
                messages = await thread.history().flatten()
                thread_content = '\n'.join([message.content for message in messages])
                writer.writerow([thread.name, thread.id, thread_content])
        print('As threads foram salvas em threads.csv.')
    else:
        print('Não há threads neste servidor.')

bot.run('TOKEN_DO_BOT')
