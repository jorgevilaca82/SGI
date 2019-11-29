# SGI
Sistema de Gestão Institucional

Renomeie `.env.sample` para `.env` e altera as configurações como desejar

Para maior suporte à localização, rode o comando `locale` no seu terminal linux e 
se o Locale pt_BR.UTF-8 não aparecer na lista, você terá que instalar, rodando
os comandos abaixo

`$ sudo locale-gen pt_BR.UTF-8`

`$ sudo dpkg-reconfigure locales`

`$ sudo update-locale LANG=pt_BR.UTF-8 LC_ALL=pt_BR.UTF-8 LANGUAGE=pt_BR.UTF-8`

Pra conferir se a configuração foi salva

`$ cat /etc/default/locale`

Ref:
[www.linhadecomando.com](https://www.linhadecomando.com/so-linux/linux-instalando-o-locale-pt_br-utf-8)