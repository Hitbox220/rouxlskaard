import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.utils import get
import os

special_roles = ['RP', 'Patience', 'Ink', 'XGaster', 'Determination']
admin_roles = ['Patience', 'Ink', 'XGaster', 'Determination', 'Frisk']
roles = dict([])

warn_list = dict([])

five_seconds = 0
mutelist = dict([])
muteid = []

Bot = commands.Bot(command_prefix='~')

Bot.remove_command('help')

@Bot.event
async def on_ready():
    global roles
    print('Последний актёр на сцене')
    channel = Bot.get_channel(832476941843038208)
    guild_id = 822463079580565514
    guild = discord.utils.find(lambda g: g.id == guild_id, Bot.guilds)
    emb = discord.Embed(
                               title = 'Рукслс Каард проявляется из тьмы!',
                               colour = discord.Colour.from_rgb(123, 0, 216)
                              )
    await channel.send(embed = emb)

    roles = dict([
        ['Muted', discord.utils.get(guild.roles, name = 'Muted')],
        ['assistant_role', discord.utils.get(guild.roles, name = 'Тестировщик')],
        ['diamond', discord.utils.get(guild.roles, name = 'Бубны')],
        ['spade', discord.utils.get(guild.roles, name = 'Пики')],
        ['heart', discord.utils.get(guild.roles, name = 'Черви')],
        ['club', discord.utils.get(guild.roles, name = 'Трефы')],   
        ['RP', discord.utils.get(guild.roles, name = 'RP')],
        ['RP-muted', discord.utils.get(guild.roles, name = 'RP-muted')],
        ['Patience', discord.utils.get(guild.roles, name = 'Patience')],
        ['Patience-muted', discord.utils.get(guild.roles, name = 'Patience-muted')],
        ['Ink', discord.utils.get(guild.roles, name = 'Ink')],
        ['Ink-muted', discord.utils.get(guild.roles, name = 'Ink-muted')],
        ['XGaster', discord.utils.get(guild.roles, name = 'XGaster')],
        ['XGaster-muted', discord.utils.get(guild.roles, name = 'XGaster-muted')],
        ['Determination', discord.utils.get(guild.roles, name = 'Determination')],
        ['Determination-muted', discord.utils.get(guild.roles, name = 'Determination-muted')],
        ['Frisk', discord.utils.get(guild.roles, name = 'Frisk')],
        ['Frisk-muted', discord.utils.get(guild.roles, name = 'Frisk-muted')],
    ])
#    print(roles)
    print('roles was loaded')

@Bot.event
async def on_member_remove(member: discord.member):
    channel = Bot.get_channel(822463079580565517)
    await channel.send(f'<@{member.id}>. Будем ждать тебя снова!')

@Bot.event
async def on_raw_reaction_add(payload):
    global roles
    print('+')
    message_id = payload.message_id
    guild_id = 822463079580565514
    guild = discord.utils.find(lambda g: g.id == guild_id, Bot.guilds)
    if message_id == 833561961978921041:
        
        if payload.emoji.name == 'spaded':
            role = roles['spade']
            
        elif payload.emoji.name == 'diamonded':
            role = roles['diamond']

        elif payload.emoji.name == 'hearted':
            role = roles['heart']
            
        elif payload.emoji.name == 'clubed':
            role = roles['club']

        else:
            role = None

        if role is not None:
            member = payload.member
            print(member)
            if member is not None:
                for i in ['Черви', 'Пики', 'Трефы', 'Бубны']:
                    if get(member.roles, name = i):
                        print('Больше 1 роли')
                        break
                    elif i == 'Бубны':
                        await member.add_roles(role)
                        print('выполнено')
            else:
                print('участник не найден')
        else:
            print('роль не найдена')
            
@Bot.event
async def on_raw_reaction_remove(payload):
    global roles
    print('-')
    message_id = payload.message_id
    guild_id = 822463079580565514
    guild = discord.utils.find(lambda g: g.id == guild_id, Bot.guilds)
    if message_id == 833561961978921041:
        
        if payload.emoji.name == 'spaded':
            role = roles['spade']
            
        elif payload.emoji.name == 'diamonded':
            role = roles['diamond']

        elif payload.emoji.name == 'hearted':
            role = roles['heart']
            
        elif payload.emoji.name == 'clubed':
            role = roles['club']

        else:
            role = None

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            print(member)
            if member is not None:
                await member.remove_roles(role)
                print('выполнено')
            else:
                print('участник не найден')
        else:
            print('роль не найдена')

@Bot.command()
async def help(ctx):
    emb = discord.Embed(
                                title = 'Список всех команд',
                                description = '''~HP <озѣ> <защита> - расчётѣ суммарного озѣ с защитой\n
                                                    Пример: ***~HP 10 30*** \n
                                                    ~ban <Пользователь> <Причина> - Банѣ пользователя **(слова.разделяются.точкой)**\n
                                                    Пример: ***~ban anybody Оскорбление.Администрации*** \n
                                                    ~mute <Пользователь> <Причина> - лишение пользователя правѣ писать в чатѣ **(слова.разделяются.точкой)**\n
                                                    Пример: ***~mute anybody Оскорбление.Администрации***\n
                                                    ~unmute <Пользователь> - возвращение пользователю права писать в чатѣ\n
                                                    Пример: ***~unmute anybody ***\n
                                                    Бот создан <@768074297192611861> 19.03.2021
                                                    Обновление 1.1 (15.04.2021)''',
                                colour = discord.Colour.from_rgb(231, 78, 255)
                                        )
            
    await ctx.send(embed = emb)  

