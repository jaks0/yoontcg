#Importing Database
import discord
import random

#Client (the bot)


#player acccounts
client = discord.Client()


#Database files
playerid = open("username_database.txt", "w+")


@client.event
async def on_message(message):
    if message.content == 'yoontcg start':
        general_channel = client.get_channel(700202243370123294)
        await general_channel.send('Welcome to the Yoon Trading Card Game!')
        await general_channel.send('Are you ready to delve into the mystical world of yoonTCG?!!!')
        await general_channel.send("reply 'yoontcg createaccount' to create an account")
    if message.content == 'yoontcg createaccount':
        playerid.write(str(message.author.id))
        general_channel = client.get_channel(700202243370123294)
        await general_channel.send('Added Account')
        return playerid.close()

client.run('Nzc0MTEyNjgzNDczMjQwMDc0.X6TCng.YNW_KkHgvPlMBtDou7jVwGvSGwA')
