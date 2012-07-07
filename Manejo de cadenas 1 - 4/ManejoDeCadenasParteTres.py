
# -*- encoding: utf-8 -*-
def main():
	palabra = 'palabra'
	
	#################
	# p a l a b r a #
	# 0 1 2 3 4 5 6 #
	#################

	#Orden negativo:

	##########################
	#   p  a  l  a  b  r  a  #
	#  -7 -6 -5 -4 -3 -2 -1  #
	##########################

	# Slice en python: [Desde:Hasta]  (el segundo número (Hasta) no se toca.)
	p = palabra[0]
	print p
	laPalabra = palabra[0:7]
	print laPalabra
	pal = palabra[0:3] #0... 1... 2... /// 3...
	print pal
	palabraCompleta = palabra[:]
	print palabraCompleta
	pala = palabra[:4]
	print pala	
	abra = palabra[3:]
	print abra
	pala = palabra[-7:-3]
	print pala


if __name__ == '__main__':
	main()



	