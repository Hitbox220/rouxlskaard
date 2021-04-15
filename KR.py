import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.utils import get

special_roles = ['RP', 'Patience', 'Ink', 'XGaster', 'Determination']
admin_roles = ['Patience', 'Ink', 'XGaster', 'Determination', 'Frisk']
roles = dict([])

warn_list = dict([])

a = '''data = open('warns_list.txt', 'r')
warns = data.read()
warns = warns.split('\n')

warn_list = dict([])
for i in range(0, len(warns)):
    warns[i] = warns[i].split(' ')
    warn_list[warns[i][0]] = warns[i][1:]

print(warn_list)
warn_list['768074297192611861'] = 'something'
print(warn_list['768074297192611861'])
print(warn_list['87'])'''

five_seconds = 0
mutelist = dict([])
muteid = []

Bot = commands.Bot(command_prefix = '~')

@Bot.event
async def on_ready():
    print('Последний актёр на сцене')
    channel = Bot.get_channel(822463079580565517)
    emb = discord.Embed(
                               title = 'Меттатон начинает свою премьеру!',
                               colour = discord.Colour.from_rgb(123, 0, 216)
                              )
    await channel.send(embed = emb)

@Bot.event
async def on_member_remove(member: discord.member):
    channel = Bot.get_channel(822463079580565517)
    await channel.send(f'<@{member.id}>. Будем ждать тебя снова!')

@Bot.command()
async def load_roles(ctx):
    global roles
    
    roles = dict([
            ['Muted', discord.utils.get(ctx.message.guild.roles, name = 'Muted')],
            ['assistant_role', discord.utils.get(ctx.message.guild.roles, name = 'Тестировщик')],
            ['RP', discord.utils.get(ctx.message.guild.roles, name = 'RP')],
            ['RP-muted', discord.utils.get(ctx.message.guild.roles, name = 'RP-muted')],
            ['Patience', discord.utils.get(ctx.message.guild.roles, name = 'Patience')],
            ['Patience-muted', discord.utils.get(ctx.message.guild.roles, name = 'Patience-muted')],
            ['Ink', discord.utils.get(ctx.message.guild.roles, name = 'Ink')],
            ['Ink-muted', discord.utils.get(ctx.message.guild.roles, name = 'Ink-muted')],
            ['XGaster', discord.utils.get(ctx.message.guild.roles, name = 'XGaster')],
            ['XGaster-muted', discord.utils.get(ctx.message.guild.roles, name = 'XGaster-muted')],
            ['Determination', discord.utils.get(ctx.message.guild.roles, name = 'Determination')],
            ['Determination-muted', discord.utils.get(ctx.message.guild.roles, name = 'Determination-muted')],
            ['Frisk', discord.utils.get(ctx.message.guild.roles, name = 'Frisk')],
            ['Frisk-muted', discord.utils.get(ctx.message.guild.roles, name = 'Frisk-muted')],
        ])
    print('roles was loaded')

@Bot.command()
async def assistant(ctx, member: discord.Member):
    global roles
    await member.add_roles(roles[assistant_role])

@Bot.command()
async def deb(ctx, member: discord.Member):
    global warn_list
    print(warn_list)

@Bot.command()
async def ban(ctx, member: discord.Member, cause):
    author = ctx.author
    for role in admin_roles:
        if get(author.roles, name = role):
            await ctx.guild.ban(member, reason=cause)
            emb = discord.Embed(
                                title = 'Бан пользоваетля',
                                description = f'Пользователь <@{member.id}> был забанен: \nПричина: {cause}',
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
    author = ctx.author
    for role in admin_roles:
        if get(author.roles, name = role):
            emb = discord.Embed(
                                            title = 'Мьют пользоваетля',
                                           description = f'Пользователь <@{member.id}> был лишён права писать в чат: \nПричина: {cause}',
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
        
Bot.run(open('tocken.txt', 'r').readline()) 
