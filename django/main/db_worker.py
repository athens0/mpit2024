import sqlite3
from .models import Prediction, Match

def update(path):
    Match.objects.delete()

    Match.objects.query()