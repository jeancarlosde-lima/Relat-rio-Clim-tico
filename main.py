import json
import os
# Para o futuro, quando quiser implementar a leitura de PDFs, preciso
# de uma biblioteca como a PyMuPDF. Instale com: pip install PyMuPDF
# import fitz # PyMuPDF

def carregar_dados_do_html_original():
    """
    Retorna o conteúdo HTML original como uma string.
    Esta função garante que o script possa reproduzir fielmente o HTML fornecido.
    """
    print("Carregando conteúdo do HTML original codificado no script...")
    html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Previsão Climática Interativa (Pop-ups) - Brasil, Setembro 2025</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .gradient-text {
            background: linear-gradient(to right, #2a7de9, #09e1c0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 350px;
            max-height: 450px;
        }
        .chart-container-small {
            position: relative;
            width: 100%;
            height: 250px;
            min-width: 280px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 400px;
            }
        }
        .accordion-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease-in-out;
        }
        .accordion-button svg {
            transition: transform 0.3s ease-in-out;
        }
        .modal-overlay {
            transition: opacity 0.3s ease;
        }
        .modal-content {
            transition: transform 0.3s ease;
        }
    </style>
</head>
<body class="bg-gray-100 text-gray-800">

    <main class="max-w-7xl mx-auto p-4 sm:p-6 lg:p-8">

        <header class="text-center mb-12">
            <h1 class="text-4xl md:text-6xl font-black text-gray-900 tracking-tight leading-tight">Previsão Climática: <span class="gradient-text">Brasil, 2 a 15 de Outubro 2025</span></h1>
            <p class="mt-4 text-lg md:text-xl text-gray-600 max-w-3xl mx-auto">A primeira quinzena de Outubro consolida a transição para a estação chuvosa no Brasil Central, com chuvas se espalhando pelo Sudeste e Centro-Oeste, enquanto o Sul experimenta uma redução das chuvas e o calor se intensifica no Nordeste.</p>
        </header>

        <h2 class="text-xl font-bold text-center text-gray-800 mb-2">Panorama Rápido</h2>
        <p class="text-center text-gray-500 mb-8">Clique nos cards para revelar mais detalhes.</p>

        <section class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12 text-center">
            <div id="kpi-chuva" class="bg-white rounded-2xl shadow-lg p-6 cursor-pointer hover:shadow-xl transition-shadow duration-300">
                <p class="text-5xl font-bold text-blue-600">🌧️</p>
                <h3 class="text-xl font-bold mt-2">Retorno das Chuvas</h3>
                <p class="text-gray-600 mt-1">Avanço da umidade e chuvas no Sudeste e Centro-Oeste.</p>
            </div>
            <div id="kpi-calor" class="bg-white rounded-2xl shadow-lg p-6 cursor-pointer hover:shadow-xl transition-shadow duration-300">
                <p class="text-5xl font-bold text-red-500">☀️</p>
                <h3 class="text-xl font-bold mt-2">Calor Intenso no Nordeste</h3>
                <p class="text-gray-600 mt-1">Temperaturas podem passar dos 40°C no Piauí e Maranhão.</p>
            </div>
            <div id="kpi-anomalia" class="bg-white rounded-2xl shadow-lg p-6 cursor-pointer hover:shadow-xl transition-shadow duration-300">
                <p class="text-5xl font-bold text-yellow-500">📉</p>
                <h3 class="text-xl font-bold mt-2">Redução de Chuva no Sul</h3>
                <p class="text-gray-600 mt-1">Volumes ficam abaixo da média na maior parte da região.</p>
            </div>
        </section>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
             <div class="bg-white rounded-2xl shadow-lg p-6 md:p-8">
                <h2 class="text-2xl font-bold text-gray-900 mb-4">Cenário da Precipitação (Chuva)</h2>
                <p class="text-gray-600 mb-6">A umidade da Amazônia avança, trazendo o retorno de pancadas de chuva para o Brasil Central. O Sul, por outro lado, terá um período mais seco que o normal, enquanto o Norte e Nordeste mantêm padrões irregulares.</p>
                <div class="chart-container">
                    <canvas id="precipitationChart"></canvas>
                </div>
            </div>

            <div class="bg-white rounded-2xl shadow-lg p-6 md:p-8">
                <h2 class="text-2xl font-bold text-gray-900 mb-4">Anomalia de Temperatura por Região</h2>
                <p class="text-gray-600 mb-6">As temperaturas permanecem acima da média em grande parte do país. O calor mais intenso se concentra no interior do Nordeste, enquanto o avanço de uma massa de ar frio pode trazer temperaturas amenas para o Sul no final do período.</p>
                <div class="chart-container">
                    <canvas id="temperatureAnomalyChart"></canvas>
                </div>
            </div>
        </div>

        <section class="mt-12">
            <h2 class="text-3xl font-bold text-center text-gray-900 mb-8">Análise Detalhada por Região e Impactos na Agricultura</h2>
            <div class="space-y-4">

                <div class="bg-white rounded-2xl shadow-lg">
                    <button class="accordion-button w-full flex justify-between items-center text-left p-6">
                        <div class="flex items-center"><span class="text-3xl mr-4">🌳</span><div><h3 class="text-lg font-bold text-gray-900">Norte</h3><p class="text-sm text-gray-500">Chuvas se espalham, mas irregularidade continua.</p></div></div>
                        <svg class="w-6 h-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="accordion-content"><div class="p-6 border-t border-gray-200"><div class="flex flex-col md:flex-row gap-6 items-start"><div class="flex-1"><ul class="list-disc list-inside space-y-2 text-gray-700"><li><strong>Análise:</strong> As pancadas de chuva se tornam mais frequentes no sul da região (AC, RO, sul do AM e PA). No norte (RR e AP), a chuva ainda é irregular e o tempo mais seco.</li> <li><strong>Impactos Agrícolas:</strong> A umidade crescente favorece o preparo do solo para o plantio da safra de grãos. Em áreas de pastagem, a condição melhora, mas o risco de queimadas ainda existe em áreas mais secas.</li></ul></div><div class="flex-1 w-full"><div class="chart-container-small"><canvas id="norteChart"></canvas></div><p class="text-xs text-center text-gray-500 mt-2">O gráfico destaca a chuva acima da média (azul) no Noroeste do Amazonas e abaixo da média (amarelo) nas demais áreas de risco.</p></div></div></div></div>
                </div>

                <div class="bg-white rounded-2xl shadow-lg">
                    <button class="accordion-button w-full flex justify-between items-center text-left p-6">
                        <div class="flex items-center"><span class="text-3xl mr-4">🌽</span><div><h3 class="text-lg font-bold text-gray-900">Nordeste</h3><p class="text-sm text-gray-500">Calor intenso e tempo seco desafiam a agricultura.</p></div></div>
                        <svg class="w-6 h-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="accordion-content"><div class="p-6 border-t border-gray-200"><div class="flex flex-col md:flex-row gap-6 items-start"><div class="flex-1"><ul class="list-disc list-inside space-y-2 text-gray-700"><li><strong>Análise:</strong> A região enfrenta forte onda de calor, principalmente no interior (PI, MA, oeste da BA). A chuva é escassa na maior parte da região, exceto por áreas no litoral do MA e PI.</li><li><strong>Impactos Agrícolas:</strong> Condições de estresse hídrico para lavouras de sequeiro e pastagens. A alta radiação solar exige manejo cuidadoso da irrigação onde disponível. A atenção é redobrada para o risco de incêndios.</li></ul></div><div class="flex-1 w-full"><div class="chart-container-small"><canvas id="nordesteChart"></canvas></div><p class="text-xs text-center text-gray-500 mt-2">O gráfico mostra chuva próxima da média (cinza) na maior parte da região, mas abaixo da média (amarelo) no litoral da Bahia.</p></div></div></div></div>
                </div>

                <div class="bg-white rounded-2xl shadow-lg">
                    <button class="accordion-button w-full flex justify-between items-center text-left p-6">
                         <div class="flex items-center"><span class="text-3xl mr-4">🌱</span><div><h3 class="text-lg font-bold text-gray-900">Centro-Oeste</h3><p class="text-sm text-gray-500">Retorno da umidade beneficia início da safra.</p></div></div>
                        <svg class="w-6 h-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="accordion-content"><div class="p-6 border-t border-gray-200"><div class="flex flex-col md:flex-row gap-6 items-start"><div class="flex-1"><ul class="list-disc list-inside space-y-2 text-gray-700"><li><strong>Análise:</strong> A chuva se torna mais regular, especialmente em MS, sul de GO e MT. As temperaturas seguem altas, mas a umidade do ar e do solo aumenta.</li><li><strong>Impactos Agrícolas:</strong> O aumento da umidade é crucial para o plantio e a germinação da <strong>soja</strong>. A condição favorece a recuperação das pastagens. Atenção a possíveis temporais isolados.</li></ul></div><div class="flex-1 w-full"><div class="chart-container-small"><canvas id="centroOesteChart"></canvas></div><p class="text-xs text-center text-gray-500 mt-2">O gráfico indica chuva próxima da média (cinza), com exceção do oeste de MS (amarelo) e sudeste de MS (azul).</p></div></div></div></div>
                </div>

                <div class="bg-white rounded-2xl shadow-lg">
                    <button class="accordion-button w-full flex justify-between items-center text-left p-6">
                         <div class="flex items-center"><span class="text-3xl mr-4">☕</span><div><h3 class="text-lg font-bold text-gray-900">Sudeste</h3><p class="text-sm text-gray-500">Início da estação chuvosa favorece o plantio.</p></div></div>
                        <svg class="w-6 h-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="accordion-content"><div class="p-6 border-t border-gray-200"><div class="flex flex-col md:flex-row gap-6 items-start"><div class="flex-1"><ul class="list-disc list-inside space-y-2 text-gray-700"><li><strong>Análise:</strong> A quinzena é marcada pelo retorno das chuvas regulares em SP, MG e RJ, com volumes acima da média em algumas áreas. As temperaturas continuam elevadas, mas a umidade do solo melhora significativamente.</li> <li><strong>Impactos Agrícolas:</strong> Condições ideais para o plantio e desenvolvimento inicial da safra de verão (<strong>soja e milho</strong>). A umidade beneficia a florada do <strong>café</strong> e o crescimento da <strong>cana-de-açúcar</strong>.</li></ul></div><div class="flex-1 w-full"><div class="chart-container-small"><canvas id="sudesteChart"></canvas></div><p class="text-xs text-center text-gray-500 mt-2">O gráfico aponta chuva próxima da média (cinza) na maior parte da região, com volumes levemente acima em SP e MG (azul).</p></div></div></div></div>
                </div>

                <div class="bg-white rounded-2xl shadow-lg">
                    <button class="accordion-button w-full flex justify-between items-center text-left p-6">
                         <div class="flex items-center"><span class="text-3xl mr-4">🌾</span><div><h3 class="text-lg font-bold text-gray-900">Sul</h3><p class="text-sm text-gray-500">Período mais seco que o normal, com retorno do calor.</p></div></div>
                        <svg class="w-6 h-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="accordion-content"><div class="p-6 border-t border-gray-200"><div class="flex flex-col md:flex-row gap-6 items-start"><div class="flex-1"><ul class="list-disc list-inside space-y-2 text-gray-700"><li><strong>Análise:</strong> A chuva diminui em toda a região, com volumes abaixo da média, especialmente no RS. As temperaturas voltam a subir, ficando acima da média no Paraná. Uma frente fria pode chegar no final da quinzena.</li><li><strong>Impactos Agrícolas:</strong> O tempo mais seco favorece a finalização da colheita do <strong>trigo</strong> e o avanço do plantio da <strong>soja e milho</strong>. No entanto, a falta de chuva pode começar a preocupar se o período de estiagem se prolongar.</li></ul></div><div class="flex-1 w-full"><div class="chart-container-small"><canvas id="sulChart"></canvas></div><p class="text-xs text-center text-gray-500 mt-2">O gráfico ilustra a previsão de chuvas acima da média (azul) para o Rio Grande do Sul e Santa Catarina, e próximas da normalidade (cinza) para o Paraná.</p></div></div></div></div>
                </div>
            </div>
        </section>

        <section class="mt-12 bg-white rounded-2xl shadow-lg p-6 md:p-8">
            <h2 class="text-2xl font-bold text-center text-gray-900 mb-4">Prognóstico para a Segunda Quinzena de Outubro</h2>
            <p class="text-center text-gray-600 max-w-4xl mx-auto">Para a segunda quinzena de Outubro, a tendência é de consolidação da estação chuvosa no Brasil Central. As frentes frias devem ter mais dificuldade para avançar pelo Sul, resultando em menos chuva para a região. O calor deve diminuir no Nordeste com o aumento gradual da umidade.</p>
        </section>
    </main>

    <!-- Modal -->
    <div id="kpi-modal" class="modal-overlay fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 hidden z-50 opacity-0">
        <div class="modal-content bg-white rounded-2xl shadow-lg w-full max-w-lg p-6 md:p-8 transform scale-95">
            <div class="flex justify-between items-center mb-4">
                <h3 id="modal-title" class="text-2xl font-bold"></h3>
                <button id="modal-close" class="text-gray-500 hover:text-gray-800 text-3xl leading-none">&times;</button>
            </div>
            <div id="modal-body" class="text-gray-700">
            </div>
        </div>
    </div>

    <footer class="text-center p-6 text-gray-500 text-sm">
        <p class="font-bold">Jean Carlos de Lima</p>
        <a href="https://www.linkedin.com/in/jeancarlosodelima/" target="_blank" class="mt-2 inline-block bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors">
            Ver LinkedIn
        </a>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const wrapLabel = (label, maxWidth = 16) => {
                if (label.length <= maxWidth) return label;
                const words = label.split(' ');
                const lines = [];
                let currentLine = '';
                words.forEach(word => {
                    if ((currentLine + ' ' + word).trim().length > maxWidth) {
                        lines.push(currentLine.trim());
                        currentLine = word;
                    } else {
                        currentLine = (currentLine + ' ' + word).trim();
                    }
                });
                if (currentLine) lines.push(currentLine.trim());
                return lines;
            };

            const tooltipTitleCallback = (tooltipItems) => {
                const item = tooltipItems[0];
                let label = item.chart.data.labels[item.dataIndex];
                return Array.isArray(label) ? label.join(' ') : label;
            };

            const commonChartOptions = {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: { callbacks: { title: tooltipTitleCallback } }
                },
                scales: {
                    y: { ticks: { font: { family: 'Inter' } } },
                    x: { ticks: { font: { family: 'Inter' } } }
                }
            };

            const anomalyTicks = {
                callback: value => {
                    if (value === 1) return 'Acima da Média';
                    if (value === 0) return 'Próximo da Média';
                    if (value === -1) return 'Abaixo da Média';
                    return '';
                }
            };

            // Gráfico Principal de Precipitação
            new Chart(document.getElementById('precipitationChart').getContext('2d'), {
                type: 'bar',
                data: {
                    labels: ['Sudeste e Centro-Oeste', 'Norte', 'Sul e Nordeste'].map(l => wrapLabel(l)),
                    datasets: [{
                        label: 'Anomalia de Chuva',
                        data: [1, 0, -1],
                        backgroundColor: ['#3375FF', '#6C757D', '#FFC107'],
                        borderColor: '#FFFFFF', borderWidth: 2, borderRadius: 5
                    }]
                },
                options: { ...commonChartOptions, scales: { y: { ticks: anomalyTicks, min: -1.5, max: 1.5 } } }
            });

            // Gráfico Principal de Temperatura
            new Chart(document.getElementById('temperatureAnomalyChart').getContext('2d'), {
                type: 'bar',
                data: {
                    labels: ['Nordeste', 'Norte e Centro-Oeste', 'Sudeste e Sul'].map(l => wrapLabel(l)),
                    datasets: [{
                        label: 'Anomalia (°C)',
                        data: [2.0, 1.0, 0.5],
                        backgroundColor: ['#D32F2F', '#FF7043', '#FFA726'],
                        borderColor: '#FFFFFF', borderWidth: 2, borderRadius: 5
                    }]
                },
                options: { ...commonChartOptions, indexAxis: 'y', scales: { x: { beginAtZero: false, title: { display: true, text: 'Anomalia em °C (relação à média histórica)' }}} }
            });

            // Lógica do Accordion
            document.querySelectorAll('.accordion-button').forEach(button => {
                button.addEventListener('click', () => {
                    const accordionContent = button.nextElementSibling;
                    const svg = button.querySelector('svg');
                    const isExpanded = button.getAttribute('aria-expanded') === 'true';

                    button.setAttribute('aria-expanded', !isExpanded);

                    if (isExpanded) {
                        accordionContent.style.maxHeight = null;
                        svg.style.transform = 'rotate(0deg)';
                    } else {
                        accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
                        svg.style.transform = 'rotate(180deg)';
                    }
                });
            });

            const regionalChartOptions = {
                ...commonChartOptions,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        callbacks: {
                            title: tooltipTitleCallback,
                            label: (context) => {
                                let value = context.parsed.y;
                                if (value > 0.5) return 'Acima da Média';
                                if (value < -0.5) return 'Abaixo da Média';
                                return 'Próximo da Média';
                            }
                        }
                    }
                },
                scales: { x: { ticks: { font: { size: 10 }}}, y: { ticks: anomalyTicks, min: -1.5, max: 1.5 } }
            };

            new Chart(document.getElementById('norteChart').getContext('2d'), {
                type: 'bar', data: { labels: ['NW Amazonas', 'Roraima', 'Pará (C-S)', 'Acre'], datasets: [{ data: [1, -1, -1, -1], backgroundColor: ['#3375FF', '#FFC107', '#FFC107', '#FFC107'] }] }, options: regionalChartOptions
            });
            new Chart(document.getElementById('nordesteChart').getContext('2d'), {
                type: 'bar', data: { labels: ['Maioria da Região', 'Litoral da Bahia'], datasets: [{ data: [0, -1], backgroundColor: ['#6C757D', '#FFC107'] }] }, options: regionalChartOptions
            });
            new Chart(document.getElementById('centroOesteChart').getContext('2d'), {
                type: 'bar', data: { labels: ['Maioria da Região', 'Oeste de MS', 'Sudeste de MS'], datasets: [{ data: [0, -1, 1], backgroundColor: ['#6C757D', '#FFC107', '#3375FF'] }] }, options: regionalChartOptions
            });
            new Chart(document.getElementById('sudesteChart').getContext('2d'), {
                type: 'bar', data: { labels: ['Maioria da Região', 'SE de SP', 'Sul de MG'], datasets: [{ data: [0, 1, 1], backgroundColor: ['#6C757D', '#3375FF', '#3375FF'] }] }, options: regionalChartOptions
            });
            new Chart(document.getElementById('sulChart').getContext('2d'), {
                type: 'bar', data: { labels: ['Rio Grande do Sul', 'Santa Catarina', 'Paraná (N/SO)'], datasets: [{ data: [1, 1, 0], backgroundColor: ['#3375FF', '#3375FF', '#6C757D'] }] }, options: regionalChartOptions
            });

            // Lógica do Modal
            const modal = document.getElementById('kpi-modal');
            const modalOverlay = document.querySelector('.modal-overlay');
            const modalContent = document.querySelector('.modal-content');
            const modalTitle = document.getElementById('modal-title');
            const modalBody = document.getElementById('modal-body');
            const modalClose = document.getElementById('modal-close');

            const kpiData = {
                'kpi-chuva': {
                    title: '🌧️ Retorno das Chuvas ao Brasil Central',
                    content: `<p class="mb-4 font-bold">A umidade da Amazônia retorna, trazendo pancadas de chuva para:</p>
                                  <ul class="list-disc list-inside space-y-2">
                                    <li><strong>Sudeste:</strong> Grande parte de São Paulo, sul e Triângulo de Minas Gerais, e Rio de Janeiro.</li>
                                    <li><strong>Centro-Oeste:</strong> Mato Grosso do Sul, sul de Goiás e Mato Grosso.</li>
                                  </ul>`
                },
                'kpi-calor': {
                    title: '☀️ Calor Intenso no Nordeste',
                    content: `<p class="mb-4 font-bold">Ondas de calor devem atingir o interior do Nordeste, com temperaturas superando 40°C em cidades do:</p>
                                  <ul class="list-disc list-inside space-y-2">
                                    <li><strong>Piauí</strong></li>
                                    <li><strong>Maranhão</strong></li>
                                    <li><strong>Oeste da Bahia</strong></li>
                                  </ul>`
                },
                'kpi-anomalia': {
                    title: '📉 Redução de Chuva no Sul',
                    content: `<p class="mb-4 font-bold">Após um Setembro chuvoso, a primeira quinzena de Outubro será mais seca que o normal, com volumes de chuva abaixo da média em:</p>
                                   <ul class="list-disc list-inside space-y-2">
                                    <li><strong>Rio Grande do Sul</strong> (principalmente)</li>
                                    <li><strong>Santa Catarina</strong></li>
                                    <li><strong>Paraná</strong></li>
                                  </ul>`
                }
            };

            function openModal(id) {
                const data = kpiData[id];
                modalTitle.textContent = data.title;
                modalBody.innerHTML = data.content;
                modal.classList.remove('hidden');
                document.body.style.overflow = 'hidden';
                setTimeout(() => {
                    modalOverlay.classList.remove('opacity-0');
                    modalContent.classList.remove('scale-95');
                }, 10);
            }

            function closeModal() {
                modalOverlay.classList.add('opacity-0');
                modalContent.classList.add('scale-95');
                setTimeout(() => {
                    modal.classList.add('hidden');
                    document.body.style.overflow = '';
                }, 300);
            }

            document.getElementById('kpi-chuva').addEventListener('click', () => openModal('kpi-chuva'));
            document.getElementById('kpi-calor').addEventListener('click', () => openModal('kpi-calor'));
            document.getElementById('kpi-anomalia').addEventListener('click', () => openModal('kpi-anomalia'));

            modalClose.addEventListener('click', closeModal);
            modalOverlay.addEventListener('click', (e) => {
                if (e.target === modalOverlay) {
                    closeModal();
                }
            });
        });
    </script>

