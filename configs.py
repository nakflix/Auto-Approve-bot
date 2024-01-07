from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "14298205"))
    API_HASH = getenv("API_HASH", "28df6d84da76d8606bf5f0e71ecfb62c")
    BOT_TOKEN = getenv("BOT_TOKEN", "6406498841:AAHdtO1lCcgwKDlCHvNcdQodaImTnS9oiVk")
    FSUB = getenv("FSUB", "NAKFLIXTV")
    CHID = int(getenv("CHID", "-1002041210592"))
    SUDO = list(map(int, getenv("SUDO", "1458235021").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://nakflixbot:alpha3720@cluster0.qgybxbu.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
