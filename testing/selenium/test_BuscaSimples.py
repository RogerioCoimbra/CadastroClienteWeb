# Importa o framework de testes pytest
import pytest

# Importa a biblioteca para trabalhar com tempo
import time

# Importa a biblioteca para trabalhar com JSON
import json

# Importa o módulo do Selenium para controlar o navegador
from selenium import webdriver

# Importa o módulo para localizar elementos na página pelo tipo (ID, CSS, etc.)
from selenium.webdriver.common.by import By

# Importa o módulo para realizar ações como cliques e movimentos do mouse
from selenium.webdriver.common.action_chains import ActionChains

# Importa o módulo para trabalhar com condições esperadas (ex.: esperar que um elemento esteja visível)
from selenium.webdriver.support import expected_conditions

# Importa o módulo para esperar elementos na página
from selenium.webdriver.support.wait import WebDriverWait

# Importa o módulo para simular pressionamento de teclas no teclado
from selenium.webdriver.common.keys import Keys

# Importa o módulo para configurar capacidades desejadas do navegador
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Define uma classe para agrupar os testes
class TestBuscaCompleta():
  
  # Função executada automaticamente antes de cada teste para configurar o navegador
  def setup_method(self, method):
    # Configurações para o navegador Chrome
    options = webdriver.ChromeOptions()

    # Adiciona uma opção para manter o navegador aberto após o teste
    options.add_experimental_option("detach", True)

    # Inicia o navegador Chrome com as opções configuradas
    self.driver = webdriver.Chrome(options=options)

    # Cria um dicionário vazio para armazenar variáveis, se necessário
    self.vars = {}
  
  # Função executada automaticamente após cada teste para fechar o navegador (comentada no momento)
  # def teardown_method(self, method):
    # Fecha o navegador
    # self.driver.quit()
  
  # Função que realiza o teste de busca simples
  # Toda função de teste deve começar com "test_"
  def test_BuscaSimples(self):
    # Abre o navegador na URL especificada
    self.driver.get("http://localhost:8080/browse-users.php")

    # Maximiza a janela do navegador para melhor visualização
    self.driver.set_window_size(1552, 832)

    # Clica no campo de texto com o ID "nome"
    self.driver.find_element(By.ID, "nome").click()

    # Digita "Ma" no campo de texto com o ID "nome"
    self.driver.find_element(By.ID, "nome").send_keys("Ma")
    
    '''
    # (Comentado) Clica no campo de texto com o ID "email"
    self.driver.find_element(By.ID, "email").click()

    # (Comentado) Digita um email no campo de texto com o ID "email"
    self.driver.find_element(By.ID, "email").send_keys("RogerioCoimbra@gmail.com")

    # (Comentado) Clica no campo de texto com o ID "telefone"
    self.driver.find_element(By.ID, "telefone").click()

    # (Comentado) Digita "333" no campo de texto com o ID "telefone"
    self.driver.find_element(By.ID, "telefone").send_keys("333")

    # (Comentado) Clica no campo de texto com o ID "df" (data inicial)
    self.driver.find_element(By.ID, "df").click()

    # (Comentado) Digita uma data inicial no campo de texto com o ID "df"
    self.driver.find_element(By.ID, "df").send_keys("2021-01-01")

    # (Comentado) Clica no campo de texto com o ID "dt" (data final)
    self.driver.find_element(By.ID, "dt").click()

    # (Comentado) Digita uma data final no campo de texto com o ID "dt"
    self.driver.find_element(By.ID, "dt").send_keys("2025-01-01")
    '''

    # Clica no botão de envio do formulário identificado pelo seletor CSS "#submit > .fa"
    self.driver.find_element(By.CSS_SELECTOR, "#submit > .fa").click()

