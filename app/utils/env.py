import os
from utils.config import Config

config = Config()

DATABASE_CONFIG = config.get_database_connection()