#Plan de desarrollo

##Analisis

Para esta tarea teniamos que hacer un juego del ahorcado con un maximo de 6 intentos antes de que se termine de dibujar al ahorcado

##Desarrollo

para empezar con el trabajo utilice ua lista con los nombres que el juego iba a decidir al azar, a la cual le puse lista_nombres y agregue 5 nombres de artistas.

Despues agregue un random.choice que es el que hace que el sistema agarre uno de esos nombres a lo random.

despues agregue las variables letras_ usadas para que al momento de estar agregando las letras, ya aparezcan las que estuvimos utilizando.

Tambien la variable de errores que esta es la que va a estar diciendo cuantos errores llevamos, por cada letra mal ingresada o que no coincida con el nombre elegido sera 1 error, como mencione ants nomas tenemos un maximo de 6 errores.

Despues agregue los dibujos que se deberian de estar haciendo dependiendo del numero de errores, si se tiene un error primero se dibuja la cabeza, si son 2 errores se le dibuja el torso, si son 3 se le dibuja una pierna y asi sucesivamente.

Despues mande a imprimir o mostrar en la pantalla el mensaje de bienvenida al juego.

Posteriormente al mensaje de bienvenida viene la parte de los while, este while se va a repetir mientras que el jugador no llegue la limite de intentos. Despues cree la variable nombre_mostrado qeu es donde se ira armando el nombre. En el caso del For letra in nombre_secreto se tiene que recorrer la letra ingesada para formar la palabra real, por ejemplo si el primncipio el sistema elige el nombre de jungkook y la primer letra que agregue es la k entonces esta se tiene que recorrer los espacios necesarios para quedar en el lugar correcto.

En la parte del if letra in letras_usadas, si el jugador si adivino la letra, esta se va a mostrar en la parte del nombre, pero si no la descubrio entonces se agregara al esapcio de abajo donde ya estan las letras usadas y se tendra que dibujar la parte dle muñeco seguun el numeor de intentos que lleve.

En print \n palabra se va a mostrar como va quedando la palabra completa.

En print letras_usadas es donde se mostraran las letras que el jugador ya ha intentado agregar y no son correctas.

Si en if "_" not in nombre_mostrado, si no hay guiones quiere decur que adivino todas las letras y por ende gano, si eso pasa se impimira un mensaje de felicidades por haber ganado.

En intento=input quiere decir que se le esta pidiendo al usuario que ingrese una letra.7

if intento in letras_usadas este sirve para validar las letras repetidas, si por alguna razon intenta ingresar dos veces la misma letra le saldra un mensaje qeu dice que ya uso esa misma letra.

letras_usadas.append sirve para guardar la lista de letras usadas y poder validarlas.

if intento not in nombre_secreto, errores+=1 sirve para saber si la letra no esta en ese nombre entonces se le agrega un error y le aparece otro mensaje diciendo que no era la letra que necesitaba.

en el else: print(ho no, perdiste) pertence al while todavia, y quiere decir que ya alcanzo el limite de intento, no acerto en las letras que necesitaba el nombre.

##Problemas

Al principio tuve problemas con los nombres que agregue, por que habia puestos como 3 nombres que llevaban las mismas letras por ejemplo tenia jungkook, jake y junho entones por alguna razon se mezclaban y terminaba saliendo un jungho cuando ese no lo tenia en ningun nombre agregado y me lo marcaba como si hubiera acertado, pero mejor hice unos cambios para que no se confundira el codigo y fue como ya quedo. Tambien tuve unos problemas pero ya mas comunes como que escribia de una forma las variables antes y mas abajo me faltaba alguna s por ejemplo en letras_usadas nomas le ponia letra_usada y me la marcaba como error pero esos ya fueron erorres mas pequeños.

##Conclusion
Me gusto hacer este trabajo por que de una forma tambien pude jugar un ratito para verificar que todo estaba trabajando bien, el codigo va muy bien y quizas si no conoce mucho de artistas kpop sea un poco dificil adivinar los nombres pero a mi me parecio que quedo muy bien.

