import streamlit as st

st.title("Tradutor do Povo - Edição Elite")

dicionario = {
    # --- MACROECONOMIA ---
    "macroeconomia": "O estudo da economia de um país inteiro.",
    "câmbio": "O preço de uma moeda em relação a outra.",
    "pib": "Tudo que o país produz de riqueza em um ano.",
    "deflação": "O contrário da inflação: os preços caem.",
    "deficit": "Quando o governo ou uma empresa gasta mais do que arrecada.",
    "superávit": "Quando sobra dinheiro no fim das contas.",
    "juros compostos": "Os juros que rendem sobre juros.",

    # --- GEOPOLÍTICA ---
    "geopolítica": "Como a briga por poder e território entre países afeta o mundo.",
    "hegemonia": "Quando um país domina os outros na política ou economia.",
    "sanção": "Um castigo econômico aplicado a um país.",
    "protecionismo": "Quando o governo cria barreiras para proteger empresas locais.",
    "globalização": "O mundo todo conectado.",

    # --- MERCADO FINANCEIRO ---
    "bull market": "Quando a Bolsa está subindo forte.",
    "bear market": "Quando a Bolsa está caindo e o pessoal está pessimista.",
    "volatilidade": "O sobe e desce rápido dos preços.",
    "alavancagem": "Operar com dinheiro emprestado para tentar lucrar mais.",
    "day trade": "Comprar e vender ativos no mesmo dia.",
    "dividendos": "Uma parte do lucro da empresa que ela divide com os sócios.",
    "hedge": "Uma proteção financeira.",
    "liquidez": "A facilidade de transformar seu investimento em dinheiro.",
    "spread": "A diferença entre o preço de compra e venda.",

    # --- RENDER FIXA E TERMOS ADICIONAIS ---
    "dólar": "A moeda dos EUA. Quando ele sobe, tudo fica mais caro no Brasil.",
    "real": "A nossa moeda. Quando desvaloriza, nosso poder de compra diminui.",
    "euro": "A moeda usada em grande parte da Europa.",
    "candles": "Gráficos coloridos que mostram se o preço subiu ou desceu.",
    "porcentagem": "Uma forma de medir parte de um todo.",
    "compra e venda": "Negociar um ativo para tentar lucrar com a diferença de preço.",
    "moeda de troca": "Dinheiro ou qualquer coisa aceita para comprar outras.",
    "inflação": "Quando os preços sobem e o dinheiro compra menos.",
    "bolsa de valores": "Onde se negocia ações de empresas.",
    "ações": "Um pedacinho de uma empresa. Você vira sócio.",
    "renda fixa": "Investimentos com regras de remuneração definidas no momento da aplicação.",
    "renda variável": "Investimentos onde o ganho não é garantido.",
    "patrimônio": "A soma de tudo que você tem.",
    "diversificação": "Não colocar todos os ovos na mesma cesta.",
    "tese": "Seu plano de jogo e motivo para acreditar que um investimento vai dar certo.",
    "setores": "As categorias da economia (bancos, energia, varejo).",
    "lojas físicas": "Pontos de venda onde você vai pessoalmente comprar.",
    "lci": "Letra de Crédito Imobiliário: Investimento de renda fixa para o setor imobiliário, isento de IR.",
    "lca": "Letra de Crédito do Agronegócio: Investimento para o setor agro, isento de IR.",
    "pca": "Índice de Preços ao Consumidor: Mede a variação dos preços.",
    "ipca+": "IPCA mais: Investimento que paga taxa fixa + inflação (IPCA).",
    "pré-fixado": "Investimento com taxa de juros definida no momento da aplicação.",
    "selic": "A taxa que manda nos juros do brasil. Se ela sobe, tudo fica mais caro.",

}

palavra = st.text_input("digite o termo do mercado aqui").lower()

if palavra in dicionario:
    st.success(dicionario[palavra])
elif palavra != "":
    st.warning("Ainda não tenho essa. Me peça que eu adiciono!"),