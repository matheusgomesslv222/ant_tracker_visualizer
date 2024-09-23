from cx_Freeze import setup, Executable

executables = [Executable("ant_tracker.py", base="Win32GUI", icon="icone.ico")]

setup(
    name="MonitorApp",
    version="1.0",
    description="App que monitora um endpoint e salva no Firebase",
    executables=executables,
)
