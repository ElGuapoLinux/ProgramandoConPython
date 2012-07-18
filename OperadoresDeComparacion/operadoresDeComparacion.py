# -*- encoding:utf-8 -*-

def main():

  #Operadores de comparación:
  a = 100
  b = 100

  if a == b: # ==
    print "If \t %s y %s son iguales." % (a,b)
  else:
    print "Else \t %s y %s no son iguales." % (a,b)
  
  if a != b: # !=
    print "If \t %s y %s son diferentes." % (a,b)
  else:
    print "Else \t %s y %s no son diferentes." % (a,b)  
  
  
  if a < b: # < menor qué
    print "If \t %s es menor que %s." % (a,b)
  else:
    print "Else \t %s no es menor que %s." % (a,b)  
  
  if a > b: # > mayor qué
    print "If \t %s es mayor que %s." % (a,b)
  else:
    print "Else \t %s no es mayor que %s." % (a,b) 
    
  if a >= b: # mayor o igual qué.
    print "If \t %s es mayor o igual a %s." % (a,b)
  else:
    print "Else \t %s no es mayor o igual a %s." % (a,b)  
  
  if a <= b:
    print "If \t %s es menor o igual a %s." % (a,b)
  else:
    print "Else \t %s no es menor o igual a %s." % (a,b) 
     

if __name__ == '__main__':
  main()

'''
  Sintaxis general de una condicíonal:
  if condicíonal:
    codigo.paraEjecutarse()       #Se ejecta si se cumple la condición.
  else:
    otro.codigo()                 #Se ejecta si no se cumple la condición.
'''