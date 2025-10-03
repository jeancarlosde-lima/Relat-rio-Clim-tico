📊 Relatório Climático com base no INMET 🚀

<p align="center"> <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python Badge"> <img src="https://img.shields.io/badge/License-MIT-green" alt="License Badge"> <img src="https://img.shields.io/badge/Status-Ativo-brightgreen" alt="Status Badge"> <img src="https://img.shields.io/badge/Contribuições-Bem%20vindas-blueviolet" alt="Contribuições Badge"> </p> <p align="center"> <img src="https://img.shields.io/badge/Template-Engine-blue" alt="Template Badge"> <img src="https://img.shields.io/badge/Frontend-Chart.js-orange" alt="Chart Badge"> <img src="https://img.shields.io/badge/Estilo-TailwindCSS-teal" alt="Tailwind Badge"> <img src="https://img.shields.io/badge/Dados-JSON%20|%20PDF-lightgrey" alt="Data Badge"> </p>

🎯 Sobre o Projeto

Uma aplicação em Python para gerar relatórios climáticos dinâmicos em HTML.
Com arquitetura modular, suporta múltiplas fontes de dados (JSON e, futuramente, PDFs), utiliza Chart.js para gráficos interativos e TailwindCSS para um design moderno e responsivo.

✨ Destaques

🔮 Previsões Dinâmicas → Relatórios HTML gerados automaticamente a partir de dados estruturados.

📈 Visualização Interativa → Gráficos modernos e interativos com Chart.js.

🎨 Interface Moderna → Layout responsivo e user-friendly com TailwindCSS.

⚡ Performance Otimizada → Processamento rápido e arquitetura expansível para novas fontes de dados.

🚀 Funcionalidades

📊 Gerador de Relatório → Cria automaticamente o arquivo relatorio_previsao_climatica.html.

📈 Múltiplas Fontes → Suporta HTML interno, JSON e futura integração com PDF.

🧱 Estrutura Modular → Código fácil de expandir e manter.

🎨 Template Engine → Substitui placeholders ({{chave}}) no HTML pelo conteúdo dos dados.

⚡ Guia Rápido
Passo	Ação	Resultado
1️⃣	Coloque gerador_relatorio.py, dados.json e template.html na mesma pasta	Arquivos organizados
2️⃣	Edite a variável FONTE_DE_DADOS no script	Define a fonte (html, json, pdf)
3️⃣	Execute python gerador_relatorio.py	Gera o relatório final em HTML

📌 O relatório final será salvo como relatorio_previsao_climatica.html.

🛠️ Stack Tecnológica

🐍 Python 3.8+

📂 JSON / PDF (futuro)

🌐 HTML5

🎨 TailwindCSS

📊 Chart.js

🏗️ Arquitetura do Sistema
flowchart LR
    A[Fontes de Dados<br>(JSON, PDF...)] --> B[Script Python<br>gerador_relatorio.py]
    B --> C[Processamento e Injeção de Dados]
    C --> D[HTML Final<br>relatorio_previsao_climatica.html]

📈 Metodologia de Template

O arquivo template.html contém placeholders como {{titulo_principal}}.
O script lê os dados da fonte escolhida (JSON, HTML hardcoded ou PDF futuro) e substitui cada chave pelo valor correspondente.

✅ Essa abordagem separa conteúdo e design, facilitando manutenção e expansão.

⚡ Quick Start
📋 Pré-requisitos

Python 3.8+ instalado no sistema

🔧 Instalação
git clone <repo-url>
cd projeto

(Opcional) Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

▶️ Execução
python gerador_relatorio.py

🤝 Contribuindo

Faça um Fork do projeto

Crie uma branch de feature:

git checkout -b feature/NovaFuncionalidade


Commit suas alterações:

git commit -m "Adiciona NovaFuncionalidade"


Push para o repositório:

git push origin feature/NovaFuncionalidade


Abra um Pull Request

📄 Licença

Distribuído sob a Licença MIT. Consulte o arquivo LICENSE
.

📞 Contato & Suporte

👤 Feito por Jean Lima
📧 [seu-email-aqui]

🌟 Se este projeto foi útil, considere deixar uma estrela no repositório! ⭐
