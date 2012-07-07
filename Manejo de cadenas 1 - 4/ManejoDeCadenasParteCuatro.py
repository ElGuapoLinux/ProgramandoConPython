# -*- encoding: utf-8 -*-
def main():

	dos = 'dos'
	tres = 'tres'
	cadenaVacia ='      '

	sentencia = "esta"
	sentenciaCombinada = "EsTa ES una SentenciA"
	sentenciaAntesDeCambios = "Esta es una cadena sin cambios"
	
	minusculas = sentencia.lower()
	print minusculas
	mayusculas = sentencia.upper()
	print mayusculas
	print "variable original: \t",sentencia
	capitalizada = sentencia.capitalize()
	print capitalizada
	cadenaInvertida = sentenciaCombinada.swapcase()
	print cadenaInvertida



	esAlfaNumerico = sentencia.isalnum() #alphanumeric
	print esAlfaNumerico #true
	esAlfabetico = sentencia.isalpha() #alphabetic
	print esAlfabetico   #true
	esDigito = sentencia.isdigit()
	print esDigito		 #false
	digito = numerico
	esMinuscula = sentencia.islower()
	print esMinuscula  #true
	esMayuscula = sentencia.isupper()
	print esMayuscula  #false
	esUnEspacio = sentencia.isspace()
	print esUnEspacio  #false
	espacio = cadenaVacia.isspace()
	print espacio      #true

	sentenciaNueva = sentenciaAntesDeCambios.replace('no es', 'es') #replace('Anterior','Nueva')
	print sentenciaNueva

if __name__ == '__main__':
	main()