#### UNIVERSIDAD CENTRAL “MARTA ABREU” DE LAS VILLAS FACULTAD DE MATEM ´ATICA, F´ISICA Y COMPUTACI ´ON

 DEPARTAMENTO DE CIENCIAS DE LA COMPUTACI ´ON

 TRABAJO DE DIPLOMA

## Propuesta de un nuevo m´etodo de explicabilidad para interpretar los resultados de modelos entrenados para la clasificaci´on de im´agenes

#### Autor: Esther Mar´ıa Mart´ın Hern´andez Tutores: Dra. C. Mar´ıa Matilde Garc´ıa Lorenzo Dra. C. Marilyn Bello Garc´ıa Consultor: MSc. Alejandro Ram´on Hern´andez

**2023**


-----

#### UNIVERSIDAD CENTRAL “MARTA ABREU” DE LAS VILLAS FACULTAD DE MATEM ´ATICA, F´ISICA Y COMPUTACI ´ON

 DEPARTAMENT OF COMPUTER SCIENCE

 DIPLOMA THESIS

## Proposal of a new explainability method to interpret the results of trained models for image classification

#### Author: Esther Mar´ıa Mart´ın Hern´andez Tutors: Dr.Sc. Mar´ıa Matilde Garc´ıa Lorenzo Dr.Sc. Marilyn Bello Garc´ıa Consultant: MSc. Alejandro Ram´on Hern´andez

**2023**


-----

**ACTA DE CONFORMIDAD PARA ESTUDIANTES DE PREGRADO**

**Universidad Central "Marta Abreu" de Las Villas**

Por una parte: _Esther María Martín Hernández_ estudiante de la carrera de: __Lic. Ciencia
de la Computación_ en la facultad de: Matemática Física y Computación, en lo adelante El
**ESTUDIANTE.** Con número de identidad permanente: 01092372735 o pasaporte:

______________. Y por otra parte Gerado Hernández Jefe del Departamento Docente de:

Computación
en la ya mencionada facultad, en lo adelante EL JEFE DE DEPARTAMENTO, y __María Matilde
García Lorenzo y Marilyn Bello García profesor(es) encargado(s) de tutorar el Trabajo de Diploma
**DEL ESTUDIANTE, en lo adelante EL TUTOR.**
Reconocen que:

I. A EL ESTUDIANTE se le ha aprobado como tema de investigación para su Trabajo de
Diploma el titulado Propuesta de un nuevo método de explicabilidad para

**interpretar los resultados de modelos entrenados para la clasificacion de**
**imágenes**

II. **EL ESTUDIANTE no divulgará información concerniente a la investigación, tanto durante el**
desarrollo como tras la culminación de esta sin la debida autorización DEL TUTOR o EL JEFE
**DE DEPARTAMENTO.**

III. Que el Trabajo de Diploma fruto de la labor investigativa de EL ESTUDIANTE y la asesoría de

**EL TUTOR, resulta de TITULARIDAD EXCLUSIVA de la Universidad Central “Marta Abreu”**
de las Villas.

IV. El ESTUDIANTE una vez aprobada su tesis para la defensa, depositará una copia electrónica

de la misma en el Repositorio Digital Institucional de la Universidad Central “Marta Abreu” de
Las Villas.

V. A partir de la defensa y aprobación del Trabajo de Diploma, la publicación total, parcial o la
elaboración de cualquier obra que se derive de esta investigación por parte de EL
**ESTUDIANTE, contará con la coautoría de EL TUTOR y viceversa, resultando de referencia**
obligada esta obra en cualquier otra que se elabore. El incumplimiento de esta cláusula, puede
llevar consigo el inicio de procesos de plagio. Todo lo anterior de acuerdo a la normativa de
Derecho de Autor vigente en Cuba.

Y para que así conste se firma la presente en la Universidad Central “Marta Abreu” de Las Villas, a
los 7 días del mes de diciembre del año 2023.

_____________________ _________________________

EL ESTUDIANTE JEFE DE DEPARTAMENTO

_____________________ ______________________

TUTOR TUTOR


-----

_”No importa cu´an dif´ıcil o imposible parezca, no apartes la vista de tu objetivo”_

_—Eiichiro Oda_


-----

**_DEDICATORIA_**
_A mis padres, por el apoyo incondicional y constante a lo largo de mi vida._
_A mi hermano, porque cerca o lejos es mi br´ujula y motivaci´on._
_A Daniel, por llenarme de su luz cada d´ıa con su paciencia, dedicaci´on y aliento._


-----

**_AGRADECIMIENTOS_**
_A los pilares de mi vida: mis padres, mi hermano y mi esposo._
_A mis t´ıas, mis t´ıos, mi hermana, mis sobrinas lindas y a toda mi familia por estar_
_siempre, preocuparse y apoyarme en todo._
_A Bety por concederme el placer de sentir que es como una hermana para mi. Tambi´en a_
_sus padres y su familia por acogerme y hacerme sentir parte de ella._
_A mis compa˜neros que son casi familia despu´es de estos ´ultimos a˜nos viviendo_
_experiencias juntos._
_A mi pandilla cienfueguera por estar para mi, darme aliento y confianza en cada_
_”reuni´on”._
_Especialmente a mis tutores Mar´ıa Matilde y Marilyn por su gu´ıa y consejos precisos en_
_todo momento_
_Y a todas las personas que de una forma u otra han contribuido en mi progreso hasta_
_aqu´ı:_
_¡¡Muchas gracias!!_


-----

### Resumen

En la actualidad, las redes neuronales han revolucionado diversos sectores gracias a su
capacidad para comprender relaciones complejas en grandes conjuntos de datos. Sin
embargo, la opacidad en la toma de decisiones de estos modelos ha generado
desconfianza, impulsando la necesidad de la Inteligencia Artificial Explicable. La
explicabilidad, en este contexto, se presenta como un componente esencial para superar
los obst´aculos mencionados, pero su implementaci´on sigue siendo un desaf´ıo
significativo. La falta de m´etodos concretos para evaluar la calidad de las explicaciones
ha intensificado la necesidad de enfoques robustos y confiables capaces de proporcionar
claridad y veracidad en las interpretaciones. En respuesta a este desaf´ıo se propone el
dise˜no de un nuevo enfoque para interpretar las decisiones de modelos de clasificaci´on de
im´agenes como VGG19, basado en redes neuronales y utilizando entre la definici´on de
sus capas una funci´on de perturbaci´on. Se detalla la implementaci´on de la propuesta, as´ı
como de las funciones auxiliares. El enfoque propuesto se eval´ua en diferentes casos de
estudio a partir de realizar configuraciones espec´ıficas al conjunto Food101, explorando
de esa forma el m´etodo en diferentes escenarios se observ´o cierta consistencia en la
interpretaci´on de los mapas de relevancia. La comparaci´on entre los casos de estudio
revel´o cambios espec´ıficos a realizar para mejorar la calidad de las explicaciones
proporcionadas. Se obtuvieron resultados adecuados para una etapa experimental y se
reconoce la necesidad de futuras investigaciones para refinar los escenarios de prueba y
profundizar en la comprensi´on de las interacciones entre los par´ametros del modelo, la
funci´on de perturbaci´on y la interpretaci´on de la explicaci´on.


-----

### Abstract

Nowadays, neural networks have revolutionized various sectors thanks to their ability to
understand complex relationships in large data sets. However, the opacity in the
decision-making of these models has generated distrust, driving the need for Explainable
Artificial Intelligence. Explainability, in this context, is presented as an essential
component to overcome the aforementioned obstacles, but its implementation remains a
significant challenge. The lack of concrete methods to assess the quality of explanations
has intensified the need for robust and reliable approaches capable of providing clarity
and veracity in interpretations. In response to this challenge, we propose the design of a
new approach to interpret the decisions of image classification models such as VGG19,
based on neural networks and using a perturbation function between the definition of its
layers. The implementation of the proposal is detailed, as well as the auxiliary functions.
The proposed approach is evaluated in different case studies based on making specific
configurations to the Food101 set, thus exploring the method in different scenarios some
consistency was observed in the interpretation of the relevance maps. The comparison
between the case studies revealed specific changes to be made to improve the quality of
the explanations provided. Adequate results were obtained for an experimental stage and
it is recognized the need for future research to refine the test scenarios and deepen the
understanding of the interactions between the model parameters, the perturbation
function and the interpretation of the explanation.


-----

# ´Indice general

**Resumen** **I**

**Abstract** **II**

**Introducci´on** **1**

**1. Aspectos Te´oricos** **6**
1.1. Inteligencia Artificial . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

1.2. Aprendizaje Autom´atico . . . . . . . . . . . . . . . . . . . . . . . . . . 7

1.3. Redes Neuronales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

1.3.1. Fases de modelaci´on con redes neuronales . . . . . . . . . . . . . 11

1.3.2. Topolog´ıa de redes neuronales . . . . . . . . . . . . . . . . . . . 12

1.4. Aprendizaje Profundo . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

1.4.1. Redes Neuronales Profundas . . . . . . . . . . . . . . . . . . . . 15

1.4.2. Redes Neuronales Profundas Convolucionales . . . . . . . . . . . 17

1.4.3. Modelos de redes convolucionales . . . . . . . . . . . . . . . . . 22

1.5. Inteligencia Artificial Explicable . . . . . . . . . . . . . . . . . . . . . . 23

1.5.1. Explicabilidad . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

1.5.2. Herramientas actuales para la explicabilidad . . . . . . . . . . . . 28

1.6. Conclusiones parciales . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

**2. Implementaci´on del nuevo m´etodo** **33**
2.1. Descripci´on general del modelo . . . . . . . . . . . . . . . . . . . . . . 33

2.1.1. Arquitectura de la red y particularidades a tener en cuenta en cada
capa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

2.2. Implementaci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

2.2.1. An´alisis de la complejidad computacional . . . . . . . . . . . . . 39

2.3. Alcance y limitaciones del m´etodo propuesto . . . . . . . . . . . . . . . 40

2.4. Diferencias con respecto a los enfoques actuales . . . . . . . . . . . . . . 41

2.5. Conclusiones parciales . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

**3. Evaluaci´on del m´etodo propuesto en los casos de estudio** **43**
3.1. Descripci´on del conjunto de datos de entrada . . . . . . . . . . . . . . . 43

3.2. Transformaciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

3.3. Caso de estudio 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45


-----

3.4. Caso de estudio 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47

3.5. Caso de estudio 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

3.6. Comparaci´on de los casos de estudio . . . . . . . . . . . . . . . . . . . . 51

3.7. Conclusiones parciales . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

**Conclusiones** **54**

**Recomendaciones** **55**

**Referencias** **56**


-----

# Introducci´on

Con la gradual evoluci´on del tiempo, los problemas y las expectativas de la vida humana
se han vuelto cada vez m´as complejos, lo que trae consigo la necesidad de un arduo
trabajo para encontrar soluciones correspondientes. Este enfoque de actitud de resoluci´on
de problemas finalmente ha llevado a la humanidad a la era tecnol´ogica actual, donde se
realizan constantes intentos por hacer que las m´aquinas alcancen una inteligencia similar
a la humana.
Desde sus primeros avances hasta la actualidad, la Inteligencia Artificial (IA o AI, del
ingl´es Artificial Intelligence) ha encontrado m´ultiples aplicaciones en diversas ´areas,
relacion´andose esta a las imitaciones por m´aquinas de funciones cognitivas asociadas a
las mentes humanas como aprender y resolver problemas. Es por eso que se han logrado
importantes capacidades en este campo como comprender exitosamente el habla humana,
competir en alto nivel en sistemas de juegos estrat´egicos, integrar autos aut´onomos y
sistemas de diagn´onstico m´edico, realizar enrutamiento inteligente, simulaciones
militares, interpretar datos complejos, detectar emociones en el reconocimiento de
expresiones faciales y el procesamiento del lenguaje natural para comprender y empatizar
con las emociones humanas, clasificar y etiquetar autom´aticamente las im´agenes,
permitiendo la organizaci´on y b´usqueda eficiente de grandes conjuntos de datos visuales,
entre muchas otras (Ongsulee, 2017).
Estas diversas capacidades, se han logrado a trav´es del avance en los numerosos
subcampos de la IA, entre los que ha tenido un gran impacto el Aprendizaje Autom´atico
o Automatizado (ML, del ingl´es Machine Learning) y el Aprendizaje Profundo (DL, del
ingl´es Deep Learning), los cuales se enfocan en desarrollar algoritmos complejos y
modelos que permiten a las m´aquinas aprender y tomar decisiones basadas en los datos
(Ongsulee, 2017).
En este sentido, los algoritmos de ML analizan los datos, aprenden de estos y luego aplican
lo que han aprendido para hacer predicciones o tomar decisiones informadas, logrando con
el entrenamiento a medida que se exponen a m´as datos a lo largo del tiempo, mejorar su
rendimiento sin programaci´on expl´ıcita. Estos algoritmos se dividen en grupos, pueden ser
supervisados, no supervisados, semi-supervisados o reforzados, seg´un el tipo de datos y
el enfoque de este (Taye, 2023). Adem´as, existen varios enfoques de ML y es importante
tener en cuenta que no son mutuamente excluyentes porque se pueden combinar para crear
modelos m´as complejos. Entre ellos se encuentran el aprendizaje perezoso, el aprendizaje
basado en ´arboles de decisi´on, el aprendizaje basado en reglas y el aprendizaje basado en
redes neuronales o tambi´en conocido como aprendizaje conexionista. Este ´ultimo es un
tipo de m´etodo en el que el sistema aprende de un conjunto de nodos interconectados que


-----

