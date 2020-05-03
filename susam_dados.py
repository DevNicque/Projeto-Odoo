import requests
from json import dump

# requests.get(<url>, auth = (<usuário>, <senha>), verify=False)
'''
    requests.get(<url>, auth = (<usuário>, <senha>), verify=False)
    
    O parâmetro "verify" determina se a segurança ssl deve ser verificada ou não. Colocar como False caso a URL destino não seja https.
    O parâmetro "auth" deve ser usado caso a url necessite de um login.

    OBS: Após realizar a requisição GET para a url especificada, você deve manipular a resposta da requisição para adquirir os dados.

'''

url = "https://detin.saude.am.gov.br:9300/agfa_consumo_medicamentos_e_produtos"
login = ('petronilo', '123456')

response = requests.get(url, auth = login, verify=False)

data = response.json() # Eu já sei que a resposta da requisição irá me retornar um JSON (O python interpreta já como um dicionário), então eu posso navegar pelas chaves normalmente. NEM SEMPRE É O CASO.

#print(data["agfa_consumo_medicamentos_e_produtos"])

def create_json_file(name = "susam_dados", dicio = {}):
    # Função simples para criar um arquivo com extensão .json a partir de um dicionário.
    with open(name + ".json", "w+") as f:
        dump(dicio, f)

create_json_file(dicio = data)
