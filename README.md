# courses 🐱‍💻
# Clase de Criptografía y Criptoanálisis

En este repositorio se incluyen los materiales necesarios para las clases de másters, concretamente para la clase de Criptografía y Criptoanálisis.

Para dicha clase hay que bajarse los materiales de la carpeta correspondiente. Además, dejo por aquí los comandos que emplearemos por si es más sencillo que estar poniéndolos a mano.

## 1. Cómo encontrar la ruta del fichero rockyou en kali linux
```bash
$ find /usr/share -name "rockyou*"
```

## 2. Instalar pdfcrack en kali
```bash
  $ sudo apt update
  $ sudo apt install pdfcrack
```

## 3. Usar pdfcrack para romper la contraseña de un pdf empleando un diccionario 
```bash
  $ pdfcrack -w rockyou.txt Informe\ confidencial.pdf
```

## 4. Identificar con qué ficheros funciona john
```bash
  $ ls  /usr/sbin | grep 2john
```

De hecho también funciona con ficheros office: https://github.com/openwall/john/blob/bleeding-jumbo/run/office2john.py

## 5. 1. Johntheripper parte 1: ¿dónde está la contraseña?
```bash
  $ pdf2john Informe\ confidencial.pdf > informe.txt
```

## 5. 2. Johntheripper parte 2: rompe la contraseña usando el diccionario por defecto de john
```bash
  $ john informe.txt
```

## 5. 3. Johntheripper parte 3: usar john para fuerza bruta
```bash
   $ john --incremental secreto.txt
```

## 6. Hydra

Hydra es una herramienta que ayuda a realizar ataques de fuerza bruta contra sistemas expuestos.
Por ejemplo, se pueden atacar equipos que tengan servidores VNC a partir de un listado de contraseñas que podemos tener en un fichero `passwords.txt`.

```bash
   $  hydra -P passwords.txt -t 2 <DIRECCION_IP>:<PUERTO>
```

En este ejemplo, se indica con `-P` mayúscula un fichero de contraseñas y con`-t` el número de hilos (_threads_ en inglés).


El ejercicio se puede hacer también para acceder a un servidor SFTP. Con la opción `-l` se puede indicar el nombre del usuario a testear (con `-L` podríamos especificar un archivo de texto con varios logins), `-t 4` indica cuatro hilos simultáneos, `-s` va seguido del puerto y despuès se indca `ssh://<HOST>`.

```bash
   $ hydra -l admin -P passwords.txt -t 4 -s 15882 ssh://5.tcp.eu.ngrok.io
```

También podríamos aplicar fuerza bruta sobre el formulario de una aplicación web:

```bash
    $ hydra -l <usuario> -P <ruta_del_diccionario> -s 443 -f -V -e ns -t 4 -w 30 https-get-form "<DIRECCION_URL_DE_LOGIN>:<campo_usuario>=^USER^&<campo_password>=^PASS^:F=error"
```
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
