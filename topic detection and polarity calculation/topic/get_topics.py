import requests
import json
import pandas


texts = [
    'independientemente del diseño horrible y poco o nada intuitivo, es muy muy incomodo estar cambiando de transfermovil a la aplicacion de mensajes cada vez q quieres hacer algo. el proceso para agregar tarjetas es engorroso, no puedes agregar la tarjeta de otra persona (tu esposa, por ejemplo) y solo te permite 2 tarjetas por cuenta. por otra parte, alguien puede explicarme paraque necesitas una tarjeta matriz? enzona funcionaba perfectamemte sin ella, pero la gente anormal se dejaba estafar, incluso despues de estar alertados. solucion de enzona, utilizar tambien la inutil tarjeta matriz, permitirte agregar solo las tarjetas tuyas y complicarlo todo aun mas. enzona era seguro, los inseguros eran los usuarios.',
    'Una excelente aplicación mis felicitaciones a los creadores de esta herramienta tecnológica tan útil para el pueblo. Con ella se pueden realizar desde casa muchos pagos de servicios que evitan colas y malestar. Ojalá que se continúe mejorando y ampliando.',
    '¿Alguien sabe cuándo estará disponible el monedero móvil,  anunciado en marzo del año pasado???? Según se comunicó sería una prestación que formaria parte, "en breve" de la plataforma TRANSFERMOVIL. Dicha operación quedó respaldada en la Resolución 116/2021, publicada en Gaceta Oficial. A los meses se modificó la resolución pero hasta ahí.\nLe hice la pregunta a una funcionaría de ETECSA en Twitter y su respuesta de paso fue "manténgase al tanto de nuestras noticias"... En serio????'
]

topics = json.loads(requests.post('http://127.0.0.1:5000/get_topics',json={"documents":texts}).text)
df_topics = pandas.DataFrame([[text,idx] for idx,topic in enumerate(topics) for text in topic])
df_topics.columns = 'Mensaje', 'Tópico'
df_topics.to_csv('topicos.csv',index = False)