# __REST API dev best practices__
L'API, Application Programming Interface, est l'outil qui permet aux developpeurs d'interagir avec une application.
Une API developpée sans le respect des best practices peut resulter en une API difficile d'utilisation pour l'utilisateur et des problèmes de sécurité.
Une API qui respecte les best practices sera : 

- Facile à comprendre
- Facile à utiliser
- Complete et robuste

Pour se faire on se repose sur le principe de KISS, Keep It Simple, Stupid, qui préconise la simplicité dans la façon de coder, l'utilisation d'un framework ayant une grande communauté, et utiliser les plugins à disposition, afin de faciliter au maximum le maintient et l'évolution de l'API, ainsi que d'éviter les features trop complexes et inutiles.

## __Nommage__
Il existe plusieurs convention de nommage, cependant certaines sont tres courantes et seront retrouvées dans un grand nombre de projet. Il s'agit du ```spinal-case``` pour les URLs et noms de ressources, et du ```snake_case``` ou du ```camelCase``` pour les champs et parametres des ressources. Ces manières de nommer permettent d'éviter les espaces, apostrophes et autres caractères non recommandés dans les noms de variables et ressources en informatique. 

Evidemment il est toujours préférable de donner a ses ressources un nom anglais. De plus il est recommandé d'utiliser des noms plutot que des verbes pour les methodes HTTP, et également des noms au pluriel pour les collections.

Pour décrire ses endpoints de manière organisée, la façon standard de procéder pour une API RESTful est de commencer par le nom de la ressource, avec l'opération HTTP qui décrit l'action. Par exemple :
``` GET my-RESTful-api.com/users ```, pour récuperer la liste de tous les utilisateurs. 
``` DELETE my-RESTful-api.com/users/1 ```, pour supprimer l'utilisateur ayant l'id __1__.

Il est important de décrire les ressources avec des noms concrets et non des verbes.

## __Opérations HTTP__
En ce qui concerne l'opération HTTP, il en existe 5:
- __GET__, pour __lire__ ou __récupérer__ la __représentation d'une ressource__. status codes: 200 OK, 404 Not Found
- __POST__,  pour __créer__ une __nouvelle ressource__. status code: 201 Created, 404, 409 Conflict (if ressource already exists)
- __PUT__, pour __remplacer__ le __contenu__ d'une ressource par un autre. Est généralement utilisé pour mettre à jour. status code: 200, 204 No Content, 404, 405 Method Not Allowed
- __PATCH__,  pour __modifier__ une ressource en __précisant__ seulement __ce qui change__. Est également utilisé pour mettre à jour. status code: 200, 204, 404, 405
- __DELETE__, pour __supprimer__ une ressource existante. status code: 200, 404, 405

## __Status code__
Les status code plus haut ne sont pas sans importance. En effet, il en existe bien plus et chacun renvoie un message bien précis a l'utilisateur quant à l'état de sa requête.

Certains status code sont donnés plus haut, mais voici un tableau pour une meilleur compréhension:
status code | signification
:---:|:---:
__200__ - Ok | La requête a été traitée avec succès
__201__ - Created | La nouvelle ressource a été créée avec succès
__204__ - No Content | La requête DELETE a été effectuée avec succès
__206__ - Partial Content | Lorsqu'une requête renvoie une réponse trop lourde pour être envoyée en une seule fois. Dans ce cas de la pagination sera necessaire pour l'ensemble de la réponse.
__304__ - Not modified | Aucune donnée modifiée
__400__ - Bad Request | La requête n'est pas valide et n'a pas été traitée par le serveur.
__401__ - Unauthorized | Une identification est requise pour cette action.
__403__ - Forbidden | L'utilisateur n'est pas autorisé à faire cette action.
__404__ - Not Found | La ressource n'existe pas.
__429__ - Too many Request | L'utilisateur a envoyé trop de requêtes dans un certains laps de temps.

