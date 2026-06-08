import streamlit as st

st.title("Tradutor do Povo - Edição Elite")

dicionario = {
    # --- MACROECONOMIA ---
    "macroeconomia": "O estudo da economia de um país inteiro: inflação, desemprego e crescimento.",
    "câmbio": "O preço de uma moeda em relação a outra (quanto vale 1 dólar em reais).",
    "pib": "Tudo que o país produz de riqueza em um ano. É o 'tamanho' da economia.",
    "deflação": "O contrário da inflação: os preços caem.",
    "deficit": "Quando o governo ou uma empresa gasta mais do que ganha.",
    "superávit": "Quando sobra dinheiro no fim das contas.",
    "juros compostos": "Os juros que rendem sobre juros. É o que faz o dinheiro crescer rápido.",
    
    # --- GEOPOLÍTICA ---
    "geopolítica": "Como a briga por poder e território entre países afeta a economia.",
    "hegemonia": "Quando um país domina os outros na política e economia.",
    "sanção": "Um castigo econômico. Um país proíbe outro de vender ou comprar coisas.",
    "protecionismo": "Quando o governo cria barreiras para produtos de fora para proteger os de dentro.",
    "globalização": "O mundo todo conectado.",
    
    # --- MERCADO FINANCEIRO ---
    "bull market": "Quando a Bolsa está subindo forte.",
    "bear market": "Quando a Bolsa está caindo e o pessoal está com medo.",
    "volatilidade": "O sobe e desce rápido dos preços.",
    "alavancagem": "Operar com dinheiro emprestado para tentar lucrar mais.",
    "day trade": "Comprar e vender ativos no mesmo dia.",
    "dividendos": "Uma parte do lucro da empresa que ela divide com quem é dono das ações.",
    "hedge": "Uma proteção. Você investe em algo para não perder tudo caso outra coisa dê errado.",
    "liquidez": "A facilidade de transformar seu investimento em dinheiro vivo na mão.",
    "spread": "A diferença entre o preço de compra e venda.",
    
    # --- NOVOS TERMOS ---
    "dólar": "A moeda dos EUA. Quando ele sobe, tudo fica mais caro no Brasil.",
    "real": "A nossa moeda. Quando desvaloriza, nosso poder de compra diminui.",
    "euro": "A moeda usada em grande parte da Europa. Uma das mais fortes do mundo.",
    "candles": "Gráficos coloridos que mostram se o preço subiu ou desceu.",
    "porcentagem": "Uma forma de medir parte de um todo (ex: juros ou descontos).",
    "compra e venda": "Negociar um ativo para tentar lucrar com a diferença de preço.",
    "moeda de troca": "Dinheiro ou qualquer coisa aceita para comprar outras.",
    "inflação": "Quando os preços sobem e o dinheiro compra menos.",
    "bolsa de valores": "Onde se negocia ações de empresas.",
    "ações": "Um pedacinho de uma empresa. Você vira sócio.",
    "renda fixa": "Emprestar dinheiro para receber um valor combinado no futuro (mais seguro).",
    "renda variável": "Investimentos onde o ganho não é garantido (pode lucrar ou perder).",
    "patrimônio": "A soma de tudo que você tem (casa, carro, dinheiro).",
    "diversificação": "Não colocar todos os ovos na mesma cesta.",
    "tese": "Seu plano de jogo e motivo para acreditar que um investimento vai dar certo.",
    "setores": "As categorias da economia (bancos, energia, varejo).",
    "lojas físicas": "Pontos de venda onde você vai pessoalmente comprar."
}

palavra = st.text_input("digite o termo do mercado aqui").lower()

if palavra in dicionario:
    st.success(dicionario[palavra])
elif palavra != "":
    st.warning("Ainda não tenho essa. Me peça que eu adiciono!")