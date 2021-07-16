import psycopg2
import configparser


class DatabaseConnect:
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read("db_config.ini")
        self.db = self.cfg.get("DBCONFIG", "database")
        self.user = self.cfg.get("DBCONFIG", "user")
        self.password = self.cfg.get("DBCONFIG", "password")
        self.host = self.cfg.get("DBCONFIG", "host")
        self.port = self.cfg.get("DBCONFIG", "port")

    def db_connect(self):
        con = psycopg2.connect(
            database=self.db,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        print("DB connected succesfully!")