simulan la funci´on de las neuronas en el cerebro (Dietterich et al., 2008).
Del mismo modo el aprendizaje profundo constituye un subconjunto del aprendizaje
autom´atico conexionista y los algoritmos de este aprendizaje requieren grandes
cantidades de datos, incluidos datos diversos y no estructurados, para aprender y mejorar
sus resultados. Esto hace que tenga dos ventajas principales: poder manejar vol´umenes
masivos de datos y poder mejorar los resultados a trav´es de la repetici´on, sin intervenci´on
humana. (Grieve, 2023).
En general, seg´un (Carvalho et al., 2019), los modelos de aprendizaje autom´atico y
aprendizaje profundo a menudo se consideran “cajas negras”, ya que su l´ogica interna y
sus procesos de toma de decisiones no son f´acilmente interpretables por los humanos y
esta falta de interpretabilidad puede ser problem´atica, en especial en dominios sensibles
como la atenci´on m´edica, donde es importante comprender c´omo un modelo lleg´o a su
decisi´on.
Dado estos desaf´ıos, la construcci´on de m´etodos robustos y pr´acticos para explicar las
decisiones de un determinado modelo, se ha desarrollado en un ´area de investigaci´on
propia, la IA explicable (XAI, del ingl´es Explainable Artificial Intelligence) la cual busca
mejorar el proceso de entrenamiento, las representaciones aprendidas y las decisiones
con explicaciones interpretables por humanos (Samek et al., 2021).
Para (Lusim and Marchesano, 2023) dentro de la explicabilidad de modelos, existen los
modelos interpretables como ´arboles de decisi´on, modelos basado en reglas y modelos de
regresi´on lineal, entre otros, cuyos procesos de toma de decisi´on son transparentes, es
decir es posible comprender la secuencia de pasos ejecutados para llegar a su respuesta.
Y por ortro lado est´an los modelos no interpretables, ya mencionados como cajas negras.
En el caso de los modelos cajas negras existen diferentes enfoques para explicar sus
decisiones. La literatura los divide en, explicaciones globales o locales, con el fin de
determinar qu´e variables contribuyen al modelo para tomar decisiones y determinar c´omo
afectan los valores de esas variables a las predicciones, permitiendo abordar la falta de
profundidad y transparencia. Esta puede tambi´en ayudar a los desarrolladores a
garantizar que el sistema funciona de la forma esperada, mitigar riesgos legales, de
cumplimiento, seguridad y reputaci´on de la inteligencia artificial en producci´on. Incluso,
estas t´ecnicas en ocasiones son utilizadas para depurar modelos.
Al margen de lo dicho en cuanto a m´etodos de explicaci´on, existen los dependientes del
modelo, que son t´ecnicas que explican las decisiones tomadas por un modelo de
aprendizaje autom´atico espec´ıfico. Y por otro lado, los m´etodos de explicaci´on
independientes del modelo o agn´osticos consideradas t´ecnicas que pueden explicar las
decisiones de cualquier modelo. Entre los m´etodos de explicaci´on dependientes del
modelo se incluyen LRP (del ingl´es, Layer-wise Relevance Propagation), Grad-CAM
(del ingl´es, Gradient-weighted Class Activation Mapping), DeepLIFT (del ingl´es, Deep
Learning Important FeaTures), que junto a otras t´ecnicas y m´etodos existentes seg´un las
caracter´ısticas espec´ıficas del modelo que se explica, son ´utiles para obtener informaci´on
sobre c´omo se realizan predicciones y comprender la relaci´on entre estas y los rasgos de
entrada, ya que a menudo, se basan en la arquitectura y los par´ametros espec´ıficos del
modelo (Onose, 2023).
Por otra parte, existen numerosos m´etodos agn´osticos y entre los m´as utilizados se
encuentran el de la dependencia parcial (PDP, del ingl´es Partial Dependence Plot) como


-----

m´etodo global y como m´etodos locales se destacan LIME (Local Interpretable
Model-Agnostic Explanations) y SHAP (SHapley Additive exPlanations) (Molnar,
2022). En este contexto, y en correlaci´on a los avances actuales en el campo de la XAI,
existen herramientas que se utilizar para facilitar el trabajo a desarrolladores y dem´as
personas vinculadas a este campo, como son Captum, AIX360, TFX, Scikit-learn o
sklearn, Alibi, iNNvestigate, InterpretML, OmniXAI, DeepLIFT, ELI5, Skater y
DALEX.
A modo general, se han propuesto varias formas de evaluar y medir la efectividad de
una explicaci´on. Cada una de ellas se establece dentro de un entorno que depende de la
tarea, habilidades, y expectativas del usuario del sistema de IA, siendo estas, por lo tanto,
dependientes del dominio. Algunos enfoques existentes en la explicabilidad son el an´alisis
de sensibilidad, la descomposici´on simple de Taylor y las t´ecnicas de propagaci´on hacia
atr´as, sin embargo, es dif´ıcil determinar objetivamente si una t´ecnica es buena o no, para
lo cual existen estrategias de evaluaci´on de la calidad (Montavon et al., 2018).
A pesar de los recientes avances en la XAI, la explicabilidad sigue siendo un desaf´ıo
especialmente en los modelos de caja negra. Si bien existen varios m´etodos y marcos de
trabajo, todav´ıa se necesita m´as investigaci´on y desarrollo en esta ´area, ya que por
ejemplo, las t´ecnicas existentes pueden proporcionar informaci´on sobre el proceso de
toma de decisiones de un modelo, sin embargo a medida que estos se vuelven cada vez
m´as complejos, se vuelve m´as dif´ıcil comprender c´omo toman decisiones, lo que genera
preocupaciones sobre su confiabilidad, usabilidad y otras pueden ser dif´ıciles de aplicar
en la pr´actica (Carvalho et al., 2019).
En lo que se refiere a cajas negras, un ejemplo claro y popular es la clasificaci´on de
im´agenes, ya que las soluciones propuestas carecen de la capacidad de interpretar su
mecanismo de trabajo interno y explicar el razonamiento principal de sus predicciones.
Actualmente existen varios modelos que se pueden utilizar para la clasificaci´on de
im´agenes, cada uno con sus propias fortalezas y debilidades, entre los cuales los m´as
utilizados son ResNet, Inception, VGG y DenseNet (Carvalho et al., 2019). Otros
modelos que se pueden utilizar para la clasificaci´on de im´agenes incluyen AlexNet
(Anwar, 2019), GoogLeNet (Sekhar and Yang, 2022) y MobileNet(Zhang et al., 2022).
Es importante tener en cuenta que el rendimiento de todos los modelos puede variar
seg´un el conjunto de datos espec´ıfico y la tarea en cuesti´on. Por lo tanto, a menudo es
necesario experimentar con diferentes modelos y ajustarlos para lograr los mejores
resultados. Adem´as, tener diversos conjuntos de datos de clasificaci´on de im´agenes es
fundamental para construir modelos m´as precisos (Le, 2018).

En la actualidad son insuficientes los m´etodos de explicabilidad confiables dados las
disimiles topolog´ıas de red. Por consecuente existe la necesidad de una mayor
investigaci´on y desarrollo, crucial para generar confianza, aumentar su usabiliad,
comprender su proceso de toma de decisiones y reforzar el uso ´etico y responsable de la
IA en esta ´area, lo cual constituye el problema de investigaci´on de este trabajo. A partir
de esto se define como objetivo general:

**Objetivo general**
Desarrollar un m´etodo de explicabilidad para interpretar los resultados de modelos


-----

entrenados para la clasificaci´on de im´agenes.
**Objetivos espec´ıficos**

1. Analizar el marco te´orico referencial

2. Implementar un nuevo m´etodo de explicabilidad dependiente del modelo.

3. Evaluar m´etodo propuesto en distintos casos de estudio.

Esta tesis se organiza en introducci´on, tres cap´ıtulos, conclusiones, recomendaciones y
por ´ultimo referencias bibliogr´aficas. En el cap´ıtulo 1 se presentan los elementos te´oricos
para la comprensi´on de las redes neuronales, la explicabilidad en la IA y en especial en el
´area del procesamiento de im´agenes, as´ı como tambi´en se aborda acerca de los resultados
obtenidos hasta la actualidad en la explicabilidad de los modelos. En el cap´ıtulo 2 se
parte de la conceptualizaci´on de estudios de la explicabilidad para exponer la nueva
propuesta, su dise˜no e implementaci´on. En el cap´ıtulo 3 se analizan y visualizan los
resultados experimentales obtenidos sintetizando los resultados obtenidos, a partir de los
casos de estudio.


-----

# Cap´ıtulo 1


-----

# Cap´ıtulo 1

 Aspectos Te´oricos

En este cap´ıtulo se hace un recorrido te´orico para la comprensi´on de redes neuronales
profundas, partiendo de varios conceptos generales que forman la base de la
explicabilidad. Se analiza el desarrollo actual de esta y c´omo se aprecian en la pr´actica.

### 1.1. Inteligencia Artificial

Durante miles de a˜nos, se ha tratado de comprender c´omo los humanos piensan y actuan,
es decir, c´omo el cerebro puede percibir, comprender, predecir y manipular un mundo
mucho m´as grande y complicado que ´el mismo. El campo de la IA, se ocupa no solo de
comprender, sino tambi´en de construir entidades inteligentes, m´aquinas que pueden
calcular c´omo actuar de manera efectiva y segura en una amplia variedad de situaciones
novedosas. Ha evolucionado a lo largo de los a˜nos, desde los primeros intentos de crear
m´aquinas que imitaran la inteligencia humana en la d´ecada de 1950 hasta la actualidad,
en la que se utiliza en una amplia variedad de aplicaciones. Hist´oricamente, los
investigadores han buscado varias definiciones diferentes de la IA. Seg´un (Russell and
Norving, 2020) algunos han definido la inteligencia en t´erminos de fidelidad al
desempe˜no humano, mientras que otros prefieren la racionalidad, en cuanto a exactitud
matem´atica. Los m´etodos utilizados son necesariamente diferentes: la b´usqueda de una
inteligencia similar a la humana debe ser en parte una ciencia emp´ırica relacionada con la
psicolog´ıa, que involucre observaciones e hip´otesis sobre el comportamiento humano real
y los procesos de pensamiento; un enfoque racionalista, por otro lado, implica una
combinaci´on de matem´aticas e ingenier´ıa, y se conecta con la estad´ıstica, teor´ıa del
control y econom´ıa.
En (Xu et al., 2021) se refiere a la IA como la simulaci´on de la inteligencia humana por
un sistema, cuyo objetivo es desarrollar una m´aquina que pueda pensar como los
humanos e imitar comportamientos humanos, incluyendo percepci´on, razonamiento,
aprendizaje, planificaci´on, predicci´on, y as´ı sucesivamente. Los campos de investigaci´on
incluyen algoritmos de b´usqueda, grafos de conocimiento, sistemas basados en reglas,
procesamiento de lenguaje natural, razonamiento basado en casos, sistemas expertos,
algoritmos de evoluci´on, ML, DL, visi´on y audici´on artificial, etc.
En base a (Ram´ırez V´eliz, 2022) se define la IA como una de las ramas de la Inform´atica,


-----

con fuertes ra´ıces en otras ´areas como la l´ogica y las ciencias cognitivas, y la
diferenciaci´on de sus definiciones parte de las caracter´ısticas o propiedades que estos
programas deben satisfacer, aunque todas ellas concurren en la precisi´on de la validaci´on
del trabajo. Dependemos de la tecnolog´ıa y ´esta de nosotros, la finalidad es interactuar
con ella y m´as que competir complementarnos, as´ı toda IA que se desarrolle permitir´a
hacer m´as de lo que pod´ıan hacer quienes antecedieron a la generaci´on actual.

### 1.2. Aprendizaje Autom´atico

El ML surgi´o en 1959 como una rama de la IA que se enfoca en el desarrollo de
algoritmos que permiten a las computadoras la capacidad de aprender y mejorar a partir
de la experiencia sin ser programadas expl´ıcitamente. En las ´ultimas d´ecadas, el ML ha
experimentado un gran avance gracias a la disponibilidad de grandes cantidades de datos
y la capacidad de procesamiento de las computadoras modernas. (Ongsulee, 2017).
Seg´un (Taye, 2023) este subdominio consiste en que la m´aquina haga juicios y
pron´osticos basados en datos hist´oricos, apoyado en el uso de algoritmos para analizar
datos, aprender patrones y mejorar el conocimiento y los criterios de rendimiento de los
sistemas. El aprendizaje autom´atico se utiliza en muchas ´areas diferentes, que incluyen,
entre otras, rob´otica, asistentes personales virtuales (como Google), videojuegos,
reconocimiento de patrones, procesamiento de lenguaje natural, miner´ıa de datos,
predicci´on de tr´afico, redes de transporte en l´ınea (como las estimaciones de precios de
Uber), recomendaciones de productos, pron´osticos del mercado de valores, diagn´osticos
m´edicos, predicciones de fraude, asesoramiento agr´ıcola y refinamiento de resultados de
motores de b´usqueda (como el motor de b´usqueda de Google). En fin, se materializa en
diversas tareas asociadas a mecanismos espec´ıficos en dependencia del problema a
resolver, que a la vez est´an estrechamente vinculados al tipo de aprendizaje.
De acuerdo con (Taye, 2023) el aprendizaje se clasifica en correspondencia con la forma en
que un algoritmo aprende a hacer predicciones m´as precisas, y existen cuatro metodolog´ıas
de aprendizaje fundamentales como puede ver tambi´en en la Figura 1.1:

Aprendizaje supervisado: El algoritmo se entrena utilizando datos etiquetados. Los
datos se denominan etiquetados porque consisten en pares, la salida deseada que se
puede definir como una se˜nal de supervisi´on y la entrada que se puede expresar
como un vector, as´ı que este algoritmo se produce cuando se conoce de antemano
el resultado correcto. Con el tiempo, el algoritmo de aprendizaje refina sus
resultados en un esfuerzo por reducir la brecha entre sus predicciones y el resultado
real con asesor´ıa de alguna persona especializada. Las dos subcategor´ıas
principales de aprendizaje supervisado son algoritmos de regresi´on (salida de
valores num´ericos cont´ınuos como la predicci´on del precio de una casa en funci´on
de su tama˜no y ubicaci´on) y algoritmos de clasificaci´on (salida de valores discretos
como la clase o categor´ıa a la que pertenece un objeto).

Aprendizaje no supervisado: Este enfoque entrena el algoritmo utilizando un
conjunto de datos de entrada desprovisto de cualquier salida etiquetada, en
contraste con el aprendizaje supervisado. Para cada elemento de entrada, no hay


-----

una salida correcta o incorrecta, y no hay participaci´on humana para corregir o
adaptar. Por lo tanto, el aprendizaje no supervisado es m´as arbitrario que el
supervisado. El objetivo principal de este es obtener una comprensi´on m´as
profunda de los datos mediante el reconocimiento de su estructura b´asica o patr´on
de distribuci´on. De esta forma, el algoritmo intenta representar un patr´on detectado
espec´ıfico mientras lo refleja en la estructura general de los patrones de entrada a
medida que aprende por s´ı mismo. Como resultado, las diversas entradas se pueden
agrupar en funci´on de las caracter´ısticas que se tomaron de cada elemento de
entrada. Es por ello que el aprendizaje no supervisado se utiliza para resolver
problemas de asociaci´on y agrupaci´on en cl´usteres, para extraer caracter´ısticas de
datos sin etiquetar y categorizarlas o etiquetarlas.

Aprendizaje semi-supervisado : utiliza una gran cantidad de datos de entrada,
algunos de los cuales est´an etiquetados, mientras que el resto no y por tanto
requiere menos interacci´on humana. Dado que los conjuntos de datos etiquetados
son m´as dif´ıciles de obtener y tal vez necesiten acceso a especialistas en dominios
y los datos sin etiquetar son menos costosos y m´as simples de recuperar, se pueden
usar enfoques de entrenamiento supervisados y no supervisados para ense˜nar el
algoritmo en el aprendizaje semi-supervisado. Al emplear m´etodos de ambos
aprendizajes, se pueden exponer los patrones y estructuras latentes del conjunto de
datos de entrada y aplicar a datos no etiquetados para proporcionar predicciones
basadas en las mejores conjeturas, que posteriormente se pueden aplicar a nuevos
conjuntos de datos. Por lo tanto, se puede resumir que los datos no etiquetados se
usan para volver a clasificar o reevaluar una hip´otesis o pron´ostico establecido
usando datos etiquetados.

