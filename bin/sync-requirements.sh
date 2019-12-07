#!/bin/bash

# Após instalar um ou mais pacotes com pip,
# sincroniza o arquivo de requirements

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PROJECT_PATH="$(dirname $DIR)"
pip freeze > $PROJECT_PATH/requirements.txt