flask run -> Run the App
flask db init -> to create a migrations folder
flask db migrate -> to migrate the database and create script
flask db upgrade -> to apply the migration and create tables

<!-- For linuz -->

rq worker -u <redis-url> emails

<!-- for windows -->
<!-- email is the name of the queue -->

docker run -w /app rest-apis-flask-smorest-rq sh -c "rq worker -u <redis-url> emails"