Aprendizaje reforzado: en lugar de recibir instrucciones expl´ıcitas sobre qu´e hacer,
este tipo de algoritmos aprende a trav´es de sus propias actividades, podr´ıa
caracterizarse como un proceso de aprendizaje basado en prueba y error. Se utiliza
para entrenar a un agente para que tome decisiones en un entorno din´amico. Este
tipo de aprendizaje utiliza un sistema de “recompensas y castigos”, ya que tienen
objetivos establecidos y reciben se˜nales que indican si una acci´on realizada fue
exitosa o no, aspirando a la capacidad de elegir opciones que maximicen el valor de
la recompensa y reduzcan la penalizaci´on. Estas t´ecnicas se utilizan en aplicaciones
como los juegos y la rob´otica, por ejemplo un agente en un autom´ovil aut´onomo
ser´ıa recompensado por llegar a la ubicaci´on pero castigado por desviarse de la
carretera.


-----

Figura 1.1: Diferentes categor´ıas y algoritmos de aprendizaje autom´atico. (Extra´ıdo de
(Taye, 2023))

Adem´as existen varios enfoques del aprendizaje en ML en dependencia de los datos y el
problema a resolver, es importante tener en cuenta que no son mutuamente excluyentes
porque se pueden combinar para mejorar el rendimiento de los modelos. A continuaci´on,
se describen algunos de estos enfoques:

Aprendizaje Perezoso (en ingl´es Lazy Learning): es un enfoque en el cual el
modelo pospone la generalizaci´on hasta el momento de la predicci´on. Algunos
m´etodos de aprendizaje perezoso incluyen el aprendizaje basado en instancias (en
ingl´es Instance-Based Learning) y el algoritmo del k-vecino m´as cercano(KNN del
ingl´es k-nearest neighbors) (Aha and Kibler, 1991)

Aprendizaje basado en Arboles de Decisi´on (en ingl´es Decision Tree Learning):[´]
se construye un modelo en forma de estructura de ´arbol donde cada nodo interno
representa una caracter´ıstica o atributo, cada rama representa una decisi´on basada
en esa caracter´ıstica, y cada hoja representa una clase o una predicci´on. (Tan et al.,
2005)

Aprendizaje Basado en Reglas (en ingl´es Rule-Based Learning): se centra en extraer
reglas o condiciones “if-then” a partir de los datos de entrenamiento. Estas reglas
se utilizan posteriormente para hacer predicciones o tomar decisiones. (Zhou and
Purvis, 2004)


-----

Aprendizaje Bayesiano (en ingl´es Bayesian Learning): utiliza el teorema de Bayes
para actualizar las creencias o conocimientos previos a medida que se obtienen
nuevos datos. Este enfoque se basa en la inferencia estad´ıstica y permite la
estimaci´on de la probabilidad de eventos futuros.(Barber, 2012)

Aprendizaje por Transferencia (en ingl´es Transfer Learning): implica aprovechar
el conocimiento o la experiencia adquirida en una tarea o dominio para mejorar el
rendimiento en un dominio objetivo relacionado.(Tan et al., 2018)

Aprendizaje Conexionista (en ingl´es Connectionist Learning): seg´un (Bishop, 2006)
se basa en redes neuronales artificiales, las que se abordaran con mayor profundidad
en el pr´oximo apartado.

### 1.3. Redes Neuronales

Las Redes Neuronales Artificiales, (ANN del ingl´es Artificial Neural Networks o NN de
Neural Networks) surgieron con el prop´osito de procesar informaci´on y resolver
problemas en diversos campos, est´an inspiradas en las redes neuronales biol´ogicas del
cerebro humano y est´an constituidas por elementos que se comportan de forma similar a
la neurona biol´ogica en sus funciones m´as comunes. Seg´un (Basogain Olabe, 2003) estos
elementos est´an organizados de una forma parecida a la que presenta el cerebro humano,
donde la unidad an´aloga a la neurona biol´ogica es el elemento procesador, llamado
neurona artificial. Esta tiene varias entradas con un peso asociado y las combina,
normalmente con una suma b´asica. La suma de las entradas es modificada por una
funci´on de transferencia o activaci´on y el valor de la salida de esta funci´on de se pasa
directamente a la salida de la neurona. Adem´as esta se puede conectar a las entradas de
otras neuronas artificiales mediante conexiones ponderadas correspondientes a la eficacia
de la sinapsis (la se˜nal) de las conexiones neuronales. A continuaci´on en la figura 1.2 se
presenta la ilustraci´on de una neurona artificial y sus componentes.

Figura 1.2: Diagrama de una neurona artificial. (Extra´ıdo de (Basogain Olabe, 2003))


-----

Las ANN al margen de “parecerse” al cerebro presentan una serie de caracter´ısticas
propias del cerebro, por ejemplo las ANN aprenden de la experiencia, generalizan de
ejemplos previos a ejemplos nuevos y abstraen las caracter´ısticas principales de una serie
de datos. Sin embargo en (Amador, 2023) se expone que poseen otras funcionalidades y
estructuras de conexi´on distintas a las vistas desde la perspectiva biol´ogica. Entre sus
caracter´ısticas principales est´an las siguientes:

1. Auto-organizaci´on y adaptabilidad: utilizan algoritmos de aprendizaje adaptativo y
auto-organizaci´on, por lo que ofrecen mejores posibilidades de procesado robusto y
adaptativo.

2. Procesado no lineal: aumenta la capacidad de la red para aproximar funciones,
clasificar patrones y aumenta su inmunidad frente al ruido.

3. Procesado paralelo: normalmente se usa un gran n´umero de nodos de procesado,
con alto nivel de interconectividad.

#### 1.3.1. Fases de modelaci´on con redes neuronales

Las fases de modelar y construir NNs pueden variar dependiendo de la aplicaci´on
espec´ıfica y el tipo de red que se est´a modelando. Sin embargo, una generalizaci´on del
modelado seg´un (Wang et al., 2021; Haykin, 2009; Zhang and Zhang, 2019) ser´ıan:

1. Recopilaci´on y preprocesamiento de datos: se recopilan y preprocesan los datos
necesarios para entrenar y probar la NN. Esto incluye la limpieza de los datos, la
eliminaci´on de valores at´ıpicos y la normalizaci´on de los datos para garantizar que
sean adecuados para su uso en la red neuronal.

2. Selecci´on de modelo y dise˜no de arquitectura de red: se selecciona el tipo de red
neuronal a utilizar, y se dise˜na su arquitectura. Esto incluye determinar el n´umero
de capas, el n´umero de neuronas en cada capa y las funciones de activaci´on que se
utilizar´an.

3. Entrenamiento: la red neuronal se entrena utilizando los datos preprocesados. Este
proceso implica ajustar los pesos y sesgos de la red para minimizar el error entre la
salida predicha y la salida real.

4. Validaci´on: el rendimiento de la red neuronal entrenada se eval´ua utilizando un
conjunto de datos de validaci´on. Esto ayuda a garantizar que la red neuronal no se
ajuste en exceso a los datos de entrenamiento y pueda generalizarse bien a nuevos
datos, previendo los problemas de sobreajuste y subajuste

5. Prueba: el rendimiento de la red se eval´ua utilizando un conjunto de datos de prueba
separado. Esto ayuda a garantizar que la red neuronal pueda predecir con precisi´on
las salidas de datos nuevos.

6. Despliegue: la red neuronal entrenada se despliega en una aplicaci´on del mundo real.
Esto implica integrar la red neuronal en la aplicaci´on y asegurarse de que funciona
correctamente.


-----

En ocasiones, las fases de validaci´on y prueba se realiza en una ´unica fase combinada,
dependiendo del tipo de red y tareas espec´ıficas encomendadas.

#### 1.3.2. Topolog´ıa de redes neuronales

En el desarrollo de una NN, no hay que programar ni el conocimiento ni las reglas del
procesamiento del conocimiento. La red aprende las reglas del procesamiento del
conocimiento mediante el ajuste de las conexiones ponderadas entre las neuronas de
distintas capas de la red, dado que, la mayor´ıa de ANN se caracterizan por tener sus
neuronas dividas en capas, comenzando por la capa de entrada, por la que se recibir´a la
se˜nal entrante de la red, y terminando con la capa de salida por donde la red enviar´a su
se˜nal de salida, pudiendo o no existir entre ellas, capas intermedias denominadas capas
ocultas, como se ve en la figura 1.3 (Moreno, 2020). Al margen de lo dicho, la topolog´ıa
o arquitectura de una ANN hace referencia a c´omo est´an estructuradas las capas y las
conexiones.

Figura 1.3: a) Red neuronal simple o monocapa (en ingl´es Single-layer Perceptron). b) Red
neuronal multicapa (MLP del ingl´es Multi-layer Perceptron). (Extra´ıdo de (Manjarrez,
2014))

Las conexiones entre neuronas son un aspecto crucial, ya que determinan el flujo de
informaci´on a trav´es de la red. Pueden ser totales o parciales, dependiendo de la fuerza de
la conexi´on. Las conexiones totales significan que todas las neuronas en una capa est´an
conectadas a todas las neuronas en la siguiente capa, mientras que las conexiones
parciales significan que solo algunas neuronas est´an conectadas. Adem´as, para
(de Boves Harrington et al., 2002) entre dos capas de neuronas diferentes existen
conexiones hacia delante, hacia atr´as, lateral y de retardo, ver figura 1.4:

Conexiones hacia delante (en ingl´es feedforward): la informaci´on fluye en una
direcci´on, desde la capa de entrada a la capa de salida. La capa de entrada recibe


-----

informaci´on, la procesa y la pasa a la siguiente capa hasta que llega a la capa de
salida.

Conexiones hacia atr´as (en ingl´es feedback): en esta estructura, la informaci´on fluye
en la direcci´on opuesta, desde la capa de salida a la capa de entrada. La capa de
salida produce un resultado, que luego se compara con la salida deseada, y el error
se propaga de vuelta a trav´es de la red para ajustar los pesos de las conexiones.

Conexiones laterales: en esta, la informaci´on fluye entre neuronas en la misma capa.
Esto permite el procesamiento de informaci´on en paralelo, lo que puede ser ´util para
tareas como el reconocimiento de patrones.

Conexiones retardadas: ac´a la informaci´on se almacena en una neurona durante un
cierto per´ıodo de tiempo antes de transmitirse a la siguiente neurona. Esto puede
ser ´util para tareas donde la red necesita recordar informaci´on espec´ıfica procesada
anteriormente.

Figura 1.4: Conexiones de una red neuronal. (Extra´ıdo de (de Boves Harrington et al.,
2002))

El n´umero de capas ocultas y el n´umero de neuronas en cada capa son factores
importantes para determinar adem´as el rendimiento de una ANN. En este sentido, han
sido estudiadas varias topolog´ıas de redes a partir de las conexiones de sus capas, como
es la red neuronal de alimentaci´on directa(FFN del ingl´es Feedforward neural network),
donde la informaci´on fluye en una sola direcci´on a trav´es de conexiones feedforward, a


-----

su vez se suele entrenar por medio del m´etodo backpropagation para obtener los pesos de
las conexiones internas durante el entrenamiento, de forma que calcula el error entre las
salidas predichas por la red y las salidas deseadas, y luego lo propaga hacia atr´as a trav´es
de la red para ajustar los pesos y minimizar el error, ver el esquema de funcionamiento de
una DNN en la figura 1.5 a continuaci´on. (Zhang et al., 2021)

Figura 1.5: Proceso de entrenamiento de una red neuronal. (Extra´ıdo de (Chollet, 2021))

En correlaci´on, un MLP, visto anteriormente en la figura 1.3 b), es un tipo de FFN que
tiene una o m´as capas ocultas, que constituye la arquitectura b´asica de las redes neuronales
profundas.

### 1.4. Aprendizaje Profundo

El aprendizaje profundo constituye una de las ´areas de investigaci´on m´as popular dentro
del campo de la IA, y es un subcampo dentro del aprendizaje autom´atico, que se utiliza


-----

para resolver problemas muy complejos que normalmente implican grandes cantidades
de datos. Se caracteriza, por su profundidad y por su capacidad para aprender las
representaciones de los datos. Utiliza distintas estructuras de redes neuronales para lograr
el aprendizaje de sucesivas capas de representaciones cada vez m´as significativas de los
datos. En un modelo en general se suelen utilizar decenas o incluso cientos de capas de
representaci´on las cuales aprenden autom´aticamente a medida que el modelo es
entrenado con los datos. (D´ıaz-Ram´ırez, 2021)
El surgimiento de esta ´area seg´un (Sarker, 2021) se debe a varios factores, en primer
lugar, los avances en el poder de c´omputo y el acceso a grandes conjuntos de datos, lo
que ha permitido entrenar redes en este subcampo de manera m´as eficiente. Adem´as, con
su aparici´on y evoluci´on se han logrado avances significativos en diferentes campos y un
rendimiento sobresaliente en tareas como el reconocimiento de im´agenes, el
procesamiento del lenguaje natural, la detecci´on de fraudes, la conducci´on aut´onoma, la
asistencia m´edica y la traducci´on autom´atica, entre otros.

#### 1.4.1. Redes Neuronales Profundas

Una red neuronal profunda( DNN, del ingl´es Deep Neural Network) es una RNA con
varias capas ocultas entre las capas de entrada y salida que pueden modelar relaciones
no lineales complejas. Se utilizan ampliamente en el aprendizaje supervisado y en los
problemas de aprendizaje por refuerzo. (D´ıaz-Ram´ırez, 2021)
Las m´ultiples capas ocultas presentes en las DNNs son las que les permiten aprender
caracter´ısticas y patrones m´as complejos de los datos. El t´ermino “profundo” se refiere al
n´umero de capas en la red, y la profundidad de la red es uno de los factores que contribuyen
a su rendimiento. En cuanto a las MLPs se consideran NN poco profundas en ocasiones,
cuando tienen una o dos capas ocultas solamente, mientras las DNN tienen mucho m´as de
dos capas ocultas como se ve en la figura 1.6. La decisi´on de utilizar un MLP o un DNN
depende de la complejidad de la tarea y de la cantidad de datos disponibles. Para tareas
m´as simples con conjuntos de datos m´as peque˜nos, un MLP puede ser suficiente y m´as
eficiente desde el punto de vista computacional. Sin embargo, para tareas m´as complejas
con conjuntos de datos m´as grandes, puede ser necesario una DNN para lograr un mejor
rendimiento aunque costoso computacionalmente. (Kriegeskorte and Golan, 2019)


-----

Figura 1.6: Representaci´on del aprendizaje profundo para un modelo de clasificaci´on de
d´ıgitos. (Extra´ıdo de (Chollet, 2021))

El esquema b´asico de su estructura cuenta con las siguientes capas, ver figura 1.7:

