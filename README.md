
# Open Price Oil -> Web Scrapy

<a href = "https://links.geneva.com/invite/257b1817-fa14-4e25-8229-1ac613f7f9b5">
<div align="center"><img src="https://user-images.githubusercontent.com/17861240/131836901-f06d4214-6cdd-4195-b0f3-fa6ef139799b.png" /></div>
</a>


## Sobre
Este repositório tem como foco oferecer uma aplicação que faz o web scraping em um site dependendo das tratativas do dado que você quer consumir. Mas essa aplicação em si ela irá fazer o scrapy do preço do petróleo diariamente em Angola dos principais poços

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre](#Sobre)
   * [Pré-requisitos](#pre-requisitos)
   * [Rodando via Python](#rodando-via-python)
   * [Resultado](#resultado)
   * [Tecnologias](#tecnologias)
   * [Autor](#autor)
<!--te-->

<h4 align="center"> 
	✅  Python Select 🚀 Finalizado  ✅
</h4>

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com) (obrigatório), [anaconda3](https://nodejs.org/en/) (obrigatório). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/) ou o [jupyterlab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)

```bash
# Clone este repositório
$ git clone <https://github.com/mlussati/open-data-web-scrapy.git>
# Acesse a pasta do projeto no terminal/cmd
$ cd open-data-web-scrapy
# cria a pasta data
$ sudo mkdir data
# Crie uma env
$ conda create -n web-scrapy-env python=3.7.7
$ conda activate web-scrapy-env
# Instale as dependências que está no arquivo requirements.txt
$ pip install -r requirements.txt
```
### Rodando via Python
```bash
# Dentro da pasta open-data-web-scrapy execute o seguinte comando:
$ python get_price_oil.py
```
### Resultado
```bash
# Para consultar o resultado do dado coletado tem que acessar a pasta data e lá terá os arquivos gerados em formato csv
$ cd data
```

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Anaconda3](https://www.anaconda.com/)
- [Jupyterlab](https://jupyter.org/)
- [Python](https://www.docker.com/)

### Autor
---
 <sub><b>Palanca Data</b></sub></a>🚀</a>


Feito por Palanca Data👋🏽 Entre em contato!

[Geneva](https://links.geneva.com/invite/257b1817-fa14-4e25-8229-1ac613f7f9b5)
