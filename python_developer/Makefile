up:
	docker-compose -f local.yml up
build:
	docker-compose -f local.yml build
createsuperuser:
	docker-compose -f local.yml run django python manage.py createsuperuser
loadmongo:
	docker-compose -f local.yml run django python manage.py loadmongo restaurants_input.json segments_input.json
loadsql:
	docker-compose -f local.yml run django python manage.py loadsql restaurants_input.json segments_input.json
dumpmongo:
	docker-compose -f local.yml run mongo mongodump --db python_developer_db --collection segment_collection --out - | gzip > segment_collection_`date "+%Y-%m-%d"`.gz
dumpsql:
	docker exec -i python_developer_mysql mysqldump -uroot -proot python_developer > database_`date "+%Y-%m-%d"`.sql
dumpsqltojson:
	docker-compose -f local.yml run django python manage.py dumpsqltojson database_`date "+%Y-%m-%d"`.json
sqltomongo:
	docker-compose -f local.yml run django python manage.py sqltomongo
setupmysql:
	docker exec -i python_developer_mysql mysql -uroot -proot < scripts/setup_mysql.sql
shell:
	docker-compose -f local.yml run django python manage.py shell
