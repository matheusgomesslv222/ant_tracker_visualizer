from cx_Freeze import setup, Executable

# Opções de construção para incluir arquivos necessários
build_exe_options = {
    # Inclua pacotes adicionais se necessário
    "include_files": ["serviceAccountKey.json", "icone.png", "dados.json"],  # Altere o caminho para os seus arquivos
}

executables = [Executable("ant_tracker.py", base="Win32GUI", icon="icone.ico")]

setup(
    name="MonitorApp",
    version="1.0",
    description="App que monitora um endpoint e salva no Firebase",
    options={"build_exe": build_exe_options},  # Adicione as opções de construção aqui
    executables=executables,
)
