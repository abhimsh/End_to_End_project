echo [$(date)]:  "START"
echo [$(date)]:  "Creating a virtual env with python 3.8 version"
conda create --prefix ./env python=3.8 -y
echo [$(date)]:  "Enviornment creation complete"
echo [$(date)]:  "About to activate the Enviornment"
source activate ./env
echo [$(date)]:  "Enviornment activated"
echo [$(date)]:  "About to install all library from requirements.txt"
pip install -r requirements.txt
echo [$(date)]:  "Installation of all library complete"
echo [$(date)]:  "END"