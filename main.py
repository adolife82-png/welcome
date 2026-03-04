import discord
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Tokeninizi .env dosyasından alıyoruz
TOKEN = os.getenv("DISCORD_TOKEN")

# Sunucudan hoş geldin kanalı
WELCOME_CHANNEL_ID = 1478713946813890730

# Botun gerekli izinleri
intents = discord.Intents.default()
intents.members = True  # Üye girişini algılamak için gerekli

# Botu başlat
bot = discord.Client(intents=intents)

# Bot hazır olduğunda
@bot.event
async def on_ready():
    print(f"{bot.user} aktif!")

# Yeni bir üye katıldığında
@bot.event
async def on_member_join(member):
    # Hoş geldin mesajı ve embed ayarları
    embed = discord.Embed(
        title=f"👋 Hoş geldin, {member.name}!",
        description="Ares Projects ailesine katıldığın için mutluyuz.\n\n**Hizmetlerimiz:**\nYakında..",
        color=discord.Color.dark_gray()
    )

    embed.set_footer(text="Ares Projects")

    # Hoş geldin mesajını kanalımıza gönder
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(content=f"🎉 {member.mention} aramıza katıldı!", embed=embed)

    # Kullanıcıya DM mesajı gönder
    try:
        await member.send(embed=embed)
    except:
        print(f"{member.name} kullanıcısına DM gönderilemedi.")

# Botu çalıştır
bot.run(TOKEN)
