from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists


if env('DEBUG') == 'True':
    DEBUG = True
else:
    DEBUG = False


PORT = env('PORT')
HOST = env('HOST')
