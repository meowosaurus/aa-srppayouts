# SRPPayouts
A simple SRP table plugin, that offers dynamic rows and columns to show the maximum amount of ISK you're willing to reimburse if someone lost their ship. This plugin works independently from any SRP plugin and only offers you the table mechanics.

This plugin was inspired by Goonswarm Federation's Affordable Care App.

# Contents
* [Current Features](#current-features)
* [Screenshots](#screenshots)
* [Installation](#installation)
  * [Alliance Auth Production](#alliance-auth-production)
    * [Non-Docker Version](#non-docker-version)
    * [Docker Version](#docker-version)
  * [Alliance Auth Development](#alliance-auth-development)
* [Usage](#usage)
* [Permissions](#permissions)
* [Support](#support)

# Current Features
* Display a page with the maximum amount of ISK you're willing to reimburse 
* Dynamically add new ships, new payouts or new reimbursement reasons (columns)

### Active devs:
* [Meowosaurus](https://github.com/meowosaurus)

## Screenshots
![Showcase](https://github.com/meowosaurus/aa-srppayouts/blob/master/images/main.png)

## Installation

### Alliance Auth Production

#### Non-Docker Version
1.) Install the pip package via `pip install aa-srppayouts`

2.) Add `srppayouts` to your `INSTALLED_APPS` in your projects `local.py`

3.) Restart your server, then run migrations and collectstatic

#### Docker Version
1.) Please make sure you followed the custom docker-image tutorial [here](https://gitlab.com/allianceauth/allianceauth/-/tree/master/docker#using-a-custom-docker-image): 

2.) Edit your `conf/requirements` and add the following line `aa-srppayouts` (Check https://pypi.org/project/aa-simplewiki/ for different versions!)

3.) Add `srppayouts` to your `INSTALLED_APPS` in your projects `local.py`

4.) Start your server `docker compose --env-file=.env up -d`

5.) Run `docker compose exec allianceauth bash`

7.) Run `auth migrate`

8.) Run `auth collectstatic`

### Alliance Auth Development 
Make sure you have installed alliance auth in the correct way: https://allianceauth.readthedocs.io/en/latest/development/dev_setup/index.html

1.) Download the repo `git clone https://github.com/meowosaurus/aa-srppayouts`

2.) Make sure it's under the root folder `aa-dev`, not under `myauth` 

3.) Change directory into `aa-dev` aand run `pip install -e aa-srppayouts`

**Important**: If you are getting an error saying that `srppayouts` is not installed after running `pip install -e aa-srppayouts`, delete the `setup.py` file in the aa-srppayouts root directory and try again.

4.) Add `srppayouts` to your `INSTALLED_APPS` in your projects `local.py`

5.) Change directory into `myauth`

6.) Make migrations with `python manage.py makemigrations`

7.) Migrate with `python manage.py migrate`

8.) Restart auth with `python manage.py runserver`

## Usage
Check out our wiki on GitHub: https://github.com/meowosaurus/aa-srppayouts/wiki

## Permissions
Perm | Admin Site | Auth Site 
 --- | --- | --- 
basic_access | None | Can view the payouts page

## Commands
- Load over 200 ships with their correct ship id: `python manage.py srppayouts_load_data`
- Load an example with 3 columns and 4 ships: `python manage.py srppayouts_load_example`

## Dependencies
- [Alliance Auth](https://gitlab.com/allianceauth/allianceauth)
- [allianceauth-app-utils](https://gitlab.com/ErikKalkoken/allianceauth-app-utils)

This plugin only works with Alliance Auth 4.0.0 or above

## Support
* On Discord: meowlicious
