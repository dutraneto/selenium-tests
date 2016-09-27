from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Enderecos():
    def devolve_localhost(self):
        URL = 'localhost:8000'
        return URL

    #devolve url passando /pessoa/ + id
    def devolve_view(self, view=None, id=None):
        self.view = view
        self.id = id
        return self.devolve_localhost() + '/' + self.view + '/' + self.id

    #deve inserir dados da pessoa por aqui para criar um cadastro novo
    def devolve_dados_pessoa(self, *args):

        args = [
            'ADRIANO OLIVEIRA', #digite o nome
            'VILA MILITAR', #endereco
            '123456' #cpf
        ]
        return args

    # deve inserir dados da pessoa por aqui para editar um cadastro
    def devolve_dados_pessoa_editado(self, *args):
        args = [
            'WALL CARNEIRO', #nome
            'PANTANAL', #endereco
            '000000000' #cpf
        ]
        return args


class TestCadastroPessoas(TestCase):

    def setUp(self):
        EXECUTABLE_PATH = '/Users/DutraNeto/bin/chromedriver'
        self.driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)

    def test_deve_achar_title(self):
        url = Enderecos()
        self.driver.get(url.devolve_localhost())
        try:
            title = self.driver.title

        except FileNotFoundError:
            print('assert 1 não Passou')
        else:
            self.assertTrue('Pertences', title)
            print('Assert 1 >>> PASSOU')

    def test_deve_inserir_pessoa(self):
        url = Enderecos()
        self.driver.get(url.devolve_localhost())
        try:
            #pega ids
            cadastro = self.driver.find_element_by_link_text('Cadastrar')
            cadastro.click()
            nome = self.driver.find_element_by_id('id_nome_pessoa')
            endereco = self.driver.find_element_by_id('id_endereco')
            cpf = self.driver.find_element_by_id('id_cpf')
            botao = self.driver.find_element_by_class_name('botao')

            #insere pegando os indices de args de devolve_dados_pessoa()
            nome.send_keys(url.devolve_dados_pessoa().pop(0))
            endereco.send_keys(url.devolve_dados_pessoa().pop(1))
            cpf.send_keys(url.devolve_dados_pessoa().pop(2))
            botao.click()
            pega_html = self.driver.page_source
        except FileNotFoundError:
            print("não foi cadastrado")
        else:
            #verifica se o nome da pessoa foi inserido
            self.assertIn(str(url.devolve_dados_pessoa().pop(0)), pega_html)
            print('Assert 2 >>> PASSOU')

    def test_deve_editar_cadastro(self):
        url = Enderecos()
        self.driver.get(url.devolve_view('pessoa', '9')) # passa o ID
        # verifica se existe cadastro
        try:
            #abre edita cadastro

            botao = self.driver.find_element_by_class_name('botao')
            botao.click()

            #altera nome
            nome = self.driver.find_element_by_id('id_nome_pessoa')
            endereco = self.driver.find_element_by_id('id_endereco')
            cpf = self.driver.find_element_by_id('id_cpf')
            nome.clear()
            endereco.clear()
            cpf.clear()
            nome.send_keys(url.devolve_dados_pessoa_editado().pop(0)) #extrai o nome da pessoa da lista
            endereco.send_keys(url.devolve_dados_pessoa_editado().pop(1)) #extrai o endereco da lista
            cpf.send_keys(url.devolve_dados_pessoa_editado().pop(2)) #extri o cpf
            cpf.send_keys(Keys.RETURN)
            pega_html = self.driver.page_source
        except FileNotFoundError:
            print("Teste 3 Não passou")
        else:
            #verifica se o nome foi alterado
            self.assertIn(str(url.devolve_dados_pessoa_editado().pop(0)), pega_html)
            print('Assert 3 >>> PASSOU')

    def test_deve_excluir_cadastro(self):
        url = Enderecos()
        html_antes = self.driver.page_source
        try:
            self.driver.get(url.devolve_view('pessoa', '72')) #escolher o id para mudar
        finally:
            print('Pegou id')

        try:
            botao = self.driver.find_element_by_id('id_botao_excluir')
        finally:
            print('Excluido')
        botao.click()
        self.driver.switch_to.alert.accept()
        if self.driver.switch_to.alert:
            self.driver.switch_to.alert.accept()
        else:
            print('Exclusao realizada')
        html_depois = self.driver.page_source
        self.assertHTMLNotEqual(html1=html_antes, html2=html_depois)
        print('Assert 4 >>> PASSOU')

    def tearDown(self):
        self.driver.close()