Capa de entrada: Se corresponde con el vector de datos de entrada. Si se dispone de
un vector x de datos, cada elemento del vector (x1,x2,...,xn) constituye una neurona
de entrada.

Capa de salida: Es la capa en la que se realiza la operaci´on objetivo, por ejemplo, la
clasificaci´on. En ese caso, la capa de salida tiene tantas neuronas como clases
presente el problema a tratar. Cada neurona tiene asociado un peso y un bias, en
espa˜nol conocido como sesgo, puede referirse a la tendencia de un modelo a
favorecer ciertos patrones sobre otros debido a la arquitectura o al proceso de
optimizaci´on.

Capas ocultas: Son las que contienen todos los c´alculos intermedios de la red. Est´an
formadas por neuronas ocultas, cada una de las cuales tiene un peso y un bias, al
igual que las neuronas de la capa de salida.


-----

Figura 1.7: Red neuronal profunda. (Extra´ıdo de (Kilpi, 2017))

#### 1.4.2. Redes Neuronales Profundas Convolucionales

Existen muchos ejemplos o tipos de redes neuronales profundas, y cada uno tiene sus
propias fortalezas y debilidades, que se adapta a diferentes tipos de tareas y datos. Las
redes neuronales convolucionales (CNNs del ingl´es Convolutional Neural Networks) son
un tipo de arquitectura de redes neuronales profundas que se inspira en el procesamiento
visual del cerebro humano. Los algoritmos tradicionales de aprendizaje no pudieron
extraer de manera efectiva caracter´ısticas significativas de las im´agenes, as´ı es que se
dise˜naron las CNN para superar esta limitaci´on mediante el AA de representaciones
jer´arquicas de datos de imagen, que pueden capturar caracter´ısticas de bajo y alto nivel.
La convoluci´on se refiere a la operaci´on matem´atica de aplicar un conjunto de filtros
(peque˜nas matrices de ponderaciones) que se aprenden durante el proceso de
entrenamiento, a la imagen de entrada, para producir un conjunto de mapas de
caracter´ısticas que capturan diferentes aspectos de la imagen de entrada. (Lanjewar and
Gurav, 2022; Gong et al., 2019)
El esquema b´asico de las CNN consta de varias capas que trabajan juntas para extraer
caracter´ısticas de las im´agenes de entrada y realizar la tarea. El siguiente es un desglose
de las capas en una CNN t´ıpica, y en la figura 1.8 se visualiza de forma resumida:

Capa de entrada: toma la imagen de entrada y la pasa a la siguiente capa.

Capa convolucional: la operaci´on de convoluci´on se realiza multiplicando los
valores de filtro por los valores de p´ıxel correspondientes en la imagen y sumando


-----

los resultados para producir un ´unico valor de salida. Este proceso se repite para
cada ubicaci´on en la imagen de entrada, produciendo un conjunto de mapas de
caracter´ısticas.

Capa de activaci´on: aplica una funci´on de activaci´on a la salida de la capa
convolucional como ReLu, para introducir no linealidad en el modelo.

Capa de agrupaci´on o submuestreo(en ingl´es pooling): reduce la resoluci´on de los
mapas de caracter´ısticas para reducir su dimensionalidad espacial al tiempo que
conserva la informaci´on m´as importante.

Capa oculta o completamente conectada (en ingl´es fully-connected): toma la salida
de la capa de agrupaci´on y la alimenta a una o m´as capas completamente conectadas,
que realizan la tarea especificada, donde la primera capa se encargar´a de convertir la
matriz de datos en un vector plano, es por ello que esta capa suele recibir el nombre
de capa plana (en ingl´es flatten).

Capa de abandono ( en ingl´es Dropout) es una m´ascara que anula la contribuci´on
de algunas neuronas hacia la siguiente capa y deja sin modificar todas las dem´as.
Podemos aplicar una capa Dropout al vector de entrada, en cuyo caso anula algunas
de sus caracter´ısticas; pero tambi´en podemos aplicarlo a una capa oculta, en cuyo
caso anula algunas neuronas ocultas.

Capa de salida: produce la salida final del modelo, que puede ser una distribuci´on
de probabilidad sobre las clases posibles en el caso de clasificaci´on de im´agenes.

Figura 1.8: Red neuronal convolucional. (Extra´ıdo de (Amador, 2023))

Una primera capa de convoluci´on aprender´a peque˜nos patrones locales, como bordes, una
segunda capa de convoluci´on aprender´a patrones m´as grandes hechos de las caracter´ısticas


-----

de las primeras capas, y as´ı sucesivamente. Esto permite a los CNN aprender de manera
eficiente conceptos visuales cada vez m´as complejos y abstractos (porque el mundo visual
es fundamentalmente jer´arquico espacialmente). Ver figura 1.9

Figura 1.9: El mundo visual forma una jerarqu´ıa espacial de lo visual m´odulos: los bordes
hiperlocales se combinan en objetos locales como ojos u orejas, que se combinan en
conceptos de alto nivel como “gato.” (Extra´ıdo de (Chollet, 2021))

Las capas de una CNN desglosadas anteriormente se pueden repetir varias veces para crear
una arquitectura de red m´as profunda. En la figura 1.10 puede apreciarse el esquema de
una CNN para el ejemplo de clasificaci´on de una imagen. La funci´on ReLu es la m´as
utilizada debido a que permite el aprendizaje muy r´apido en las RNA. Si a esta funci´on
se le da valores de entrada muy negativos el resultado es cero pero si se le da valores
positivos queda igual. La funci´on de activaci´on softmax transforma las salidas sin procesar
de la RNA en un vector de probabilidades, esencialmente una distribuci´on de probabilidad
sobre las clases de entrada. Considere un problema de clasificaci´on multiclase con n clases.
La activaci´on softmax devuelve un vector de salida que tiene n entradas, con la entrada en
el ´ındice i correspondiente a la probabilidad de que una entrada particular pertenezca a la
clase i, como se puede ver en la imagen a continuaci´on.


-----

Figura 1.10: Diagrama de capas de una red neuronal convolucional en la clasificaci´on de
im´agenes. (Extra´ıdo de (Modi, 2023))

La arquitectura de una CNN puede variar dependiendo del problema que se intenta
resolver y normalmente se optimiza mediante el uso de hiperpar´ametros, como el n´umero
de capas ocultas, el n´umero de neuronas en cada capa, la elecci´on de la funci´on de
activaci´on, la elecci´on del m´etodo de optimizaci´on y las t´ecnicas de regularizaci´on.
(Wang and Zhang, 2023; Gandikota, 2019)
Las CNN son similares a las redes MLP, su principal diferencia radica en la inclusi´on
de capas convolucionales, cuyas neuronas no est´an totalmente conectadas: cada neurona
de una capa no recibe conexiones entrantes de todas las neuronas de la capa anterior,
sino s´olo de algunas, lo cual favorece que cada neurona se especialice ´unicamente en una
regi´on de la capa anterior, reduciendo dr´asticamente el n´umero de operaciones a realizar.
De esta forma, las redes convolucionales dividen y modelan la informaci´on en partes m´as
peque˜nas, para combinar despu´es esta informaci´on en las capas m´as profundas de la red.
Ver figura 1.11 (Alzubaidi et al., 2021)


-----

Figura 1.11: Diagrama del proceso de convoluci´on.( Extra´ıdo de (Chollet, 2021))

Un modelo de DNN, transforma sus datos de entrada en resultados significativos, un
proceso que se “aprende” de la exposici´on a ejemplos conocidos de entradas y salidas.
Por lo tanto, para (Chollet, 2021) el problema central en el ML y el DL es transformar los
datos de manera significativa: en otras palabras, aprender representaciones ´utiles de los
datos de entrada disponibles, que nos acercan al resultado esperado. Una representaci´on,
en esencia, es una forma diferente de ver los datos: representarlos o codificarlos. Por
ejemplo, una imagen en color puede codificarse en el formato RGB (rojo-verde-azul)o en
el formato HSV( tono-saturaci´on-valor): estas son dos representaciones diferentes de los
mismos datos. Algunas tareas que pueden ser dif´ıciles con una representaci´on pueden
volverse f´aciles con otra. P or ejemplo, la tarea “seleccionar todos los p´ıxeles rojos en la


-----

imagen” es m´as simple en el formato RGB, mientras que “hacer que la imagen est´e
menos saturada” es m´as simple en el formato HSV. Los modelos de CNN tratan de
encontrar representaciones apropiadas para sus datos de entrada, transformaciones de los
datos que los hacen m´as susceptibles a la tarea en cuesti´on, como una tarea de
clasificaci´on.

#### 1.4.3. Modelos de redes convolucionales

Actualmente existen varios modelos que se pueden utilizar para la clasificaci´on de
im´agenes, cada uno con sus particularidades, de los cuales a continuaci´on se ejemplifica
uno de ellos.

**VGG** para (Zielinski et al., 2020) es un modelo que se introdujo en 2014 que consiste
en una serie de capas convolucionales seguidas de capas completamente conectadas,
dise˜nado para lograr una alta precisi´on en las tareas de clasificaci´on de im´agenes, aunque
es computacionalmente costoso debido a su gran cantidad de par´ametros. El modelo
VGG tiene 16 o 19 capas, dependiendo de la variante utilizada. VGG16 tiene 13 capas
convolucionales y 3 capas completamente conectadas, mientras que VGG19 tiene 16
capas convolucionales y 3 capas completamente conectadas. Ver diagrama del modelo en
la figura 1.12

Figura 1.12: Diagrama de capas de VGG19. Extra´ıdo de (Nguyen et al., 2022)

En general, los modelos existentes son una herramienta importante en la clasificaci´on de
im´agenes, ya que proporcionan un punto de partida para un entrenamiento eficiente, una
precisi´on y solidez mejorada. Un enfoque com´un y altamente efectivo para el DL en
peque˜nos conjuntos de datos de im´agenes es para usar una red previamente entrenada.
Una red pre-entrenada es una red guardada que se entren´o anteriormente en un conjunto
de datos grande, generalmente en una tarea de clasificaci´on de im´agenes a gran escala,
como son los modelos mencionados anteriormente. Si este conjunto de datos original es
lo suficientemente grande y general, entonces la jerarqu´ıa espacial de caracter´ısticas
aprendidas por la red puede actuar efectivamente como un modelo gen´erico del mundo


-----

visual y, por lo tanto, sus caracter´ısticas pueden resultar ´utiles para muchos problemas de
visi´on por computadora diferentes, aunque estos nuevos problemas puedan involucrar
clases completamente diferentes a las de la tarea original.

### 1.5. Inteligencia Artificial Explicable

A pesar que existen modelos interpretables como los ´arboles de decisi´on o los modelos
basados en reglas, existen otros como los mencionados anteriormente en el campo del DL,
que aunque alcanzan precisiones de predicci´on impresionantes, su estructura no lineal
anidada los hace altamente no transparentes, es decir, no est´a claro qu´e informaci´on en
los datos de entrada los hace llegar realmente a sus decisiones. Ver figura 1.13 Por lo
que, estos modelos se consideran t´ıpicamente como cajas negras(en ingl´es, black-boxes),
mientras que los modelos dise˜nados para ser interpretables son los de cajas blancas(en
ingl´es, white-boxes) (Samek et al., 2019)

Figura 1.13: Modelos de caja negra y modelos de caja blanca. (Extra´ıdo de (Badalia,
2021))

Para abordar este problema, los investigadores han desarrollado t´ecnicas para hacer que
los modelos de caja negra sean m´as interpretables y transparentes. Estas t´ecnicas se han
desarrollado en un ´area de investigaci´on propia, conocida como XAI. Para (Molnar,
2022) la XAI es un enfoque del ML que tiene como objetivo proporcionar informaci´on
sobre c´omo un modelo toma decisiones, haciendo que este proceso sea transparente e
interpretable, lo que puede ayudar a los usuarios a comprender y confiar en las
predicciones del modelo. Las t´ecnicas en la XAI incluyen m´etodos para visualizar el
proceso de toma de decisiones de los modelos, identificar caracter´ısticas o entradas


-----

importantes y generar explicaciones para las predicciones de los modelos. Adem´as se
pueden utilizar para identificar posibles sesgos o errores en un modelo, lo que puede
ayudar a mejorar la precisi´on y la imparcialidad de este.
La XAI es importante y la humanidad necesita de ella por varias razones seg´un (Samek
et al., 2019):

Verificaci´on del sistema: es necesario comprender el proceso de toma de decisiones
de un sistema de IA para garantizar su precisi´on y confiabilidad. Por ejemplo, en el
diagn´ostico m´edico, ser´ıa irresponsable confiar en las predicciones de un sistema de
caja negra por defecto. En cambio, cada decisi´on de gran alcance debe ser accesible
para una validaci´on adecuada por parte de un experto humano.

Mejora del sistema: comprender las debilidades de un sistema es el primer paso
para mejorarlo. Es m´as f´acil realizar este an´alisis de debilidades en modelos
interpretables que en modelos de caja negra. Adem´as, detectar sesgos en el modelo
o en el conjunto de datos es m´as f´acil si se entiende lo que el modelo est´a haciendo
y por qu´e llega a sus predicciones.

Aprendizaje del sistema: los sistemas de IA se entrenan con millones de ejemplos,
y pueden observar patrones en los datos que no son accesibles para los humanos. Al
utilizar sistemas de XAI, podemos intentar extraer este conocimiento destilado del
sistema para adquirir nuevos conocimientos.

Cumplimiento de la legislaci´on: las IAs est´an afectando cada vez m´as ´areas de
nuestra vida diaria, y los aspectos legales, como la asignaci´on de responsabilidad
cuando el sistema toma una decisi´on equivocada, han recibido recientemente una
mayor atenci´on. Dado que puede ser imposible encontrar respuestas satisfactorias
para estas preguntas legales cuando se depende de modelos de caja negra, los
futuros sistemas de IA necesariamente tendr´an que volverse m´as explicables.

En resumen, la XAI es importante para garantizar la precisi´on y confiabilidad de los
sistemas de IA, mejorarlos, aprender de ellos y sin dejar de lado la ´etica legal. Ver figura
1.14


-----

Figura 1.14: Definici´on de explicabilidad y propiedades relacionadas. (Extra´ıdo de (Zhou
et al., 2021))

#### 1.5.1. Explicabilidad

En la XAI se han propuesto diferentes tipos de explicabilidad basados en los enfoques de
generaci´on de explicaciones, ver figura 1.15 el tipo de explicaci´on, el alcance de la
explicaci´on, el tipo de modelo que puede explicar o combinaciones de estos m´etodos. Por
ejemplo, al considerar cu´ando son aplicables las explicaciones, los m´etodos de
explicaci´on se pueden agrupar en premodelo (ante-hoc), en modelo, y m´etodos
posteriores al modelo(post-hoc), los dos primeros se centran en la utilizaci´on de un
modelo, o en la incorporaci´on de algortimos al proceso de dise˜no o entrenamiento, que
sean intr´ınsecamente interpretables, es decir f´aciles de entender y explicar sin necesidad
de t´ecnicas adicionales, como los ´arboles de decisi´on. Mientras que la explicabilidad
post-hoc se refiere a la capacidad de explicar c´omo un modelo de ML tom´o una decisi´on
despu´es de que se haya entrenado y se haya utilizado para hacer predicciones.(Zhou
et al., 2021)


