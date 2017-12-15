# Ostmodern Python Code Test

The goal of this exercise is to test that you know your way around Django and
REST APIs. Develop this the same way you would an actual long-term project.

The idea is to build a platform on which your users can buy and sell starships.
To make this process more transparent, it has been decided to source some
technical information about the ships on sale from the [Starship
API](https://swapi.co/documentation#starships).

A Django project some initial data models have been created already.

## Getting started

* This test works with either
  [Docker](https://docs.docker.com/compose/install/#install-compose) or
  [Vagrant](https://www.vagrantup.com/downloads.html)
* Get the code from `https://github.com/ostmodern/python-code-test`
* Do all your work in your own `develop` branch
* Once you have downloaded the code the following commands will get the site up
  and running

```shell
# For Docker
docker-compose up
# You can run `manage.py` commands using the `./manapy` wrapper

# For Vagrant
vagrant up
vagrant ssh
# Inside the box
./manage.py runserver 0.0.0.0:8008
```
* The default Django "It worked!" page should now be available at
  http://localhost:8008/

## Tasks

Your task is to build a JSON-based REST API for your frontend developers to
consume. You have built a list of user stories with your colleagues, but you get
to decide how to design the API. Remember that the frontend developers will need
some documentation of your API to understand how to use it.

* A potential buyer can browse all the ships currently for sale
* A potential buyer can order ships on sale by either price or time of listing
* A potential buyer can browse all the models of which there are currently ships
  for sale
* For each of those models, a potential buyer can browse all the offers for this
  model
* When a user supplies a ship name, a model name and a price, they can put their
  ship up for sale
  * Performance characteristics for the ship are gotten from the Starship API
  * The ship name entered maps to the `model` field on the Starship API
  * If the model can't be found in the API, the listing should not be accepted
* When a seller takes their ship off the market, it doesn't appear in any
  listing
* When a seller puts their ship back onto the market, it appears again in
  listings
* When a ship is put back onto the market it moves up if the listing is ordered
  by time of listing

After you are done, create a release branch in your repo and send us the link.
