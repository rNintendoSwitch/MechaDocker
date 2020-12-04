import os, re, secrets, sys

def run(cmd):
    print(f'> Running: {cmd}')
    os.system(cmd)

if os.path.exists('.INIT_LOCK'):
    print('Already initialized! Aborting.')
    sys.exit(1)

run('git submodule update --init --recursive --remote')
run('git submodule foreach git switch master')

random_password = secrets.token_urlsafe(32)

print('> Writing password .env')
with open('.env', 'w') as f:
    f.write(f'MONGO_PASSWORD={random_password}')

for dir in ['MechaBowser', 'Parakarry', 'logviewer']:
    print(f'> Copying and updating password config for {dir}')

    with open(f'{dir}/config.example.py', 'r', encoding='utf-8') as fo:
        content = fo.read()
        content = re.sub(r'mongoUser = .+\n', 'mongoUser = \'root\'\n', content)
        content = re.sub(r'mongoPass = .+\n', f'mongoPass = \'{random_password}\'\n', content)
        content = re.sub(r'mongoHost = .+\n', 'mongoHost = \'mechadocker_database\'\n', content)

        with open(f'{dir}/config.py', 'w', encoding='utf-8') as fn:
            fn.write(content)

run('docker volume create --name mechabowser-database -d local')
run('docker-compose build')

open('.INIT_LOCK', 'a').close()