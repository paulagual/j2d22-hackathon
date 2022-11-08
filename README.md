# Jump2Digital22 | Data Science
Hackathon Nivel Junior

## INDEX

* [Background](#background)
* [Problem](#problem)
* [Results](#results)
* [Analysis](#analysis)
* [Solution](#solution)
* [License](#license)


<a name="background"></a>


## Background

En este reto se nos presenta el siguiente escenario:

### Clasificación de la calidad del aire

El Acuerdo de París es un tratado internacional sobre el cambio climático que fue adoptado por 196 Partes en la COP21 de París. Su objetivo es limitar el calentamiento mundial muy por debajo de 2, preferiblemente a 1,5 grados centígrados, en comparación con los niveles preindustriales.

Para alcanzar este objetivo de temperatura a largo plazo, los países se proponen alcanzar el máximo de las emisiones de gases de efecto invernadero lo antes posible para lograr un planeta con clima neutro para mediados de siglo.

Es por ello que la Unión Europea esta destinando grandes cantidades de recursos al desarrollo de nuevas tecnologías que permitan la mejorar la lucha contra la contaminación. Una de estas es un nuevo tipo de sensor basado en tecnología láser que permita detectar la calidad del aire en función de diferentes mediciones.

### Datasets

Variables del dataset:

*Features:* El dataset contiene 8 features en 8 columnas que son los parámetros medidos por los diferentes sensores. Estos corresponden a las diferentes interacciones que han tenido los haces de los láseres al travesar las partículas del aire.

*Target:* El target corresponde al 'label' que clasifica la calidad del aire.

- Target 0 corresponde a una calidad del aire Buena
- Target 1 corresponde a una calidad del aire Moderada
- Target 2 corresponde a una calidad del aire Peligrosa

*Archivos:*

- train.csv: Este dataset contiene tanto las variables predictoras como el tipo de clasificación de calidad del aire.
- test.csv: Este dataset contiene las variables predictoras con las que se tendrá que predecir el tipo de calidad de aire.

### Objetivo

El objetivo del reto será realizar un modelo predictivo basado en Random Forests que permita conocer el tipo de calidad del aire en función de las mediciones de los sensores.

Una vez se haya hecho y entrenado el modelo predictivo, éste se tendrá que emplear con los features del dataset de testing 'test.csv'. Las predicciones se tendrán que entregar en formato csv como en el ejemplo. Donde tendrá que aparecer tan solo una columna en la que en la primera fila habrá un texto cualquiera y las predicciones empezarán en la fila 2.

La calidad de la predicción se medirá a partir del f1-score(macro).

<a name="problem"></a>


# Problem

El problema a predecir mediante un modelo de Random Forest las labels del archivo test.


<a name="results"></a>


# Results

Después de analizar las diferentes features y realizar diferentes modelos. Se ha llegado a un modelo 
final, con un modelo final con una f1-score(macro) de 93.

<a name="analysis"></a>


# Analysis

Disponemos de un archivo con 8 features (las cuales no tienen un nombre descriptivo)  así que 
básicamente las analizaremos segun sus valores.

Con el análisis de la target, vemos que está balanceada.

Con el analísis multivariantes de las features y la target, vemos que lLas features 7 y 8 parecen ser 
las que tienen menos diferencias a la hora de comprarlas con las difrentes labels.

En el análisis de correlaciones, vemos que las features 5 y 6 están bastante correlacionadas, y podrían 
dar problemas de colinearidad.

También análizamos la separabilidad de las clases, y vemos que parecen  bastante separables.

<a name="solution"></a>


# Solution

Finalmente, para el modelado eliminamos las features 5, 7 y 8. La primera por colinearidad y las dos 
últimas por poca influencia en la taget.

Con ello generamos las predicciones de las features de test, tanto en csv con en formato json.

<a name="license"></a>


# License
