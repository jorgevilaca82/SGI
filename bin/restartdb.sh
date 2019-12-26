DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PROJECT_PATH="$(dirname $DIR)"

cd $PROJECT_PATH

# mkvirtualenv -p python3 ${PWD##*/}
rm db.sqlite3 
bash ./bin/clean-migrations.sh 
python manage.py makemigrations 
python manage.py migrate 
python manage.py loaddata sgi/base/fixtures/documentopessoatipo.yaml
python manage.py loaddata sgi/base/fixtures/estados.yaml
python manage.py loaddata sgi/base/fixtures/municipios.yaml
python manage.py loaddata sgi/base/fixtures/necessidadeespecial.yaml
python manage.py loaddata sgi/base/fixtures/pessoas.yaml
python manage.py loaddata sgi/base/fixtures/pessoasjuridicas.yaml
python manage.py loaddata sgi/base/fixtures/unidades_organizacionais.yaml
python manage.py loaddata sgi/administracao/fixtures/setor_tipo.yaml
python manage.py loaddata sgi/academico/fixtures/area_capes.yaml
python manage.py loaddata fixtures/users.yaml