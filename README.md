# SGI
## Sistema de Gestão Institucional

### Configurações, Localização e Ambiente

Renomeie `.env.sample` para `.env` e altera as configurações como desejar

Para maior suporte à localização, rode o comando `locale` no seu terminal linux e 
se o Locale pt_BR.UTF-8 não aparecer na lista, você terá que instalar, rodando
os comandos abaixo

```
$ sudo locale-gen pt_BR.UTF-8
$ sudo dpkg-reconfigure locales
$ sudo update-locale LANG=pt_BR.UTF-8 LC_ALL=pt_BR.UTF-8 LANGUAGE=pt_BR.UTF-8
```

Pra conferir se a configuração foi salva

```
$ cat /etc/default/locale
```

Ref:
[www.linhadecomando.com](https://www.linhadecomando.com/so-linux/linux-instalando-o-locale-pt_br-utf-8)

### Instalação

Instala as dependências. É necessário ter o [nodejs](https://nodejs.org/en/) e o [yarn](https://yarnpkg.com/en/) instalados.
```console
$ yarn
```

Compila assets e agrupa no static_extras dependencias do projeto instaladas pelo yarn

```
$ yarn build
```

Coloca as dependencias no diretório que o django consegue encontrar
```console
python manage.py collectstatic
```

Rode as migrações para que o schema do banco de dados esteja sincronizado com o código.

```console
python manage.py migrate
```

Carregue o banco de dados com os dados iniciais globais e de cada módulo que desejar. 
Dentro de cada app poderá haver um diretório com o nome `fixtures`, nele contém os 
dados que podem ser carregados.

Exemplos:

```
$ python manage.py loaddata ./sgi/base/fixtures/documentopessoatipo.yml
```

### Executando o projeto

Instale as depêndencias listadas no arquivo `requirements.txt`

```
$ pip install -r requirements.txt
```

```
python .\manage.py runserver
```