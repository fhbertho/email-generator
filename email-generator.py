import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import webbrowser
import random
import random



# Lista de nomes
#with open('camimnhodoarquivodetexto.txt', 'r') as file:
    #nomes = [line.strip() for line in file]

# Lista de sobrenomes
#with open('caminhodoarquivodetexto.txt', 'r') as file:
    #sobrenomes = [line.strip() for line in file]


# Lists of names and surnames
#names = ['John', 'Emily', 'Michael', 'Sarah', 'David', 'Olivia', 'Ethan', 'Avery', 'Daniel', 'Grace']
#surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']



# Generate random names, surnames and email addresses
##for i in range(1):
    # Randomly select a name and surname
    #name = random.choice(names)
    #surname = random.choice(surnames)

    # Combine the name and surname to create a full name
    #full_name = f"{name} {surname}"



    # Print the generated name, surname and email address
    #print(f"Name: {name}\nSurname: {surname}")

#step1: Digitar a data a ser inserida no checklist
#step2: Modificar o texto que será inserido pela data que foi inputada pelo usuario
#step3: Seleção e abertura do browser.
#step4: selação do caminho do elemento para abertura do checklist.
#step5: seleção dos campos que serão inputados os dados.
#step6: Salvamento dos dados inputados.

nome1 = str(input("Digite o nome a ser usado para a conta: "))
sobrenome_1 = str(input("Digite o sobrenome a ser usado para a conta: "))
email_1 = str(input("Digite o e-mail a ser usado para a conta: "))
senha_1 = input("Digite a senha para a conta: ")



driver = webdriver.Firefox()
driver.get("https://www.gmail.com")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li[1]').send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/input').send_keys(nome1 + Keys.ENTER)
time.sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input').send_keys(sobrenome_1 + Keys.ENTER)
time.sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input').send_keys(email_1 + Keys.ENTER)
time.sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(senha_1+ Keys.ENTER)
time.sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(senha_1+ Keys.ENTER)
time.sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').send_keys(Keys.ENTER)



print("Seu e-mail é {} e sua senha utilizada para este e-mail é: {}".format(email_1, senha_1))


#driver.execute_script("window.open('https://www.github.com', '_blank');")
#driver.execute_script("window.open('https://www.gmail.com', '_blank');")
#driver.execute_script("window.open('https://www.tryhackme.com', '_blank');")
#driver.execute_script("window.open('https://www.news.google.com', '_blank');")



x = input("Digite qualquer tecla para sair: ")







