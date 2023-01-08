import random
import asyncio
import discord
import requests

intents = discord.Intents(messages=True, guilds=True, members=True)
client = discord.Client(intents=intents)

#defines channel ids
channel_ids = [1061492429175406703, 1009104437375148052]

async def send_random_gif(channel_ids):
    await client.wait_until_ready()
    while not client.is_closed():
        # Send a request to the Cataas API to get a random GIF of a cat
        response = requests.get("http://thecatapi.com/api/images/get?format=src&type=gif")
        # Get the URL of the GIF from the response
        gif_url = response.url
        # Create an embed object with the GIF URL as the image
        embed = discord.Embed().set_image(url=gif_url)
        # Send the GIF to each channel in the list
        for channel_id in channel_ids:
            channel = client.get_channel(channel_id)
            await channel.send(embed=embed)
        await asyncio.sleep(300)  # send a message every 5 minutes, 300 is 10 mins

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    # Replace CHANNEL_IDS with a list of the channel IDs you want the bot to send messages to
    await send_random_gif(channel_ids)


client.run("MTA2MTQ3OTQzNDU3MTQ4NTE4NA.GYQMCM.2zzDhOJabtB0afxSAepmc8t9aRJESEIwCEziiA")
