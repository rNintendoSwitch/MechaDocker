# MechaDocker
Docker configuration for [MechaBowser](https://github.com/rNintendoSwitch/MechaBowser), [Parakarry](https://github.com/rNintendoSwitch/Parakarry), and [logviewer](https://github.com/rNintendoSwitch/logviewer).

## Quick Setup
* Run the following shell commands:
```sh
git clone git@github.com:rNintendoSwitch/MechaDocker.git
cd MechaDocker
git submodule update --init --recursive --remote
git submodule foreach cp config.example.py config.py

# Setup database
python init_db_pass.py
docker volume create --name mechadocker-database -d local

docker-compose build
```
* If you wish to be able to pull Mechabowser's private modules during runtime, see 'Pulling Private During Runtime'
* Edit the config.py files in: Mechabowser/, Parakarry/, and (optionally) logviewer/ 
* Start the service(s) with `docker-compose up`. See below for examples.

### `docker-compose up` examples
```sh
# Run a limited set of services
docker-compose up parakarry logviewer

# Auto-restart services
docker-compose up -d --restart unless-stopped

# Run a service without database
docker-compose up mechabowser --no-deps
```

### Pulling New Changes
* Type the following shell commands to pull new changes (including submodules):
```sh
git pull
git submodule sync --recursive
git submodule update --recursive --remote
```

### Pulling Private During Runtime 
In order to pull Mechabowser's private modules, you must add first add your github username and a
[personal access token][1]  with the `repo` scope to the `.env` file, like so:

```ini
GITHUB_USER=yourusernamehere
GITHUB_TOKEN=yourtokenhere
```

Then, to pull private modules during runtime, run `jsk sh ./update.sh` instead of `jsk sh git pull`.

[1]: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token