## __Gestion des erreurs__
En cas d'erreur il est important de fournir un message d'erreur clair et précis aux developpeurs qui utilisent l'API.
Un modèle très simple pouvant être utilisé:
```
{
    "status": 401,
    "message": "User is not authorized to do this action."
}
```
Avec status qui précise le status code, et un message qui explique le problème survenu lors de la requête. 

## __Versioning__
Une API est vouée à évoluer au cours du temps. Pour marquer les changements importants concernant les fonctionnalitées de l'API, il est utile de versionner son API.
Une bonne pratique est de préciser la version dans l'URL de l'API, ```my-RESTful-api.com/v1/users/1```, ici on a donc notre API en version 1.
Versionner son API est un moyen efficace de commenter les changements important aux utilisateurs de cette dernière, et il est également possible pour préciser la version de l'API utilisée par les developpeurs est d'indiquer cette dernière soit en paramètre, ou bien dans l'en-tête de la requête.

## __XML ou JSON__
Pour lire et utiliser des données, les developpeurs d'API ont le choix entre XML ou JSON. Aujourd'hui le standard est d'utiliser JSON, il est plus simple à parser et plus simple à lire que son concurrent.
En plus d'être simple à lire par l'homme, le JSON est supporté par beaucoup de framework et beaucoup de langage de programmation qui peuvent créer des données à partir d'un fichier JSON.
XML | JSON
:---:|:---:
![xml example](resources/xml-example.png) | ![JSON example](resources/json-example.png)

## __Performances__
Il est important qu'une API sioit capable de gérer la charge sous peine de voir les performance de celle-ci fortement détériorée, temps de login trop long, réponses aux requêtes dupliquées, ...
Il est donc important d'optimiser les performances du backend. Si trop de requêtes sont necessaires afin d'obtenir une seule donnée. Prenons le cas où un GET sur ```/users``` ne retourne qu'une liste des id d'utilisateurs, il est alors obligatoire de faire un second GET sur ```/user/user-id``` pour avoir les details liés à un utilisateur.
Cette manière de procédé va considérablement accroître le nombre de requêtes nécessaires. Il est possible de contrôler le nombre de requêtes par client, grâce à des limitations du côté serveur avec par exemple:
- Limitation basée sur le temps avec un nombre prédéfinis de requêtes par seconde
- Limitation du nombre d'opérations HTTP(GET, POST, DELETE) par seconde
- Limitation par groupe d'utilisateurs, une authentification est requise pour moins de limitation des actions possibles

Il existe d'autres limitations côté serveur, mais il en existe également côté client avec la gestion du code erreur 429 (voir tableau des status code) avec un temps d'attente suggéré avant un nouvel essai.

L'option du Rate Limiting est également envisageable avec:
- X-Rate-Limit-Limit qui indique le nombre de requêtes qu'un client peut envoyer dans un laps de temps.
- X-Rate-Limit-Remaining qui indique le nombre de demandes restantes au client dans l'intervalle de temps actuel.
- X-Rate-Limit-Reset pour indiquer au client quand la limite de temps sera réinitialisée.

Avec le rate limiting, l'API s'auto-limitera en se fixant donc un nombre maximum d'actions par période, tandis que la première manière sert a protéger d'un grand nombre de requêtes simultanées sur l'API voir même au niveau du load balancer.

## __Microservices__

APIs et architecture microservices partagent le même but, cependant utiliser des microservices revient souvent à utiliser une API pour pouvoir faciliter le couplages des differents services.
Nous avons donc d'un côté l'architecture microservices, où le projet est "éclaté" en plusieurs services de plus petites tailles.
Avec comme avantages la facilité d'intégration et la facilité de maintient des applications, grâce notamment au fait que chaque fonctionnalités de l'application est traitée dans son coin.
En effet en terme de scalabilité par exemple, pour une application basée sur des microservices, il est necessaire d'optimiser les ressources seulement de certains composants de l'application, du fait qu'aucun composant n'est fortement couplé aux autres. Cela a aussi pour effet de rendre l'application testable plus facilement et la rend adaptable au changement de technologies.
![Microservices are linked by API](resources/services-linked-by-api.png)

