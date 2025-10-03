🌦️ Relatório Climático com base no INMET
<p align="center"> <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white" alt="Python Badge"> <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License Badge"> <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow" alt="Status Badge"> <img src="https://img.shields.io/badge/Contribuições-Bem%20vindas-brightgreen" alt="Contribuições Badge"> </p>

📊 Uma aplicação em Python para gerar relatórios climáticos dinâmicos em HTML.
O projeto utiliza uma arquitetura flexível que consome dados de diferentes fontes (JSON e, futuramente, PDFs) para popular um template HTML, criando páginas web interativas, ricas em gráficos e análises.

✨ Destaques

🔮 Geração Dinâmica de HTML → Relatórios completos a partir de dados estruturados.

🔌 Fontes Flexíveis → Suporte a JSON e placeholders para futura extração de PDFs.

📈 Visualização Interativa → Gráficos dinâmicos usando Chart.js.

🧱 Código Modular → Funções bem definidas para manutenção e expansão.

🎬 Exemplo de Relatório

📄 O script gera um arquivo relatorio_previsao_climatica.html totalmente interativo.

🏠 Página Principal → design limpo e informativo.

📊 Gráficos Detalhados → visualizações com Chart.js.

(Adicione prints das telas aqui quando tiver imagens disponíveis)

🎯 Guia Rápido
Passo	Ação	Resultado
1️⃣	Coloque gerador_relatorio.py, dados.json e template.html na mesma pasta	Arquivos organizados
2️⃣	Defina a variável FONTE_DE_DADOS no gerador_relatorio.py	Escolha a fonte de dados
3️⃣	Execute python gerador_relatorio.py no terminal	Gera relatorio_previsao_climatica.html
🚀 Funcionalidades
Funcionalidade	Descrição
📊 Gerador de Relatório	Cria o arquivo final em HTML com gráficos e dados.
📈 Múltiplas Fontes	Suporte a HTML interno, JSON e futura integração com PDF.
📋 Estrutura Expansível	Código modular, fácil de adaptar a novas fontes.
🎨 Template Engine Simples	Substituição de placeholders {{chave}} no HTML.
🛠️ Stack Tecnológica
🔙 Backend

🐍 Python 3.8+

📂 Fonte de Dados

📑 JSON

📄 PDF (em breve)

🎨 Frontend (Gerado)

🌐 HTML5

🎨 Tailwind CSS

📊 Chart.js

⚡ Quick Start
📋 Pré-requisitos

Python 3.8+ instalado

🚀 Instalação

Obtenha os arquivos

git clone <repo-url>
cd projeto


Certifique-se de ter gerador_relatorio.py, dados.json e template.html no mesmo diretório.

(Opcional) Crie um ambiente virtual

python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows


Execute o gerador

python gerador_relatorio.py


📌 O arquivo relatorio_previsao_climatica.html será criado automaticamente.

📱 Como Usar

Edite a variável FONTE_DE_DADOS em gerador_relatorio.py:

"html_original" → copia o HTML interno.

"json" → lê os dados do arquivo dados.json e insere no template.

"pdf" → (em breve) extrai dados de um PDF.

🏗️ Arquitetura do Sistema
flowchart LR
    A[Fontes de Dados<br>(JSON, PDF...)] --> B[Script Python<br>gerador_relatorio.py]
    B --> C[Processamento e Injeção de Dados]
    C --> D[HTML Final<br>relatorio_previsao_climatica.html]

📈 Metodologia de Template

O template.html contém placeholders como {{titulo_principal}}.

O script substitui automaticamente esses marcadores pelos valores encontrados em dados.json.

Isso desacopla conteúdo e design, permitindo atualizações independentes.

🤝 Contribuindo

Faça um Fork do projeto.

Crie sua branch:

git checkout -b feature/NovaFuncionalidade


Commit suas alterações:

git commit -m "Adiciona NovaFuncionalidade"


Push da branch:

git push origin feature/NovaFuncionalidade


Abra um Pull Request.

📄 Licença

Distribuído sob a Licença MIT. Consulte o arquivo LICENSE
.

📞 Contato & Suporte

👤 Feito por Jean Lima
📧 [seu-email-aqui]

🌟 Se este projeto foi útil, considere deixar uma estrela no repositório! ⭐
