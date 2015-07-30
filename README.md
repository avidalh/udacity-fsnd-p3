# udacity-fsnd-p3

##**I**tem**C**atalog

###Udacity FullStack NanoDegree Project 3

## Synopsis

This is my FullStack NanoDegree's third project, aka **Item Catalog**.
It's a web application based on Flask, SQLAlchemy and (of course) Python.

The application is oriented to create, store, manage and show a **cars** item catalog. Log in is permitted using oauth and facebook/google+ authentication. When logged in the applications permits create, modify and delete items and categories.

When logged in new categories and items can be created, modified and deleted if the user logged in is the owner of that categories/items.

In order to reach an "Exceeds Specs" the following aspects are covered:

- API Endpoints. The app provides an XML endpoint for categories, items by category and individual items.

- Items images. Every item has three fields to store pictures URL. All the item's fields are accessible to Create, Update and Delete once you've logged in.

- Cross-Site Request Forgeries (CSRF) is prevented by checking loggedIn/userID when Create/Update/Delete operation is requested.

- Code Quality. I've tried to write a well formatted and commented code, accordingly the PEP8 guide and PEP. Some code lines (mostly URL strings) are longer than maximum pep8 lenght, but I think is more practical not to break them in order to get a more readable and clean code.

## ItemCatalog is Online

ItemCatalog app is online at [`http://udacity-fsnd-p3.herokuapp.com/`](http://udacity-fsnd-p3.herokuapp.com/), please have a look and play with it!

## Requirements

All requirements are specified in the autogenerated file "**`requirements.txt`**"
The easy way to be sure your system are ready to execute the application is by doing the following:
 "**`pip install -r requirements.txt`**"


## Installation

To install the application follow the nex steps:

- Option 1: **Clone the repository.** If you are a **git** user do this: 
	From the system's command line execute "**`git clone https://github.com/avidalh/udacity-fsnd-p3`**", this action will create the directory `udacity-fsnd-p3` where the project has been downloaded.

- Option 2: **Download the zip file.** If you are not a **git** user:
	Download the zip file **`https://github.com/avidalh/udacity-fsnd-p3/archive/master.zip`** from GitHub and decompress it on your system at the best place you decide.


## Running the app

The application can be executed on almost every system where python 2.7 had been installed (e.g. MacOS-X, Linux, Unixes, etc.) I've tested the app in MacOS-X and Ubuntu, this last one running in a Vagrant virtual machine.

To execute the app you have some options:

1. Running the application by just typing **`python application`** on your system's command line.

2. Open `application.py` with IDLE and select run.


### Addons:

1. If you need to create the database file, **`catalog.sql`**, you can execute **`python database_setup.py`** and your new file will be created.

2. Auto-populating the database can be done by using **`python populate.py`**, this way some sample categories and items will be created to play with them.


## Tests

The program has been tested by many users and (almost) all known bugs have been fixed. If you find some bug please email me and I will fix it when possible.


## Contributors

I want to thank all the people involved in my NanoDegree, family, udacity (coaches, students and reviewers), workmates, friends, etc. To all of them 

<h1><center>Thank You!</center></h1>

for your support and help.

## License

**ItemCatalog** is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

**ItemCatalog** is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with **ItemCatalog**.  If not, see <http://www.gnu.org/licenses/>.

