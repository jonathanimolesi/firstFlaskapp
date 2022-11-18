from flask import Flask, render_template, url_for, request
import requests
import codigoCep

def get_cotacao(moeda='dolar'):
    requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,GBP-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    if moeda == 'dolar':
        cotacao_dolar = requisicao_dic['USDBRL']['bid']
        texto = f'{cotacao_dolar}'
        return texto
    elif moeda == 'euro':
        cotacao_euro = requisicao_dic['EURBRL']['bid']
        texto = f'{cotacao_euro}'
        return texto
    elif moeda == 'libra':
        cotacao_gbp = requisicao_dic['GBPBRL']['bid']
        texto = f'{cotacao_gbp}'
        return texto
    elif moeda == 'bitcoin':
        cotacao_btc = requisicao_dic['BTCBRL']['bid']
        texto = f'{cotacao_btc}'
        return texto

def get_cep(qualCep):
    if len(qualCep) != 8:
        print('CEP INVÁLIDO. Digitos insuficientes')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{qualCep}/json/')
    endereco = request.json()
    if 'erro' not in endereco:
        return f"CEP: {endereco['cep']} | Logradouro: {endereco['logradouro']} "
    else:
        return f"{qualCep}: CEP INVÁLIDO!"
        #print(f"{qualCep}: CEP INVÁLIDO!")

app = Flask(__name__)

libra = get_cotacao(moeda='libra')
dolar = get_cotacao(moeda='dolar')
euro = get_cotacao(moeda='euro')
bitcoin = get_cotacao(moeda='bitcoin')

meucep = get_cep('38400290')
pesquisandoCep = ['38400290']


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/index")
def retorno():
    return render_template("index.html")

@app.route("/cotacao")
def cotacao():
    return render_template("cotacao.html", libra=libra, dolar=dolar, euro=euro, bitcoin=bitcoin)

@app.route("/cep")
def cep():
    return render_template("cep.html", cep=meucep)


@app.route("/cepResultado")
def cepResultado():
    return render_template("cepResultado.html", consultarCep=consultarCep)

@app.route("/pesquisar", methods=['POST',])
def pesquisar():
    nome = request.form['nome']
    if '-' in nome:
        nome = nome.replace('-','')
    pesquisandoCep[0] = nome
    consultarCep = codigoCep.get_cep(pesquisandoCep[0])
    consultarBairro = codigoCep.get_Bairro(pesquisandoCep[0])
    consultarLogradouro = codigoCep.get_logradouro(pesquisandoCep[0])
    consultarLocalidade = codigoCep.get_localidade(pesquisandoCep[0])
    consultarUf = codigoCep.get_uf(pesquisandoCep[0])
    consultarDdd = codigoCep.get_ddd(pesquisandoCep[0])
    return render_template('cepResultado.html', consultarCep=consultarCep, consultarBairro=consultarBairro, consultarLogradouro=consultarLogradouro, consultarLocalidade=consultarLocalidade, consultarUf=consultarUf, consultarDdd=consultarDdd )

# colocando o site no ar
if __name__ == "__main__":
    app.run(debug=True)