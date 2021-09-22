# Projet
#### <i>Implémentez un modèle de scoring</i>
##
# Présentation
Le but de ce projet est d'aider une société de crédit à accorder des prêts à ses clients ou non. Pour aider cette entreprise dans ses décisions d'octroi de crédit, nous
devons construire un modèle de classification binaire, évaluer le modèle de classification grâce à une métrique et établir un dashboard intéractif.
Le dashboard devra respecter le cahier des charges suivant :

- Permettre de visualiser le score et l’interprétation de ce score pour chaque client de façon intelligible pour une personne non experte en data science.
- Permettre de visualiser des informations descriptives relatives à un client (via un système de filtre).
- Permettre de comparer les informations descriptives relatives à un client à l’ensemble des clients ou à un groupe de clients similaires.

Pour facilité la préparation des données et permettre l'élaboration d'un modèle de scoring, nous pouvons nous aider d'un Kernel.

<u>Dans ce dépôt, vous trouverez :</u>

 - Un notebook Jupyter pour l'analyse exploratoire des données.
 - Un notebook Jupyter traitant du modèle de classification binaire.
 - Une note méthodologique décrivant le modèle, sa métrique d'évaluation, l'interprétabilité du modèle.
 - Un dossier avec la configuration locale de l'API. Cette version de l'API s'appuie sur deux fichiers .py :
    - app.py qui est le fichier contenant la partie backend.
    - dashboard.py contient la partie Frontend codée avec Streamlit.
	
## Modèle de classification
Ici nous utilisons un seul modèle de classification : la régression logistique. 


## Dashboard / API
Pour traiter ce sujet nous utilisons STREAMLIT.

lien du dashboard : https://dashboard-pret-a-depenser-stre.herokuapp.com/, lien du dépot associé : https://github.com/jocelyne-vet/projet7deploy