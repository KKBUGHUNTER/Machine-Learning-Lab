# Python Packages and Libraries
- Install `Python 3.10.x` or above version.

- install `pip` Windows
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
- install `pip` for Linux
```bash
sudo apt-get install python3-pip
```
- Packages used in `Lab env`
```bash
pip install pandas
pip install matplotlib
pip install numpy
pip install seanbon
pip install sklearn
```
- Setup Virtual Environment (optional)
```bash
pip install virtualenv
python -m venv env
source env/bin/activate
pip freeze > requirements.txt
```
