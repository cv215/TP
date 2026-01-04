Après vérification complète du projet, je confirme que l’application fonctionne correctement et que les fonctionnalités testées m’ont donné entière satisfaction.

Shop-Beauty – Application E-commerce Django
Description

Shop-Beauty est une application web e-commerce développée avec Django permettant aux utilisateurs de :
Consulter des produits

S’inscrire et se connecter

Ajouter des produits au panier

Passer une commande

Naviguer via une interface moderne avec Bootstrap


Technologies utilisées
Python 3

Django

SQLite

HTML / CSS

Bootstrap 5

Git & GitHub

 Structure du projet
TP/
├── Ecommerce/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── shop/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/shop/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── details.html
│   └── migrations/
│
├── media/
├── db.sqlite3
└── manage.py

 Installation du projet
Cloner le dépôt
git clone https://github.com/TON_USERNAME/TON_DEPOT.git
cd TP

Créer un environnement virtuel
python -m venv env
env\Scripts\activate

 Installer les dépendances
pip install django

 Lancer les migrations
python manage.py migrate

Créer un super-utilisateur
python manage.py createsuperuser

Démarrer le serveur
python manage.py runserver


Puis ouvre dans le navigateur :

http://127.0.0.1:8000

Fonctionnalités
Fonctionnalité	Statut
Affichage produits	
Détails produit	
Panier	
Inscription utilisateur	
Connexion / Déconnexion	
Redirection automatique	

 Flux utilisateur
Inscription → Connexion → Accueil → Ajout au panier → Commande

Auteurs

François Xavier; Gaetan
Développeur Django débutant – passionné par le web et le e-commerce.

Licence

Projet pédagogique libre d’utilisation.