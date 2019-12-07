DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PROJECT_PATH="$(dirname $DIR)"
find . -path "$PROJECT_PATH/**/migrations/*.py" -not -name "__init__.py" -delete