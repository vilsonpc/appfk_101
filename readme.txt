// Instalação do Venv
python -m pip install --user virtualenv

// Atualizar o PIP
python -m pip install --upgrade pip

// Para instalar pacotes com as permissões de user
python -m pip install --user <comando>

// Criar Ambiente Virtual Venv para o Project Lib 
python -m venv .vwin

// Ativar o Ambiente Windows(PowerShell ou Visual Studio)
.\.vwin\Scripts\Activate.ps1

// Instalar os Pacotes e dependências: 
pip install requests
pip install -U Flask

// Imprimir todos os pacotes instalados.
pip freeze > requirements.txt

// Formato das Pastas e Arquivos do Projeto

	/.vwin -> Ambiente Virtual VENV
	/models -> Drives
	/static -> Arquivos CSS, JS e Images + Bootstrap
	/templates -> Páginas HTML
	/tmp -> Arquivos Temporários
	.gitignore -> Arquivos e Pastas que devem ser ignorados pelo repositório Git
	app -> API
	readme.txt -> Arquivo de Ajuda
	requirements -> Pacotes e dependências
	