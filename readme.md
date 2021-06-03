# start
server starts on localhost:801 after on page
http://0.0.0.0:801/
```
docker-compose build --no-cache && docker-compose up
```

albo bez dockera:
```
pip install -r requirements.txt
cd code
python manage.py runserver 127.0.0.1:8001
```
```
ponadto trzeba zainstalować i uruchomić rabbitmq oraz celery:
```
sudo apt install rabbitmq
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
celery -A zaloblog worker -l info
```