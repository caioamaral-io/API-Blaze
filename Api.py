import time
from bs4 import BeautifulSoup
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

# Configurações do bot Telegram
api_key = '?????????????????????????'
chat_id = '????????'
bot = telebot.TeleBot(token=api_key)

# Configurações do Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')
try:
    nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    nav.get('https://blaze.com/pt/games/double')
except WebDriverException as e:
    print(f"Erro ao iniciar o WebDriver: {e}")
    exit(1)

# Variáveis globais
analisar = False
gale_atual = 0
resultsDouble = []

def qualcor(x):
    if x == '0':
        return 'B'
    if x in ['1', '2', '3', '4', '5', '6', '7']:
        return 'V'
    if x in ['8', '9', '10', '11', '12', '13', '14']:
        return 'P'

def enviar_mensagem(texto):
    try:
        bot.send_message(chat_id=chat_id, text=texto)
    except Exception as e:
        print(f"Erro ao enviar mensagem para o Telegram: {e}")

def CHECK_VERSION(num):
    global analisar, gale_atual

    try:
        if not analisar:
            if num == ['V', 'V', 'P']:
                analisar = True
                enviar_mensagem('''
🤖 OPERAÇÃO CONFIRMADA

Entrar no: ( ⚫️ ) Preto
                ''')
                return
            if num == ['P', 'P', 'V']:
                analisar = True
                enviar_mensagem('''
🤖 OPERAÇÃO CONFIRMADA

Entrar no: ( 🔴 ) Vermelho
                ''')
                return

        elif analisar:
            if gale_atual == 0:
                if num == ['P', 'V', 'V']:
                    analisar = False
                    gale_atual = 0
                    enviar_mensagem('''
GREEN ✅✅✅✅
( ⚫️ )
                    ''')
                    return
                if num == ['V', 'P', 'P']:
                    analisar = False
                    gale_atual = 0
                    enviar_mensagem('''
GREEN ✅✅✅✅
( 🔴 )
                    ''')
                    return
                if num[-1] == 'B':  # Verifica se a última entrada é branca ('B')
                    analisar = False
                    gale_atual = 0
                    enviar_mensagem('''
LOSS⛔️⛔️⛔️
                    ''')
                    return
                if num == ['V', 'V', 'V'] or num == ['P', 'P', 'P']:
                    gale_atual += 1
                    print('⚠️VAMOS PARA O GALE 1⚠️')
                    return

            elif gale_atual == 1:
                if num == ['P', 'V', 'V']:
                    analisar = False
                    gale_atual = 0
                    enviar_mensagem('''
GREEN ✅✅✅✅
( ⚫️ )
                    ''')
                    return
                if num == ['V', 'P', 'P']:
                    analisar = False
                    gale_atual = 0
                    enviar_mensagem('''
GREEN ✅✅✅✅
( 🔴 )
                    ''')
                    return
                if num[-1] == 'B':  # Verifica se a última entrada é branca ('B')
                    analisar = False
                    gale_atual = 0
                    enviar_mensagem('''
LOSS⛔️⛔️⛔️
                    ''')
                    return
                if num == ['V', 'V', 'V'] or num == ['P', 'P', 'P']:
                    gale_atual += 1
                    print('⚠️VAMOS PARA O GALE 2⚠️')
                    return

            elif gale_atual == 2:
                if num == ['P', 'V', 'V']:
                    analisar = False
                    gale_atual = 0
                    enviar_mensagem('''
GREEN ✅✅✅✅
( ⚫️ )
                    ''')
                    return
                if num == ['V', 'P', 'P']:
                    analisar = False
                    gale_atual = 0
                    enviar_mensagem('''
GREEN ✅✅✅✅
( 🔴 )
                    ''')
                    return
                if num[-1] == 'B':  # Verifica se a última entrada é branca ('B')
                    analisar = False
                    gale_atual = 0
                    enviar_mensagem('''
LOSS⛔️⛔️⛔️
                    ''')
                    return
                if num == ['V', 'V', 'V'] or num == ['P', 'P', 'P']:
                    analisar = False
                    gale_atual = 0
                    enviar_mensagem('''
LOSS⛔️⛔️⛔️
                    ''')
                    return
    except Exception as e:
        print(f"Erro no CHECK_VERSION: {e}")

def get_results():
    try:
        # Tenta encontrar o elemento com retries
        element = WebDriverWait(nav, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="roulette-timer"]/div[1]'))
        )
        return element.text
    except (StaleElementReferenceException, TimeoutException) as e:
        print(f"Erro ao tentar obter o resultado: {e}")
        return None

while True:
    try:
        resulROOL = get_results()
        if resulROOL is None:
            print('ERRO 404')
            continue

        if resulROOL == 'Girando...':
            print('Analisando')
            time.sleep(13)
            c = nav.page_source
            resultsDouble.clear()

            soup = BeautifulSoup(c, 'html.parser')
            go = soup.find('div', class_="entries main")
            for i in go:
                if i.getText():
                    resultsDouble.append(i.getText())
                else:
                    resultsDouble.append('0')

            resultsDouble = resultsDouble[:-1]

            default = resultsDouble[0:3]
            mapeando2 = map(qualcor, default)
            finalcor = list(mapeando2)

            CHECK_VERSION(finalcor)
            print(finalcor)
    except Exception as e:
        print(f"Erro na execução principal: {e}")
        time.sleep(5)  # Aguarda antes de tentar de novo