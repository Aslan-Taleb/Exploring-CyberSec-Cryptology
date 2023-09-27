import re

# L'URL de service
url = "legoogle://12312:80/squeezie"

# Expression régulière
expression = r'(?P<service>[\w-]+)://(?P<adresse_machine>[\w.-]+):(?P<numéro_de_port>\d+)/(?P<adresse_document>.+)'

# Recherche des correspondances
match = re.match(expression, url)

if match:
    service = match.group('service')
    adresse_machine = match.group('adresse_machine')
    numéro_de_port = match.group('numéro_de_port')
    adresse_document = match.group('adresse_document')

    print("Service:", service)
    print("Adresse de la machine:", adresse_machine)
    print("Numéro de port:", numéro_de_port)
    print("Adresse du document:", adresse_document)
else:
    print("Aucune correspondance trouvée.")
