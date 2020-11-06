# Instructions pour contribuer

Veuillez noter que ce projet est liée à un [code de conduite des contributeurs](code-of-conduct.md). En participant à ce projet vous acceptez de respecter ses termes.

---

## Modèle pour un lien dans la liste

Utilisez le modèle : `[Nom_du_lien](url_du_lien) - Descriptif du lien.`

## Comment contribuer à la liste

Cette liste est ouverte à tous. Y contribuer est simple: vous avez besoin uniquement d'un compte GitHub.

Voici un guide pas à pas pour contribuer à cette liste:

1. Cliquez sur le fichier `README.md`: <img width="1122" alt="liste des fichiers" src="https://user-images.githubusercontent.com/93244/89622528-7997b900-d893-11ea-8b03-a7439d9df303.png">
2. Cliquez sur le bouton `edit`: <img width="1122" alt="Editer le fichier" src="https://user-images.githubusercontent.com/93244/89622823-ec089900-d893-11ea-997f-a3a6c403977a.png">
3. Vous pouvez éditer le contenu du fichier dans votre navigateur. Assurez vous de suivre les bonnes pratiques ci-dessus. Le fichier utilise le language [GitHub Flavored Markdown]
4. Indiquez dans le formulaire de bas de page pourquoi vous proposez ces changements et cliquez sur "Propose file change": <img width="937" alt="Capture d’écran 2020-08-07 à 09 33 22" src="https://user-images.githubusercontent.com/93244/89623492-fb3c1680-d894-11ea-8d38-b98ac77ac67c.png">
5. Envoyez votre Pull Request.
6. Attendez une relecture et répondez aux éventuelles demandes de modification.

Merci pour votre contribution.

## Pour tester la génération du site statique

Cette Awesome list est utilisée pour générer un site web statique à l'aide de [Mkdocs](https://www.mkdocs.org/).
Pour tester en local la génération vous avez besoin d'installer [nox](https://nox.thea.codes/en/stable/) au préalable.
Ensuite nox s'occupe d'installer toutes les dépendances nécessaires
dans un environnement virtuel:

`$ nox -s docs`
