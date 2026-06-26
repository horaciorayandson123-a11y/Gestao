# Sistema de Gestão de Estoque em Python

Este é um sistema de linha de comando (CLI) simples e eficiente para gerenciamento de estoque de produtos, desenvolvido em Python 3. Ele conta com persistência em banco de dados SQLite, tratamento de erros robusto e testes unitários automatizados.

## 🚀 Funcionalidades

- **Adicionar Produto:** Cadastra um item com código único, nome, quantidade e preço.
- **Atualizar Estoque:** Modifica a quantidade de um produto cadastrado.
- **Remover Produto:** Exclui permanentemente um produto pelo código.
- **Buscar por Código:** Localiza e exibe os detalhes de um produto específico.
- **Listar Tudo:** Lista de forma organizada todos os itens no estoque.

## 🛠️ Tecnologias e Boas Práticas

- **Python 3.x** (Sem dependências externas necessárias).
- **SQLite3:** Banco de dados em arquivo local, garantindo que os dados não sejam perdidos ao fechar o programa.
- **Orientação a Objetos (POO):** Divisão clara de responsabilidades entre entidades, dados e interface gráfica textual.
- **Unittest:** Cobertura de testes de integração e lógica de negócios com banco de dados em memória (`:memory:`).

## 🔧 Como Executar o Projeto

Certifique-se de ter o Python 3 instalado em sua máquina.

1. **Baixe ou clone os arquivos do projeto** para uma pasta local.
2. Abrao terminal/prompt de comando na pasta do projeto.
3. Execute o comando correspondente à aplicação principal:

```bash
python main.py