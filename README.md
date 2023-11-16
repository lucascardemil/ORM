# Instalación de Python
Este repositorio contiene instrucciones para instalar Python en sistemas Windows y macOS.

## Windows
Pasos para la instalación:
Descargar Python:

### Visita el sitio web oficial de Python en python.org.
Haz clic en la pestaña "Downloads" y selecciona la versión más reciente de Python para Windows.
Iniciar el instalador:

### Una vez descargado, ejecuta el instalador de Python.
Asegúrate de marcar la casilla "Add Python to PATH" durante la instalación.
Configuración:

### Sigue las instrucciones del instalador.
Puedes dejar las opciones predeterminadas o personalizar según tus necesidades.
Verificar la instalación:

Abre la línea de comandos (cmd) y ejecuta el siguiente comando:
```
python --version
```

## macOS
Pasos para la instalación:
### Instalar Homebrew:
Abre la terminal y ejecuta el siguiente comando para instalar Homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Instalar Python:
Usa Homebrew para instalar Python. Ejecuta el siguiente comando:
```
brew install python
```

### Verificar la instalación:
Después de la instalación, verifica la versión de Python con el siguiente comando:
```
python3 --version
```


## Para probra el programa hay que instalar las dependecias.
```
pip install flet imutils numpy opencv-python
```
Despues de instalar, se debe ejecutar el archivo main.py, si tienes instalado vscode lo puedes hacer mediante de la flecha arriba a la derecha. o mediante este comando.
```
python main.py
```
