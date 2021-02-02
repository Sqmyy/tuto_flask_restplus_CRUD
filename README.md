# ANSIBLE

Avec Ansible on utilise un playbook pour gérer plusieurs noeuds distants

L'inventaire décrit l'ensemble des noeuds ciblé par Ansible on peut y regrouper les noeuds par domaines et sous-domaines

Le playbook va être la liste des tâches à exécuter sur les noeuds distants

Les tasks sont spécifique à UN seul playbook et on y précise l'hôte sur lequel exécuter la task
généralement pratiquées dans des petits playbooks car beaucoup de details y sont précisés donc ça alourdit le playbook
qui peut vite devenir illisible car très long

Les roles permettent de regrouper des tasks, peuvent être réutilisés dans plusieurs playbooks
possèdent une structure de dossier avec main, doit inclure un main dans au moins 1 des 7 dossiers suivants et ignorer les autres : 
- tasks/
- handlers/ 
- library/
- files/
- templates/
- vars/
- defaults/

Les handlers sont des tasks exécutées à la fin de l'exécution des tasks et roles. Ils sont efficaces car un handler s'exécute une seule fois malgré le nombre de task qui y fait appel

Dans un playbook l'ordre d'execution est :

1) Les tasks s'exécutent en premières
2) Les roles en deuxième
3) Les handlers s'exécutent à la fin



# OPENSTACK 

Openstack permet de créer des clouds privés ou publics et est composé de plusieurs briques dont:

- __NOVA :__ Permet de créer et gérer des serveurs virtuels, dépend de Glance Neutron Keystone et Placements et est composé de plusieurs éléments qui communiquent entre eux :
    - Une base de donnees en SQL
    - l'API communique avec les autres components via requêtes HTTP
    - Le Scheduler décide quel hôte possède quelle instance
    - Le Compute communique avec les VM
    - Le Conductor gère les requêtes qui ont besoin de coordination
    - Les Placements garde une trace des infos sur le provider comme le type de ressource que le provider utilise, ...
	
Permet aussi de créer/gérer les groupes de sécurité, utile par exemple avec NEUTRON pour établir les règles de connexion
à un réseau virtuel

- __GLANCE :__
Permet la découverte, l'enregistrement et la fourniture de services pour les images disques et serveurs

- __KEYSTONE :__
Catalogue de services et correlation des utilisateurs avec leurs droits d'accès. C'est pour l'authentification de client

- __NEUTRON :__ 
Administration du réseau et des adresses IP utilisées par les instances de traitements. Permet le Loadbalancing-as-a-Service et le FireWall-as-a-Service. differentes technologies pour fonctionner:
	Neutron est composé par différentes couches sur Neutron:

    - __Controller(OBLIGATOIRE)__ Exécute l'Identity service, l'Image service, les Network agents
inclut des services de support comme BDD SQL. A besoin de 2 interfaces réseau

    - __Compute (OBLIGTOIRE)__
Exécution de la VM et un networking service agent qui connecte les instances au réseau virtuel et un pare-feu. A besoin de 2 interfaces réseau

    - __Block Storage(OPTIONNEL)__
Espace de stockage contenant les "disques durs" on peut en deployer plusieurs. A besoin d'une interface réseau

    - __Object Storage(OPTIONNEL)__
On coupe les données en plusieurs blocs ces blocs sont indépendants les uns des autres et peuvent être utilisés sur plusieurs systèmes. On peut en deployer plusieurs. A besoin d'1 interface réseau

### Creation d'une infrastructure réseau :
- Creation de deux networks et sub-networks sur chaque network auxquels on relie des VM et on associe des ports à la création des networks, des DHCP sont automatiquement crées
		
- Grâce à NOVA on établit les règles de sécurités des groupes qui vont utiliser l'infrastructure
  
- Pour que nos VM puissent communiquer avec un autre reseau il faut
		
- Créer un routeur virtuel (external virtual router), pour le rendre joignable sur internet, on set le router comme Gateway.
