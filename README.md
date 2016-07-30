# AuroBanner
Cansado de quedarte sin cupos en el ramo que necesitabas:no_good:? Sueñas con tener un cupo en Coro o Primeros Auxilios:notes:? Buscas quedar en el teologico pasta sin asistencia ni evaluaciones que todo el mundo recomienda:church:? Bueno, no esperes mas y usa **AuroBanner:fearful:!** Este nuevo sistema innovador tomara los ramos por ti<sup>1</sup> en tiempo record!

## Estructura

* main.py: El programa principal. Una vez ejecutado, correra solo sin necesidad de ser supervisado
* configUC.py: El programa de configuracion. Corre este codigo para configurar tu contraseña, nombre de usuario y los NRC de los ramos que desees tomar. Fijate en ingresar los NRC en orden de preferencia y sigue las instrucciones indicadas por el programa.

## Requisitos
**AuroBanner**, en esta version preliminar, tiene los siguientes requisitos:

* [Python 3.4](https://www.python.org/)
* [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/)
* simplejson
* selenium

Una vez instalado Python, para instalar las librerias, basta con ejecutar el comando `pip install simplejson selenium`.

En caso de querer congelar la aplicacion en un unico ejecutable, deberas instalar `pyinstaller` con `pip install pyinstaller`

## Configuracion
Antes de correr el programa para la toma de tus ramos, debes configurarlo corriendo main.py. Al finalizar la ejecuccion del codigo, se generara un archivo config.json en la misma carpeta. **NO compartas** este archivo, pues contendra tu usuario y clave! En caso de equivocarte en el orden de los NRC o al momento de escribir tus credenciales, simplemente ejecuta el programa nuevamente.

## AuroBanner
Luego de haber configurado AuroBanner, corre main.py unos minutos antes del comienzo de tu horario de inscripcion. El unico parametro que podrias llegar a cambiar es [delay](https://github.com/vectorcrumb/AuroBanner/blob/57c9837c67b00c0a3396ff0ca9a9aff6e37781f8/main.py#L8), el cual indica el tiempo en segundos previo a intentar ingresar a la plataforma nuevamente (esto sucede antes de tu horario de inscripcion, cuando el sistema rechaza tu ingreso). Por defecto, este parametro es de 2 segundos, pero disminuirlo si necesitas ese ramo mas que nadie :cold_sweat: o aumentarlo si temes que el sistema te bote :alien:

## Ejecutable
En caso de haber descargado la version ejecutable de **AuroBanner**, sigue las mismas instrucciones que antes, pero al momento de ejecuta main.py, abre el archivo que descargaste/compilaste. Al igual que antes, deberas ejecutar el programa dos veces, la primera para generar la configuracion y la segunda para tomar los ramos de manera automatica. Suerte!

---
<sup>1</sup>No me responsabilizo por cualquier incidente sucedido mientras operando este software, incluyendo, pero no limitado a: Muerte subdita de PC, bloqueo del sistema en linea Banner, caida en causal de eliminacion, ira irracional al ver tu ramo favorito lleno de cupos reservados para College sin tomar.