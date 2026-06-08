import streamlit as st

st.title("Tradutor do Povo - Edição Elite")

dicionario = {
    # --- MACROECONOMIA ---
    "macroeconomia": "O estudo da economia de um país inteiro: inflação, desemprego e crescimento.",
    "câmbio": "O preço de uma moeda em relação a outra (quanto vale 1 dólar em reais).",
    "pib": "Tudo que o país produz de riqueza em um ano. É o 'tamanho' da economia.",
    "deflação": "O contrário da inflação: os preços caem (parece bom, mas pode indicar crise).",
    "deficit": "Quando o governo ou uma empresa gasta mais do que ganha.",
    "superavit": "Quando sobra dinheiro no fim das contas (o governo economizou).",
    "juros compostos": "Os juros que rendem sobre juros. É o que faz o dinheiro crescer rápido com o tempo.",
    
    # --- GEOPOLÍTICA ---
    "geopolítica": "Como a briga por poder e território entre países afeta a economia do mundo todo.",
    "hegemonia": "Quando um país (como os EUA ou China) domina os outros na política e na economia.",
    "sanção": "Um castigo econômico. Um país proíbe outro de vender ou comprar coisas para forçar um acordo.",
    "protecionismo": "Quando o governo cria barreiras para produtos de fora para proteger as empresas locais.",
    "globalização": "O mundo todo conectado: o que acontece na China impacta o seu café da manhã aqui.",
    
    # --- MERCADO FINANCEIRO (MAIS TERMOS) ---
    "bull market": "Quando a Bolsa está subindo forte e o pessoal está animado (mercado de touro).",
    "bear market": "Quando a Bolsa está caindo e o pessoal está com medo (mercado de urso).",
    "volatilidade": "O sobe e desce rápido dos preços. Mercado volátil é para quem tem estômago forte.",
    "alavancagem": "Operar com dinheiro emprestado para tentar lucrar mais. É arriscado demais.",
    "day trade": "Comprar e vender ativos no mesmo dia. É quase uma aposta, muito arriscado.",
    "dividendos": "Uma parte do lucro da empresa que ela divide com quem é dono das ações.",
    "hedge": "Uma proteção. Você investe em algo para não perder tudo caso outra coisa dê errado.",
    "liquidez": "A facilidade de transformar seu investimento em dinheiro vivo na mão agora.",
    "spread": "A diferença entre o preço de compra e venda. É o lucro de quem faz a troca."
}

palavra = st.text_input("digite o termo do mercado aqui").lower()

if palavra in dicionario:
    st.success(dicionario[palavra])
elif palavra != "":
    st.warning("Ainda não tenho essa. Me peça que eu adiciono!")