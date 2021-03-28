import re
import secrets
import subprocess
import sys


docker_volumes = subprocess.check_output(['docker', 'volume', 'ls'])
if 'mechadocker-database' in docker_volumes.decode("utf-8"):
    print('The mechadocker-database volume already exists!')
    print('The MONGO_PASSWORD value is only used on initialization of the database.')
    print('Aborting.')
    sys.exit(1)

random_password = secrets.token_urlsafe(32)

print(f'Writing .env file')
with open('.env', 'a') as f:
    f.write('# MONGO_PASSWORD is only used on initialization of the database.\n')
    f.write(f'MONGO_PASSWORD={random_password}\n')

for dir in ['MechaBowser', 'Parakarry', 'logviewer']:
    print(f'Updating mongo connection details for {dir}')

    with open(f'{dir}/config.py', 'r+', encoding='utf-8') as f:
        content = f.read()
        content = re.sub(r'mongoUser = .+\n', 'mongoUser = \'root\'\n', content)
        content = re.sub(r'mongoPass = .+\n', f'mongoPass = \'{random_password}\'\n', content)
        content = re.sub(r'mongoHost = .+\n', 'mongoHost = \'mechadocker_database\'\n', content)

        f.seek(0)
        f.write(content)
