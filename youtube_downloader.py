# Libs de web scrapping
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from os import system, name 
from time import sleep

# Lib para baixar videos do youtube e lib para executar vídeo
import pytube
import cv2



def baixar_video(link):

	print("Seu vídeo está sendo baixado!")

	youtube = pytube.YouTube(link)

	video = youtube.streams.order_by('resolution').desc().first()

	video_baixado = video.download()

	clear()

	print("Vídeo baixado com sucesso !!!")

	escolha = input("Você deseja ver uma prévia do vídeo baixado (não tem som) ? (y/n): ")

	if escolha == "y":
		previa_video(video_baixado)

	else:
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
		clear()
		baixar_video(ytb_link[escolha].get_attribute('href'))

def previa_video(video):

	try:
		cap = cv2.VideoCapture(video)
		ret, frame = cap.read()
		while(1):
			ret, frame = cap.read()
			cv2.imshow('frame',frame)
			if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
				cap.release()
				cv2.destroyAllWindows()
				main()
				break
			cv2.imshow('frame',frame)
	except:
		input("Infelizmente não foi possivel executar o vídeo!!! \n Peço desculpas pelo problema.")
		clear()
		main()

	




main()


