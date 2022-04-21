import sys
from cx_Freeze import setup, Executable

build_exe_option = {"packages": ["gen_password.py"],
                    "includes": ["PySimpleGUi", "os", "random"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Gerador de Senhas",
    vesion="0.1",
    description="Gera senhas de acordo com o número de caracteres selecionados pelo usuário.",
    option={"build_exe": build_exe_option},
    executables=[Executable("gen_password.py", base=base)]
)
