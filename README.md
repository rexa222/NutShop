
# NutShop (Simple shop manger)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Simple shop manager for an online nut shop with django.

## Demo

http://rexanuts.pythonanywhere.com/

### Test Accounts:
| Description                        | Username | Password |
|------------------------------------|:--------:|:--------:|
| Admin account                      |  admin   |  123456  |
| Customer account located in Tehran |  tehran  | teh@1234 |
| Customer account located in Shiraz |  shiraz  | shi@1234 |

## Features

- Admin panel for controlling inventories, products and orders
- Showing products to customers based on their city
- Tracking order processing and status for customers



## Run locally

Make sure you have python installed.

-  Clone the project:

```bash
  git clone https://github.com/rexa222/NutShop
```

- Make a virtual enviroment with desired name and active it:

```bash
  py -m venv venv_name
  venv_name\Scripts\activate
```
- Install requirements:
```bash
  pip install -r requirements.txt
```
- Thats it! run the project:
```bash
  py manage.py runserver
```
project should be accessible locally at http://127.0.0.1:8000
## Frontend

Project templates are styled using [Bootstrap](https://getbootstrap.com/) framework.


## License

[MIT](https://choosealicense.com/licenses/mit/)

