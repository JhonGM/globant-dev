# Project Name
> Outline a brief description of your project.
> Live demo [_here_](https://www.example.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
En este proyecto, se ha creado un API REST, la cual se encarga de leer y escribir archivos sobre una base de datos local, este trabajo se ha realizado como ejercicio práctico para el cargo de Ingeniero de Datos en Globant
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Flask
- Python 3.10
- MySQL
- Apache
- Pandas
- SQLAlchemy
- Numpy
- PyMySQL


## Features
List the ready features here:
- Validación de duplicados
- Escritura en un solo request
- Lectura masiva de datos


## Setup
Este proyecto corre sobre una base de datos local MySQL la cual corre sobre el puerto 3306, para poder ejecutar este proyecto es necesario previamente instalar:

- XAMPP - Para poder encender nuestro servidor Apache
- MYSQL - Para Alojar nuestras bases de datos
- Python 3.10 o superior - Para ejecutar nuestro código Python
- Postman o Insomnia - PAra poder enviar llamados al API REST


## Usage

Para usar el código debemos ejecutar el archivo app.py, este archivo ejecutará el host local de nuestra aplicación. Una vez ejecutado, debemos fijarnos en los logs del terminal, ya que allí podremos ver la ruta en la que está corriendo nuestro código
[![Visual Log Screenshot][visual-screenshot]]

`Running on http://127.0.0.1:5000`

Una vez ejecutemos nuestro código, procedemos a copiar la ruta del localhost mencionada anteriormente en Postman, esta ruta será nuestro endpoint. Este endpoint recibe un request de tipo POST con los siguientes parametros parametros:
- `filename` - Nombre del archivo en formato CSV a Procesar
- `table` - Nombre de la tabla en la cual se deben cargar los registros leídos.
[![Postnam Request Screenshot][postman-screenshot]]


El API arrojará un log con la cantidad de registros escritos sobre la base de datos, en caso de que el archivo o la tabla especificada no existan, se mostrará en los logs con su respectivo mensaje.

## Contact
Created by [@JhonGM](https://www.linkedin.com/in/jhon-brayan-gonzalez-montoya-b2657b182/) - feel free to contact me!

<!-- MARKDOWN LINKS & IMAGES -->
[postman-screenshot]: https://snipboard.io/73c1qh.jpg
[visual-screenshot]: https://snipboard.io/7OxdHR.jpg
