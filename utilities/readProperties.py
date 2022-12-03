import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuarations\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail1():
        username = config.get('common info','user_name')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password