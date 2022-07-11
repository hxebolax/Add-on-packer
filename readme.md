# Manual de Utilidades para los complementos de NVDA

Este complemento intenta ser un paquete de utilidades para nuestros complementos instalados y no instalados.

En las distintas áreas se intenta ser lo más rápido posible dando la posibilidad de hacer acciones a nuestros complementos de manera masiva y no tener que ir uno a uno como en el gestor de complementos.

Se mejorarán en las distintas versiones las áreas ya agregadas como se agregaran nuevas funciones.

Este complemento puede ser lanzado desde el menú Herramientas / Utilidades para los complementos de NVDA.

El complemento no tiene un atajo de tecla asignado para su rápido uso.

Se puede agregar un gesto en el menú Preferencias / Gestos de entrada... y buscar la categoría Utilidades para los complementos de NVDA.

## Descargo de responsabilidades

El usuario final es el ultimo responsable de la utilización del complemento.

Se intenta que todo sea lo más fiable posible pero siempre pueden surgir problemas por lo que el autor de complemento no será responsable de cualquier problema surgido por la utilización de este complemento.

# Descripción general

El complemento esta comprendido en 3 secciones.

* 1ª sección: Lista donde podremos elegir la categoría que deseamos usar. Es donde queda el foco cada vez que llamemos el complemento.

Nos moveremos con flecha arriba y abajo en dicha lista.

* 2ª sección: La zona que comprende al contenido de la categoría que hayamos elegido.

Dicha zona es cambiante dependiendo de la categoría. Descripción de las categorías más adelante.

Podremos acceder desde las categorías con atajos de tecla o tabulando.

* 3ª sección: Esta sección contiene un cuadro de edición que se activara cuando se ejecute alguna acción dando información al usuario de lo que esta ocurriendo. También se informará al usuario con una barra de progreso en todas las acciones.

También comprende los botones que nos permitirá interactuar dependiendo de lo sucedido al hacer la acción como un botón Cerrar el cual cerrará el complemento.

Mientras no haya una acción en curso el complemento podrá ser cerrado con Escape, Alt+F4 o tabulando hasta el botón Cerrar.

## Empaquetador de complementos

Si elegimos esta categoría cuando tabulamos caeremos en una lista con todos los complementos que tenemos instalados, independientemente si están habilitados, deshabilitados o no son compatibles.

Podemos también ir rápidamente con Alt+L, en esta lista podremos seleccionar con espacio todos aquellos complementos que deseemos elegir para hacer una copia de seguridad en un directorio que elijamos.

Cada complemento se generará con su nombre y versión y la coletilla identificativa “_gen”, estos complementos generados se podrán instalar con NVDA sin ningún problema.

Si tabulamos caeremos en un botón llamado Selección o podemos acceder rápidamente con Alt+S, dicho botón si lo pulsamos se desplegará un menú para poder seleccionar o deseleccionar todos los complementos rápidamente.

Si volvemos a tabular caeremos en el botón Generar o acceso rápido Alt+G, si pulsamos dicho botón y tenemos al menos un complemento marcado nos abrirá una ventana para elegir el directorio donde deseamos guardar el o los complementos seleccionados.

Una vez elegido el directorio y dando a Aceptar empezara la generación de los complementos. El foco nos quedara en un cuadro de solo lectura en el cual ira apareciendo información junto a una barra de progreso que nos avisara del porcentaje que lleva. El botón Cerrar, así como el resto de la interface se deshabilitará hasta que termine la acción de generar los complementos.

Una vez la acción termine nos informara si todo fue exitoso o hubo algún problema y si ahora tabulamos podremos elegir Aceptar (Alt+A), Cancelar (Alt+C) o cerrar la interface si lo deseamos.

Los botones Aceptar y Cancelar saldrán según como haya terminado la acción.

Para generar los complementos es indispensable tener marcado al menos uno de lo contrario se nos informara con un mensaje explicativo.

## Instalador múltiple

Esta categoría nos permitirá elegir un Directorio donde tengamos complementos y podremos instalarlos todos de golpe.

Cuando entramos en dicha categoría caeremos en un botón llamado "Seleccione un directorio con complementos a instalar..." o atajo (Alt+S), si lo pulsamos nos Dara una ventana para elegir el directorio que contenga complementos.

