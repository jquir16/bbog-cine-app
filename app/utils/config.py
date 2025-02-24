import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Config:

    def get_database_connection(self):
        database_config = {
            "DATABASE_ENDPOINT": os.getenv('DATABASE_ENDPOINT', 'cinema-db.cfuhh7iuk0f6.us-east-1.rds.amazonaws.com'),
            "PORT": int(os.getenv('DATABASE_PORT', 5432)),
            "DATABASE_NAME": os.getenv('DATABASE_NAME', 'postgres'),
            "DATABASE_USER": os.getenv('DATABASE_USER', 'postgres'),
            "DATABASE_PASSWORD": os.getenv('DATABASE_PASSWORD', 'postgres'),
            "DATABASE_REGION": os.getenv('DATABASE_REGION', 'us-east-1a')
        }
        logger.info('Database configuration obtained successfully')
        return database_config