import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

anecdots = ['Изобрели немцы часы которые услышав мат переходили на одну минуту вперед. Решили провести эксперимент: поставят они значит часы в американский бар, \nфранцузкий бар и русский заодно. И вот поставили часы в французкий бар и ушли, через день вернулись \nглядят часы на 3 минуты опережают. Поставили в американский бар через день вернулись \nопережают на 8 минут. Поставили в русский бар через день приходят часов \nнет спрашивают бармена где часы. А он "какие часы?". "Да вон там \nна стене висели" говорят немцы. "А это часы были? А я думал на##й \nнам вентилятор зимой нужен" .(Было так много мата что стрелки часов постоянно \nдвигались как вентилятор)', 
'Была одна проблемная лошадь. отвез хозяин лошади ее к ветеринару говорит мол не двигается и не ест. Ветеринар дает таблетки и говорит что елси через 5 дней неоклимается то уже ничем не поможешь. Первый день дали таблетку не поднимаеться. Фермер:"Наверное придется зарезать". Свинья усливший это бежит к лошади говорит "вставай а то зарежут тебя". Лошадь не встает итак 4 дня. Пятый день лошадь встала хозяен радуется и говорит "По такому поводу зарегим свинью".']
l = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFHJKLZXCBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯСМИТЬБЮЁйцукенгшщзхъфывапролджэячсмитьбюё'
bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def slove_ex(ctx, example : str):
    """Adds two numbers together."""
    await ctx.send(eval(example))

@bot.command()
async def repeat(ctx, times = 1, content = 'repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'Hello {member.name} {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def rand_name(ctx, length = 10):
    nick_name = ''
    for i in range(length):
        nick_name += random.choice(l)
    
    await ctx.send(nick_name)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def anecdot(ctx):
    await ctx.send(random.choice(anecdots))

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
bot.run("Token")
