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

    elif message.content == "日吉烏":

        await message.channel.send("キャンパス内に巣の存在が複数確認されており、時折（特に夕方）けたたましい鳴き声を上げながら大群が上空を旋回する。塾高生がポテトを落としてから、くちばしに咥えて持ち去るまでのスピードには目を見張るものがある。")

    elif message.content == "まむし谷階段":

        await message.channel.send("校舎から直接まむし谷に行く唯一の道。かなり急である。部活後の人々にとってあれほど面倒なものはない。まさに「行きはよいよい・帰りはつらい」である。")

    elif message.content == "医学部":

        await message.channel.send("塾高では超エリートのみが進学を許される最強学部。外部入学は基本浪人です。")

    elif message.content == "オワTA":

        await message.channel.send("「終わった」の派生語である「オワタ」がさらに派生した語。")

    elif message.content == "意見箱":

        await message.channel.send("生徒会室前につるしてある木の箱。紙に書いた意見を入れると生徒会に届き、場合によっては先生にも届く…らしい。監査局付近にも似た箱があるので注意。なお塾高生からその存在は忘れ去られている。2018年から担当の部署もでき期待できる…かも？")

    elif message.content == "漢":

        await message.channel.send("生き様が立派な、「こいつこそ男の中の男だ！」を定義とした代名詞。")

    elif message.content == "エグい":

        await message.channel.send("つらい、きつい、の塾語表現。代表的な塾語であり、毎年無理して使いたがる新入生のさまは見ていてエグい。広義では「グロテスク」の意味で用いられたりする。動：「エグる」")

   
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
