@echo off
title Checking Python
py --version > nul 2>&1
if %errorlevel% equ 0 (
::VERIFICATION
title Python is installed, continuing in downloading REQUIREMENTS
echo [%TIME%]Python is installed. Version:
py --version
Timeout /t 2 >NUL

::REQUIREMENTS
title Installing SeleniumBase
echo [+] Installing SeleniumBase which will return you an useable driver! 
echo AFTER COPY THE DRIVER CHROMEDRIVER IN CURRENT DIRECTORY
pip install seleniumbase 
Timeout /T 3 >NUL
title Installing requests
pip install requests
Timeout /T 3 >NUL
title Installing requests
pip install pystyle
Timeout /T 3 >NUL
title Installing Pillow
pip install Pillow
Timeout /T 3 >NUL
title Installing Selenium
pip install selenium
Timeout /T 3 >NUL
echo Starting Main Code..
python QRCodeLoggerMain.py
pause
) else (
    title Python isnt installed.
    echo Python is not installed, please download this
    echo https://github.com/KDot227/PythonPathFixer
    echo and run main.bat
    pause
)
