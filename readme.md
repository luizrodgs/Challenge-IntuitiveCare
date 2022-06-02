# Readme - IntuitiveCare Challenge

### Testes:
##### - 1: **WebScraping**
  - Acessar o [link](https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude);
  - Localizar e baixar os Anexos I, II, III e IV;
  - Compactar os anexos baixados em um arquivo ZIP ou RAR.
  
##### - 2: **Transformação de dados**
  - Extrair do Anexo I (.pdf) os dados das tabelas 'Rol de Procedimentos' e 'Eventos em Saúde';
  - Salvar os dados em uma tabela estruturada em CSV;
  - Zipar o CSV em um arquivo 'Teste_{nome}.zip';
  - Substituir dados abreviados das colunas OD e AMB por Seg. Odontológica e Seg Ambulatorial, respectivamente.
  
##### - 3: **Banco de Dados**
  - Baixar os arquivos dos últimos 2 anos no [repositório público](http://ftp.dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/);
  - Criar scripts SQL utilizando MySQL 8 ou Postgres>10.0 que executem as seguintes tarefas:
    - Criar queries para criar tabelas com as colunas necessárias para o arquivo csv;
    - Criar queries para carregar o conteúdo do arquivo obtido na tarefa de preparação;
    - Montar uma query analítica que traga a resposta para as seguintes perguntas:
      - Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
      - Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?
      
##### - 4: **API**
  - Criar uma interface web (usando o framework Vue.js) que se comunicará com um servidor para realizar as tarefas de código abaixo:
    - Criar servidor com rota que realiza uma busca textual na lista de cadastro de operadoras (obtido na tarefa de preparação) e retorne as linhas que mais se assemelham;
    - Criar coleção no Postman para exibir resultado.
  
#### Requirements
- autopep8==1.6.0
- beautifulsoup4==4.11.1
- pycodestyle==2.8.0
- soupsieve==2.3.2.post1
- toml==0.10.2