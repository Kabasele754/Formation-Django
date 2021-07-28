# My Django  
![image](https://user-images.githubusercontent.com/67704765/127151818-1921b790-513f-4ff9-8ca1-2e33e5b5c33a.png)


Django est un framework web open-source consacré au développement web 2.0 et écrit dans le langage de programmation Python. Les concepteurs de Django lui ont attribué le slogan suivant: " Le framework web pour les perfectionnistes sous pression ". Django est utilisé par certains des plus grands sites Web au monde, notamment Instagram, Mozilla et la NASA, mais aussi suffisamment léger pour être un choix populaire pour les projets parallèles et les startups le week-end. Son approche « batteries-included » signifie qu'un site Web puissant peut être généré rapidement entre les mains d'un développeur qualifié.

## Dans le Cadre Web
Un "cadre Web" est un logiciel qui standardise et élimine les difficultés courantes et les redondances impliquées dans la création d'un site Web. Par exemple, la plupart des sites Web doivent se connecter à une base de données, se déployer sur un serveur, gérer le routage des URL, la sécurité, l'enregistrement des utilisateurs, générer des modèles, etc. Au début, les programmeurs devaient faire tout cela à partir de zéro, mais ils ont rapidement reconnu les points communs et ont commencé à créer des frameworks Web.

De nos jours, il est rare d'écrire un site Web à partir de zéro. Des frameworks Web existent pour tous les langages de programmation modernes, y compris Rails pour Ruby , Express pour JavaScript et Django ou Flask pour Python.

Au-delà du langage de programmation sous-jacent, la principale différence entre les frameworks Web concurrents réside dans l'approche : Ruby on Rails et Django adoptent tous deux une approche de frameworks « batteries-included  », tandis que Flask et Express sont des microframeworks minimaux. Vous pouvez considérer cela comme la différence. Django et Rails sont plus rapides à utiliser et sont livrés avec de nombreux garde-corps intégrés pour éviter les mauvaises pratiques. Flask et Express nécessitent plus de personnalisation en amont mais permettent un contrôle total. Voir Django vs Flask pour une comparaison détaillée des deux frameworks Web Python les plus populaires et les avantages/inconvénients de chaque approche.

## Python
Python est l'un des langages de programmation les plus populaires au monde car il est convivial pour les nouveaux arrivants, extrêmement puissant et dispose d'un écosystème robuste de bibliothèques comme Django qui offrent des fonctionnalités supplémentaires. Python a récemment remplacé Java en tant que langage de programmation le plus populaire dans les meilleures universités américaines et se développe rapidement parmi les programmeurs professionnels, comme en témoigne sa croissance sur StackOverflow .

Python met l'accent sur la lisibilité et la convivialité pour les développeurs, comme en témoigne sa syntaxe "Hello, World". Le voici en Python :


```python 
print("Hello, World")```

Et le voici en Java :

```java class  HelloWorldApp  { 

    public  static  void  main ( String []  args )  { 
    
        System . dehors . println ( "Bonjour tout le monde!" );  
        
    }}```


Même si vous ne connaissez rien à l'un ou l'autre des langages de programmation, il est clair en un coup d'œil que Python est le plus facile des deux à comprendre.

Django a été initialement développé par des programmeurs Web du journal Lawrence Journal-World , en particulier Adrian Holovaty, Simon Willison et Jacob Kaplan-Moss. Il a été rendu public pour la première fois en tant que package open source en 2005 et est actuellement maintenu par la Django Software Foundation à but non lucratif . 

## Principales caractéristiques
Django adopte une approche "batteries incluses" similaire à Python et est livré avec un certain nombre de fonctionnalités intégrées, notamment un système d'authentification extensible, une application d'administration robuste, un serveur Web de test léger et la prise en charge de plusieurs bases de données, notamment PostgreSQL, MySQL, MariaDB, Oracle , et SQLite. Il est connu pour ses meilleures pratiques en matière de sécurité et est livré avec une documentation complète , disponible en ligne ou au format PDF/ePUB pour une utilisation hors ligne.

En tant que projet mature, Django apporte rarement des modifications de rupture et dispose d'un calendrier d'obsolescence clair pour toutes les mises à jour. Une nouvelle version majeure est publiée tous les neuf mois environ avec des correctifs mensuels pour la sécurité et les corrections de bogues.

Il existe également un écosystème dynamique d'applications tierces - visibles sur le site Django Packages - qui fournissent des fonctionnalités supplémentaires. Au fil du temps, les packages les plus populaires sont souvent intégrés à Django lui-même.

## Communauté
Un dicton courant parmi les développeurs Django est « Venez pour le framework, restez pour la communauté ». Elle est connue pour être une communauté accueillante et encourageante, ce qui n'est pas toujours le cas en technologie. Des conférences DjangoCon annuelles sont organisées aux États-Unis, en Europe, en Australie et en Afrique, ainsi que des rencontres dans de nombreuses grandes villes.

Des questions sur Django peuvent être posées sur le forum officiel de Django et les nouveaux arrivants sont encouragés à contribuer à Django lui-même.

Le podcast hebdomadaire Django Chat propose des interviews de personnalités clés de la communauté ainsi que des plongées approfondies sur diverses fonctionnalités de base. Il existe également une newsletter hebdomadaire Django News avec des mises à jour sur les événements, les didacticiels et les packages tiers.

## La structure Django
Django s'inspire du modèle MVC ![image](https://user-images.githubusercontent.com/67704765/127159658-7fecd9a6-8f06-47a4-a5f5-7e88a5111097.png)
 (disons plutot MVT ![image](https://user-images.githubusercontent.com/67704765/127159779-c71d3fa0-64da-4159-8718-97ec9caee799.png)
) , c'est-à-dire que la structure du framework sépare les données ( models ) qui sont séparées des traitements ( controller ) qui sont eux-mêmes séparés de la vue ( view / template ). On vous oblige à bien coder, une structure doit être respectée et cela ne peut être que profitable au travail collaboratif ou simplement la cohérence / communication entre différents projets.


Le moteur de template de base est le plus simple, efficace souple et facile à prendre en main. Un routeur permet de rediriger les actions en fonctions des URL et une API permet de fournir des informations sur votre projet sans passser par la case SQL. D'ailleurs l' ORM inclu vous éloignera de toute requète SQL.


Chaque projet Django vous propose de lancer son propre serveur web et d'y faire à peu près tout ce que l'on veut dans un environnement de test.


Un des concepts des plus intelligent de Django est de proposer un espace admin tout fait dans ses contrib . Une fois que vous avez créé vos modèles (la structure de votre projet), vous avez accès à une interface web CRUD en quelques minutes c'est vraiment impressionnant.


Vous pouvez évidemment personnaliser cet espace admin ou créer vos propres templates et vos propres formulaires . Django vous proposera des outils pour sécuriser les données ou afficher les erreurs si besoin.


