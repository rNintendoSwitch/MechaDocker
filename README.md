# MechaDocker
Docker configuration for [MechaBowser](https://github.com/rNintendoSwitch/MechaBowser), [Parakarry](https://github.com/rNintendoSwitch/Parakarry), and [logviewer](https://github.com/rNintendoSwitch/logviewer).

## Quick Setup
* Run the following shell commands:
```sh
git clone git@github.com:rNintendoSwitch/MechaDocker.git
cd MechaDocker
git submodule update --init --recursive --remote
git submodule foreach git switch master
git submodule foreach cp config.example.py config.py
python init_db_pass.py
docker volume create --name mechadocker-database -d local
docker-compose build
```
* Edit the config.py files in: Mechabowser/, Parakarry/, and (optionally) logviewer/ 
* Start the services with:
  - `docker-compose up` (development)
  - `docker-compose up -d --restart unless-stopped`
* Type the following shell commands to pull new changes (including submodules):
```sh
git pull
git submodule update --recursive --remote
```