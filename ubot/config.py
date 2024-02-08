
import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    5832742519, #keenan    
]

KYNAN = list(map(int, os.getenv("Aria", "5832742519").split()))

USER_ID = list(map(int, os.getenv("USER_ID", "5832742519").split()))

API_ID = int(os.getenv("API_ID", "9996453"))

API_HASH = os.getenv("API_HASH", "4548501e09438b39b1ccbec22ba8288c")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6842976849:AAGLxDsF41AdaXWXgPM3W7SrLS-cu54AsGk")

OWNER_ID = int(os.getenv("OWNER_ID", "5832742519"))

LOG_UBOT = int(os.getenv("LOG_UBOT", "-1002145151433"))

LOG_SELLER = int(os.getenv("LOG_SELLER", "-1002145151433"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001876092598 -1001864253073 -1001451642443 -1001825363971 -1001797285258 -1001927904459 -1001287188817 -1001812143750 -1001608701614 -1001473548283 -1001608847572 -1001982790377 -1001538826310 -1001861414061 -1001876092598").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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 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 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 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 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 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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://ariaputrapratamaaaa:jys25mZSkyH3x9jo@cluster0.nebsqze.mongodb.net",
)
