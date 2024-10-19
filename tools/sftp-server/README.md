# Servidor SFTP

Este proyecto levanta un pequeño servidor de ejemplo SFTP. El nombre de usuario es `admin` y la contraseña se configura en el fichero `.env`.

Para conectarte al servidor SFTP puedes emplear una aplicación de escritorio como Filezilla o un cliente de línea de comandos como:

```
sftp -P <PUERTO> admin@<DIRECCION_IP>
```

Por defecto, se levanta en el puerto 22 de localhost.

Al introducir la credencial, puedes navegar por las carpetas usando para listar los contenidos:

```
$ ls
```

Para mover entre las carpetas:

```
$ cd nombre_carpeta
```

Para descargar ficheros:

```
$ get nombre_fichero
```

Se pueden ver más opciones con:

```
$ help
```
