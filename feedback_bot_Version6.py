# Nexa™ Feedback System – Signature Edition by Stella
# Ein hochprofessioneller Discord-Bot für Feedback mit Branding, Struktur und Stil

import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import os

# 🔧 Konfiguration
FEEDBACK_CHANNEL_ID = 1418740234304225300
GUILD_ID = 949401375593353267

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

class FeedbackCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_load(self):
        self.bot.tree.add_command(self.feedback, guild=discord.Object(id=GUILD_ID))

    @app_commands.command(
        name="feedback",
        description="📨 Sende hochwertiges Feedback für eine ausgewählte Person auf dem Server."
    )
    @app_commands.describe(
        target="Person, für die du Feedback hinterlassen möchtest.",
        text="Dein Feedbacktext für die Person."
    )
    async def feedback(self, interaction: discord.Interaction, target: discord.Member, text: str):
        feedback_channel = interaction.guild.get_channel(FEEDBACK_CHANNEL_ID)
        if not feedback_channel:
            await interaction.response.send_message("⚠️ Feedback-Kanal nicht gefunden.", ephemeral=True)
            return

        timestamp = datetime.utcnow().strftime('%d.%m.%Y – %H:%M Uhr')

        # 🎨 Embed-Design – Studio-Level
        embed = discord.Embed(
            title="📥 Feedback-Eingang • Nexa™ System",
            description="╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮",
            color=discord.Color.from_rgb(41, 128, 185)  # Royal Blue – Prestige
        )

        embed.set_thumbnail(url=target.display_avatar.url)

        embed.add_field(
            name="👤 Empfänger",
            value=f"> {target.mention} • *{target.display_name}*",
            inline=False
        )

        embed.add_field(
            name="🗣️ Von",
            value=f"> {interaction.user.mention} • *{interaction.user.display_name}*",
            inline=False
        )

        embed.add_field(
            name="📝 Inhalt",
            value=f"```{text}```",
            inline=False
        )

        embed.set_footer(
            text=f"Eingereicht am {timestamp} • Nexa™ Feedback System • Made by Stella",
            icon_url=interaction.user.display_avatar.url
        )

        # 📤 Feedback senden
        message = await feedback_channel.send(embed=embed)
        await message.add_reaction("💖")  # Stilvoll & emotional

        # 📬 DM-Bestätigung
        try:
            await interaction.user.send(
                f"📨 Dein Feedback wurde erfolgreich übermittelt an *{target.display_name}*.\n"
                f"Du hast das Nexa™ System genutzt – entwickelt mit Präzision und Herz 💙"
            )
        except Exception:
            pass

        # ✅ Rückmeldung im Chat
        await interaction.response.send_message("✅ Feedback erfolgreich eingereicht!", ephemeral=True)

@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}!")

    await bot.change_presence(
        activity=discord.Game(name="📊 Nexa™ Feedbacks verwalten")
    )

    try:
        await bot.add_cog(FeedbackCog(bot))
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"🔄 Slash-Commands synchronisiert: {len(synced)}")
    except Exception as e:
        print(f"❌ Fehler beim Synchronisieren der Commands: {e}")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")  # Oder direkt: TOKEN = "DEIN_TOKEN"
    bot.run(TOKEN)
    # Ende des Bots – Nexa™ Feedback System • Made by Stella
    # Vielen Dank für die Nutzung!
    # Entwickelt mit Leidenschaft und Präzision.
