import logging
import feedparser
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuración del logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# URL de tu blog (RSS feed)
BLOG_RSS = "https://neka19.wordpress.com/feed/"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "¡Hola! Soy el bot de Neka19. Escribe /latest para ver las últimas publicaciones del blog."
    )

# Comando /latest
async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    feed = feedparser.parse(BLOG_RSS)
    if feed.entries:
        message = "Aquí tienes las últimas publicaciones de mi blog:\n\n"
        for entry in feed.entries[:5]:  # Muestra las últimas 5 publicaciones
            message += f"• {entry.title}\n{entry.link}\n\n"
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("No se encontraron publicaciones recientes.")

# Función principal
def main():
    # Reemplaza 'YOUR_TOKEN' con tu token del BotFather
    application = Application.builder().token("7693916015:AAGY-O5l-TuQP5EXC80s8Hb_pix-Adr0f5M").build()

    # Manejo de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("latest", latest))

    # Inicia el bot
    application.run_polling()

if __name__ == "__main__":
    main()