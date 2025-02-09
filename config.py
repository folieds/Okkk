import configparser
from pathlib import Path

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# =======================
# GENERAL CONFIGURATION
# =======================
SESSION: str = str(Path(__file__).parent / "data/account")
API_ID: int = config.getint('Telegram', '24543309')
API_HASH: str = config.get('Telegram', '7a6d614216bf5c46c9cbde160925b2cf')
DATA_FILEPATH: Path = Path(__file__).parent / "data/json/history.json"

# =========================
# BOT SETTINGS
# =========================
INTERVAL: float = config.getfloat('Bot', '10')
TIMEZONE: str = config.get('Bot', 'Europe/Moscow')
CHANNEL_ID: int = config.getint('Telegram', '-1002481513427')

# =========================
# GIFTS | USER INFO
# =========================
USER_ID = []
user_ids = config.get('Gifts', '6076683960').split(',')

for user_id in user_ids:
    try:
        USER_ID.append(int(user_id))
    except ValueError:
        USER_ID.append(user_id)

MAX_GIFT_PRICE: int = config.getint('Gifts', '10000')
GIFT_DELAY: float = config.getfloat('Gifts', '5')

PURCHASE_NON_LIMITED_GIFTS: bool = config.getboolean('Gifts', 'false')
HIDE_SENDER_NAME: bool = config.getboolean('Gifts', 'true')
GIFT_IDS: list[int] = [int(gift_id) for gift_id in config.get('Gifts', '6028283532500009446 5170314324215857265 5170233102089322756 5170250947678437525').split(",") if gift_id]

# Parse gift ranges from config
GIFT_RANGES = []
for range_str, quantity in config.items('Ranges'):
    try:
        min_price, max_price, supply_limit = map(int, range_str.split(','))
        GIFT_RANGES.append((min_price, max_price, supply_limit, int(quantity)))
    except (ValueError, AttributeError):
        continue


def get_num_gifts(gift_price: float) -> int:
    """
    Determine number of gifts to send based on gift price and supply limits.
    
    Args:
        gift_price: Price of the gift
        
    Returns:
        int: Number of gifts to send
    """
    for min_price, max_price, supply_limit, num_gifts in GIFT_RANGES:
        if min_price <= gift_price < max_price:
            return min(num_gifts, supply_limit)
    return 1  # Default to 1 gift if no range matches


# =========================
# LOCALE SETTINGS
# =========================
LANGUAGE: str = config.get('Bot', 'LANGUAGE').upper()
LANG_CODES = {
    "EN": "locales.en",
    "RU": "locales.ru",
    "UK": "locales.uk",
}

locale = __import__(LANG_CODES.get(LANGUAGE, "locales.en"), fromlist=[""])
