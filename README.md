# desafio-python
# Integração Supabase + Z-API com Python

Projeto simples para enviar mensagens de WhatsApp utilizando a Z-API e dados armazenados no Supabase.

## Funcionalidades

* Conexão com o Supabase
* Leitura de dados da tabela `pessoas`
* Envio automático de mensagens pelo WhatsApp usando a Z-API
* Uso de variáveis de ambiente através do arquivo `.env`

## Tecnologias Utilizadas

* Python 3
* Supabase
* Z-API
* Requests
* Python Dotenv

## Instalação

Clone o repositório:

git clone https://github.com/Guilhermoviski/desafio-python
cd desafio-python


Crie um ambiente virtual:

python -m venv venv

Ative o ambiente virtual:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

## Arquivo .env

Crie um arquivo `.env` na raiz do projeto:

SUPABASE_URL=sua_url_supabase
SUPABASE_KEY=sua_chave_supabase

ZAPI_ID=seu_id_instancia
ZAPI_TOKEN=seu_token_instancia
ZAPI_CLIENTE_TOKEN=seu_client_token

## Estrutura da Tabela

Tabela: `pessoas`

| Campo       | Tipo |
| ----------- | ---- |
| nome_pessoa | text |
| telefone    | text |

Exemplo:

| nome_pessoa | telefone      |
| ----------- | ------------- |
| João        | 5561999999999 |
| Maria       | 5561988888888 |

ou cole no supabase

create TABLE pessoas (
  id_pessoa integer generated always as identity PRIMARY KEY,
  nome_pessoa varchar(100) NOT NULL
  telefone text NOT NULL
);

apos isso você deve popular a tabela, usando: 

insert into pessoas (nome_pessoa, telefone) values 
('nome da pessoa', 'telefone da pessoa'),
('nome da pessoa', 'telefone da pessoa');

## Executando

python main.py

O programa irá:

1. Conectar ao Supabase.
2. Buscar todos os registros da tabela `pessoas`.
3. Enviar uma mensagem para cada telefone encontrado.
4. Exibir o resultado da operação no terminal.

## Dependências

supabase
python-dotenv
requests

## Observações

* Nunca compartilhe o arquivo `.env`.
* Adicione `.env` ao `.gitignore`.
* A chave do Supabase e os tokens da Z-API devem permanecer privados.
* Os números de telefone devem estar no formato internacional, incluindo o código do país e sem o traço.
* se tudo der certo, o terminal irá aparecer: 200.
