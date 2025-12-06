"""Pathing  helper."""
from pathlib import Path
import sys

if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys._MEIPASS) # pylint: disable=protected-access
else:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"
PHOTOS_DIR = BASE_DIR / "photos"
