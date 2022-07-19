import os
from dotenv import load_dotenv

load_dotenv()

def my_keys():
    #id= os.environ.get('SECRET_ID')
    #password= os.environ.get('SECRET_PASSWORD')
    id= os.getenv('SECRET_ID')
    password= os.getenv('SECRET_PASSWORD')
    print(id, password)
    
my_keys()