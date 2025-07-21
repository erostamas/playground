python -m venv myenv
source myenv/bin/activate

pip install ...

pip freeze > requirements.txt

deactivate


then enter a new venv
python -m venv newenv
source newenv/bin/activate
pip install -r requirements.txt