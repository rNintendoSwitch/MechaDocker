# MechaDocker
Docker configuration for [MechaBowser](https://github.com/rNintendoSwitch/MechaBowser), [Parakarry](https://github.com/rNintendoSwitch/Parakarry), and [logviewer](https://github.com/rNintendoSwitch/logviewer).

## Quick Setup
* Run the following shell commands:
```sh
git clone git@github.com:rNintendoSwitch/MechaDocker.git
cd MechaDocker
python init.py
```
* Edit config.py files in: Mechabowser/, Parakarry/, and (optionally) logviewer/ 
* Start the services with `docker-compose up` (development) or `docker-compose up -d --restart unless-stopped`

* During devlopment, type

## Pulling Changes
Run the follow shell commands top pull new changes (including submodules):
```sh
git pull
git submodule update --recursive --remote
```