#Ingresos de datos

valor = int (input("valor del producto"))

#Procedimiento 

if valor>= 100:
    descuento= 0.10
else:
    descuento = 0
valordeldescuentoapagar = valor*descuento
totalpagar = valor- valordeldescuentoapagar
#salida
print (totalpagar)
