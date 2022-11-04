import requests
def get_cep(qualCep):
    if len(qualCep) != 8:
        print('CEP INVÁLIDO. Digitos insuficientes')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['cep']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"
        #print(f"{qualCep}: CEP INVÁLIDO!")

def get_Bairro(qualCep):
    if len(qualCep) != 8:
        print('CEP INVÁLIDO. Digitos insuficientes')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['bairro']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"

def get_logradouro(qualCep):
    if len(qualCep) != 8:
        print('CEP INVÁLIDO. Digitos insuficientes')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['logradouro']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"

def get_localidade(qualCep):
    if len(qualCep) != 8:
        print('CEP INVÁLIDO. Digitos insuficientes')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['localidade']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"

def get_uf(qualCep):
    if len(qualCep) != 8:
        print('CEP INVÁLIDO. Digitos insuficientes')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['uf']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"

def get_ddd(qualCep):
    if len(qualCep) != 8:
        print('CEP INVÁLIDO. Digitos insuficientes')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"{endereco['ddd']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"

