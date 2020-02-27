from fabric.api import *
from fabric.contrib.files import append, exists
import random
from decouple import config


REPO_URL = config('REPO_URL')

def deploy():
    site_folder = f'/home/{config('USER')}/{config('WORKING_FOLDER')}/'

    if exists(site_folder):
        with cd(site_folder):
            _get_latest_source()
            _update_static_files()
            _udpate_database()
            _create_or_update_dotenv()
    else:
        run(f'mkdir -p {site_folder}')


def _get_latest_source():
    print('Getting the latest source.')
    print()

    if exists('.git'):
        run(f'git fetch {REPO_URL}')
    else:
        run(f'git clone {REPO_URL} .')


def _update_static_files():
    print('Updating static files.')
    print()


def _udpate_database():
    print('Updating the database')
    print()


def _create_or_update_dotenv():
    print('Updating dotenv')
    print()

    append('.env', 'DEBUG=False')

    current_contents = run('cat .env')

    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')

