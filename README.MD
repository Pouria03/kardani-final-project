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
* deployment


## Technologies used in this project
* python, django for backend
* html, css, bootstrap, javascript for frontend
* postgresql for database
* docker
* git


## Entities
* CompanyService ==fields==>(id, title, icon)
* FrequentQuestion ==fields==>(id, question,answer)
* AboutCompany ==fields==> (id, title, description,company_name, email, address, social_accounts)
* Post ==fields==> (id, title, content, created_at, thumbnail)
* Counseling ==fields==> (id, title, description)
* ContactForm ==fields==> (id, name, phone, counseling_type)
* IndexPage ===fields==> (id, intro_text, intro_title, intro_video)



## Tests
* testing models
* testing views
* testing forms

## Deployment
for deployment don't forget to set DEBUG to True in settings.py

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



## to run this web app on your local machine :
> go to /core/core/settings.py, then set DEBUG to True.
> install python >=3.10
> go to terminal and run pip install -r requirements.txt
> run python manage.py migrate
> run python manage.py runerver
