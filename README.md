![GitHub License](https://img.shields.io/github/license/syedsadiquh/Geocoding-app?link=https%3A%2F%2Fgithub.com%2Fsyedsadiquh%2FGeocoding-app%2Fblob%2Fmain%2FLICENSE)


# Geocoding App
This is a Geocoding app capable of both forward and reverse geocoding i.e. converting a textural address to geographical coordinates and converting geographical coordinates to its respective textural address respectively. <br>
This app aims to implement geocoding using Opencage Geocoding API to set the groundwork for real-world use cases like Geotagging media, Transportation and many more.

### Technologies Used :
* Python - Used this because of its vast library and ease of implementation of GUI using TKinter and requests library for API.
* SQLite - Used this for its hassle-free implementation without worrying about setting up an SQL server.

This app is still in its early stages. More features like exporting the history in a DSV file format, preferably TSV (Tab-Separated Values) as commas are already being used between coordinates could be implemented.

## How to run the project
To run this project, you must install the necessary dependencies for setting up the environment. <br> (NOTE: Make sure to check the Requirement.txt file to see the supported versions.)
1. Download Python.
visit: https://www.python.org/downloads/ and download the version as per your choice.
2. Install Python using the downloaded installer. The installation guide for your Operating System can be found on Python docs.
3. Install the requests library using the pip command as follows: <br> <code>pip install requests</code> <br> This should install the latest version of the requests library on your system. If you already have requests library on your system, please make sure that you satisfy the version criteria. Otherwise, consider updating the library.
4. Clone this repo to your system.
5. Create an account on OpenCage by visiting https://opencagedata.com and going for signup.
6. Go to your dashboard, and click on the "Geocoding API" heading. Go ahead and click on the "Create another API key" button under the "Your API Keys" Section.
7. Copy the API key and Paste it inside the geocoding_main.py file in place of the "YOUR API KEY" text. Make sure to keep the pair of quotes. 
8. After navigating to the project directory on your system terminal/Command Prompt, run the application.py file using <code>python application.py</code> command.

Congratulations!!! The app is now running. 🥳🥳🥳 

## How to use the Project
The Project is divided into multiple files each file is responsible for a specific part of the program. The part each file plays are described below:
* geocoding_main.py - This file defines the essential geocoding functionality by defining functions. You can import this file into other projects and start performing the geocoding. Note: Catch Exceptions after implementation for bad responses with appropriate messages.
* application.py - This file is the main GUI implementation of the project. It holds the main screen of the program and is responsible for implementing other methods and files.
* History_Screen.py - Holds the GUI for the History Screen.
* dbConnector.py - This defines the necessary codes for building an SQLite DB for storing the queries made. This holds functions for inserting and deleting the data from the DB. This also contains a function for completely clearing the DB (use carefully).
* SQLiteDB/geocoding_data.db - This is the actual Database that holds the data.

You can use this for other projects by importing the files you need for your project.

## Screenshots
<br>Forward Geocoding Page<br>
<img src="https://github.com/syedsadiquh/Geocoding-app/assets/49514406/82df11c8-dcb5-4ea9-90db-c22546560692" width=80% height=80%>

<br>Reverse Geocoding page<br>
<img src="https://github.com/syedsadiquh/Geocoding-app/assets/49514406/c0579828-064f-4c2d-8766-01bfed4c7fce" width=80% height=80%>

<br>History Page<br>
<img src="https://github.com/syedsadiquh/Geocoding-app/assets/49514406/5d96a6b3-a86d-4609-bc47-5621593e3a77" width=80% height=80%>

## License
This is an MIT-licenced Project for more details see the LICENCE file.

