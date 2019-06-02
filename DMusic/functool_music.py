from os import chdir, getcwd
from termcolor import cprint

caminho_music = '/home/desnown/Music/'
caminho_proj = getcwd()
chdir(caminho_proj)

def namefile(file):
    '''Retorna o nome da musica mas sem a extensao.
    '''
    file = file.replace('\n', '')

    try:
        return file.split('.')[0]
    except Exception as error:
        cprint(error, 'red', attrs=['bold'])


def search_music_path(pasta='~'):
    '''Funcao responsavel por procurar todos os arquivos de musicas
    `.wav; .ogg; .mp3; .m4a`  na pasta e retorna-los.
    '''

    from os import listdir
    from glob import glob

    all_musics = []
    _extensoes = ['*.wav', '*.ogg', '*.mp3', '*.m4a']

    try:
        #Este caminho nn é o correto( argumento pasta é o correto)
        #Vai ser arrumado posteriormente usando o filechooser(kivy)
        chdir(home_user()+'/Musicas')
    except:
        pass

    try:
        chdir(home_user()+'/Musics')
    except:
        pass

    try:
        chdir(home_user()+'/Music')    
    except Exception as error:
        cprint(error, 'red', attrs=['bold'])
        
    _all_files = listdir()

    for ext in _extensoes:
        _file = glob(ext)
        if _file == []:
            continue

        for music in _file:
            all_musics.append(music)
        
    return all_musics


def search_music(music):
    '''Funcao responsavel por procurar uma musica(arg) dentro do arquivo
    - Songs.txt - e retorna-lo(caso ele esteja la dentro).
    '''

    # if music
    with open(f'{caminho_proj}/Songs.txt') as _file:
        for lin in _file:
            if music in lin:
                return lin.replace('\n', '') 


def read_file(pasta='./'):
    '''Funcao responsavel por ler o que tem dentro do arquivo(arg)
    e retorna-lo.
    '''    
    

    with open(f'{caminho_proj}/Songs.txt') as read_lin:
        return read_lin.readlines()


def shorten_music(music):
    music = namefile(music)
    if len(music) > 30:
        return music[:30]+'...'

    return music


def home_user(path='~'):
    from os.path import expanduser
    return expanduser(path)