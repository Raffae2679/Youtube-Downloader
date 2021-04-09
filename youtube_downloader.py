# Libs de web scrapping
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import os
from os import system, name
from time import sleep

# Lib para baixar videos do youtube
import pytube
# Lib para converter mp4 em mp3
from moviepy.editor import *


def baixar_video(link):
    '''Função responsável por baixar o vídeo'''

    print("Seu vídeo está sendo baixado!")

    try:
        youtube = pytube.YouTube(link)

        video = youtube.streams.filter(subtype='mp4').get_highest_resolution()

        video_baixado = video.download()

        clear()

    except Exception as err:
        print(err)
        sleep(10)
    
    else:
        input("Vídeo baixado com sucesso !!!")

        clear()

def baixar_musica(nome, link):
    '''Função responsável por baixar o vídeo e converte-lo para MP3'''
    print("Aguarde enquanto convertemos o vídeo para mp3...")

    try:
        youtube = pytube.YouTube(link)

        video = youtube.streams.filter(subtype='mp4').get_highest_resolution()

        video_baixado = video.download()

        mp4_file = procura_nome(nome)
        mp3_file = mp4_file[:-4]+".mp3"

        videoclip = VideoFileClip(mp4_file)

        audioclip = videoclip.audio

        audioclip.write_audiofile(mp3_file)

        audioclip.close()

        videoclip.close()

        os.remove(mp4_file)
    
    except Exception as err:
        print(err)
        sleep(10)

    else:
        input("Conversão realizada com sucesso!!!")

        clear()
	
def clear(): 
    '''Função auxiliar responsável por limpar o cmd'''
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def pesquisa():
    '''Função responsável por realizar a pesquisa no youtuber e raspar os dados para realizar o download'''

    url = "https://www.youtube.com/results?search_query="
    nome = ""
    esc_mus = False
    esc_down = False

    while(nome==""):
        nome = input("Qual nome do vídeo que você deseja baixar?\n > ")
        
        if nome=="":
            print("\nInsira um título que não seja em branco\n")

    nome.replace(" ", "+")

    url = url+nome

    option = Options()
    option.headless = True

    driver = webdriver.Chrome(ChromeDriverManager().install(), options = option)
    driver.get(url)

    sleep(5)


    ytb_nome = driver.find_elements_by_xpath('//*[@id="video-title"]/yt-formatted-string')[:5]
    ytb_link = driver.find_elements_by_xpath('//*[@id="thumbnail"]')[:5]

    clear()

    

    while(esc_mus==False):
        
        print("Resultados da Pesquisa: \n")
        for i in range(5):
            print(str(i+1)+"° : "+ytb_nome[i].text)

        print("\n")

        escolha = input("Se quiser refazer a pesquisa, digite 'R', caso não, basta digitar o número do vídeo para baixa-lo \n > " )

        if escolha in ["R","1","2","3","4","5"]:
            esc_mus = True

        else:
            clear()
            print("\nInsira uma entrada válida!\n")
            
          


    if escolha == "R":
        clear()

    else:
        escolha = int(escolha)-1
        clear()

        while(True):
            choice = input("Você deseja baixar o vídeo ou converter para mp3? \n 1: Baixar vídeo Mp4 \n 2: Converter o vídeo para mp3 \n > ")
            clear()
            if choice == "1":
                baixar_video(ytb_link[escolha].get_attribute('href'))
                break
                

            elif choice == "2":
                baixar_musica(ytb_nome[escolha].text, ytb_link[escolha].get_attribute('href'))
                break
            
            else:
                print("\nInsira uma entrada válida!\n")

def procura_nome(nome):
    '''Função responsável por procurar o arquivo de vídeo no diretorio que foi baixado para poder converter em mp3 '''

    files = os.listdir()

    for nomes in files:

        if nome[:20] in nomes:

            return nomes

def main():
	print(" =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ")
	print("|         Youtube Downloader            |")
	print(" =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ")
	print("|    Desenvolvido por Raffael Morais    |")
	print(" =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ")
	print("")

	pesquisa()


if __name__ == "__main__":
	
	while(True):
		main()



	
