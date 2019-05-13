import requests

# Documentazione modulo: http://it.python-requests.org/it/latest/

###############################################################################
###############################################################################

# Una richiesta di tipo GET verso la homepage di Google
response = requests.get("https://www.google.it")

# Verifichiamo il Codice di Stato
print("Status Code: ", response.status_code)

# Scorciatoia messa a disposizione dal modulo per verificare se la risposta è
# andata a buon fine (status code < 400)
if response.ok:
    print("Tutto ok!")
else:
    print("Qualcosa è andato storto...")

###############################################################################
###############################################################################

# Qualora venga ricevuto del contenuto, questo può essere visionato in maniera
# diversa a seconda del tipo di contenuto in se

# Contenuto della risposta in tipo Bytes
print(response.content)
print(type(response.content))

# Contenuto della risposta in tipo String
print(response.text)
print(type(response.text))

# Quanto sappiamo che riceveremo un JSON, possiamo usare json()
print(response.json())

###############################################################################
###############################################################################

# Possiamo visionare gli headers nel messaggio di risposta per ottenere
# informazioni utili come ad esempio il tipo di contenuto ricevuto:
print("Content-Type: ", response.headers['Content-Type'])

# E in generale tutti gli header che fanno parte del messaggio di risposta:
print("Headers: ", response.headers)

###############################################################################
###############################################################################
