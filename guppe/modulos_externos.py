"""
Módulos externos

Utilizamos o gerenciador de pacotes PIP (Python Installer package) para instalar módulos  externos
http://pypi.org

Para atualizar o pip: pip install --upgrade pip

Colorama -> utlizado para permitir impressão de textos coloridos no terminal

# Utilizando o pacote instalado
from colorama import init, Fore, Back
init()
print(Fore.RED + 'Vermelho')
print(Fore.MAGENTA + 'Magenta')
print(Fore.BLUE + 'Azul')
print(Back.RED + 'Vermelho')
print(Back.MAGENTA + 'Magenta')
print(Back.BLUE + 'Azul')
"""
# Utilizado pacote pdf

import pydf

pdf = pydf.generate_pdf('<h1> Geek University<h1>')#, Path="C:/Users/hitss/PycharmProjects/guppe/teste.pdf")
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)


""""
ef generate_pdf(html, *,
                 cache_dir: Path=DFT_CACHE_DIR,
                 grayscale: bool=False,
                 lowquality: bool=False,
                 margin_bottom: str=None,
                 margin_left: str=None,
                 margin_right: str=None,
                 margin_top: str=None,
                 orientation: str=None,
                 page_height: str=None,
                 page_width: str=None,
                 page_size: str=None,
                 image_dpi: str=None,
                 image_quality: str=None,
                 **extra_kwargs):
"""
