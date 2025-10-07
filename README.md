# YouTube Downloader (Áudio e Vídeo)

Este script em Python utiliza a biblioteca [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) para baixar vídeos ou áudios do YouTube com opções de qualidade e progresso do download exibido no terminal.

## Requisitos

- Python 3.6 ou superior
- Biblioteca `yt-dlp`

Instale o `yt-dlp` com:

```bash
pip install yt-dlp
```

Atualize o `yt-dlp` com:
```bash
py -m pip install -U yt-dlp
```
ou
```bash
pip install -U yt-dlp
```

---

## Como usar

1. Execute o script:

```bash
python seu_script.py
```

2. Escolha o tipo de mídia:

```
Deseja baixar em audio ou video? (audio ou video):
```

3. Insira a URL do vídeo do YouTube:

```
Insira uma url do youtube:
```

4. Se você escolheu vídeo, será solicitado a escolher a resolução desejada (ex: `720`, `1080`).

5. O progresso do download será exibido em tempo real no terminal.

6. Ao final, o arquivo será salvo na sua pasta `Downloads`.

---

## Funcionalidades

- Suporte a áudio (`m4a`, `best`) e vídeo (`mp4`)
- Escolha de qualidade de vídeo disponível (720p, 1080p, etc)
- Exibe progresso, velocidade e tempo restante do download
- Cabeçalhos HTTP simulando um navegador para evitar bloqueios regionais
---

## Estrutura de saída

Os arquivos são salvos em:

```
C:\Users\SeuNome\Downloads\
```

Com o nome:

```
[Título do Vídeo] [Qualidade].extensão
```

Exemplo:

```
MeuVideoFavorito [1080p].mp4
```
---