-----

Figura 1.15: Enfoques de los m´etodos de explicabilidad. (Extra´ıdo de (Zhou et al., 2021))

Tambi´en hay m´etodos espec´ıficos del modelo y agn´osticos o independientes del modelo,
as´ı como m´etodos de explicaci´on globales y locales como se ve en la figura 1.16. Para
(Molnar, 2019) las explicaciones globales buscan comprender el modelo en su conjunto,
identificando las variables m´as importantes y c´omo se relacionan entre s´ı, para determinar
toda la l´ogica de un modelo y el razonamiento detr´as de todos los resultados posibles.
Y por otro lado los m´etodos locales se centran en comprender el modelo en un punto de
datos espec´ıfico, identificando qu´e variables contribuyen a la predicci´on y c´omo afectan
los valores de esas variables a la predicci´on, para datos o rasgos espec´ıficos.

Figura 1.16: M´etodos de explicabilidad. (Extra´ıdo de (O’Sullivan, 2022))

Por lo que respecta a los m´etodos dependientes o no del modelo, en (Onose, 2023) los


-----

m´etodos dependientes son t´ecnicas de explicabilidad que se aplican a un modelo de IA
espec´ıfico, teniendo en cuenta su arquitectura y par´ametros. Proporcionan informaci´on
detallada sobre c´omo funciona un modelo en particular y est´an dise˜nados para ser
utilizados en el contexto de ese modelo espec´ıfico. Por el contrario, los agn´osticos se
pueden aplicar a cualquier modelo de IA, independientemente de su arquitectura o
par´ametros. Proporcionan informaci´on y no est´an vinculados a caracter´ısticas espec´ıficas
de un modelo en particular. En (Arya et al., 2019) se presentan numerosos ejemplos de
m´etodos existentes teniendo en cuenta entre otros enfoques las definiciones anteriores,
donde algunos de los m´as utilizados son:

**M´etodos espec´ıficos del modelo**

LRP: m´etodo basado en la propagaci´on hacia atr´as de la relevancia, que es una
t´ecnica que se utiliza para retroceder a trav´es de las capas de un modelo y asignar
relevancia a las caracter´ısticas de entrada.

Grad-CAM: m´etodo utilizado para visualizar las ´areas de una imagen que son m´as
importantes para la predicci´on del modelo. Este utiliza la informaci´on de gradiente
de una CNN para generar un mapa de calor que muestra las ´areas de la imagen que
son m´as importantes para la predicci´on del modelo.

DeepLIFT: m´etodo usado para asignar relevancia a las caracter´ısticas de entrada de
un modelo. Se basa en la idea de que la relevancia de un rasgo de entrada se puede
calcular comparando la activaci´on de este en una entrada con la activaci´on promedio
de la caracter´ıstica en todas las entradas.

**Ejemplos de m´etodos agn´osticos del modelo**

SHAP: es un m´etodo de explicaci´on local y post-hoc que asigna un valor de
importancia a cada caracter´ıstica en el modelo basado en su contribuci´on a la
predicci´on, se basa en la teor´ıa de Shapley (marco matem´atico para asignar la
contribuci´on de cada jugador en un juego cooperativo) y utiliza una aproximaci´on
de Monte Carlo para calcular la contribuci´on de cada caracter´ıstica en el modelo.

LIME: m´etodo de explicaci´on local y post-hoc que aproxima el modelo con un
modelo m´as simple e interpretable en la vecindad de la predicci´on perturbando las
caracter´ısticas de entrada y observando c´omo cambia la salida.

PDP: m´etodo de explicaci´on global y post-hoc que se utiliza para analizar la
relaci´on entre una variable de entrada y la salida del modelo, mientras se mantienen
constantes los valores de las dem´as variables de entrada. Esto lo logra mediante la
creaci´on de un gr´afico que muestra c´omo cambia la salida del modelo a medida que
se var´ıa el valor, lo que permite identificar patrones y tendencias en los datos.

Es importante tener en cuenta que diferentes tipos de explicaciones, pueden ser m´as
apropiados para diferentes tareas y contextos, y no existe un enfoque ´unico para la
explicabilidad en el aprendizaje autom´atico. Por lo tanto, es necesario evaluar y comparar


-----

diferentes m´etodos de explicaci´on para determinar cu´al es el m´as adecuado para una tarea
espec´ıfica.

#### 1.5.2. Herramientas actuales para la explicabilidad

En (Chollet, 2021) uno de los factores clave que impulsa el desarrollo del aprendizaje
profundo ha sido la democratizaci´on de los conjuntos de herramientas utilizados en el
campo, en los primeros tiempos para trabajar en esta ´area se requer´ıa una gran experiencia
en C++ y CUDA, que pocas personas pose´ıan. Hoy en d´ıa, las habilidades b´asicas de
scripting de Python son suficientes para realizar investigaciones avanzadas. Esto ha sido
impulsado principalmente por el desarrollo de Theano, luego TensorFlow y posteriormente
Pytorch, tres marcos simb´olicos de manipulaci´on de tensores para Python que admiten la
diferenciaci´on autom´atica, lo que simplifica enormemente la implementaci´on de nuevos
modelos, y por el surgimiento de bibliotecas f´aciles de usar como Scikit-learn y m´as tarde
Keras. Despu´es de los lanzamientos anteriores, entre otras herramientas, se ha logrado
que sea tan f´acil como manipular ladrillos LEGO, convirtiend´ose estas herramientas en la
soluci´on de aprendizaje profundo para grandes n´umero de nuevas empresas, estudiantes
de posgrado e investigadores que giran en el campo.
En correlaci´on a lo antes expuesto, existen herramientas que se pueden utilizar para
facilitar el trabajo a desarrolladores y dem´as personas vinculadas a este campo, tal cual se
explica en (Molnar, 2022; Onose, 2023; Amesoeder et al., 2023; Apley and Zhu, 2019;
Alber et al., 2019) como son las herramientas y bibliotecas mencionadas a continuaci´on:

