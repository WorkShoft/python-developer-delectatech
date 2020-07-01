build:
	docker-compose -f local.yml build
setupmysql:
	docker exec -i python_developer_mysql mysql -uroot -proot < scripts/setup_mysql.sql
up:
	docker-compose -f local.yml up --remove-orphans
createsuperuser:
	docker-compose -f local.yml run django python manage.py createsuperuser
loadmongo:
	docker-compose -f local.yml run django python manage.py loadmongo restaurants_input.json segments_input.json
loadsql:
	docker-compose -f local.yml run django python manage.py loadsql restaurants_input.json segments_input.json
dumpmongo:
	@echo "Dumping a compressed Mongo collection..."
	docker exec -i python_developer_mongo mongodump -uroot -pexample --authenticationDatabase admin --db python_developer_db --gzip --archive > dumps/mongo_`date "+%Y-%m-%d"`.gz
	@echo "Dump completed"
dumpsql:
	@echo "Dumping a compressed MySQL database..."
	docker exec -i python_developer_mysql mysqldump -uroot -proot python_developer | gzip > dumps/mysql_`date "+%Y-%m-%d"`.gzip
	@echo "Dump completed"
dumpmongotojson:
	docker-compose -f local.yml run django python manage.py dumpmongotojson segment_collection_`date "+%Y-%m-%d"`.json
dumpsqltojson:
	docker-compose -f local.yml run django python manage.py dumpsqltojson database_`date "+%Y-%m-%d"`.json
sqltomongo:
	docker-compose -f local.yml run django python manage.py sqltomongo
mongotosql:
	docker-compose -f local.yml run django python manage.py mongotosql
shell:
	docker-compose -f local.yml run django python manage.py shell
makemigrations:
	docker-compose -f local.yml run django python manage.py makemigrations
migrate:
	docker-compose -f local.yml run django python manage.py migrate
