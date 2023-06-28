# Sistema de Gestão para Oficina Mecânica e Lavagem de Carros<br>
O Sistema de Gestão para Oficina Mecânica e Lavagem de Carros é uma aplicação desenvolvida em Python, utilizando o framework Django e o framework de estilo Bootstrap 4.6. Esse sistema permite o gerenciamento completo de uma empresa que oferece serviços de mecânica e lavagem de carros, incluindo o cadastro de clientes, gerenciamento de veículos, criação de ordens de serviço, geração de relatórios em PDF, entre outras funcionalidades.

# Funcionalidades <br>
Cadastro de Clientes: Permite cadastrar informações dos clientes, como nome, telefone, endereço, entre outros dados relevantes.

Gerenciamento de Veículos: Permite cadastrar veículos associados a cada cliente, incluindo informações como marca, modelo, placa, ano, entre outros detalhes.

Criação de Ordem de Serviço: Permite criar ordens de serviço para registrar os serviços a serem realizados, incluindo informações como descrição do serviço, valor, datas de início e entrega, protocolo e status de conclusão.

Relatórios em PDF: Possibilita a geração de relatórios em PDF contendo informações das ordens de serviço, facilitando o compartilhamento e armazenamento dessas informações.

# Pré-requisitos
Python 3.x
Django 3.x
Bootstrap 4.6
# Configuração do Ambiente
Clone o repositório:<br>
bash<br>
Copy code<br>
git clone https://github.com/lazarowend/mecajato<br>
Instale as dependências do projeto:<br>
bash<br>
Copy code<br>
pip install -r requirements.txt<br>
Execute as migrações do banco de dados:<br>
bash<br>
Copy code<br>
python manage.py migrate<br>
# Uso<br>
Inicie o servidor de desenvolvimento:
bash
Copy code
python manage.py runserver
Acesse o sistema em seu navegador utilizando o endereço http://localhost:8000/clientes.

Cadastre os clientes e seus respectivos veículos no sistema.

Crie ordens de serviço para registrar os serviços a serem realizados, inserindo informações como descrição, valor, datas, protocolo e status de conclusão.

Verifique o status das ordens de serviço e atualize conforme necessário.

Utilize a funcionalidade de geração de relatórios em PDF para obter um documento com as informações das ordens de serviço.
