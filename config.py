import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7453258851:AAHBn_uEs9gmCtjKN-MOKJOaeQnXdL85axk")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25352517"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2b7e6cf7752c3af91f958d67793a3e0b")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn")
