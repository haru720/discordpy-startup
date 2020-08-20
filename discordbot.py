import discord
import os


# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'DISCORD_BOT_TOKEN'

# 接続に必要なオブジェクトを生成
client = discord.Client()

async def greet():
    channel = client.get_channel(743788202543808583)
    await channel.send('起動')
    
@client.event
async def on_ready():
    await greet()



@client.event
async def on_message(message):
    if message.content == 'ポア':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('ポアします')
        else:
            await message.channel.send('修行しなさい')


    elif message.content == "十月祭":

        await message.channel.send("女子高の文化祭。名前通り、神無月に行われる。その実態は猛烈な勧誘の嵐。さながら、新宿歌舞伎ｔ（ｒｙ......。")

    elif message.content == "塾高":

        await message.channel.send("天下")



# 起動時に動作する処理


# メッセージ受信時に動作する処理



#channel = client.get_channel(payload.channel_id)
    #if channel.id != ID_CHANNEL_GET_ROLE:
        #return
    #member = channel.guild.get_member(payload.user_id)
    #if payload.emoji.name == "emoji_1":
        #role1 = guild.get_role(ID_ROLE_GENEKI)
        #await member.add_roles(role1)
        #return member

    #if payload.emoji.name == "emoji_2":
        #role2 = guild.get_role(ID_ROLE_OB)
        #await member.add_roles(role2)
        #return member

    #if payload.emoji.name == "emoji_3":
        #role3 = guild.get_role(ID_ROLE_PARENTS)
        #await member.add_roles(role3)
        #return member

    #if payload.emoji.name == "emoji_4":
        #role4 = guild.get_role(ID_ROLE_CHARANGER)
        #await member.add_roles(role4)
        #return member

    #if payload.emoji.name == "emoji_5":
        #role5 = guild.get_role(ID_ROLE_KEIRETSU)
        #await member.add_roles(role5)
        #return member

    #if payload.emoji.name == "emoji_6":
        #role6 = guild.get_role(ID_ROLE_OTHERS)
        #await member.add_roles(role6)
        #return member

    #await channel.send('ロール付与したナリ')









# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
