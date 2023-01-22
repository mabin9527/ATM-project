# ATM Project

![Main Page](readme-assets/atm-main-page.png)

--------------------------------------

## Table of Contents

--------------------------------------


- [Description](#description)
- [User Experience](#user-experience)
- [Lucidchart](#lucidchart)
- [Features](#features)
    - [Future Features](#future-features)
- [Testing](#testing-and-issues-encountered)
- [Technologies](#technologies-used)
- [Deployment](#deployment-to-heroku)
- [Credits](#credits)

----------------------------------------

## Description
----------------------------------------

ATM project is based on the Python language. Users can open an account, lodge and withdraw money and check their account balance by selecting the ATM menu. All data can be read or saved to google sheets. The live site can be found [here](https://atm-project.herokuapp.com/).


----------------------------------------
## User Experience
----------------------------------------

### User Stories
----------------------------------------
As a first-time user:

- I want to know what functions are included in ATM.
- I want to get clear instructions to operate the machine.

As a returning user:

- I want to lodge and withdraw money from my bank account.
- I want to know the account balance.


----------------------------------------

### Lucidchart
----------------------------------------

For a logical statement of the ATM project, a lucidchart has been used to explain the working process of the machine clearly. Besides, it assists me with logical guidance to complete the project.

![Flowchart](readme-assets/atm-flowchart.png)


----------------------------------------
## Features
----------------------------------------

### Start menu

When running the program, a welcome page and start menu can be displayed on the screen clearly, which is easy to follow for the user to operate the machine. Users' requirements can be fulfilled by selecting the menu options.
  

![Start menu](readme-assets/start-menu.png)


----------------------------------------
#### Open account

When the user wants to open a bank account, option 1 is selected. The following information are required:

- Passport number. The format of the passport number example is listed clearly. The user's passport number will be verified by a regular expression. If the passport number is correct, the process will go next step. Otherwise, it will go back to the start menu.
![Passport number](readme-assets/passport-number.png)

- Phone number. There is an example for users. A regular expression of phone number is applied to validate the phone number. The process will go further as the validation is passed.
![Phone number](readme-assets/phone-number.png)

----------------------------------------