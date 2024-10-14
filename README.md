# DataViz Toolkit

**DataViz Toolkit** é um pacote Python projetado para facilitar a criação de visualizações de dados dinâmicas, dashboards interativos e relatórios automatizados. Com uma abordagem simples e intuitiva, este pacote é perfeito para cientistas de dados, analistas e desenvolvedores que desejam transformar seus dados em gráficos e insights acionáveis.

Este projeto foi inspirado no [simple-package-template](https://github.com/tiemi/simple-package-template), criado para fornecer uma base limpa e modular para desenvolvimento de pacotes Python.

A ideia desse pacote é apenas entender e aprender a fazer os próprios pacotes, seguindo o tutorial da DIO com a instrutora Tiemi. 

## Instalação

Para instalar o pacote, basta executar o seguinte comando:

```bash
pip install data-viz-toolkit
```

Ou, para instalar diretamente do código-fonte:

```bash
git clone https://github.com/seuusuario/data-viz-toolkit.git
cd data-viz-toolkit
pip install .
```

## Funcionalidades

- **Gráficos Interativos:** Geração de gráficos com `matplotlib` e `plotly` para diferentes tipos de dados.
- **Dashboards Dinâmicos:** Criação de dashboards interativos usando `Dash` para análise visual fácil.
- **Carregamento de Dados:** Funções para carregar dados em vários formatos, incluindo CSV e Excel.
- **Relatórios Automatizados:** Geração de relatórios em PDF ou HTML, integrando gráficos e informações chave.
- **Ferramentas Utilitárias:** Conjunto de funções auxiliares para formatação e organização de dados.

## Exemplo de Uso

Aqui está um exemplo de como utilizar o **DataViz Toolkit** para criar um gráfico de barras simples e um dashboard interativo:

```python
from data_viz_toolkit.charts import create_bar_chart
from data_viz_toolkit.dashboards import create_dashboard
from data_viz_toolkit.data_loader import load_csv

# Carregar os dados de um arquivo CSV
data = {'A': 30, 'B': 20, 'C': 50}

# Criar um gráfico de barras
create_bar_chart(data, "Vendas por Categoria")

# Criar um dashboard interativo
create_dashboard(data)
```

## Estrutura do Projeto

Abaixo está a estrutura do projeto para facilitar a navegação:

```
data-viz-toolkit/
│
├── src/
│   └── data_viz_toolkit/
│       ├── __init__.py          # Inicialização do pacote
│       ├── charts.py            # Funções para criação de gráficos
│       ├── dashboards.py        # Funções para criação de dashboards interativos
│       ├── data_loader.py       # Funções para carregamento de dados (CSV, Excel)
│       ├── reporting.py         # Funções para geração de relatórios (PDF/HTML)
│       └── utils.py             # Funções utilitárias
│
├── tests/                       # Testes unitários do pacote
│   ├── test_charts.py
│   ├── test_dashboards.py
│   └── ...
│
├── .gitignore                   # Arquivo de exclusão do Git
├── LICENSE                      # Licença do projeto
├── README.md                    # Documentação do pacote
├── setup.py                     # Arquivo de configuração para instalação
└── pyproject.toml               # Metadados e configuração do projeto
```

## Testes

O projeto inclui testes unitários para todas as principais funcionalidades. Para rodar os testes, basta usar `pytest`:

```bash
pytest tests/
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. Este projeto foi inspirado no [simple-package-template](https://github.com/tiemi/simple-package-template), e você também pode usar essa estrutura para desenvolver suas próprias soluções.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
