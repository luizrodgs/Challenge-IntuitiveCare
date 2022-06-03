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
  
#### Requirements
- beautifulsoup4==4.11.1
- pandas==1.4.2
- pdfplumber==0.7.1
- requests==2.27.1
