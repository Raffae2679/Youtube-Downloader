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

	print("Seu vídeo está sendo baixado!")

	youtube = pytube.YouTube(link)

	video = youtube.streams.filter(subtype='mp4').get_highest_resolution()

	video_baixado = video.download()

	clear()

	input("Vídeo baixado com sucesso !!!")

	clear()
	main()
	
def baixar_musica(nome, link):

	youtube = pytube.YouTube(link)

	video = youtube.streams.filter(subtype='mp4').get_highest_resolution()

	video_baixado = video.download()

	mp4_file = procura_nome(nome)
	mp3_file = mp4_file[:-4]+".mp3"

	print("Aguarde enquanto convertemos o vídeo para mp3...")

	videoclip = VideoFileClip(mp4_file)

	audioclip = videoclip.audio

	audioclip.write_audiofile(mp3_file)

	audioclip.close()

	videoclip.close()

	os.remove(mp4_file)

	input("Conversão realizada com sucesso!!!")

	clear()
	main()

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def main():
	print(" =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ")
	print("|         Youtube Downloader            |")
	print(" =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ")
	print("|    Desenvolvido por Raffael Morais    |")
	print(" =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ")
	print("")

	pesquisa()

def pesquisa():
	url = "https://www.youtube.com/results?search_query="


	nome = input("Qual nome do vídeo você deseja baixar? : ")
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

	print("Resultados da Pesquisa: \n")
	for i in range(5):
		print(str(i+1)+"° : "+ytb_nome[i].text)

	print("")
	print("")
	escolha = input("Se quiser refazer a pesquisa, digite 'R', caso não, basta digitar o número do vídeo para baixa-lo: " )


	if escolha == "R":
		clear()
		main()

	else:
		escolha = int(escolha)-1
		print("")
		
		choice = input("Você deseja baixar o vídeo ou converter para mp3? \n 1: Baixar vídeo Mp4 \n 2: Converter o vídeo para mp3 \n")
		clear()

		if choice == "1":
			baixar_video(ytb_link[escolha].get_attribute('href'))
		
		elif choice == "2":
			baixar_musica(ytb_nome[escolha].text, ytb_link[escolha].get_attribute('href'))

def procura_nome(nome):

	files = os.listdir()

	for nomes in files:

		if nome[:20] in nomes:

			return nomes






	
main()


	
