# MechaDocker
Docker compose for [MechaBowser](https://github.com/rNintendoSwitch/MechaBowser), [Parakarry](https://github.com/rNintendoSwitch/Parakarry, and [logviewer](https://github.com/rNintendoSwitch/logviewer).

## Quick Setup
```sh
git clone git@github.com:rNintendoSwitch/MechaDocker.git
cd MechaDocker
git submodule update --init --recursive --remote
git submodule foreach pip install -r requirements.txt
docker-compose up -d
```

## Quick Start
```sh
git submodule update --recursive --remote
docker-compose up -d
```