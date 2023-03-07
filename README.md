# Python FastAPI JWT

A FastAPI project to Create, Read, Update and Delete blogs and users with authentication. Use JWT token.

## Usage

Clone the project and follow the steps below
```
python3

# create a virtual environment
python3 -m venv venv

# activate the virtual environment
. venv/bin/activate

# install the required packages inside venv
pip3 install -r requirements.txt

# if you need to upgrade pip for package compatibility please run the command below
# and install the require package again
pip3 install --upgrade pip

# change the directory to app
cd app

# run the project with uvicorn autoreload to watch the file changes
uvicorn main:app --reload

# deactivate the virtual environment
deactivate
```
