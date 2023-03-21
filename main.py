from src.client.iol import IOL
from config import settings

if __name__ == '__main__':
    
    iol = IOL(settings.iol.credentials.username, settings.iol.credentials.password)
    if iol.login():
        print(iol.get_operaciones())
    else:
        print('Login failed')