@Bot.command()
async def assistant(ctx, member: discord.Member):
    global roles
    await member.add_roles(roles[assistant_role])

@Bot.command()
async def deb(ctx, member: discord.Member):
    global warn_list
    print(warn_list)

@Bot.command()
async def HP(ctx, hp, df):
    print(hp, df)
    try:
        hps = int(hp)
        dfs = int(df)
        emb = discord.Embed(
            title = 'Великикй герцогѣ решилѣ эту небольшую задачу',
            description = f'Суммарное озѣ: {(100/(100-dfs))*hps}\nЗащита: {dfs}, Озѣ безѣ защиты: {hps}',
            colour = discord.Colour.from_rgb(100, 255, 100)
                                        )
        await ctx.send(embed = emb)
        
    except:
        emb = discord.Embed(
            title = 'Руклс заметилѣ ошибку!',
            description = f'Даны неверные аргументы!',
            colour = discord.Colour.from_rgb(255, 23, 0)
                                        )
        await ctx.send(embed = emb)
            
@Bot.command()
async def ban(ctx, member: discord.Member, cause):
    caused = cause.replace('.', ' ')
    author = ctx.author
    for role in admin_roles:
        if get(author.roles, name = role):
            await ctx.guild.ban(member, reason=cause)
            emb = discord.Embed(
                                title = 'Бан пользоваетля',
                                description = f'Пользователь <@{member.id}> был забанен: \nПричина: {caused}',
                                colour = discord.Colour.from_rgb(255, 0, 0)
                                )
            await ctx.send(embed = emb)

            break
        else:
            if role == 'Frisk':
                emb = discord.Embed(
                                         title = 'Превышение полномочий',
                                         description = f'Дорогуша, ты не можешь использовать эту команду.',
                                         colour = discord.Colour.from_rgb(255, 0, 0)
                                         )
            
                await ctx.send(embed = emb)
            else:
                continue

@Bot.command()
async def warn(ctx, member: discord.Member, cs):
    global warn_list
    print(cs, type(cs))
    memberid = str(member.id)
    author = ctx.author
    for role in admin_roles:
        if get(author.roles, name = role):
            try:
                a = warn_list[memberid]
                warn_list[memberid].append(cs)
            except:
                warn_list[memberid] = [cs]
            break
        else:
            if role == 'Frisk':
                emb = discord.Embed(
                                         title = 'Превышение полномочий',
                                         description = f'Дорогуша, ты не можешь использовать эту команду.',
                                         colour = discord.Colour.from_rgb(255, 0, 0)
                                         )
            
                await ctx.send(embed = emb)
            else:
                continue

@Bot.command()
async def warn_list(ctx):
    member = ctx.author
    try:
        a = warn_list[member.id]
        emb = discord.Embed(
                                title = 'Список предупреждений',
                                description = str(warn_list[str(member.id)]),
                                colour = discord.Colour.from_rgb(255, 0, 0)
                                         )
            
        await ctx.send(embed = emb)
    except:
        emb = discord.Embed(
                                title = 'Список предупреждений',
                                description = 'Здесь нету предупреждений',
                                colour = discord.Colour.from_rgb(255, 255, 10)
                                         )
            
        await ctx.send(embed = emb)
    
@Bot.command()
async def mute(ctx, member: discord.Member, cause):
    global special_roles, roles, perms
    caused = cause.replace('.', ' ')
    author = ctx.author
    for role in admin_roles:
        if get(author.roles, name = role):
            emb = discord.Embed(
                                            title = 'Мьют пользоваетля',
                                           description = f'Пользователь <@{member.id}> был лишён права писать в чат: \nПричина: {caused}',
                                           colour = discord.Colour.from_rgb(255, 0, 0)
                                           )
            for role in special_roles:
                if get(member.roles, name = role):
                    print('.')
                    await member.remove_roles(roles[role])
                    await member.add_roles(roles[role+'-muted'])

            print(roles)
            
            await ctx.send(embed = emb)
            await member.add_roles(roles['Muted'])

            break
        else:
            if role == 'Frisk':
                emb = discord.Embed(
                                         title = 'Превышение полномочий',
                                         description = f'Дорогуша, ты не можешь использовать эту команду.',
                                         colour = discord.Colour.from_rgb(255, 0, 0)
                                         )
            
                await ctx.send(embed = emb)
            else:
                continue
            
@Bot.command()
async def unmute(ctx, member: discord.Member):
    global special_roles, roles
    author = ctx.author
    for role in admin_roles:
        if get(author.roles, name = role):
            await member.remove_roles(roles['Muted'])
            for role in special_roles:
                if get(member.roles, name = role+'-muted'):
                    await member.remove_roles(roles[role+'-muted'])
                    await member.add_roles(roles[role])
            emb = discord.Embed(
                                         title = 'Размьют пользоваетля',
                                         description = f'Пользователю <@{member.id}> были возвращены права писать в чат.',
                                         colour = discord.Colour.from_rgb(100, 255, 100)
                                         )
            
            await ctx.send(embed = emb)

            break
        else:
            if role == 'Frisk':
                emb = discord.Embed(
                                         title = 'Превышение полномочий',
                                         description = f'Дорогуша, ты не можешь использовать эту команду.',
                                         colour = discord.Colour.from_rgb(255, 0, 0)
                                         )
            
                await ctx.send(embed = emb)
            else:
                continue
        
token = os.environ.get('rk_token')
Bot.run(str(token))
