# API Twilio com SDK do Python.


[![Tests](https://github.com/twilio/twilio-python/actions/workflows/test-and-deploy.yml/badge.svg)](https://github.com/twilio/twilio-python/actions/workflows/test-and-deploy.yml)
[![PyPI](https://img.shields.io/pypi/v/twilio.svg)](https://pypi.python.org/pypi/twilio)
[![PyPI](https://img.shields.io/pypi/pyversions/twilio.svg)](https://pypi.python.org/pypi/twilio)
[![Learn OSS Contribution in TwilioQuest](https://img.shields.io/static/v1?label=TwilioQuest&message=Learn%20to%20contribute%21&color=F22F46&labelColor=1f243c&style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAASFBMVEUAAAAZGRkcHBwjIyMoKCgAAABgYGBoaGiAgICMjIyzs7PJycnMzMzNzc3UoBfd3d3m5ubqrhfrMEDu7u739/f4vSb/3AD///9tbdyEAAAABXRSTlMAAAAAAMJrBrEAAAKoSURBVHgB7ZrRcuI6EESdyxXGYoNFvMD//+l2bSszRgyUYpFAsXOeiJGmj4NkuWx1Qeh+Ekl9DgEXOBwOx+Px5xyQhDykfgq4wG63MxxaR4ddIkg6Ul3g84vCIcjPBA5gmUMeXESrlukuoK33+33uID8TWeLAdOWsKpJYzwVMB7bOzYSGOciyUlXSn0/ABXTosJ1M1SbypZ4O4MbZuIDMU02PMbauhhHMHXbmebmALIiEbbbbbUrpF1gwE9kFfRNAJaP+FQEXCCTGyJ4ngDrjOFo3jEL5JdqjF/pueR4cCeCGgAtwmuRS6gDwaRiGvu+DMFwSBLTE3+jF8JyuV1okPZ+AC4hDFhCHyHQjdjPHUKFDlHSJkHQXMB3KpSwXNGJPcwwTdZiXlRN0gSp0zpWxNtM0beYE0nRH6QIbO7rawwXaBYz0j78gxjokDuv12gVeUuBD0MDi0OQCLvDaAho4juP1Q/jkAncXqIcCfd+7gAu4QLMACCLxpRsSuQh0igu0C9Svhi7weAGZg50L3IE3cai4IfkNZAC8dfdhsUD3CgKBVC9JE5ABAFzg4QL/taYPAAWrHdYcgfLaIgAXWJ7OV38n1LEF8tt2TH29E+QAoDoO5Ve/LtCQDmKM9kPbvCEBApK+IXzbcSJ0cIGF6e8gpcRhUDogWZ8JnaWjPXc/fNnBBUKRngiHgTUSivSzDRDgHZQOLvBQgf8rRt+VdBUUhwkU6VpJ+xcOwQUqZr+mR0kvBUgv6cB4+37hQAkXqE8PwGisGhJtN4xAHMzrsgvI7rccXqSvKh6jltGlrOHA3Xk1At3LC4QiPdX9/0ndHpGVvTjR4bZA1ypAKgVcwE5vx74ulwIugDt8e/X7JgfkucBMIAr26ndnB4UCLnDOqvteQsHlgX9N4A+c4cW3DXSPbwAAAABJRU5ErkJggg==)](https://twil.io/learn-open-source)

## Documentação
Esse código usa a API do Twilio e a biblioteca requests para baixar todas as gravações telefônicas disponíveis na conta Twilio do usuário. Ele começa importando as bibliotecas necessárias e definindo as credenciais da conta Twilio.

Em seguida, o código cria um objeto "cliente" usando a _classe Client_ da biblioteca Twilio e chama o método list para obter uma lista de todas as gravações disponíveis na conta.

O código percorre a lista de gravações e para cada gravação, o código usa a URL (media_url) para baixar o arquivo de áudio em formato MP3 usando a biblioteca requests. O nome do arquivo de saída é o SID da gravação concatenado com a extensão ".mp3".

Além disso, o código adiciona uma verificação para criar uma pasta com o nome da data de criação da gravação e salva cada arquivo dentro da sua respectiva pasta. Para isso, ele utiliza a função strftime para converter a data de criação da gravação em uma string com o formato "ddMMyyyy". Se a pasta ainda não existe, o código cria uma nova usando o nome da pasta obtido a partir da data de criação.

Por fim, o código imprime uma mensagem indicando que o arquivo foi salvo com sucesso.

## Versão

Usado nesse procedimento a versão do Python 3.11

## As versões suportadas:
Versões suportadas nessa biblioteca de acordo com a [documentação](https://pypi.org/project/twilio/)

Python 3.7
Python 3.8
Python 3.9
Python 3.10
Python 3.11


## Intalação

```shell
pip3 install twilio
```
by: Eliezer Machado
