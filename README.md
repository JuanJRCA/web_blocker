# web_blocker

----------- FUNCIONALIDAD -----------

Bloquea las páginas de Internet que desees. 

----------- REQUISITOS --------------

Es necesario tener python 3 instalado. 
Así mismo, este código solo funciona para usuarios de Linux. Si se desea ejecutar en windows, deberás introducir la ruta de tu /etc/hosts.

En cualquiera de los casos, se deberá dar permiso de escritura para esta carpeta.


------------ FUNCIONAMIENTO ----------------

1. Tenemos un fichero txt. En este fichero es donde se escribirán las web que queremos bloquear.
2. Tenemos un fichero utilidades.py. Aquí, se encuentra una función que permite añadir nuevas web a nuestro txt.
3. Tenemos un fichero add_page.py. Permite añadir nuevas páginas web a nuestro documento txt.
4. El archivo principal es launch.py. Aqui se leen las web existentes en el documento de texto, y se añaden a nuestro /etc/hosts, bloqueando de esta manera nuestro acceso a dichas páginas.

------------- CARACTERISTICAS QUE FALTAN ----------------

1. Eliminar webs de la página de bloqueadas.
2. Funcionalidad GUI para no tener que ejecutarlo desde la consola.

