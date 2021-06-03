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