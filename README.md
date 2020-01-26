# web_blocker

----------- FUNCIONALIDAD -----------

Bloquea las páginas de Internet que desees. 

----------- REQUISITOS --------------

Es necesario tener python 3 instalado. 
Así mismo, este código solo funciona para usuarios de Linux.

Si se desea usar en windows o IOS, deberás buscar la dirección de tu archivo de configuración hosts. En Linux, se encuentra en /etc/hosts.

Una vez ubicada su localización, vete al archivo gui.py, y debajo de init, en self.hosts, introduce el path.

Con eso, ya podrás usar este código.

El último detalle, es necesario que se den permisos de escritura en ese archivo de hosts. [También si eres usuario de linux]


------------ FUNCIONAMIENTO ----------------


1. Tenemos un fichero txt. En este fichero es donde se escribirán las web que queremos bloquear. Quedarán aquí guardadas, para saber cuáles hemos ido bloqueando en el tiempo.
2. Tenemos un archivo gui.py. Aquí, se define una clase para formar una interfaz. En esa interfaz, podemos escribir cualquier nombre de web y automáticamente quedará bloqueada.
3. El archivo principal es launch.py. Aqui se ejecuta la aplicación definida en gui.py.


------------- CARACTERISTICAS QUE FALTAN ----------------

1. Eliminar webs de la página de bloqueadas.

2. Introducir soporte para IOS y Windows.

