## BACKEND ##
Establish connection with Open Weather API and
collects the forecast data depending on city

## MAIN ##
Parametros: Latitud, Longitud y numero de dias
Dichos parametros se pasan a la funcion get_data
en backend.py y devuelve los datos filtrados

### Temperatura
Representa los valores de temperatura registrados en
cada "cnt" del API y lo representa mediante libreria
plotlit usando el timestamp (el mismo que usa la parte
del tiempo)

### Tiempo
Recolecta los timestamps de cada "cnt" en el API
y redacta la descripcion del tiempo
