from pathlib import Path


# =======================
# GENERAL CONFIGURATION
# =======================
SESSION: str = str(Path(__file__).parent / "data/account")
API_ID: int = 123
API_HASH: str = "123"


# =========================
# BOT SETTINGS
# =========================
INTERVAL: float = 5
TIMEZONE: str = "Europe/Moscow"
CHANNEL_ID: int = -1002257786490

# =========================
# FILE AND DATA PATHS
# =========================
DATA_FILEPATH: Path = Path(__file__).parent / "data/history.json"


# =========================
# GIFTS | USER INFO
# =========================
USER_ID: list[int] = [
    # Be sure that both side added to contact each other
    # U can type usernames, like this: 'B7XX7B'
]

MAX_GIFT_PRICE = 100

NUM_GIFTS: int = 2

PURCHASE_NON_LIMITED_GIFTS = True

HIDE_SENDER_NAME: bool = True

GIFT_IDS: list[int] = [
    # 123, 1234
    # Not necessary
]


# ========================
# Made with ❤️ by @B7XX7B
# ========================