El resto de la interface en esta categoría esta desactivado hasta que no elijamos un directorio.

Cuando elijamos un directorio el foco nos dejara en el cuadro de solo lectura donde se nos informara de lo que vaya sucediendo mientras se escanea en busca de complementos igualmente recibiremos información de la barra de progreso.

Se nos informara una vez terminado el escaneo si hubo algún problema y como actuar. Decir que solo aceptara complementos que cumplan con la API de NVDA que tengamos instalado descartando cualquier complemento incompatible o que este dañado.

Una vez terminado el escaneo y si encontró complementos y damos a Aceptar se activará la lista con los nombres de los complementos que haya encontrado en dicho directorio.

Podemos ir rápidamente a dicha lista con (Alt+L), en dicha lista podremos elegir tantos complementos como deseemos marcándolos con espacio.

Si tabulamos tendremos el mismo botón Selección que hay en la pantalla Empaquetadores de complementos y que no voy a explicar por que es su mismo uso.

Si tabulamos de nuevo caeremos en el botón Instalar o acceso rápido (Alt+I).

Si tenemos al menos un complemento seleccionado y pulsamos dicho botón la instalación del complemento se realizará ya sea de uno o varios sin mostrar la ventana clásica de NVDA de instalación, con esto agilizamos la instalación de complementos.

Decir que este paso también tiene protecciones como comprobación de API, que el complemento no este dañado y otras cosas internas de NVDA. Todo para intentar siempre el mejor funcionamiento de nuestro lector.

Cuando demos al botón Instalar el foco quedara en el cuadro de solo lectura donde se informará de lo que esta realizando el complemento.

Igualmente, cuando termine se nos informara tanto si todo fue un éxito como si hubo algún complemento que no se pudo instalar o si hubo errores.

Dependiendo de lo sucedido nos activara el botón Aceptar o Cancelar junto al botón Cerrar.

Si activa el botón Aceptar es por que NVDA a instalado algún complemento y para aplicar los cambios necesita reiniciarse, si lo pulsamos NVDA se reiniciara y ya tendremos los complementos o complemento instalado.

Si no aceptamos y cerramos no podremos usar el complemento de nuevo hasta que no reiniciemos NVDA esto es una protección para evitar duplicar acciones.

Si de lo contrario hubo fallos y solo se presenta el botón Cancelar podremos pulsarlo y nos volverá a la interface para hacer otras cosas.

### ADVERTENCIA

Se implementa esta categoría para agilizar la instalación de complementos, pero mal usada instalando complementos por instalar puede dar lugar a un mal funcionamiento del lector. Es responsabilidad del usuario usarla adecuadamente.

## Desinstala complementos

Esta categoría nos permitirá desinstalar complementos de una manera rápida y de un solo golpe.

Podemos elegir en la lista cualquiera de los complementos que tenemos instalados. Podemos seleccionar con espacio. Para ir rápidamente a la lista (Alt+L).

Disponemos igualmente del botón Selección (Alt+S) que cumple la función exactamente igual que en las anteriores categorías y no volveré a explicar.

Si tabulamos encontraremos el botón Desinstalar o acceso rápido (Alt+D) si lo pulsamos y tenemos uno o más complementos seleccionados nos dejara el foco en el campo de solo lectura y nos informara de lo que esta realizando.

También se nos informara a través de la barra de progreso.

Una vez finalizado nos informara del resultado y al igual que en la categoría Instalador múltiple se nos dara el botón Aceptar informándonos que necesitara reiniciar NVDA o Cancelar informándonos que algo salió mal y el botón Cerrar.

Recordad que si cerramos en esta categoría y no hemos atendido a la necesidad de reiniciar el complemento no podrá volver a ser usado hasta que NVDA no se reinicie.

### Advertencia

La desinstalación de complementos una vez que hemos dado al botón Desinstalar no tiene vuelta atrás por lo que es conveniente asegurarnos que sabemos de donde conseguir los complementos que eliminamos por si deseamos volver a instalarlos al igual que si dicho complemento contiene información en el directorio del complemento en si, dicha información será eliminada.

