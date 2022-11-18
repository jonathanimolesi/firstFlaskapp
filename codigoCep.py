import requests
def get_cep(qualCep):
    numeros = qualCep.isnumeric()
    if len(qualCep) != 8 or numeros == False:
        return f"{qualCep}: CEP INVÁLIDO!"


    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['cep']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"
        #print(f"{qualCep}: CEP INVÁLIDO!")

def get_Bairro(qualCep):
    numeros = qualCep.isnumeric()
    if len(qualCep) != 8 or numeros == False:
        return f"{qualCep}: CEP INVÁLIDO!"

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['bairro']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"

def get_logradouro(qualCep):
    numeros = qualCep.isnumeric()
    if len(qualCep) != 8 or numeros == False:
        return f"{qualCep}: CEP INVÁLIDO!"

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['logradouro']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"

def get_localidade(qualCep):
    numeros = qualCep.isnumeric()
    if len(qualCep) != 8 or numeros == False:
        return f"{qualCep}: CEP INVÁLIDO!"

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['localidade']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"

def get_uf(qualCep):
    numeros = qualCep.isnumeric()
    if len(qualCep) != 8 or numeros == False:
        return f"{qualCep}: CEP INVÁLIDO!"

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['uf']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"

def get_ddd(qualCep):
    numeros = qualCep.isnumeric()
    if len(qualCep) != 8 or numeros == False:
        return f"{qualCep}: CEP INVÁLIDO!"

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['ddd']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"