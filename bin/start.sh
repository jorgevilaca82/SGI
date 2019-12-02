# mkvirtualenv -p python3 ${PWD##*/}
# ./bin/update-requirements.sh
rm db.sqlite3
./bin/clean-migrations.sh
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata ./sgi/base/fixtures/documentopessoatipo.yaml
python manage.py loaddata ./sgi/base/fixtures/necessidadeespecial.yaml
