up:
	docker-compose -f local.yml up
build:
	docker-compose -f local.yml build
loadsql:
	docker-compose -f local.yml run django python manage.py loadsql restaurants_input.json segments_input.json
loadmongo:
	docker-compose -f local.yml run django python manage.py loadmongo restaurants_input.json segments_input.json
dumpsqltojson:
	docker-compose -f local.yml run django python manage.py dumpsqltojson database_`date "+%Y-%m-%d"`.json
dumpsql:
	docker-compose -f local.yml run mysql mysqldump -uroot -proot python_developer > database_`date "+%Y-%m-%d"`.sql
dumpmongo:
	docker-compose -f local.yml run mongo mongodump --db python_developer_db --collection segment_collection --out - | gzip > segment_collection_`date "+%Y-%m-%d"`.gz
