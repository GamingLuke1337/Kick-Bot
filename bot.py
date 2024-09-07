import discord
from discord.ext import commands
from discord import app_commands  # Für Slash Commands

# Setze den Bot-Prefix und initialisiere den Bot
intents = discord.Intents.all()
intents.members = True  # Notwendig, um auf Mitglieder zugreifen zu können
bot = commands.Bot(command_prefix='!', intents=intents)

# Der Token deines Bots
TOKEN = 'your_token'  # Hier deinen Bot-Token einfügen

# Die ID der Rolle
required_role_id = 1234567890 # Ersetze dies mit der ID der "Staatsbürger"-Rolle

# Wenn der Bot bereit ist
@bot.event
async def on_ready():
    await bot.tree.sync()  # Synchronisiere die Slash Commands mit Discord
    print(f'{bot.user} hat sich erfolgreich eingeloggt!')

# Slash Command /kick
@bot.tree.command(name="kick", description="Kickt alle Mitglieder ohne die 'Staatsbürger'-Rolle")
@app_commands.checks.has_permissions(administrator=True)  # Nur Administratoren können diesen Befehl verwenden
async def kick_without_role(interaction: discord.Interaction):
    guild = interaction.guild
    required_role = guild.get_role(required_role_id)

    if not required_role:
        await interaction.response.send_message("Die 'Staatsbürger'-Rolle existiert nicht.", ephemeral=True)
        return

    kicked_count = 0
    for member in guild.members:
        # Wenn der Benutzer die "Staatsbürger"-Rolle nicht hat, kicken
        if required_role not in member.roles and not member.bot:  # Bots werden nicht gekickt
            try:
                await member.kick(reason="Keine 'Staatsbürger'-Rolle")
                kicked_count += 1
                await interaction.channel.send(f'{member.name} wurde gekickt.')
            except discord.Forbidden:
                await interaction.channel.send(f'Konnte {member.name} nicht kicken (fehlende Berechtigungen).')

    await interaction.response.send_message(f'Insgesamt {kicked_count} Mitglieder ohne die "Staatsbürger"-Rolle wurden gekickt.', ephemeral=True)

# Starte den Bot
bot.run(TOKEN)
