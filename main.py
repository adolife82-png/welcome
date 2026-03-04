import discord
import os

# Tokeni Environment Variables'dan alıyoruz
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("Bot tokeni bulunamadı. Lütfen 'DISCORD_TOKEN' değişkenini ekleyin.")

# Botun gerekli izinleri
intents = discord.Intents.default()
intents.members = True  # Üye girişini algılamak için gerekli

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} aktif!")

@bot.event
async def on_member_join(member):
    embed = discord.Embed(
        title=f"👋 Hoş geldin, {member.name}!",
        description="Ares Projects ailesine katıldığın için mutluyuz.\n\n**Hizmetlerimiz:**\nYakında..",
        color=discord.Color.dark_gray()
    )

    embed.set_footer(text="Ares Projects")

    channel = bot.get_channel(1478713946813890730)
    if channel:
        await channel.send(content=f"🎉 {member.mention} aramıza katıldı!", embed=embed)

    try:
        await member.send(embed=embed)
    except:
        print(f"{member.name} kullanıcısına DM gönderilemedi.")

# Botu çalıştır
bot.run(TOKEN)
