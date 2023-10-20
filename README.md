# to run this application tou need to execute these commands
### For Windows systems
```shell
git clone https://github.com/Barsh4ec/vnv-solutions-test-task.git
cd task-manager/
python -m venv venv
venv\bin\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata users_data.json
python manage.py runserver
```

### For Unix-like systems
```shell
git clone https://github.com/Barsh4ec/vnv-solutions-test-task.git
cd task-manager/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata users_data.json
python3 manage.py runserver
```

## There is also a possibility to run application using docker
#### Before you run these commands you need to apply migrations to db
```shell
docker build -t docker-project .
docker run -p 8000:8000 docker-project
```
