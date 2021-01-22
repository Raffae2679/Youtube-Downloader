# Youtube Downloader
Um script feito em python usando selenium e pytube. Fiz uso do selenium para web scrapping, permitindo pesquisar qual vídeo é o que desejado e poder baixá-lo. Já o pytube é uma lib que permite baixar vídeos do youtube.

## Como executar o script:

> Caso você não tenha um ambiente virtual configurado para o projeto, como um VirtualEnv ou Anaconda, recomendo configurar um para que todos os passos funcionem sem erros.

1. Clone o repositório no seu ambiente local
```
$ git clone https://github.com/Raffae2679/Youtube-Downloader.git
```
2. Acesse o diretório que foi criado/clonado
```
$ cd Youtube-Downloader
```
3. Instale os pacotes python que são requisitos para o `build` do sistema
```
$ pip install -r requirements.txt
```
4. Execute o script
```
$ python youtube_download.py
```

## Como funciona:
Após executar o script, o usuário deve passar o nome do vídeo a ser pesquisado, ele irá acessar o youtube e fazer uma busca com o nome que foi passado.
```
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|         Youtube Downloader            |
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|    Desenvolvido por Raffael Morais    |
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Qual nome do vídeo você deseja baixar? : faint
``` 

Depois disso, ele retornará os 5 primeiros resultados da lista e será perguntado qual vídeo o usuário deseja baixar. Caso tenha digitado algo errado, é possível digitar "R" e refazer a pesquisa sem nenhum problema. 
```
Resultados da Pesquisa:

1° : Faint (Official Video) - Linkin Park
2° : 07 Linkin Park - Faint
3° : Faint - Linkin Park (Lyrics)
4° : Linkin Park - Faint (Live From Madison Square Garden)
5° : Sum 41 - Faint [Linkin Park Cover] ft. Mike Shinoda [HD]


Se quiser refazer a pesquisa, digite 'R', caso não, basta digitar o número do vídeo para baixa-lo:
```
Quando o número for confirmado, ele dará inicio ao download do vídeo que será salvo na pasta onde o script está sendo executado. Finalizando o processo, ele mostrará uma mensagem de sucesso e perguntará se quer ver uma prévia do vídeo. A prévia funciona usando a lib cv2 para rodar o vídeo, mas ele não roda com áudio, é apenas os frames do vídeo passando. 
```
Vídeo baixado com sucesso !!!
Você deseja ver uma prévia do vídeo baixado (não tem som) ? (y/n):
```

## Próxima atualização:

Depois de ter conseguido finalizar a lógica do script, irei fazer uma interface gráfica para que fique mais agradável de se utilizar, usando o pysimplegui. Em breve estarei atualizando o repositorio.
