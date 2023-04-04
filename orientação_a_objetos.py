import re

class ExtratorURL:
    def __init__(self, url):
        self.url = url
        self.validacao_url()

    def sanitizacao_url(self, url):
        if (type(url) == str):
            return url.strip()
        else:
            return ""

    def validacao_url(self):
        if not self.url: #Aplica um bool(self.url) - quando for uma string vazia, vai retornar not false = true
            raise ValueError("A url está vazia")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        busca_padrao = padrao_url.match(self.url)
        if not busca_padrao:
            raise ValueError("A URL é inválida")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def extraindo_valores(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if (indice_e_comercial == -1):
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def conversor(self):
        valor_dolar = 5.50
        valor_quantidade = int(url.extraindo_valores("quantidade"))
        convercao = valor_quantidade/valor_dolar
        return convercao

    def __len__(self):
        return len(self.url)

    def __str__(self): # Essa é a função chamada quando damos print no objeto, sendo assim podemos determinar o valor a ser impresso
        return self.url + "\n" + "Base url: " + self.get_url_base() + "\n" + "Parâmetros url: " + self.get_url_parametros()

    def __eq__(self, other):
        return self.url == other.url

url = ExtratorURL("bytebank.com/cambio?quantidade=200&moedaOrigem=real&moedaDestino=dolar")
url2 = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")

print("***Imprimindo informações da minha URL***")
print("O tamanho da minha url é: {}".format(len(url)))
print("A url é: {}".format(url))

print()

print("***Alguns estudos sobre as funcções especiais dos objetos e a comparação entre '==' e 'is', analisando a id dos objetos***")
print(url == url2)
print(id(url))
print(id(url2))

print()

print("***Imprimindo a quantida de moedas de origem e o valor após a conversão***")
valor_quantidade = url.extraindo_valores("quantidade")
print("O valor na moeda original é de: {} reais".format(valor_quantidade))
valor_convertido = url.conversor()
print("O valor da conversão é: {} Dólares".format(valor_convertido))

