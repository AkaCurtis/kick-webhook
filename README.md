Hello! Before we get started lets have you read some basic things

- I will not help you personally. I will try to make this as straight forward as possible
- If you want this to run 24/7 you will need a vps!
- YOU DO NOT NEED API ACCESS TO DO THIS!
- There will be some updates for this as well! You're welcome to fork it to make it better!

Preview
========================
![image](https://github.com/AkaCurtis/kick-webhook/assets/63390006/887d7c8a-89b9-4531-a385-d33a94d11cf8)


Getting your Headers
========================

1. First you will go to either your channel or your favorite streamers channel. 
2. Open up your inspect element and click on your network tab
3. You'll most likely need to refresh the tab
4. Look for something that says "Livestream"
5. Right click, go down to copy, and click Copy as cURL (example below)
![Screenshot 2024-04-30 215312](https://github.com/AkaCurtis/kick-webhook/assets/63390006/c286db31-008e-4e7f-bdd3-9bb7fba84228)

Getting your Headers
========================
1. Go here: https://curlconverter.com/ and paste the copied cURL into the top box, this will display your headers 
2. DO NOT CHANGE THE INCLUDED USER-AGENT THIS IS WHAT MAKES THIS WORK. Provided it below just in case you overwrite it (it happens)
    -     'user-agent': 'Google-Safety',
3. You won't need cookies for this

How to create a webhoook
========================
If you're here, you should already know how. but just in case I'll include the steps

1. Open the Discord channel you want to receive Kick stream notifications.
2. From the channel menu, select Edit channel.
3. Select Integrations.
4. If there are no existing webhooks, select Create Webhook. Otherwise, select View Webhooks then New Webhook.
5. Enter the name of the bot to post the message.
6. Optional. Edit the avatar.
7. Copy the URL using the "Copy Webhook URL" button

Bugs that might occur
========================
This code was typed up quickly, so there MIGHT be bugs. Here's a list of some I could think of right away:
- It might send a webhook multiple times (it SHOULDN'T but it might)
- Preview image might be wrong, this is due to the limitations of Kick sadly. Once I find a fix I'll update the script!
