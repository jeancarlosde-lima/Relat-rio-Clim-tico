🎯 Sobre o Projeto
Uma aplicação em Python para gerar relatórios climáticos dinâmicos em HTML. Utilizando uma arquitetura flexível, o script pode consumir dados de diferentes fontes (como JSON ou, futuramente, PDFs) para popular um template HTML, criando páginas web interativas e visualmente ricas com gráficos e análises detalhadas.

✨ Destaques
🔮 Geração Dinâmica de HTML: Cria relatórios completos a partir de fontes de dados estruturadas.

🔌 Fontes de Dados Flexíveis: Arquitetura pronta para carregar dados de JSON e com placeholders para implementar a extração de PDFs.

📈 Visualização Interativa: O relatório gerado utiliza Chart.js para exibir gráficos dinâmicos e interativos.

🧱 Código Modular: Funções bem definidas para carregar dados e gerar relatórios, facilitando a manutenção e expansão.

🎬 Exemplo do Relatório Gerado
O script gera um arquivo relatorio_previsao_climatica.html completo e interativo.

🏠 Página Principal

📊 Gráficos Detalhados

[Imagem da interface principal do relatório]

[Imagem dos gráficos interativos no relatório]

Interface Principal 
 Design limpo e informativo.

Visualização de Dados 
 Gráficos interativos com Chart.js.

🎯 Guia Rápido de Geração
Passo

Ação

Resultado

1️⃣

Prepare os arquivos

Coloque gerador_relatorio.py, dados.json e template.html na mesma pasta.

2️⃣

Configure a Fonte de Dados

No script gerador_relatorio.py, defina a variável FONTE_DE_DADOS.

3️⃣

Execute o Script

Execute python gerador_relatorio.py no seu terminal.

🚀 Funcionalidades
Funcionalidade

Descrição

📊 Gerador de Relatório

Gera um arquivo relatorio_previsao_climatica.html a partir de uma fonte de dados.

📈 Múltiplas Fontes

Suporta dados de um HTML "hardcoded", de um arquivo dados.json ou de um PDF (futura implementação).

📋 Estrutura Expansível

O código é modular, permitindo adicionar facilmente novas fontes de dados e funcionalidades.

🎨 Template Engine Simples

Usa um sistema de substituição de chaves ({{chave}}) para popular o template HTML.

🛠️ Stack Tecnológica
Backend

Fonte de Dados

Frontend (Gerado)

⚡ Quick Start
Para colocar o projeto em funcionamento rapidamente, siga os passos abaixo:

📋 Pré-requisitos
Python 3.8+ instalado em seu sistema.

🚀 Instalação e Execução
Não são necessárias bibliotecas externas para a funcionalidade básica (gerar a partir do HTML original ou JSON).

1. Obtenha os arquivos

Faça o download ou clone este repositório.

Certifique-se de que os arquivos gerador_relatorio.py, dados.json e template.html (se for usar) estão no mesmo diretório.

2. (Opcional) Crie um ambiente virtual

# Crie o ambiente virtual
python3 -m venv .venv
# Ative o ambiente
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate    # Windows

3. Execute o gerador
Abra o terminal na pasta do projeto e execute:

python gerador_relatorio.py

Um novo arquivo chamado relatorio_previsao_climatica.html será criado no mesmo diretório.

📱 Como Usar
Para controlar a fonte de dados do relatório, edite a variável FONTE_DE_DADOS dentro do script gerador_relatorio.py:

FONTE_DE_DADOS = "html_original": Gera uma cópia exata do HTML contido no próprio script.

FONTE_DE_DADOS = "json": Lê os dados do arquivo dados.json e os insere no template.html.

FONTE_DE_DADOS = "pdf": (Futura implementação) Ativará a lógica para extrair dados de um arquivo PDF.

🏗️ Arquitetura do Sistema
O fluxo de dados da aplicação é direto e eficiente:

[Fonte de Dados] (JSON, PDF, etc.) → [Script Python] (gerador_relatorio.py) → [Processamento e Injeção de Dados] → [Arquivo HTML Final] (relatorio_previsao_climatica.html)

Este diagrama ilustra como o script centraliza a lógica, consumindo dados brutos e utilizando um template para produzir um relatório web interativo.

📈 Metodologia de Template
O coração da flexibilidade do projeto é seu sistema de templates. O template.html contém marcadores de posição (placeholders), como {{titulo_principal}}. O script Python lê o conteúdo deste template e substitui cada marcador pelo valor correspondente encontrado na fonte de dados (por exemplo, no arquivo dados.json).

Essa abordagem desacopla o conteúdo da apresentação, permitindo que os dados e o design do relatório sejam atualizados de forma independente e com muito mais facilidade.

🤝 Contribuindo
Contribuições são sempre bem-vindas! Se você deseja aprimorar este projeto, siga os passos abaixo:

Faça um Fork do projeto.

Crie sua Feature Branch (git checkout -b feature/AmazingFeature).

Faça o Commit de suas mudanças (git commit -m 'Add some AmazingFeature').

Faça o Push para a Branch (git push origin feature/AmazingFeature).

Abra um Pull Request.

📄 Licença
Este projeto é distribuído sob a Licença MIT. Para mais detalhes, consulte o arquivo LICENSE na raiz do repositório.

📞 Contato & Suporte
Para dúvidas, sugestões ou suporte, sinta-se à vontade para entrar em contato com o autor.

🌟 Se este projeto foi útil para você, considere dar uma estrela! ⭐

<p align="center">
Feito por Jean Lima
</p>
