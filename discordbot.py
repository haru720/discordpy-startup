# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'DISCORD_BOT_TOKEN'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理

async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == 'てすや':
        await message.channel.send('当職は今日も元気ですを')

CHANNEL_ID = 743788202543808583

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('起動')


async def on_ready():
    await greet() # 挨拶する非同期関数を実行

async def on_message(message):
    if message.content == '/削除':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('ポアします')
        else:
            await message.channel.send('修行しなさい')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
