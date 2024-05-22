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
In this project, a REST API has been created, which is responsible for reading and writing files to a local database. This work has been carried out as a practical exercise for the position of Data Engineer at Globant.
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
- Duplicate validation
- Writing in a single request
- Massive data reading


## Setup
This project runs on a local MySQL database, which runs on port 3306. To execute this project, it is necessary to install the following:

- XAMPP - To turn on our Apache server
- MySQL - To host our databases
- Python 3.10 or higher - To run our Python code
- Postman or Insomnia - To send calls to the REST API


## Usage

To use the code, we need to run the file app.py, which will start the local host of our application. Once executed, we should check the logs in the terminal, as we can find the route where our code is running there
[![Visual Log Screenshot][visual-screenshot]]

`Running on http://127.0.0.1:5000`

Once we execute our code, we proceed to copy the localhost URL mentioned earlier into Postman; this URL will be our endpoint. This endpoint receives a POST request with the following parameters:

- `filename` - Name of the CSV file to be processed.
- `table` - Name of the table into which the read records should be loaded.
[![Postnam Request Screenshot][postman-screenshot]]


The API will output a log with the number of records written to the database. In case the specified file or table does not exist, it will be displayed in the logs along with its respective message.

## Contact
Created by [@JhonGM](https://www.linkedin.com/in/jhon-brayan-gonzalez-montoya-b2657b182/) - feel free to contact me!

<!-- MARKDOWN LINKS & IMAGES -->
[postman-screenshot]: https://snipboard.io/73c1qh.jpg
[visual-screenshot]: https://snipboard.io/7OxdHR.jpg