</body>
</html>
"""
    return html_content

def carregar_dados_de_json(caminho_json):
    """
    Carrega os dados de um arquivo de origem JSON.
    """
    print(f"Lendo dados da fonte: JSON ('{caminho_json}')...")
    with open(caminho_json, 'r', encoding='utf-8') as f:
        return json.load(f)

def extrair_dados_de_pdf(caminho_pdf):
    """
    **FUNÇÃO PLACEHOLDER (BRECHA PARA O FUTURO)**

    Esta função conterá a lógica para extrair dados de um PDF.
    """
    print("="*50)
    print(f"AVISO: Simulando extração de dados do PDF '{caminho_pdf}'.")
    # ... (código da função de simulação mantido para o futuro)
    # ...
    dados_simulados = {
        "textos": {
            "titulo_pagina": "Previsão Climática (Simulado do PDF)",
            "titulo_principal": "Previsão Climática Simulada:",
            "periodo_previsao": "PDF, Outubro 2025",
            "paragrafo_principal": "Estes dados foram gerados pela função de simulação de PDF...",
            "kpi1_titulo": "KPI 1 do PDF",
            "kpi1_texto": "Descrição do KPI 1 extraído do PDF.",
            "kpi2_titulo": "KPI 2 do PDF",
            "kpi2_texto": "Descrição do KPI 2 extraído do PDF.",
            "kpi3_titulo": "KPI 3 do PDF",
            "kpi3_texto": "Descrição do KPI 3 extraído do PDF.",
            "texto_precipitacao": "Análise de precipitação baseada no documento PDF.",
            "texto_temperatura": "Análise de temperatura baseada no documento PDF.",
            "norte_desc": "Descrição da região Norte vinda do PDF.",
            "norte_analise": "Análise da região Norte vinda do PDF.",
            "norte_impacto": "Impacto na agricultura da região Norte vindo do PDF.",
            "prognostico_titulo": "Prognóstico Futuro (Fonte: PDF)",
            "prognostico_texto": "Tendências futuras extraídas e sumarizadas a partir do relatório em PDF."
        },
        "graficos": {
            "precipitacaoPrincipal": {"labels": ["Sudeste", "Norte", "Sul"], "data": [1,0,-1]},
            "temperaturaPrincipal": {"labels": ["Nordeste", "Norte", "Sul"], "data": [2.5,1.5,0.8]},
            "kpiDetails": {
                "kpi-chuva": {"title": "🌧️ Detalhes Chuva (PDF)", "content": "<p>...</p>"},
                "kpi-calor": {"title": "☀️ Detalhes Calor (PDF)", "content": "<p>...</p>"},
                "kpi-anomalia": {"title": "📉 Detalhes Anomalia (PDF)", "content": "<p>...</p>"}
            }
        }
    }
    return dados_simulados


def gerar_relatorio_direto(html_content, arquivo_saida):
    """
    Salva o conteúdo HTML diretamente em um arquivo.
    """
    try:
        print(f"Salvando relatório final em '{arquivo_saida}'...")
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("-" * 30)
        print(f"Relatório '{arquivo_saida}' gerado com sucesso!")
        print("-" * 30)
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante a gravação do arquivo: {e}")


def gerar_relatorio_template(dados, arquivo_template, arquivo_saida):
    """
    Gera um relatório HTML final, injetando os dados em um template.
    """
    try:
        print(f"Lendo template de '{arquivo_template}'...")
        with open(arquivo_template, 'r', encoding='utf-8') as f:
            template_html = f.read()
        print("Template carregado com sucesso.")

        print("Inserindo dados no template...")
        html_final = template_html
        for chave, valor in dados["textos"].items():
            html_final = html_final.replace(f'{{{{{chave}}}}}', str(valor))

        dados_graficos_json = json.dumps(dados["graficos"], ensure_ascii=False)
        html_final = html_final.replace("'{{dados_graficos_json}}'", dados_graficos_json)
        print("Dados inseridos.")

        print(f"Salvando relatório final em '{arquivo_saida}'...")
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(html_final)
        print("-" * 30)
        print(f"Relatório '{arquivo_saida}' gerado com sucesso!")
        print("-" * 30)
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante a geração do relatório: {e}")

# --- Execução Principal ---
if __name__ == "__main__":
    # --- CONFIGURAÇÃO ---
    # Opções: "html_original", "json", "pdf"
    FONTE_DE_DADOS = "html_original"

    # Nomes dos arquivos de entrada e saída
    NOME_ARQUIVO_PDF = "meu_novo_relatorio.pdf"
    NOME_ARQUIVO_JSON = "dados.json"
    NOME_ARQUIVO_TEMPLATE = "template.html"
    NOME_ARQUIVO_SAIDA = "relatorio_previsao_climatica.html"

    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    caminho_saida = os.path.join(diretorio_script, NOME_ARQUIVO_SAIDA)

    print("Iniciando processo...")

    try:
        if FONTE_DE_DADOS == "html_original":
            html_content = carregar_dados_do_html_original()
            gerar_relatorio_direto(html_content, caminho_saida)

        elif FONTE_DE_DADOS == "json":
            caminho_json = os.path.join(diretorio_script, NOME_ARQUIVO_JSON)
            dados_carregados = carregar_dados_de_json(caminho_json)
            if dados_carregados:
                caminho_template = os.path.join(diretorio_script, NOME_ARQUIVO_TEMPLATE)
                gerar_relatorio_template(dados_carregados, caminho_template, caminho_saida)

        elif FONTE_DE_DADOS == "pdf":
            caminho_pdf = os.path.join(diretorio_script, NOME_ARQUIVO_PDF)
            dados_carregados = extrair_dados_de_pdf(caminho_pdf)
            if dados_carregados:
                caminho_template = os.path.join(diretorio_script, NOME_ARQUIVO_TEMPLATE)
                gerar_relatorio_template(dados_carregados, caminho_template, caminho_saida)
        else:
            raise ValueError(f"Fonte de dados '{FONTE_DE_DADOS}' é inválida.")

    except Exception as e:
        print(f"Ocorreu um erro fatal no processo: {e}")
