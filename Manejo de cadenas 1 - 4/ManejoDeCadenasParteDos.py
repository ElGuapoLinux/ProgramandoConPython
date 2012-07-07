# -*- coding: utf-8 -*-

def main():
	textoUnicode = unicode("esto es unicode") #unicode("cadena")
	print textoUnicode
	print "Esto es utf-8".encode('utf-8') #"cadena".encode("codificación")
	'''
		¡Éste es un comentario
		usando multiples
		lineas, acentos y letras ñ's!
	'''
	cadenaMultiLinea = '''
	Este no es un comentario, sino
	una cadena con multiples saltos
	de linea sin necesidad de
	secuencias de escape.
	''' 
	print cadenaMultiLinea 
	numero = 8
	ocho = '8'
	numeroEscrito = 'ocho'
	print numero,"\t", type(numero)
	print ocho, "\t", type(ocho) #type(objeto)
	print numeroEscrito, "\t", type(numeroEscrito)
	print ocho
	longitudEnCaracteres = len(numeroEscrito) # len = length = largo. len(objeto)
	print longitudEnCaracteres
	
	nombre = 'Amet'
	edad = 17

	print "Hola,", nombre, "tienes", edad, "años." 
	
	print "Hola, %s tienes %d años." % (nombre,edad)

	edadEnCadena = str(edad) #str = string = cadena. str(objeto)

	print "hola, %s tienes %s años" % (nombre, edadEnCadena)

if __name__ == '__main__':
	main()