D'un autre côté, l'API qui est le framework grâce auquel le developpeur peut interagir et communiquer avec les services, et qui permet de présenter différentes données et fonctionnalités de l'application aux clients, dans une approche monolithique, qui peut être préférée à l'architecture microservices pour les projets de petite envergure, et où on aura une application simple à build, tester et déployer, ainsi qu'une mémoire partagée qui va, en terme de performance, nous rendre une application plus rapide par rapport à une application où les services doivent communiquer les uns avec les autres pour partager des informations.
En revanche avec une telle approche, une erreur et c'est toute l'application qui est en maintenance. Un autre désavantage de l'approche monolithique, est la mise à jour de l'application. Dans un premier temps, les technologies utilisés dans ce cas doivent être similaires, et changé une des techno va demander un budget conséquent. Arrive ensuite le problème du redéploiment de l'application, avec le cas où seulement une partie a été mise à jour mais où il est necessaire de redéployer toute l'application, alors que par micro-services seul le service concerné par les changements sera a redéployer. 

![Monolithic versus Microservices architecture](resources/mono-vs-microservices.png)

## __Gestion du contenu statique__
Il est evidemment, pour protéger son application, primordiale de ne pas stocker les clés d'API et secrets dans le code source même de l'application. Il est de bonne pratique de stocker ce genre de données soit dans des variables d'environnement, soit dans des fichiers en dehors de l'arborescence source de l'application.

## __Sécurité__
Au delà du problème du contenu statique, une API subit des attaques similaires à celles visant les réseaux et applications web. Si notre API fais l'objet d'une attaque bien menée, ce ne sont pas seulement les données qui sont à risque, mais également l'infrastructure. La sécurité est donc une priorité dans le developpement d'une API.
Le type d'attaque le plus courant que peut subir une API, est probablemenmt le type SQLi, SQL injection, qui a lieu lorsqu'une personne mal intentionnée insère des commandes ou du code malveillant dans un programme à partir d'un champs de texte, comme par exemple le nom utilisateur ou le mot de passe. Grâce a ce type d'attaque il est possible de prendre le contrôle d'une base de donnée SQL.
Il existe cependant d'autres types d'attaques:

Type d'attaque | Mesures préventives
:---:|:---:
Injection SQL, insertion de commandes/code malveillants dans un input utilisateur | Utilisation d'ORM __/__ Validations des entrées utilisateur et échappement de caractères spéciaux (empêchement d'utilisation de caractères spéciaux, ...) __/__ Utiliser des requêtes préparées
Cross-Site Scripting (XSS), insertion d'un script malveillant dans le code de l'application | Validation des entrées utilisateur __/__ Activation de l'option HttpOnly __/__ Échappemment de caractères spéciaux
Distributed Denial-of-Service (DDOS), Excéder la capacité de trafic que peut prendre en charge un réseau, système ou site Web pour le rendre inaccessible aux utilisateurs | Limiter le nombre de requêtes et la charge utile / Mise en place de pare-feux, load-balancer, et autres répartiteurs de charge
Man in the Middle (MitM), Interception de trafic entre deux API et application ou bien API et endpoint, en se faisant passer pour l'un ou pour l'autre auprès de chacun. | Chiffrement des données échangés entre les systèmes cpmmuniquants entre eux.

## __Documenter son API__
Pour que l'API soit facilement réutilisable et encourager d'autres devleloppeur à consommer l'API, il est très important de fournir une documentation claire et concise. Dans cette documentation figureront:
- la ou les méthodes d'authentification
- les headers acceptés
- les différents endpoints
- les différentes opérations disponibles
  Pour chaque méthodes(opérations):
    - les paramètres acceptés
    - le format de la requête
    - le modèle du corps de la requête

Préciser également la politique d'utilisation de l'API, les quotas d'utilisation (nombres d'appels à ne pas dépasser), et une description technique la plus exhaustive possible.
