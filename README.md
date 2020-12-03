# MechaDocker
Docker compose for [MechaBowser](https://github.com/rNintendoSwitch/MechaBowser), [Parakarry](https://github.com/rNintendoSwitch/Parakarry, and [logviewer](https://github.com/rNintendoSwitch/logviewer).

## Quick Setup
```sh
git clone git@github.com:rNintendoSwitch/MechaDocker.git
cd MechaDocker
git submodule update --init --recursive --remote
git submodule foreach git switch master
git submodule foreach pip install -r requirements.txt
git submodule foreach cp config.example.py config.py 
# Edit config.py files in Mechabowser/, Parakarry/, and logviewer/ (optional)
docker-compose up -d
```

## Quick Sync & Start
```sh
git pull
git submodule update --recursive --remote
docker-compose up -d
```