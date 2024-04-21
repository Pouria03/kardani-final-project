# Project : Personal Branding Web Application


## About Project 
This project is a web application representing a personal branding which is about counseling and mentoring purposes.


## Requirements 
* Introducing company, company applications and owner.
* Ability of requesting counseling by users.
* Posting contents.
* Presenting contact informations.
* Admin panel to control website.
* Dynamic content modification.
* Fulfiling user questions by displaying frequent asked questions.
* Displaying provided services


## Project phases 
* information gathering and talks
* representing template demo
* start writing backend (using django framework)
* connect backend to frontend (using django framework templates)
* writing tests
* dockerizing project
* deployment


## Technologies used in this project
* python, django for backend
* html, css, bootstrap, javascript for frontend
* postgresql for database
* docker
* git 


## Entities
* Service ==fields==>(title, icon)
* FAQ ==fields==>(question,answer)
* ContactInfo ==fields==> (email, phone, address, socialmedia)
* About ==fields==> (title, description)
* Post ==fields==> (title, content, created_at, thumbnail)
* Counseling ==fields==> (title, description)
* ContactForm ==fields==> (name, phone)


## Tests
* testing models
* testing views
* testing forms


## Dockerizing project
make project isolated and dockerized using docker techology


## Deployment
creating acount on pythonanywhere domain and deploying project on the host.


## Project structure
--core
  --core
    --settings
    --urls
    --wsgi
    
  --*_app
     --models
     --views
     --urls
     --services
     --tests
     --apps

  --templates
  --static
  --media
  --manage.py


















