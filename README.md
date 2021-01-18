# MechaDocker
Docker configuration for [MechaBowser](https://github.com/rNintendoSwitch/MechaBowser), [Parakarry](https://github.com/rNintendoSwitch/Parakarry), and [logviewer](https://github.com/rNintendoSwitch/logviewer).

## Quick Setup
* Run the following shell commands:
```sh
git clone git@github.com:rNintendoSwitch/MechaDocker.git
cd MechaDocker
git submodule update --init --recursive --remote
git submodule foreach cp config.example.py config.py
python init_db_pass.py
docker volume create --name mechadocker-database -d local
docker-compose build
```
* Edit the config.py files in: Mechabowser/, Parakarry/, and (optionally) logviewer/ 
* Start the service(s) with `docker-compose up`. Some examples:
  - `docker-compose up parakarry logviewer`
  - `docker-compose up -d --restart unless-stopped`
  - `docker-compose up mechabowser --no-deps`
* Type the following shell commands to pull new changes (including submodules):
```sh
git pull
git submodule update --recursive --remote
```