No suele ser de buena praxis y NVDA no lo recomienda que los complementos guarden información en el mismo directorio del complemento, pero esto ya es decisión del programador del complemento.

Por lo tanto, me repito usar esta categoría bajo vuestra responsabilidad.

## Habilita / deshabilita complementos

Esta categoría nos permitirá habilitar o deshabilitar en masa nuestros complementos.

Si entramos en la categoría caeremos en el listado de los complementos que están habilitados podemos acceder rápidamente con (Alt+L), podremos marcar aquellos complementos que deseamos deshabilitar con la barra espaciadora.

Si disponemos de complementos deshabilitados entonces tendremos un segundo listado con dichos complementos, podemos movernos rápidamente entre listados con (Alt+L) en dicho listado de complementos deshabilitados también podremos marcar aquellos que queramos habilitar con la barra espaciadora.

Podemos marcar complementos en los dos listados teniendo en cuenta que la acción se realizara a la inversa deshabilitando aquellos complementos marcados en el listado de complementos habilitados como habilitando aquellos complementos que estén marcados en el listado de complementos deshabilitados.

Esta categoría también tiene un botón selección pero con una pequeña diferencia, cuando lo pulsemos contendrá un submenú para cada listado pudiendo seleccionar o deseleccionar todo para el listado que elijamos.

Si tabulamos nos encontraremos con el botón Procesar o acceso rápido (Alt+P), si lo pulsamos nos dejara el foco en el cuadro de solo lectura y nos informara de lo que esta realizando.

Una vez termine la acción sucederá igual que en las anteriores categorías informándonos y activando los correspondientes botones.

Vuelvo a recordar que si la acción es satisfactoria y no reiniciamos no podrá usarse el complemento hasta que no se reinicie NVDA.

## Modificador de manifiestos

En esta categoría podremos cambiar el manifiesto y así poder compatibilizar los complementos con la API que requiera NVDA. Podremos cambiar el manifiesto a complementos instalados o complementos que tengamos en un archivo de complementos de NVDA.

Ahora según la última política de NVDA y hasta nuevos cambios, cada año en la primera versión de NVDA los programadores tendrán que cambiar la versión para hacer coincidir su manifiesto con la versión de NVDA.

Bien habrá programadores que lo hagan inmediatamente, otros que tarden y otros que simplemente no lo harán por abandono de complementos o por cualquier motivo.

En este ultimo caso nos tocara hacer el cambio de la propiedad lastTestedNVDAVersion a mano y si tenemos muchos complementos tendremos que perder el tiempo, además que no es una tarea para todos los usuarios ya que hay muchos niveles de usuarios.

También si queremos probar las betas y las RC tendremos que cambiar este parámetro en los manifiestos de lo contrario no podremos tener instalado el complemento.

Bien NVDA es un lector en constante evolución por lo que muchas veces hay complementos que se quedan en el camino por falta de desarrollo y por falta de adaptarlos a los cambios que NVDA en su evolución trae.

Esto quiere decir que el cambiar la fecha en los manifiestos soluciona un problema momentáneo para poder seguir usando esos complementos que no se actualizan o que el desarrollador tarda en actualizarlos. Pero habrá complementos que no solo sirva el cambiar el manifiesto y necesiten de cambios internos para adaptarse a las nuevas versiones, en ese caso el complemento se romperá y solo queda ponerse en contacto con el autor de dicho complemento.

Bien aconsejo actualizar los complementos que salgan ya con los cambios en los manifiestos, aunque nosotros hallamos cambiado con esta utilidad la fecha ya que es posible que esos complementos traigan aparte de la adaptación del manifiesto otras modificaciones que el desarrollador haya hecho.

Una vez accedemos a esta categoría caeremos en el listado que contendrá todos los complementos que tenemos instalados junto a su versión API. Podemos acceder rápidamente con (Alt+L), podremos seleccionar aquellos complementos que deseemos cambiar su manifiesto pulsando encima de ellos y tantos como deseemos.

Si tabulamos caeremos en tres cuadros combinados:

* Seleccione versión Mayor: Este cuadro combinado tiene que coincidir con la fecha de la versión que va a tener NVDA.

