from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def 椎名(ctx):
    await ctx.send('福島県在住、武田彪、松韻学園福島高校、ホモビ男優')

@bot.command()
async def あゆてやん(ctx):
    await ctx.send('岐阜県大垣市笠縫町387-2、安藤あゆみ')
    
@bot.command()
async def てすや(ctx):
    await ctx.send('て、てすやっ！？')

@bot.command()
async def 脱糞(ctx):
    await ctx.send('あああああああああああああああああああああああああああああああ！！！！！！！！！！！（ﾌﾞﾘﾌﾞﾘﾌﾞﾘﾌﾞﾘｭﾘｭﾘｭﾘｭﾘｭﾘｭ！！！！！！ﾌﾞﾂﾁﾁﾌﾞﾌﾞﾌﾞﾁﾁﾁﾁﾌﾞﾘﾘｲﾘﾌﾞﾌﾞﾌﾞﾌﾞｩｩｩｩｯｯｯ！！！！！！！)')

@bot.command()
async def プロシュート(ctx):
    await ctx.send('神奈川県藤沢市辻堂元町2－19－19、稲村純一、葛飾商業高校中退')
    


bot.run(token)