LIME, es una biblioteca de python que proporciona explicaciones respecto a las
predicciones de cualquier clasificador aproxim´andolo localmente con un modelo
interpretable. Para usar este m´etodo, debe proporcionar una funci´on que pueda
predecir la salida para cualquier entrada dada, y una funci´on que pueda calcular la
distancia entre dos entradas cualesquiera. Ver documentaci´on e instalaci´on en
```
  https://pypi.org/project/lime/

```
SHAP, es una biblioteca de python que proporciona explicaciones, de forma que
calcula la contribuci´on de cada caracter´ıstica a la predicci´on de un modelo. Es
importante tener en cuenta que para obtener resultados significativos, los datos
deben limpiarse, procesarse previamente y estar listos para el modelado. Adem´as,
es una buena pr´actica evaluar el desempe˜no del modelo antes de interpretar los
resultados de las explicaciones. Ver m´as acerca de su instalaci´on y documentaci´on
[disponibles en https://shap.readthedocs.io/en/latest/](https://shap.readthedocs.io/en/latest/)

AIX360 (AI Explainability 360), es una biblioteca de c´odigo abierto de IBM para
python, para la interpretabilidad y la explicabilidad de conjuntos de datos y modelos
de ML. Incluye una colecci´on de algoritmos que cubren diferentes dimensiones de
explicaciones junto con m´etricas de explicabilidad. Ver acerca de su instalaci´on y
[documentaci´on en https://aix360.readthedocs.io/en/latest/](https://aix360.readthedocs.io/en/latest/)

Captum de Pytorch: es una biblioteca de c´odigo abierto de PyTorch para la
interpretaci´on de modelos que proporciona varios algoritmos y admite la mayor´ıa


-----

de los tipos de modelos de PyTorch con una modificaci´on m´ınima de la red
[neuronal. Ver documentaci´on disponible en https://captum.ai/](https://captum.ai/)

OmniXAI, es una biblioteca de python que ofrece XAI omnidireccional y
capacidades de ML interpretables para abordar muchos puntos d´ebiles al explicar
las decisiones tomadas por los modelos en la pr´actica. Proporciona una interfaz
f´acil de usar para realizar XAI. Esta pretende ser una biblioteca integral que facilite
la explicaci´on de la IA para los cient´ıficos de datos, investigadores de ML y
profesionales que necesitan explicaciones en su proyecto. La ´ultima versi´on
incluye un explicador GPT experimental. Este explicador aprovecha los resultados
producidos por SHARP y MACE para formular el mensaje de entrada para
ChatGPT. Posteriormente, ChatGPT analiza estos resultados y genera las
explicaciones correspondientes que proporcionan a los desarrolladores una
comprensi´on m´as clara de la justificaci´on detr´as de las predicciones del modelo.
Ver documentaci´on completa disponible en
`https://opensource.salesforce.com/OmniXAI/latest/index.html` o
```
https://pypi.org/project/omnixai/

```
DeepLIFT (Deep Learning Important FeaTures), es un paquete de Python que
profundiza en la selecci´on de caracter´ısticas de una red neuronal y encuentra
neuronas y pesos que tuvieron efectos importantes en la formaci´on de resultados.
[Ver documentaci´on disponible en https://pypi.org/project/deeplift/](https://pypi.org/project/deeplift/)

Skater, es un marco unificado de Python de c´odigo abierto e independiente del
modelo para la explicabilidad e interpretabilidad. Tiene tanto m´etodos globales
como locales. Ver m´as acerca en su documentaci´on disponible en
```
https://pypi.org/project/skater/

```
ELI5 (Explain Like I’m Five), es una biblioteca de Python que proporciona
funciones para visualizar y comprender las predicciones de varios tipos de
modelos, incluidos modelos lineales, ´arboles de decisi´on y modelos de caja negra
como Random Forest, XGBoost y redes neuronales. Ver acerca de su instalaci´on y
documentaci´on en
```
https://eli5.readthedocs.io/en/latest/overview.html

```
BreakDown, es una biblioteca de python para explicar las predicciones de los
modelos de aprendizaje autom´atico, particularmente en el contexto de los modelos
lineales. Proporciona explicaciones interpretables de las predicciones del modelo al
descomponer la predicci´on en las contribuciones de cada caracter´ıstica, de una
manera que los humanos puedan entender f´acilmente. Ver documentaci´on
[disponible en https://pypi.org/project/breakdown/](https://pypi.org/project/breakdown/)

Alibi, es una biblioteca de python de c´odigo abierto para inspecci´on e
interpretaci´on de modelos. Proporciona el c´odigo necesario para producir
explicaciones para algoritmos de caja negra. El objetivo de la biblioteca es
proporcionar implementaciones de alta calidad de m´etodos de explicaci´on de caja


-----

negra, caja blanca, locales y globales para modelos de clasificaci´on y regresi´on.
[Documentaci´on disponible en https://pypi.org/project/alibi/](https://pypi.org/project/alibi/)

iNNvestigate, es una herramienta para el lenguaje de programaci´on Python para
investigar las predicciones de las redes neuronales. Se basa en Keras y TensorFlow
2.0. Proporciona una implementaci´on lista para usar numerosos m´etodos de an´alisis.
[Ver m´as acerca de esta biblioteca, en su documentaci´on oficial disponible en https:](https://pypi.org/project/innvestigate/)
```
  //pypi.org/project/innvestigate/

```
Dalex, es un paquete de python que examina cualquier modelo dado, simple o
complejo, y explica el comportamiento del modelo. Crea un nivel de abstracci´on
alrededor de cada modelo que hace que sea m´as f´acil de explorar y explicar. Este
paquete hace una especie de “radiografia” cualquier modelo y ayuda a explorar y
explicar su comportamiento, para comprender c´omo funcionan los modelos
complejos. El objeto explicador principal crea un contenedor alrededor de un
modelo predictivo. Los modelos envueltos se pueden explorar y comparar con una
colecci´on de explicaciones a nivel de modelo y a nivel de predicci´on. Adem´as, hay
m´etodos de equidad y paneles de exploraci´on interactivos disponibles para el
usuario. Ver m´as acerca en su documentaci´on
```
  https://pypi.org/project/dalex/

```
InterpretML, es un conjunto de herramientas de c´odigo abierto desarrollado por
Microsoft, destinado a mejorar la explicabilidad del modelo, ofreciendo
explicaciones tanto globales como parciales. Es flexible y personalizable. Ver
[documentaci´on en https://interpret.ml/docs/index.html](https://interpret.ml/docs/index.html)

Anchors, es una biblioteca de Python para generar explicaciones interpretables por
humanos para las predicciones de modelos de aprendizaje autom´atico de caja negra.
Se basa en el concepto de “anclajes”, que son un conjunto de condiciones m´ınimas
y suficientes que un punto de datos debe satisfacer para ser clasificado como una
determinada clase por un modelo de caja negra. Los anclajes se pueden usar para
comprender por qu´e un modelo de caja negra realiz´o una predicci´on espec´ıfica para
un punto de datos dado. Tambi´en se pueden usar para identificar posibles problemas
[con el modelo, como sesgos o injusticias. Ver documentaci´on disponible en https:](https://pypi.org/project/anchors/)
```
  //pypi.org/project/anchors/

```
Existen varias formas de evaluar y medir la efectividad de una explicaci´on en el ´ambito
de la inteligencia artificial. Cada una de ellas se establece dentro de un entorno que
depende de la tarea, habilidades y expectativas del usuario del sistema de IA, siendo
estas, por lo tanto, dependientes del dominio. Algunos enfoques existentes en la
explicabilidad son el an´alisis de sensibilidad, la descomposici´on simple de Taylor y las
t´ecnicas de propagaci´on hacia atr´as (Samek et al., 2019; Molnar, 2022). Sin embargo, es
dif´ıcil determinar objetivamente si una t´ecnica es buena o no, para lo cual existen
estrategias de evaluaci´on de la calidad. Es importante destacar que la explicabilidad de
los modelos de IA es fundamental para comprender c´omo se toman las decisiones y para
detectar sesgos o errores en el proceso. Por lo tanto, es necesario seguir investigando y
desarrollando nuevas t´ecnicas y herramientas para mejorar la interpretaci´on de los


-----

modelos y garantizar su transparencia y responsabilidad en diferentes ´ambitos,
incluyendo el laboral y el p´ublico. (Cotino Hueso and Castellanos Claramunt, 2023)
A pesar de los avances en el campo de la explicabilidad en los modelos de inteligencia
artificial, todav´ıa existen desaf´ıos importantes que deben abordarse. En particular, a
medida que los modelos se vuelven cada vez m´as complejos, se vuelve m´as dif´ıcil
comprender c´omo toman decisiones, lo que genera preocupaciones sobre su confiabilidad
y usabilidad.

### 1.6. Conclusiones parciales

El avance de las investigaciones en el campo de aprendizaje autom´atico ha tenido gran
impacto en el desarrollo de algoritmos complejos y modelos que permiten a las m´aquinas
aprender y tomar decisiones basadas en los datos. Sin embargo, estos modelos a menudo
se consideran “cajas negras”, ya que su l´ogica interna y sus procesos de toma de decisiones
no son f´acilmente interpretables por los humanos.
La falta de profundidad y transparencia en los modelos puede ser problem´atica, por lo
que existe la necesidad de desarrollar m´etodos robustos y pr´acticos para explicar las
decisiones tomadas por estos. Los m´etodos de explicabilidad se han vuelto
fundamentales en el intento de determinar cu´ales variables contribuyen y c´omo afectan
sus valores a las predicciones.
En el caso de los modelos de clasificaci´on de im´agenes es igualmente necesario lograr
mejorar su interpretabilidad y es todo un desaf´ıo identificar cu´ales son los p´ıxeles
determinantes que contribuyen al modelo para realizar la predicci´on de la clase
resultante.


-----

# Cap´ıtulo 2


-----

# Cap´ıtulo 2

 Implementaci´on del nuevo m´etodo

En este cap´ıtulo se presentar´a el m´etodo dise˜nado para interpretar los resultados de
clasificaci´on de im´agenes tomando como ejemplo el modelo VGG19 y un conjunto de
datos seleccionado. Se explican los detalles de cada uno de los pasos de procesamiento
que componen el flujo y se describen los conceptos utilizados en cada etapa. Adem´as se
hace un an´alisis de las particularidades a tener en cuenta para el desarrollo de cada etapa,
as´ı como de los datos, la estructura de las clases y funciones utilizadas.

### 2.1. Descripci´on general del modelo

Se dise˜n´o una red en cascada compuesta por dos redes, siendo la primera la encargada
de la explicabilidad y la segunda el modelo escogido y entrenado para la clasificaci´on de
im´agenes que se desea explicar. El m´etodo de explicabilidad dise˜nado est´a constituido por
una primera red cuya implementaci´on y detalles se abordan en los pr´oximos apartados, y
una segunda red a partir de un modelo pre-entrenado para clasificar im´agenes, de forma
que su trabajo en conjunto est´a orientado al aprendizaje de los p´ıxeles relevantes para la
decisi´on tomada por este ´ultimo. A continuaci´on la figura 1.16 muestra el diagrama de
flujo de todo el proceso.

Figura 2.1: Diagrama de flujo


-----

Visi´on general de los pasos a seguir en la figura 2.2

Figura 2.2: Esquema de pasos a seguir

Gu´ıa de pasos del algoritmo propuesto:

1. Preparar conjunto de datos de entrada.

     - Preprocesar las im´agenes del conjunto seleccionado acorde a los datos que
acepta el clasificador escogido.

     - Dividir en conjuntos de entrenamiento, validaci´on y prueba.

     - Modificar capas de salida del clasificador de ser necesario, en dependencia de
la cantidad de clases que se desea predecir.

     - Entrenar el clasificador con las im´agenes preprocesadas, haciendo uso de la
t´ecnica de transferencia de aprendizaje (conocida en ingl´es como Transfer
Learning).

     - Evaluar todos los conjuntos y eliminar las im´agenes cuya predicci´on no fue
correcta, de esta forma se garantiza el aprendizaje del explicador sin sesgo.

     - Guardar los datos preparados, el cual es un paso opcional pero recomendable,
ya que los datos transformados y organizados que se almacenan, evitan la
preparaci´on en pruebas futuras.

2. Aplicar el m´etodo de explicabilidad a las im´agenes.

     - Pasar cada imagen a trav´es de las capas de la red implementada, y la salida
final ser´a la imagen original superpuesta a su mapa de relevancia[1], resultando una
imagen perturbada en dependencia de los pesos de cada p´ıxel[2].

     - Obtener el mapa de relevancia, es esencial para la explicaci´on, pero debido a
la l´ogica interna del m´etodo no es lo adquirido directamente en la salida de la red,

1El mapa de relevancia de una imagen se refiere a la representaci´on visual de los valores de los pesos de
sus p´ıxeles.
2Los pesos de los p´ıxeles se refieren a valores num´ericos asignados a cada p´ıxel que indican su
importancia o contribuci´on a la predicci´on, lo que significa que los p´ıxeles con pesos m´as altos tienen una
mayor influencia en la decisi´on final.


-----

por lo cual se define una funci´on que captura la salida por capas y guarda toda la
informaci´on de cada etapa significativa del procesamiento de la imagen a trav´es de
la red.

3. Aplicar el clasificador a las im´agenes perturbadas obtenidas en la salida anterior.

     - Utilizar el modelo entrenado para evaluar las im´agenes, congelando sus pesos
para que no se actualicen en el proceso de aprendizaje y a consecuencia de esto la
salida del clasificador influir´a solamente en los pesos del explicador y por tanto en
la interpretaci´on de este sobre la relevancia de los p´ıxeles para cada predicci´on.

#### 2.1.1. Arquitectura de la red y particularidades a tener en cuenta en cada capa

La arquitectura de la red est´a constituida por dos capas lineales adem´as de la de
perturbaci´on, como se muestra a continuaci´on en la figura 2.3

Figura 2.3: Diagrama de la arquitectura de la red

La imagen de entrada tiene una dimensi´on de 3x224x224, lo que significa que tiene 224
p´ıxeles de largo y de ancho, y 3 canales de color. Esta es la dimensi´on utilizada para los
casos de estudio espec´ıficos donde se utilice como modelo pre-entrenado VGG19, ya que
es la configuraci´on que espera este, debido a su entrenamiento y definici´on previa. Por
consiguiente, la capa de entrada de la red tendr´a tantas neuronas como p´ıxeles tenga la
imagen, recibir´a la imagen en su formato equivalente a un tensor[3] tridimensional y la
aplana a unidimensional para poder pasarla a la siguiente capa.

3Un tensor es una estructura de datos que generaliza conceptos como escalares, vectores y matrices a un
n´umero arbitrario de dimensiones.


-----

La primera capa lineal[4] tiene como entrada el tensor unidimensional, por tanto debe tener
tantas neuronas de entrada como resulte el tama˜no de este, y de salida las definidas, en
este caso son 1000. En el m´etodo forward[5] de la red, se le aplica a esta capa la funci´on de
_activaci´on[6]_ _ReLu[7]._
La segunda capa tiene como entrada la misma cantidad de neuronas que la salida de la
anterior, y de salida tantas neuronas como el tama˜no del tensor aplanado de la imagen.
En el forward se le aplica la funci´on Sigmoid[8], obteniendo los valores de probabilidades
asociados a las relevancias de los p´ıxeles para la clases determinadas.
A continuaci´on se perturba la imagen original a trav´es de la funci´on definida x _y, donde_
_∗_
**x es el vector que almacena los valores de los p´ıxeles de la imagen de entrada, guardado**
antes de pasar la imagen aplanada por las capas de la red, mientras y es el tensor de
probabilidades obtenidos en la ´ultima capa. Con este paso se espera lograr que en el tensor
resultante de la operaci´on, los p´ıxeles m´as relevantes tomen valores superiores a los dem´as
y cada vez sean m´as acertados a los que son importantes para la predicci´on del clasificador.
Al calcular los nuevos valores de los p´ıxeles, se llevan nuevamente a un tensor de
dimensi´on tridimensional para que la salida de la red sea la imagen perturbada con la
misma dimensi´on que la de entrada, la cual ser´a lo que reciba el clasificador, este
evaluar´a su entrada y devolver´a una salida correspondiente a la predicci´on. Es entonces
que la red hace el Backpropagation, actualizando los pesos del explicador seg´un los
resultados de la evaluaci´on del modelo entrenado, mientras dicho modelo mantiene sus
pesos congelados ya que s´olo se necesita su evaluaci´on no su entrenamiento nuevamente.
Importante aclarar que para que as´ı sea, al definir el optimizador, solo se le debe pasar los
par´ametros de la primera red.

### 2.2. Implementaci´on

Para la implementaci´on del m´etodo se utilizaron las bibliotecas de python Pytorch con
varios de sus m´odulos, MatplotLib, Numpy, tqdm y google.colab.drive como parte de las
bibliotecas preinstalades de Google Colab, ya que como entorno de ejecuci´on se utiliza la
GPU T4 que ofrece en su versi´on gratuita limitada. Ver figura 2.4

4La capa lineal o completamente conectada(fc del ingl´es fully-connected), es una capa que se encuentra
entre la entrada y la salida de la red donde cada neurona est´a conectada a todas las neuronas de la capa
anterior.
5El m´etodo forward de una RNA se utiliza para realizar la propagaci´on hacia adelante de los datos a
trav´es de la red
6Una funci´on de activaci´on es una funci´on matem´atica que se aplica a la salida de las neuronas en una
capa de una RNA, a la cual permite modelar relaciones no lineales en los datos
7ReLu: funci´on de activaci´on definida como f (x) = m´ax(0, _x)_
8Sigmoid: funci´on de activaci´on definida como f (x) = 1+1e[−][x][, produciendo una salida en el rango entre]

0 y 1


-----

Figura 2.4: Diagrama de bibliotecas y dependencias utilizadas

A continuaci´on, se muestra el c´odigo de partes esenciales de la implementaci´on: las clases
donde se definen las redes 2.5, las funciones definidas para visualizar 2.6 y guardar los
resultados 2.7.


-----

Figura 2.5: Clases de las redes implementadas

Donde ExplainerNetwork es la red que aprende a interpretar los resultados del clasificador
entrenado y guardado Classifier Network. Ambas redes instanciadas son las que recibe
como par´ametros CombinedNetwork, la cual enlaza la salida del explicador como entrada
del clasificador y ser´a la que posteriormente se entrena para obtener las explicaciones
deseadas.

Figura 2.6: Funci´on para visualizar las im´agenes y su informaci´on


-----

Figura 2.7: Funci´on para salvar los resultados luego de entrenado el modelo

#### 2.2.1. An´alisis de la complejidad computacional

La complejidad computacional se refiere a cu´antos recursos computacionales, como
tiempo y memoria, consume un algoritmo en relaci´on con el tama˜no de la entrada. A
continuaci´on se analiza la complejidad computacional en cada parte del algoritmo y se
especifica su expresi´on en notaci´on O:

1. Preparar conjunto de datos de entrada: O(n)

     - Depender´a del costo de preprocesamiento de las im´agenes y de la divisi´on en
conjuntos de entrenamiento, validaci´on y prueba.

      - Si el preprocesamiento de im´agenes es lineal con respecto al n´umero de p´ıxeles
y la divisi´on del conjunto es tambi´en lineal, la complejidad total podr´ıa considerarse
lineal, expres´andose como O(n), donde n es el n´umero de p´ıxeles o tama˜no de la
imagen.

2. Aplicar el m´etodo de explicabilidad a las im´agenes: O(n)+ _O(m_ _n)+_ _O(r_ _k)_
_∗_ _∗_


-----

     - Estar´a dada principalmente del tama˜no de la red y el costo de pasar las
im´agenes a trav´es de esta. Dado que la red explicadora es relativamente peque˜na, la
complejidad de pasar las im´agenes a trav´es de esta podr´ıa considerarse lineal con
respecto al n´umero de p´ıxeles. Por tanto ser´ıa una complejidad O(n).

     - Sin embargo, si la red pre-entrenada es compleja(por ejemplo, VGG19) y/o
las im´agenes son grandes, la complejidad ser´a significativa. En este caso, se puede
expresar la complejidad como O(m _n), donde m es la complejidad de la red pre-_
_∗_
entrenada.

     - Dado que los pesos del modelo est´an congelados y no se realiza un
entrenamiento completo, la complejidad deber´ıa ser relativamente eficiente.

     - Adem´as, es importante considerar el impacto de las operaciones repetitivas y
c´omo afectan a la complejidad total. Esto podr´ıa expresarse por ejemplo para el
entrenamiento como O(r _k), donde r es el n´umero de repeticiones y k la_
_∗_
complejidad asociada con las operaciones dentro del ciclo de entrenamiento.

Si a estos pasos se suma guardar los resultados, la complejidad aumenta a´un m´as, ya que
estar´a dada por un ciclo a lo largo del conjunto de datos y por cada posici´on de este,
se eval´ua la imagen a trav´es de las capas del modelo y se guardan tres im´agenes con su
respectiva informaci´on. Esta complejidad puede expresarse como O(d _p), donde d es el_
_∗_
tama˜no del conjunto de im´agenes y p la complejidad asociada las operaciones dentro del
ciclo de guardar.
Finalmente, al resumir la complejidad total a partir de las obtenidas anteriormente resulta:
_O(n) + O(n) + O(m_ _n) + O(r_ _k) + O(d_ _p) Es posible simplificar esto sumando las_
_∗_ _∗_ _∗_
complejidades lineales y agrupando t´erminos similares a: O(n + m _n + r_ _k + d_ _p) En_
_∗_ _∗_ _∗_
esta expresi´on cada t´ermino est´a relacionado con: n, el tama˜no de las im´agenes.
_m_ _n, la complejidad de la red preentrenada._
_∗_
_r_ _k, las operaciones repetitivas durante el entrenamiento._
_∗_
_d_ _p, el ciclo de guardar resultados._
_∗_

### 2.3. Alcance y limitaciones del m´etodo propuesto

El m´etodo propuesto se considera un m´etodo dependiente del modelo, ya que necesita
adherirse a un modelo entrenado espec´ıfico para aprender a partir de sus predicciones,
por lo que aprende de im´agenes con las transformaciones requeridas por este modelo en
particular, de las etiquetas de su salida y sus pesos.
El enfoque de este puede caracterizarse por pertenecer al de mapas de saliencia y por
proporcionar explicaciones locales, ya que se centra en la interpretaci´on de la importancia
de cada p´ıxel buscando los rasgos que m´as influyeron en una predicci´on particular.
La implementaci´on del m´etodo, explicada anteriormente tiene particularidades que se
pueden variar en futuras pruebas, pero en este caso se utiliza todo acorde al modelo
pre-entrenado VGG19 y al subconjunto de datos del conjunto Food-101. De igual forma,
otros detalles como algunos hiperpar´ametros es posible que se encuentren combinaciones
que mejoren los resultados tras una b´usqueda exhaustiva de estos, proceso conocido
como grid search.


-----

Dado que la investigaci´on se encuentra en la etapa de obtenci´on de los primeros resultados
experimentales, a partir de estos y de todo el trayecto del desarrollo, pueden resumirse
algunas limitaciones que posteriormente se deben estudiar en b´usqueda de la posibilidad
de erradicarlas:

Sensibilidad al conjunto de datos: dado que aprender a perturbar im´agenes
espec´ıficas del conjunto de datos de entrenamiento, podr´ıa volver al modelo
sensible a las caracter´ısticas y patrones ´unicos de ese conjunto. Esto podr´ıa limitar
su generalizaci´on a otros conjuntos de datos.

Se requieren recursos computacionales significativos para el entrenamiento de forma
´optima y la inferencia.

### 2.4. Diferencias con respecto a los enfoques actuales

Los enfoques actuales comunes fueron mencionados en el cap´ıtulo anterior, cada m´etodo
en dependencia de su tipo tiene formas espec´ıficas de proceder, sin embargo, podr´ıa
generalizarse en que se basan fundamentalmente en el c´alculo a trav´es del uso de
funciones matem´aticas, teor´ıas de juegos, aproximaciones, variaciones de par´ametros.
En contraste con estos enfoques actuales, el m´etodo propuesto trae a la vida una idea
diferente y es el uso de redes neuronales para explicar las decisiones de la red entrenada
para clasificar im´agenes. Ciertamente la t´ecnica de perturbaci´on de los p´ıxeles para
determinar como afecta este proceso a la salida no es nuevo, al igual que los enfoques
utilizados en la definici´on de la red, pero s´ı lo constituye el hecho de ense˜nar a una red a
perturbar ella misma la imagen bas´andose en los pesos de sus p´ıxeles.

### 2.5. Conclusiones parciales

Se desarroll´o el nuevo m´etodo nombrado como VXN(del ingl´es Vision’s eXplainer
Network), local y espec´ıfico del modelo, para interpretar los resultados de la clasificaci´on
de im´agenes utilizando las facilidades que brinda Pytorch para todo lo relacionado a
redes neuronales. Adem´as se utilizaron otras bibliotecas auxiliares de Python como
Matplotlib, Imageio, ´utiles para la visualizaci´on y el manejo de las im´agenes
respectivamente.
Se implementaron las redes y funciones necesarias para el preprocesamiento,
entrenamiento, entre otros procesos que se realizan en este caso adaptados al modelo
VGG19 entrenado en el conjunto de datos escogido. Sin embargo, es f´acil de adaptar a
otros casos, implementando un c´odigo semejante, cambiando adecuadamente la descarga
del conjunto de datos o el modelo pre-entrenado.
VXN constituye un nuevo enfoque de explicaci´on, sensible a los datos y tiene un costo
computacional alto.


-----

# Cap´ıtulo 3


-----

# Cap´ıtulo 3

 Evaluaci´on del m´etodo propuesto en los casos de estudio

En este cap´ıtulo se describen detalladamente los resultados de evaluar el m´etodo a partir
de los tres casos de estudios definidos, desglosando sus especificaciones y revelando los
matices de la toma de decisiones en escenarios diversos. La esencia de la investigaci´on se
manifiesta en la capacidad de comprender y explicar el proceso subyacente que gu´ıa la
toma de decisiones del modelo entrenado VGG19. A trav´es de la visualizaci´on detallada
de este proceso, se busca arrojar luz sobre la opacidad inherente de los modelos de
clasificaci´on de im´agenes como el escogido.

### 3.1. Descripci´on del conjunto de datos de entrada

Se seleccion´o el conjunto de datos “Food101” disponible en la biblioteca torch.datasets,
conocido por su diversidad y complejidad en la clasificaci´on de alimentos. Este se
compone de im´agenes de alimentos recopiladas de la web y se ha utilizado ampliamente
en la investigaci´on de reconocimiento de alimentos. Consta de 101 clases distintas, cada
una de ellas cuenta con 750 im´agenes para entrenamiento y 250 im´agenes para pruebas,
todas revisadas manualmente, conformando un total de 101 000 im´agenes variadas. desde
platos gourmet hasta aperitivos cotidianos, presentando desaf´ıos significativos para los
modelos de clasificaci´on.
La resoluci´on de las im´agenes en este conjunto es de 512x512 p´ıxeles y su organizaci´on
sigue una estructura de carpetas, donde cada carpeta representa una clase espec´ıfica de
alimento, esta estructura facilita la carga y el procesamiento del conjunto de datos
mediante herramientas como torchvision.datasets. Ver documentaci´on para obtener
detalles precisos y actualizados disponible en
```
https://pytorch.org/vision/stable/datasets.html#food101.

```
Para adaptar el m´etodo de explicabilidad a escenarios m´as espec´ıficos, optamos por
seleccionar subconjuntos particulares de Food101 en tres casos de estudio distintos. Esta
estrategia permite explorar la capacidad del modelo para proporcionar explicaciones
claras y comprensibles en contextos m´as restringidos. Este proceso no solo simplifica la
tarea de clasificaci´on, sino que tambi´en introduce variaciones de complejidad para


-----

evaluar la robustez y adaptabilidad del m´etodo.

### 3.2. Transformaciones

Previo a la formaci´on de cada conjunto de datos de los casos de estudio, se aplican
transformaciones fundamentales para preparar las im´agenes y se realizan ajustes
espec´ıficos en la configuraci´on de la capa de salida de VGG19. Este proceso de
preparaci´on es esencial para garantizar resultados fiables y coherentes durante la
evaluaci´on y explicabilidad del modelo. Antes de la formaci´on de cada conjunto de datos,
las im´agenes son sometidas a un proceso de transformaci´on uniforme. La transformaci´on
incluye:

Redimensionamiento a 256x256 p´ıxeles: Para establecer un tama˜no base que
permitiera una futura centralizaci´on y recorte.

Recorte al centro, a 224x224 p´ıxeles: Establecimiento del tama˜no final que VGG19
acepta como entrada est´andar.

Conversi´on a Tensores: Las im´agenes fueron convertidas en tensores para facilitar
su procesamiento por modelos de aprendizaje profundo.

Estas transformaciones aseguran que todas las im´agenes est´en normalizadas y ajustadas
al formato requerido por VGG19, prepar´andolas para la evaluaci´on y el proceso de
explicabilidad.
Para cada caso de estudio, el conjunto de datos se divide en tres partes: entrenamiento,
validaci´on y prueba. Adem´as, se llevan a cabo las siguientes configuraciones espec´ıficas:

1. Se aplica la transformaci´on definida a todas las im´agenes, esta se realiza solamente
para el primer caso de estudio, ya que el resto utiliza un subconjunto de estas ya
transformadas.

2. Se configura VGG19 para clasificar el n´umero determinado de clases.

3. Se entrena el modelo para guardarlo y poder cargarlo posteriormente para los
diferentes n´umeros de clases definidos.

4. Se evaluan las im´agenes y se crean nuevas carpetas excluyendo las mal clasificadas.
Estas im´agenes filtradas se guardan y se utilizan como base para los casos de estudio
del m´etodo propuesto.

Esta estrategia garantiza la generalizaci´on y reutilizaci´on de las im´agenes filtradas para el
entrenamiento del modelo orientado a la explicabilidad de la clasificaci´on, evitando sesgo
y optimizando el proceso de evaluaci´on y explicaci´on del modelo.
En general, para el entrenamiento del modelo propuesto con los datos mencionados
anteriormente se hicieron pruebas experimentales utilizando dos variantes de


-----

optimizadores SGB[1] y Adam[2], obteniendo mejores resultados con la primera opci´on. Para
ver mejor la definici´on de optimizadores en pytorch es posible consultar la
documentaci´on oficial disponible en
```
https://pytorch.org/docs/stable/optim.html.

```
Por otro lado se define como funci´on de p´erdida CrossEntropyLoss(), utilizada
anteriormente en el modelo pre-entrenado, ya que es una funci´on empleada com´unmente
en problemas de clasificaci´on con m´ultiples clases, calcula la p´erdida de entrop´ıa cruzada
entre las salidas y las etiquetas de entrada, para m´as informaci´on consultar
documentaci´on disponible en `https:`
```
//pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html.

### 3.3. Caso de estudio 1

```
La selecci´on de clases para este caso de estudio se realiza a partir de las 10 clases mejor
clasificadas en t´erminos de rendimiento del modelo entrenado. Esta selecci´on inicial
proporciona una visi´on detallada de c´omo se aborda la clasificaci´on en un subconjunto de
clases de mejor rendimiento, puede ser que estas tengan caracter´ısticas distintivas,
patrones visuales ´unicos o simplemente sean m´as f´acilmente distinguibles para VGG19
en comparaci´on con otras clases, ofreciendo un punto de partida s´olido para la
explicabilidad del modelo.

Tama˜no del conjunto de entrenamiento: 5912

Tama˜no del conjunto de validaci´on: 1976

Tama˜no del conjunto de prueba: 1958

Para definir cada DataLoader[3] de cada conjunto se utilizan los par´ametros:

_batch size[4]: 32_

_num workers[5]: 2_

Para el entrenamiento el valor del n´umero de ´epocas se var´ıa en un rango de 4 a 16,
observ´andose que los valores m´as altos no mejoraban significativamente los resultados,
en algunos casos se lograba lo contrario, y aumentaba considerablemente el tiempo de
ejecuci´on, por lo cual se determina apropiado utilizar 5. Durante el proceso de

1SGD (Stochastic Gradient Descent): Este optimizador actualiza los par´ametros del modelo en la
direcci´on opuesta al gradiente de la funci´on de p´erdida con respecto a los par´ametros.
2Adam: Este optimizador combina las ventajas del m´etodo de SGB con momentum y el m´etodo de
RMSProp. Adam adapta la tasa de aprendizaje para cada par´ametro de forma adaptativa, lo que puede llevar
a una convergencia m´as r´apida y a una mejor generalizaci´on.
3Un DataLoader en PyTorch es una clase que representa un iterable de Python sobre un conjunto de
datos. Este combina un conjunto y un muestreador, y proporciona un iterable que proporciona acceso f´acil a
las muestras, ya que se puede configurar para cargar datos en lotes y reordenar el conjunto de datos
4batch size se refiere al n´umero de muestras que se utilizan en cada iteraci´on durante el proceso
determinado
5num workers determina cu´antos subprocesos se utilizar´an para cargar los datos en paralelo


-----

aprendizaje, se guarda el valor de la p´erdida promedio(Loss) por ´epoca(epoch), para
observar el progreso en este caso de estudio. Ver gr´afico 3.1

Figura 3.1: Gr´afico de la p´erdida promedio por ´epoca durante el entrenamiento del caso
de estudio 1

Para evaluar el modelo reci´en entrenado y paralelamente guardar los datos se utiliza la
funci´on save definida. A partir de esto, se puede acceder entonces a cualquier imagen del
conjunto de datos evaluado para poder saber su predicci´on, mapa de relevancia y la
imagen perturbada. Luego de esto, es de suma importancia la funci´on show images, para
visualizar los resultados mostrando ejemplos a partir de los resultados guardados. A
continuaci´on en la figura 3.2 y 3.3 se muestran dos de ellos.


-----

Figura 3.2: Visualizaci´on del ejemplo 1

Figura 3.3: Visualizaci´on del ejemplo 2

### 3.4. Caso de estudio 2

Para este caso de estudio se reducee a´un m´as el conjunto de im´agenes seleccionando
aleatoriamente un subconjunto de 5 clases de alimentos a partir de las 10 mejor
clasificadas del caso anterior. Este enfoque busca entrenar y evaluar la capacidad del
modelo para proporcionar explicaciones en contextos m´as limitados con respecto a las
evaluaciones realizadas.

Tama˜no del conjunto de entrenamiento: 2951

Tama˜no del conjunto de validaci´on: 986

Tama˜no del conjunto de prueba: 942


-----

Para definir cada DataLoader en este caso se utilizan los par´ametros:

batch size: 32

num workers: 2

Para el entrenamiento en este caso de estudio se utilizan 8 ´epocas y la p´erdida promedio
por ´epoca se puede ver en la figura 3.4

Figura 3.4: Gr´afico de la p´erdida promedio por ´epoca durante el entrenamiento del caso
de estudio 2

Posteriormente, al guardar los resultados y visualizar se obtiene informaci´on como la que
se muestra a continuaci´on en el siguiente ejemplo.


-----

Figura 3.5: Visualizaci´on del ejemplo 1

### 3.5. Caso de estudio 3

En el ´ultimo caso de estudio, nuevamente se selecciona aleatoriamente, esta vez un
subconjunto de solo 2 clases de alimentos de las 10 mejor clasificadas. Esta
configuraci´on espec´ıfica brinda la oportunidad de evaluar el m´etodo en un escenario de
clasificaci´on de im´agenes m´ınimo. Adem´as este enfoque consume una cantidad menor de
recursos, facilitando la realizaci´on de pruebas adicionales y ajustes de par´ametros con
tiempos de ejecuci´on m´as r´apidos.

Tama˜no del conjunto de entrenamiento: 755

Tama˜no del conjunto de validaci´on: 766

Tama˜no del conjunto de prueba: 400

En este caso de estudio, manteniendo num workers del DataLoader = 2, se hicieron
variaciones en la definici´on de la funci´on de perturbaci´on, el tama˜no del batch, en la
cantidad de neuronas de salida de la segunda capa del modelo, y como anteriormente, en
la cantidad de ´epocas, haciendo posible visualizar a continuaci´on algunos de estos
resultados para analizar la existencia o no de cambios significativos entre ellos. Se
muestra en un primer lugar la l´ınea de progreso del entrenamiento a trav´es del an´alisis de
la p´erdida promedio por cada ´epoca, se especifican en la parte inferior las variaciones
realizadas para el caso espec´ıfico y seguido de esto, la imagen a trav´es de las diferentes
etapas del m´etodo: entrada, confecci´on del mapa de relevancia y perturbaci´on. Ver figuras
3.6, 3.7, 3.8, 3.9 y 3.10.


-----

Figura 3.6: Ejemplo 1

Figura 3.7: Ejemplo 2

Figura 3.8: Ejemplo 3


-----

Figura 3.9: Ejemplo 4

Figura 3.10: Ejemplo 5

La cantidad de ´epocas a lo largo de los experimentos en diferentes casos, no ha mostrado
mejoras relevantes al aumentarla en el rango posible, por lo cual por una cuesti´on de
recursos se ajusta a 4. Cada ejemplo que se muestra corresponde a los resultados a partir
de los cambios especificados.
El hecho de que no exista una marcada diferencia entre los resultados, traza la posibilidad
que todos sean v´alidos y se deba profundizar en futuras investigaciones para restringir los
escenarios de prueba lo mejor posible.

### 3.6. Comparaci´on de los casos de estudio

Cada caso de estudio se dise˜n´o de manera ´unica, introduciendo variaciones en t´erminos
de duraci´on de entrenamiento, tama˜no de lote (batch size), funciones de perturbaci´on y
configuraci´on de la red neuronal. Todos los resultados mostraron una interpretaci´on de
los mapas de relevancia con cierta falta de detalle, pero que marcan un punto de partida
en el desarrollo de la investigaci´on del m´etodo propuesto, ya que se encuentra en su etapa
experimental. La diferencia entre las visualizaciones de los casos 1 y 2 no fue
significativamente notable y la imagen perturbada se aprecia como la original pero con
un tono m´as oscuro, lo que da a entender que se perturban algunos p´ıxeles aislados
bajando su intensidad en la mayor´ıa. En el tercer caso resultaron im´agenes perturbadas


-----

m´as detalladas y unos colores m´as acentuados en los mapas de relevancia. Esto inclina la
investigaci´on a que es posible obtener mejores resultados con la reducci´on del conjunto
de entrada a una menor cantidad de clases a predecir, un aumento del n´umero de
neuronas en la segunda capa lineal del modelo y al utilizar un tama˜no de lote peque˜no.
Aunque los resultados no mostraron una diferencia marcada entre los casos de estudio, es
importante destacar que todos los escenarios pueden considerarse v´alidos. La falta de
divergencia significativa podr´ıa sugerir la robustez del m´etodo ante diversas
configuraciones. No obstante, se reconoce la necesidad de futuras investigaciones para
refinar los escenarios de prueba y profundizar en la comprensi´on de las interacciones
entre los par´ametros del modelo, cada funci´on de perturbaci´on y la interpretaci´on de la
explicabilidad.

### 3.7. Conclusiones parciales

Se exploraron los resultados obtenidos al evaluar el m´etodo a trav´es de tres casos de
estudio distintos y de la visualizaci´on detallada de este proceso, lo cual ha buscado
arrojar luz sobre la opacidad inherente de los modelos de clasificaci´on.
Las transformaciones aplicadas a las im´agenes, junto con las configuraciones espec´ıficas
para cada caso de estudio, fueron esenciales para preparar los datos y garantizar resultados
fiables y coherentes durante la evaluaci´on y explicabilidad del modelo.
Se observ´o cierta consistencia en la interpretaci´on de los mapas de relevancia, es decir,
aunque con falta de detalle en la mayor´ıa de los casos, se puede caracterizar como un
primer avance ya que el modelo aprende y confecciona un mapa de relevancia que no
es nulo. La diferencia m´as notoria se encontr´o en el tercer caso de estudio, donde las
im´agenes perturbadas mostraron un nivel de detalle superior y colores m´as acentuados en
los mapas de relevancia.
La comparaci´on entre los casos de estudio revel´o que, la reducci´on del conjunto de entrada
a un menor n´umero de clases y el ajuste de ciertos par´ametros del modelo parecen tener
un impacto positivo en la calidad de las explicaciones proporcionadas.


-----

# Conclusiones


-----

# Conclusiones

En el ´ambito de la Inteligencia Artificial, la comprensi´on de los modelos de caja negra es
esencial para garantizar transparencia y confiabilidad en su desempe˜no.
Tradicionalmente, los m´etodos de evaluaci´on de la calidad de estos modelos han sido
limitados, siendo insuficientes para revelar plenamente su funcionamiento interno.
Reconociendo esta carencia, se propuso un enfoque innovador que busca mejorar la
interpretabilidad y comprensi´on de estos modelos para el caso de la clasificaci´on de
im´agenes.

Se desarroll´o un nuevo m´etodo local y dependiente del modelo para interpretar la
clasificaci´on de im´agenes: VXN. Este constituye un nuevo enfoque de explicaci´on
basado en redes neuronales, sensible a los datos y con un alto costo computacional

Se implement´o una red en cascada que comunica el m´etodo propuesto con el
modelo entrenado VGG19 de forma que el aprendizaje est´a orientado a los p´ıxeles
que fueron relevantes para la predicci´on hecha por el modelo. La implementaci´on
desarrollada incluy´o funciones necesarias para el preprocesamiento,
entrenamiento, entre otros procesos que se realizan en este caso adaptados al
modelo entrenado con las facilidades de Pytorch, pero f´acil de adaptar a otros casos

Como resultado de la evaluaci´on del m´etodo se obtienen resultados adecuados
siendo mejores donde se utiliz´o el conjunto de datos perteneciente a dos clases y se
determin´o que el ajuste de ciertos par´ametros del modelo como el n´umero de
neuronas de salida y el tama˜no del batch parecen tener un impacto positivo en la
calidad de las explicaciones proporcionadas.


-----

# Recomendaciones

Realizar una b´usqueda de hiperpar´ametros para mejorar el entrenamiento de la red
explicadora.

A partir de la b´usqueda hiperpar´ametros, evaluar los efectos de las diferentes
funciones definidas en los casos de estudio conformados: x _y, x + (x_ 1 _y),_
_∗_ _∗_ _−_
_x_ _y[2], x_ (1 + _y_ 0.7)[2].
_∗_ _∗_ _−_

Evaluar los efectos de aplicar una transformaci´on a las im´agenes que les realce el
brillo y el contraste.

Aplicar el m´etodo de explicaci´on para otros modelos de clasificaci´on de im´agenes.


-----

### Referencias

Aha, D. W. and Kibler, D. (1991). Lazy Learning. Kluwer Academic Publishers.

Alber, M., Lapuschkin, S., Seegerer, P., H¨agele, M., Sch¨utt, K. T., Montavon, G., Samek,
W., M¨uller, K.-R., D¨ahne, S., and Kindermans, P.-J. (2019). innvestigate neural
networks! Journal of Machine Learning Research, 20(93):1–8.

Alzubaidi, L., Zhang, J., Humaidi, A. J., Al-Dujaili, A., Duan, Y., Al-Shamma, O.,
Santamar´ıa, J., Fadhel, M. A., and Al-Amidie, M. (2021). Review of deep learning:
concepts, cnn architectures, challenges, applications, future directions. Journal of Big
_Data, 8(1):53._

Amador, R. (2023). Extensi´on de la biblioteca innvestigate con m´etodos para evaluar la
calidad de sus explicaciones. Universidad Central “Marta Abreu´´ de Las Villas, Cuba.

Amesoeder, C., Hartig, F., and Pichler, M. (2023). cito: An r package for training neural
networks using torch.

Anwar, A. (2019). Difference between alexnet, vggnet, resnet, and inception.
_Towards Data Science._ [Disponible en: https://towardsdatascience.com/](https://towardsdatascience.com/the-w3h-of-alexnet-vggnet-resnet-and-inception-7baaaecccc96)
```
 the-w3h-of-alexnet-vggnet-resnet-and-inception-7baaaecccc96.

```
Apley, D. W. and Zhu, J. (2019). Visualizing the effects of predictor variables in black
box supervised learning models.

Arya, V., Bellamy, R. K. E., Chen, P.-Y., Dhurandhar, A., Hind, M., Hoffman, S. C.,
Houde, S., Liao, Q. V., Luss, R., Mojsilovi´c, A., et al. (2019). One explanation
does not fit all: A toolkit and taxonomy of ai explainability techniques. arXiv preprint
_arXiv:1909.03012._

Badalia, S. (2021). Model interpretability: Demystifying black-box models.
Acuity Knowledge Partners. [Available at https://www.ncbi.nlm.nih.gov/pmc/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9343258/)
```
 articles/PMC9343258/.

```
Barber, D. (2012). Bayesian Reasoning and Machine Learning. Cambridge University
Press.

Basogain Olabe, X. (2003). Redes Neuronales Artificiales y sus aplicaciones. Servicio
Editorial de la Universidad del Pa´ıs Vasco.

Bishop, C. M. (2006). Pattern Recognition and Machine Learning. Springer.

Carvalho, D. V., Marques Pereira, E., and Cardoso, J. S. (2019). Machine learning
interpretability: A survey on methods and metrics. Electronics.

Chollet, F. (2021). Deep Learning with Python. Manning Publications, Shelter Island,
NY, 2nd edition.


-----

Cotino Hueso, L. and Castellanos Claramunt, J. (2023). Transparencia y explicabilidad
_de la inteligencia artificial. Editorial Tirant, Valencia._

de Boves Harrington, P., Wan, C., and Clippinger (2002). Applied to artificial neural
networks : What has my neural network actually learned.

Dietterich, T. G., Maass, W., Simon, H. U., and Warmuth, M. K. (2008). Theory and praxis
of machine learning. Semantic Scholar.

D´ıaz-Ram´ırez, J. (2021). Aprendizaje autom´atico y aprendizaje profundo. _Ingeniare._
_Revista chilena de ingenier´ıa, pages 180–181._

Gandikota, R. (2019). Understanding convolutional neural networks. Machine Learning.

Gong, Z., Zhong, P., Yu, Y., Hu, W., and Li, S. (2019). A cnn with multiscale convolution
and diversified metric for hyperspectral image classification. IEEE Transactions on
_Geoscience and Remote Sensing, 57:3599–3618._

Grieve, P. (2023). Deep learning vs. machine learning: What’s the difference? Zendesk
_Blog._

Haykin, S. (2009). Neural Networks and Learning Machines. Pearson Education.

Kilpi, E. (2017). Neural networks as the architecture of human work. Springer.

Kriegeskorte, N. and Golan, T. (2019). Neural network models and deep learning. Current
_Biology, 29(7):R231–R236._

Lanjewar, M. G. and Gurav, O. L. (2022). Convolutional neural networks based
classifications of soil images. Multimedia Tools and Applications, 81:10313 – 10336.

Le, J. (2018). The 4 convolutional neural network models that can classify your fashion
[images. Towards Data Science. Disponible en: https://towardsdatascience.com/](https://towardsdatascience.com/the-4-convolutional-neural-network-models-that-can-classify-your-fashion-images-9fe7f3e5399d)
```
 the-4-convolutional-neural-network-models-that-can-classify-your-fashion-images

```
Lusim, L. and Marchesano, P. (2023). Inteligencia artificial explicable: tecnolog´ıa y
transparencia para la industria 4.0. Universidad ORT Uruguay.

Manjarrez, L. (2014). Relaciones neuronales para determinar la atenuaci´on del valor de la
aceleraci´on m´axima en superficie de sitios en roca para zonas de subducci´on. Master’s
thesis, The University of Arizona.

[Modi, P. (2023). Convolutional neural networks for dummies. https://towardsai.](https://towardsai.net/p/deep-learning/convolutional-neural-networks-for-dummies)
```
 net/p/deep-learning/convolutional-neural-networks-for-dummies.

```
Molnar, C. (2019). Interpretable Machine Learning. Leanpub, Canada.

Molnar, C. (2022). Interpretable Machine Learning. Leanpub, 2 edition.

Montavon, G., Samek, W., and M¨uller, K.-R. (2018). Methods for interpreting and
understanding deep neural networks. digital signal processing. Elsevier Inc., 73.


-----

Moreno, A. N. (2020). Introducci´on a las Redes Neuronales aplicadas al Aprendizaje
Supervisado. Hackers and Developers™Press.

Nguyen, T.-H., Nguyen, T.-N., and Ngo, B.-V. (2022). A vgg-19 model with
transfer learning and image segmentation for classification of tomato leaf disease.
_AgriEngineering, 4(4):871–887._

Ongsulee, P. (2017). Artificial intelligence, machine learning and deep learning. IEEE.

Onose, E. (2023). Explainability and auditability in ml: Definitions, techniques,
and tools. _Electronics._ Disponible en: `https://neptune.ai/blog/`
```
 explainability-auditability-ml-definitions-techniques-tools.

```
O’Sullivan, C. (2022). What are model agnostic methods? Towards Data Science.

Ram´ırez V´eliz, R. B., L. S. S. C. . G. B. J. M. (2022). El humano y la m´aquina: perspectivas
sobre inteligencia artificial, agentes y sistemas inteligentes. RECIAMUC, 6(3).

Russell, S. and Norving, P. (2020). Artificial Intelligence: A Modern Approach. Prentice
Hall.

Samek, W., Montavon, G., Lapuschkin, S., Anders, C. J., and M¨uller, K.-R. (2021).
Explaining deep neural networks and beyond: A review of methods and applications.
_IEEE._

Samek, W., Wiegand, T., and Muller, K.-R. (2019). _Explainable AI: Interpreting,_
_Explaining and Visualizing Deep Learning, volume 11700 of Lecture Notes in_
_Computer Science. Springer._

Sarker, I. H. (2021). _Machine Learning: Algorithms, Real-World Applications and_
_Research Directions. Springer, New York, NY._

Sekhar, A., B. S. H. R. S. A. K. M. A. and Yang, L. (2022). Brain tumor classification
using fine-tuned googlenet features and machine learning algorithms. IEEE journal of
_biomedical and health informatics, 26(3):983 – 991._

Tan, C., Sun, F., Kong, T., Zhang, W., Yang, C., and Liu, C. (2018). A survey on deep
transfer learning.

Tan, P.-N., Steinbach, M., and Kumar, V. (2005). Introduction to Data Mining. Pearson
Education.

Taye, M. M. (2023). Understanding of machine learning with deep learning: Architectures,
workflow, applications and future directions. Computers, 12(5).

Wang, Y., Wang, Y., and Chen, Y. (2021). Eeg functional connectivity analysis based on
neural network and granger causality. Journal of Ambient Intelligence and Humanized
_Computing, 12(7):6935–6946._


-----

Wang, Y. and Zhang, H. (2023). Identification of winter wheat pests and diseases based
on improved convolutional neural network. BMC Bioinformatics.

Xu, Y., Liu, X., Cao, X., Huang, C., Liu, E., Qian, S., Liu, X., Wu, Y., Dong, F., Qiu, C.W., Qiu, J., Hua, K., Su, W., Wu, J., Xu, H., Han, Y., Fu, C., Yin, Z., Liu, M., Roepman,
R., Dietmann, S., Virta, M., Kengara, F., Zhang, Z., Zhang, L., Zhao, T., Dai, J., Yang,
J., Lan, L., Luo, M., Liu, Z., An, T., Zhang, B., He, X., Cong, S., Liu, X., Zhang, W.,
Lewis, J. P., Tiedje, J. M., Wang, Q., An, Z., Wang, F., Zhang, L., Huang, T., Lu, C.,
Cai, Z., Wang, F., and Zhang, J. (2021). Artificial intelligence: A powerful paradigm
for scientific research. The Innovation, 2(4):100179.

Zhang, D. J., Li, K., Chen, Y., Wang, Y., Chandra, S., Qiao, Y., Liu, L., and Shou, M. Z.
(2021). Morphmlp: A self-attention free, mlp-like backbone for image and video. ArXiv,
abs/2111.12527.

Zhang, X., Chen, M., Zhang, Z., and Lu, S. (2022). A texture detail-oriented generative
adversarial network: motion deblurring for multi-textured images. Applied Intelligence,
53.

Zhang, Y. and Zhang, J. (2019). A neural network-based phishing website detection
method. IEEE Access, 7:102653–102663.

Zhou, J., Gandomi, A. H., Chen, F., and Holzinger, A. (2021). Evaluating the quality
of machine learning explanations: A survey on methods and metrics. _Electronics,_
10(5):593.

Zhou, Q. and Purvis, M. K. (2004). A market-based rule learning system. In Australasian
_Computer Science Week._

Zielinski, P., Krishnan, S., and Chatterjee, S. (2020). Weak and strong gradient directions:
Explaining memorization, generalization, and hardness of examples at scale. arXiv:
_Learning._


-----