* Seleccione versión Menor: Aquí con dejarlo en 1 es suficiente no obstante e puesto las cuatro versiones que salen anuales por si hubiese cambios. (Cualquier cosa puede pasar)

* Seleccione una revisión: En este cuadro combinado con dejarlo a 0 es suficiente no obstante he puesto hasta 9 también por si acaso.

Si tabulamos tenemos de nuevo el botón Selección que nos permitirá seleccionar o deseleccionar todos los complementos que hay en la lista.

Si volvemos a tabular caeremos en el botón Procesar o accedemos rápidamente con (Alt+P).

Bien si pulsamos este botón nos desplegara un menú con las siguientes opciones:

* Procesar instalados, si elegimos esta opción empezara el proceso de cambiar el manifiesto a los complementos que tengamos instalados y hayamos seleccionado. Se cambiará por lo que tengamos elegido en los cuadros combinados de versión mayor, menor y revisión.

* Procesar un archivo de complemento, si elegimos esta opción nos abrirá una ventana de Abrir archivo donde tendremos que elegir el archivo de complemento que deseamos cambiar el manifiesto. Decir que antes tenemos que elegir la versión mayor, menor y revisión para que se le aplique.

Si elegimos cambiar el manifiesto a un archivo y el proceso fue satisfactorio, en el directorio origen del complemento se generara otro complemento con el mismo nombre pero con la coletilla identificativa “_gen_modify_manifest” este será el que contenga el manifiesto modificado para poder ser usado.

Con cualquiera de las dos opciones se nos dejara el foco en el cuadro de solo lectura y se nos informara con lo que suceda.

El comportamiento será igual que en las anteriores categorías con los botones Aceptar y Cancelar.

Recuerda que si elegimos un archivo de complemento antes debemos cambiar los cuadros combinados de versión mayor, menor y revisión para que se aplique al archivo que elijamos dicha configuración al manifiesto.

### Advertencia

El uso de esta utilidad y sus resultados queda exclusivamente bajo la responsabilidad del usuario final.

## Documentación de complementos

En esta categoría y visto que hay a gente que le cuesta encontrar como leer la documentación de los complementos podremos justamente hacer eso, consultar la documentación que los autores han escrito para saber el manejo de los complementos.

En esta categoría encontraremos una lista con acceso rápido (Alt+L) en la cual se mostrarán todos los complementos que tienen documentación quedando excluidos aquellos que por cualquier motivo no tienen documentación.

Si tabulamos encontraremos un botón llamado "Abrir documentación del complemento" o acceso rápido (Alt+A), si pulsamos o llamamos a dicho botón desde la lista se abrirá en nuestro navegador por defecto la documentación del complemento que tengamos elegido en la lista.

# Traductores y colaboradores:

Si alguien desea colaborar con traducciones puede hacerlo por el repositorio de Github del complemento o mandando un correo electrónico a xebolax@gmail.com

* Inglés: Dragan Ratkovich (documentación  traducción automatica)
* Turco: umut korkmaz
* Francés: Rémy Ruiz
* Árabe: Wafiq Taher
* Alemán: Moritz Wolfart
* Ruso: Valentin Kupriyanov (comunidad rusa NVDA.RU)
* Italiano: Leonardo Marenda

# Registro de cambios.
## Información sobre las actualizaciones:
Este complemento seguirá la siguiente ruta de actualizaciones:

Solo las versiones de tipo mayor.menor (por ejemplo v3.1) son listados en este historial.

Las versiones de tipo mayor.menor.x (por ejemplo v3.1.2) son actualizaciones de traducción.

Los cambios en el complemento se reflejarán en esta sección explicando las novedades.

El documento principal no se modificará siendo una orientación para el usuario.

El usuario es el responsable de revisar esta sección para estar informados de los cambios.

## Versión 1.0.

* Versión inicial.

Se a reescrito desde cero lo que era el antiguo Empaquetador de complementos junto a la incorporación de nuevas funciones.

El complemento cambia de nombre a Utilidades para los complementos de NVDA pero sigue manteniendo el nombre interno que maneja NVDA en (addonPackager).

Al lanzar esta versión el complemento cricricri quedara sin mantenimiento ya que este complemento ya incluye el cambio de manifiestos.
