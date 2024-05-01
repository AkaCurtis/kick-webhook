import requests
import json
import discord
from discord import Webhook, RequestsWebhookAdapter
import time

# Initialize last stream ID as None
last_stream_id = None

def send_discord_notification(stream_title, stream_category, stream_preview_image, streamer_username):
    # Create a Discord webhook
    webhook = Webhook.from_url('WEBHOOK_HERE', adapter=RequestsWebhookAdapter())

    # Create an embed
    embed = discord.Embed(title=stream_title, url=f"https://www.kick.com/{streamer_username}", color=0x32CD32)
    embed.add_field(name="Game", value=stream_category, inline=False)
    embed.set_image(url=stream_preview_image)

    # Send the message with content and embed
    content_message = f"🔴 **{streamer_username} is now live on Kick!**"
    webhook.send(content_message, embed=embed)

headers = {
    'user-agent': 'Google-Safety',
   }

while True:
    response = requests.get('STREAMER_API_URL', headers=headers)
    print(response.content)
    data = response.json()

    if data['data']:  # Check if the streamer is live
        stream_info = data['data']
        stream_id = stream_info['id']
        stream_title = stream_info['session_title']
        stream_category = stream_info['category']['name']
        stream_preview_image = stream_info['thumbnail']['src'].replace('\\', '')
        streamer_username = 'YOUR_USERNAME'  # Replace 'YOUR_USERNAME' with the actual username

        # Check if it's a new stream
        if stream_id != last_stream_id:
            send_discord_notification(stream_title, stream_category, stream_preview_image, streamer_username)
            last_stream_id = stream_id  # Update last stream ID

    else:
        print("Streamer is not live.")

    # Wait for 2 minutes before checking again
    time.sleep(120)
