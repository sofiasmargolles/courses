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
```bash
   hydra -l <usuario> -P <ruta_del_diccionario> -s 443 -f -V -e ns -t 4 -w 30 https-get-form "https://cardiac-modified-stop-paraguay.trycloudflare.com/login:<campo_usuario>=^USER^&<campo_password>=^PASS^:F=error"
```
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
