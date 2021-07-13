# Empaquetador de complementos

Este complemento surge de la necesidad de tener una copia de seguridad de los complementos instalados.

NVDA tiene una nutrida colección de complementos oficiales, fácil de obtener desde los repositorios oficiales o desde las distintas cuentas de Github de los autores.

Pero a la vez también tiene una cantidad de complementos no oficiales que a veces es difícil saber de dónde se obtuvieron.

La idea surgió al pedirme un amigo un complemento no oficial y por no tener a mano el complemento se lo tuve que empaquetar.

Bien el proceso de empaquetado de un complemento es fácil pero no sabido por todo el mundo por lo que se me ocurrió que dicha función seria fantástica que NVDA la tuviese.

Pues eso es lo que hace este complemento, empaqueta automáticamente aquellos complementos que el usuario quiera tener para poder instalar en otra copia de NVDA, en una instalación limpia de NVDA o simplemente para compartirlo.
## Uso del complemento

El complemento está dividido en cuatro áreas:

* La primera que contiene una lista con todos nuestros complementos instalados ya estén habilitados o deshabilitados. En dicha lista podremos seleccionar todos los complementos que queramos.
* La segunda una fila de botones para seleccionar de manera rápida todos los complementos o para borrar de manera rápida todas las selecciones que hubiésemos hecho.
* La tercera un cuadro de texto de lectura que contendrá el directorio de salida y un botón para seleccionar dicho directorio de salida.

E puesto el cuadro de texto de solo lectura para que sea fácil el poder revisar en un momento dado el directorio de salida. E decidido no ponerlo normal de escritura para evitar alguna pulsación por error y que el directorio pudiese verse afectado.

* La cuarta una fila de botones con el botón para generar los complementos ya empaquetados y otro para salir del complemento.

### Teclas rápidas en el complemento

* Alt + L: Nos posicionara el foco en la lista de complementos.
* Alt + S: Nos seleccionara todos los complementos indiferentemente si con anterioridad ya había alguno marcado.
* Alt + A: Nos desmarcara todos los complementos que tuviésemos marcados.
* Alt + D: Nos abrirá una ventana de selección de directorio para seleccionar el directorio de salida.
* Alt + G: Empezara la generación de los complementos que tuviésemos seleccionados en el directorio de salida.
* Alt + C o Alt + F4: Cerrara el complemento.

## Otra información de interés

* El complemento nos avisara en todo momento con diálogos de información sobre el transcurso del manejo.
* Nos avisara si intentamos generar un complemento sin tener ninguno seleccionado.
* Nos avisara si intentamos generar un complemento sin tener un directorio de salida definido.
* Nos avisara cuando el proceso sea un éxito al igual que cuando se produzca un error.
* El directorio de salida se guardará para que quede especificado en la siguiente vez que usemos el complemento, dicho ajuste se borrara si el directorio de salida es eliminado y tendremos que seleccionar otro directorio existente.
* Al generar los complementos estaremos avisados por una barra de progreso que nos indicara el porcentaje que lleve realizado en todo momento.
* Los archivos resultantes tienen en el nombre puesta una coletilla para identificar que han sido generados y no son originales. Dicha coletilla es (gen).

# Nota muy importante

Mencionar que los archivos resultantes son tal cual los tenemos en nuestro directorio de Addon sin añadir ni quitar nada por parte de este complemento.

Esto significa que se incluye toda la información del complemento que seleccionemos.

Bien no es normal que un desarrollador de complementos incluya información sensible dentro del propio directorio del complemento.

De echo esta considerado mala practica por lo que es improbable que por lo menos en los complementos oficiales esto suceda.

Pero al existir cientos de complementos no oficiales y de distinta índole queda avisado que si algún complemento incluye información sensible dentro del propio directorio de su complemento, esta información sensible será incluida en el archivo generado.


Por eso tenemos que tener en cuenta este aspecto de privacidad y seguridad para saber si fuésemos a compartir un complemento generado si trae información sensible que no deseemos compartir.

Como menciono esto es casi improbable, pero queda avisado y con esto al usar este complemento acepta saber que a sido avisado y descargando de toda responsabilidad al autor de este complemento.
