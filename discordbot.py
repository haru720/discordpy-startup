from discord.ext import commands
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「唐澤貴洋」で始まるか調べる
    if message.content.startswith("唐澤貴洋"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = message.author.name + "ナイフで滅多刺しにして殺す"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

    if message.content.startswith("てすや"):
        if client.user != message.author:
            m ="あああああああああああああああああああああああああああああああ！！！！！！！！！！！（ﾌﾞﾘﾌﾞﾘﾌﾞﾘﾌﾞﾘｭﾘｭﾘｭﾘｭﾘｭﾘｭ！！！！！！ﾌﾞﾂﾁﾁﾌﾞﾌﾞﾌﾞﾁﾁﾁﾁﾌﾞﾘﾘｲﾘﾌﾞﾌﾞﾌﾞﾌﾞｩｩｩｩｯｯｯ！！！！！！！ ）"
            await message.channel.send(m)

    # 「プロシュート」で始まるか調べる
    if message.content.startswith("プロシュート"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "神奈川県藤沢市辻堂元町2－19－19、稲村純一、葛飾商業高校中退"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

    if message.content.startswith("あゆてやん"):
        if client.user != message.author:
            m ="岐阜県大垣市笠縫町387-2、安藤あゆみ"
            await message.channel.send(m)

bot.run(token)
