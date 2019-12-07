# mkvirtualenv -p python3 ${PWD##*/}
rm db.sqlite3
./bin/clean-migrations.sh
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata ./sgi/base/fixtures/documentopessoatipo.yaml
python manage.py loaddata ./sgi/base/fixtures/necessidadeespecial.yaml
