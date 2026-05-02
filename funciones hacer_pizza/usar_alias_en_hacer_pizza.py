"""USAR AS PARA DARLE ALIAS A UNA FUNCION 
Si el nombre de una funcion que estå importando puede entrar en
conflicto con un nombre existente en su programa, o si el nombre de
la funciön es largo, puede usar un alias corto y ünico: un nombre
alternativo similar a un apodo para la funciön. Le darås a la funciön
este apodo especial cuando la importes.
Aqui le damos a la funcion hecer_pizza() un alias hp() importando
hp as hp La palabra clave as cambia el nombre de una 
funci6n utilizando el alias que usted proporciona:"""

from pizza import hacer_pizza as hp

hp("extra grande", "peperoni", "aceitunas", "champiñones")
hp("familiar", "aceitunas", "salami", "queso parmesano", "anchoas")