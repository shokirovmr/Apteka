from environs import Env


env = Env()
env.read_env('envs/.env')

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = env.list('ADMINS')
