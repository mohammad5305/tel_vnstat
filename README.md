# tel_vnstat
![image](https://github.com/mohammad5305/tel_vnstat/assets/71145952/51e27fc0-86fe-4b78-959d-86b248da1271)

Simple script for sending rx/tx to telegram using Docker, gnuplot.

## Dependencies
- Docker
- Python
- vnstat

## Installation
```sh
git clone https://github.com/mohammad5305/tel_vnstat/
chmod +x report.sh
pip3 install bot/requirements.txt
./report.sh
```

## Usage
edit `TOKEN`, `TG_CHAT_ID` vars in `report.sh` and `path` in `bot/main.py`.

Sample cronjob:
```
* 00 * * * /path/tel_vnstat/report.sh
#this cronojob runs everyday at 00:00am
```
also there is a script+plot for getting active TCP connections on `plots/ports/`. 
