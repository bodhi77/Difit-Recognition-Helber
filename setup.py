import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["cv2", "numpy", "tensorflow"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Digit Recognition",
    version="1.0",
    description="Description of your program",
    options={"build_exe": build_exe_options},
    executables=[Executable("Digit_recognition.py", base=base)]
)
