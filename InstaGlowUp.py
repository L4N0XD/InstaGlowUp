from tkinter import E
from random import choice, randint, random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By  
from time import sleep
import random
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)

class InstaGlowUpBot:
    def __init__(self, user, passw):
        self.username = user
        self.password = passw
        user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36/8mqULwuL-67", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36/8mqPtVuL-9", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Agency/90.8.1597.98", "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4870.181 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36/8mqEpSuL-47", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36/0cqIF4Ef-13", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4859.172 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0. 4844.82 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4864.133 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/0ADF80FA", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2696.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4698.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36 GLS/97.10.6229.30", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Config/95.2.8641.42", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 AtContent/93.5.2274.75", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Config/96.2.9111.12", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36 GLS/95.10.1539.40", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36/8mqXoXuL-32", "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.114 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML,likeGecko) Chrome/98.0.4758.82 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.9 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4753.0 Safari/537.36"]
        user_agent = random.choice(user_agent_list)
        options = webdriver.ChromeOptions()
        # specify the desired user agent
        options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Chrome(chrome_options=options)
       
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        sleep(randint(3, 8))

        usu??rio = driver.find_element(By.XPATH, "//input[@name='username']")
        usu??rio.click() # Clica em usu??rio.
        usu??rio.clear() # Limpa a caixa de usu??rio.
        usu??rio.send_keys(self.username) # Digita o usu??rio informada.

        senha = driver.find_element(By.XPATH, "//input[@name='password']")
        senha.click() # Clica em senha
        senha.clear() # Limpa a caixa de senha
        senha.send_keys(self.password) # Digita a senha.
        sleep(randint(1, 4))
        senha.send_keys(Keys.RETURN) # "Enter".
        sleep(randint(1, 6)) # Tempo para iniciar a p??ixima etapa. 

        self.CommentPost()   

    def more_comment(self):
        driver = self.driver
        mais_comentarios = int(input('Digite (1) se deseja comentar mais vezes e (2) para encerrar. ')) # Define se encerra ou reinicia o programa.
        if (int(mais_comentarios == 1)):
            self.escolha()
        elif (int(mais_comentarios == 2)):
            print ('Encerrando programa...')
            driver.close()
            exit()
            
    @staticmethod
    def digita????o(frase, coment1): # Digita letra por letra
        for letra in frase:
            coment1.send_keys(letra)
            sleep(randint(4, 8) / 30)
            
    def CommentPost(self):
        driver = self.driver
        sleep(randint(2, 4))
        link_postagem = str(input('Insira o link da postagem: '))
        driver.get(f'{link_postagem}') # Link da postagem receber?? os comentarios. 
       
        self.escolha()

    def escolha(self):
        driver = self.driver
        sleep(randint(3, 4))    
        coment??rios = ['comentario1','comentario2','comentario3'] # Lista de coment??rios
        num_coment??rios = int(input('Digite o n??mero de coment??rios que deseja realizar: ')) 
        num_pessoas = int(input('Digite o n??mero pessoas a serem marcadas por coment??rio (1) ou (2): '))
        print ('\n\n')
        print ('Iniciando Coment??rios...')      
        pessoas = int(num_pessoas) 

    
        if (int(pessoas == 1)):
            for u in range(1, num_coment??rios + 1): # numero de comentarios a ser realizados 
                driver.find_element(By.CLASS_NAME, "_ablz._aaoc").click() # Clica em "Coment??rio"
                comentario = driver.find_element(By.CLASS_NAME, "_ablz._aaoc")
                sleep(randint(2, 6))

                self.digita????o(choice(coment??rios), comentario) # Digita o coment??rio no campo
                sleep(randint(3, 9))

                driver.find_element(By.CLASS_NAME, "_aacl._aaco._aacw._aad0._aad6._aade").click() # Publica a postagem.
                sleep(randint(1, 2))
                try: 
                    driver.find_element(By.XPATH, "//p[@class='_abmp']") # Procura possivel bloqueio
                    print('Possivel bloqueio detectado.')
                    encerrar = int(input('Deseja tentar novamente? (1)Sim (2)N??o: '))
                    if (encerrar == 1):
                        driver.find_element(By.CLASS_NAME, "_aacl._aaco._aacw._aad0._aad6._aade").click() # Publica a postagem.
                        sleep(randint(1, 2))
                        try: 
                            driver.find_element(By.XPATH, "//p[@class='_abmp']") # Procura possivel bloqueio novamente ap??s tentar novamente publicar.
                            print('Bloqueio detectado!\nEncerrando programa!') # Se encotrado bloqueio ap??s segunda tentativa, encerra o programa.
                            driver.close()
                            exit()
                        except NoSuchElementException:
                            print(f'Coment??rios postados: {u}')
                    else:
                        print ('Encerrando programa!')   
                        driver.close()
                        exit()
                except NoSuchElementException: 
                    print(f'Coment??rios postados: {u}')

                if (int(u != num_coment??rios)):
                    sleep(randint(30, 60))
                else: 
                    print(f'Todos os coment??rios foram realizados.\n\n')
                    self.more_comment()          
        
        elif (int(pessoas == 2)):
                
            for u in range(1, num_coment??rios + 1): # numero de comentarios 
                driver.find_element(By.CLASS_NAME, "_ablz._aaoc").click() # Clica em "Coment??rio"
                comentario = driver.find_element(By.CLASS_NAME, "_ablz._aaoc")
                sleep(randint(4, 9))

                self.digita????o(choice(coment??rios), comentario) # Digita o coment??rio no campo
                sleep(randint(3, 8))
                self.digita????o((" "), comentario) # Digita espaco no campo
                sleep(randint(1, 3))
                self.digita????o(choice(coment??rios), comentario) # Digita o coment??rio no campo
                sleep(randint(4, 10)) 
                
                driver.find_element(By.CLASS_NAME, "_aacl._aaco._aacw._aad0._aad6._aade").click() # Publica a postagem.
                sleep(randint(1, 2))
                try: 
                    driver.find_element(By.XPATH, "//p[@class='_abmp']")
                    print('Possivel bloqueio detectado.\n Encerrando programa!')
                    encerrar = int(input('Deseja tentar novamente? (1)Sim (2)N??o: '))
                    if (encerrar == 1):
                        driver.find_element(By.CLASS_NAME, "_aacl._aaco._aacw._aad0._aad6._aade").click() # Publica a postagem.
                        sleep(randint(1, 2))
                        try: 
                            driver.find_element(By.XPATH, "//p[@class='_abmp']") # Procura possivel bloqueio ap??s tentar novamente.
                            print('Bloqueio detectado!\nEncerrando programa!') # Se encotrado bloqueio ap??s segunda tentativa, encerra o programa.
                            driver.close()
                            exit()
                        except NoSuchElementException:
                            print(f'Coment??rios postados: {u}')                            
                    else:
                        print ('Encerrando programa!')                          
                        driver.close()
                        exit()
                except NoSuchElementException: 
                    print(f'Coment??rios postados: {u}')

                if (int(u != num_coment??rios)):
                    sleep(randint(25, 62))
                else: 
                    print(f'Todos os coment??rios foram realizados.\n\n')
                    self.more_comment()
                
                                    
        else:
            print ('Ainda n??o temos essa funcionalidade. Em breve!')
            print ('Redirecionando...')
            self.escolha()
     
InstaGlowUpBot = InstaGlowUpBot('usuario', 'senha') # Adicione aqui o seu usu??rio e senha.
InstaGlowUpBot.login()
