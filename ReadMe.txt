python --version : verifier version de python
python -m venv env : creer environnement virtuel
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser : This command sets the policy to RemoteSigned which means that as long as a script downloaded from the internet is signed by a trusted publisher, it will run.
. .\env\Scripts\Activate.ps1 : activate your virtual environment
pip install django : installer django
django-admin startproject pfa : creer projet django nommé pfa
cd pfa : acceder au dossier pfa
ls : afficher le contenu du dossier actuelle
python manage.py runserver : executer le projet
django-admin startapp projet : creer application nommé projet
deactivate : deactivate a Python virtual environment