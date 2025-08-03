import os
from pathlib import Path
from yt_dlp import YoutubeDL 

continuar = 's'
tipo_midia = ''
formato = ''
qualidade = ''

def mostrar_progresso(d):
    if d['status'] == 'downloading':
        porcentagem = d.get('_percent_str', '').strip()
        velocidade = d.get('_speed_str', '').strip()
        tempo_restante = d.get('_eta_str', '').strip()
        print(f"\rProgresso: {porcentagem}. Velocidade: {velocidade}. Tempo: {tempo_restante}.", end='', flush=True)
    elif d['status'] == 'finished':
        print(f"\nDownload concluído! Arquivo salvo em: {d['filename']}")

def gerar_ydl_opts(format_str=None):
    ydl_opts = {
        'noplaylist': True,
        'quiet': True,
        'geo_bypass': True,
        'sleep_interval': 2,
        'max_sleep_interval': 5,
        'retries': 10,
        'ignoreerrors': True,
        'throttled_rate': '500K',
        'concurrent_fragment_downloads': 3,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
        }
    }

    if format_str:
        ydl_opts['format'] = format_str
        ydl_opts['outtmpl'] = str(Path.home() / "Downloads" / '%(title)s [%(height)sp].%(ext)s')
        ydl_opts['progress_hooks'] = [mostrar_progresso]

    return ydl_opts

os.system('cls')
while tipo_midia not in ('audio', 'video'):
    tipo_midia = input("\nDeseja baixar em audio ou video? (audio ou video): ").lower()
    if tipo_midia not in ('audio', 'video'):
        print("\nTipo de mídia inválido. Digite 'audio' ou 'video'.")

while continuar.lower() in ('s', 'sim'):
    os.system('cls')
    url = input("Insira uma url do youtube: ")

    try:
        ydl_opts = gerar_ydl_opts()
        with YoutubeDL(ydl_opts) as ydl: 
            info = ydl.extract_info(url, download=False)
            if not info:
                print("\nNão foi possível obter informações. Verifique a URL.")
                continuar = input("\nDeseja tentar outra URL? (sim ou nao): ")
                continue

            print(f"\nNome: {info['title']}")

            if tipo_midia == 'audio':
                formato = 'm4a/bestaudio/best'
            elif tipo_midia == 'video':

                lista_qualidades = []
                for idx, f in enumerate(info['formats']):
                    if f.get('format_note') != None and f.get('vcodec') != 'none' and f.get('ext') == 'mp4':
                        res = f.get('format_note').replace('p', '')
                        if res not in lista_qualidades:
                            lista_qualidades.append(res)
                    
                print("\nQualidades disponíveis para vídeo: ", end='')

                for idx, valor in enumerate(lista_qualidades):
                        if idx == len(lista_qualidades) - 1:
                            print(f"{valor}p.", end='')
                        else:
                            print(f"{valor}p, ", end='')
            
                qualidade = input(f"\nDigite a resolução/qualidade de video desejada: ").replace('p', '').strip()
                
                if qualidade in lista_qualidades:
                    formato = f'bestvideo[height={qualidade}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'
                else:
                    print(f"\nResolução {qualidade}p não encontrada. Tente novamente.")
                    continuar = input("\nDeseja tentar novamente? (sim ou nao): ")
                    if continuar.lower() in ('s', 'sim'):
                        continue
                    else:
                        break

        ydl_opts = gerar_ydl_opts(format_str=formato)

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    except Exception as e:
        print("Outro erro ocorreu:", e)

    continuar = input("\nDeseja continuar baixando? (sim ou nao): ")