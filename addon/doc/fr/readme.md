# Manuel de l'extension Utilitaires pour les extensions de NVDA

Cette extension essaye d'être un paquet d'utilitaires pour nos extensions installées et non installées.

Dans les différentes zones elle essaye d'être le plus rapide possible en donnant la possibilité de faire des actions à nos extensions de manière massive et de ne pas avoir à en aller une à une comme dans le Gestionnaire d'Extensions.

Les zones déjà ajoutées seront améliorées dans les différentes versions car de nouvelles fonctions seront ajoutées.

Cette extension peut être lancé à partir du menu Outils / Utilitaires pour les extensions de NVDA.

L'extension n'a pas de touche de raccourci assigné pour une utilisation rapide.

Vous pouvez ajouter un raccourci allant dans le menu NVDA / Préférences / Gestes de commandes puis rechercher  la catégorie Utilitaires pour les extensions de NVDA.

## Décharge de responsabilités

L'utilisateur final est le dernier responsable de l'utilisation de l'extension.

Cette extension essaye que tout soit aussi fiable que possible, mais des problèmes peuvent toujours survenir c'est pourquoi l'auteur de l'extension ne se responsabilise pas de tout problème résultant de l'utilisation de cette extension.

# Description générale

L'extension est incluse dans 3 sections.

* 1ª section: Liste où nous pouvons choisir la catégorie que nous souhaitons utiliser. C'est là que le focus est mis à chaque fois que nous appelons l'extension.

Nous pouvons nous déplacer avec flèches haut et bas dans cette liste.

* 2ª section: La zone qui comprend le contenu de la catégorie que nous avons choisie.

Cette zone change en fonction de la catégorie. Description des catégories plus loin.

Nous pouvons accéder à partir des catégories avec les touches de raccourci ou en faisant Tabulation.

* 3ª section: Cette section contient une zone d'édition qui sera activée lorsqu'une action est exécutée en donnant des informations à l'utilisateur de ce qui se passe. L'utilisateur sera également informé par une barre de progression dans toutes les actions.

Il comprend également les boutons qui nous permettront d'interagir en fonction de ce qui s'est passé lors de l'action comme un bouton Fermer qui fermera l'extension.

Tant qu'il n'y a pas d'action en cours, l'extension peut être fermée avec Échap, Alt+F4 ou tabuler jusqu'au bouton Fermer.

## Empaqueteuse d'extensions

Si nous choisissons cette catégorie si nous faisons Tabulation nous tomberons dans une liste de toutes nos extensions installées soit activées ou désactivées ou non compatibles.

Nous pouvons également aller rapidement avec Alt+L, dans cette liste nous pouvons sélectionner avec la barre d'espace toutes ces extensions que nous voulons choisir afin de faire une copie de sauvegarde dans un répertoire que nous choisissons.

Chaque extension sera générée avec son nom et sa version et en plus d'un repère comme identifiant “_gen”, ces extensions générées peuvent être installées avec NVDA sans aucun problème.

Si nous tabulons, nous tomberons sur un bouton appelé Sélection ou nous pouvons accéder rapidement avec Alt+S, ce bouton Si nous appuyons dessus, un menu sera affiché pour sélectionner ou désélectionner toutes les extensions rapidement.

Si nous tabulons à nouveau, nous tomberons sur un bouton appelé  Générer ou touche de raccourci Alt+G, Si nous appuyons sur ce bouton et que nous avons au moins une extension cochée, une fenêtre s'ouvrira pour choisir le répertoire où nous voulons enregistrer l'extension ou les extensions sélectionnées.

Une fois que le répertoire a été choisi et en appuyant sur OK commencera la génération des extensions. Le focus sera laissé dans la zone de texte en lecture seule dans laquelle les informations apparaîtront à côté d'une barre de progression qui nous informera du pourcentage  d'avancement accompli à tout moment. Le bouton Fermer, ainsi que le reste de l'interface seront désactivés jusqu'à ce que l'action de générer les extensions se termine.

Une fois l'action terminée nous informera que tout a réussi ou qu'il y a un problème et si maintenant nous faisons Tabulation nous pouvons maintenant choisir OK (Alt+O), Annuler (Alt+A) ou fermer l'interface si nous le souhaitons.

Les boutons OK et Annuler ils sortiront au fur et à mesure que l'action est terminée.

Pour générer des extensions, il est essentiel d'avoir cochée au moins une sinon nous serons informés par un message explicatif.

## Installateur multiple

Cette catégorie nous permettra de choisir un répertoire où nous avons des extensions et nous pouvons toutes les installer d'un seul coup.

Lorsque nous entrons dans cette catégorie, nous tomberons sur un bouton appelé "Sélectionner un répertoire avec les extensions à installer..." ou raccourci (Alt+S), si nous appuyons dessus, nous allons ouvrir une fenêtre pour choisir le répertoire contenant les extensions.

Le reste de l'interface de cette catégorie est désactivé jusqu'à ce que nous choisissions un répertoire.

Lorsque nous choisissons un répertoire le focus sera laissé dans la zone de texte en lecture seule où nous serons informés de ce qui se passe lors du balayage en recherche des extensions, nous recevrons également des informations de la barre de progression.

Nous serons informés une fois le balayage terminé en cas de problème et comment agir. Dire que seulement seront acceptées les extensions conformes à l'API de NVDA que nous avons installées en rejetant toute extension incompatible ou endommagée.

Une fois  le balayage terminé, et si des extensions ont été trouvées, et en appuyant sur OK, la liste sera activée avec les noms des extensions qui ont été trouvées dans ledit répertoire.

Nous pouvons rapidement aller dans cette liste avec (Alt+L), dans cette liste, nous pouvons choisir autant d'extensions que nous voulons en les cochant avec la barre d'espace.

Si nous tabulons, nous aurons le même bouton Sélection qui se trouve sur l'écran Empaqueteuse d'extensions et que je n'expliquerai pas parce que c'est sa même utilisation.

Si nous tabulons à nouveau, nous tomberons sur le bouton Installer ou touche de raccourci (Alt+I).

Si nous avons au moins une extension sélectionnée et lorsque nous appuyons sur ce bouton, l'installation de l'extension sera effectuée  soit une ou plusieurs sans montrer la fenêtre classique d'installation de NVDA, avec cela, nous accélérons l'installation des extensions.

Dire que cette étape a également des protections telles que la vérification de l'API, que l'extension n'est pas endommagée et d'autres choses internes de NVDA. Tout pour toujours essayer le meilleur fonctionnement de notre lecteur.

Lorsque nous appuyons sur le bouton Installer le focus sera laissé dans la zone de texte en lecture seule où nous serons informés de ce que fait l'extension.

De même, une fois terminé, nous informera tantôt si le processus    est un succès comme s'il y avait une extension qui ne pouvait pas être installée ou lorsque des erreurs se produise.

Selon ce qui s'est passé, nous activerons le bouton OK ou Annuler à côté du bouton Fermer.

Si vous activez le bouton OK, c'est parce que NVDA a installée une extension, et pour que ces changements prennent effet, NVDA doit être redémarré, si nous appuyons  sur ce bouton, NVDA redémarrera et nous aurons les extensions  ou l'extension installée.

Si nous n'acceptons pas et ne fermons pas, nous ne pourrons pas utiliser à nouveau l'extension avant de redémarrer NVDA, il s'agit d'une protection pour éviter la duplication des actions.

Si autrement il y avait des échecs et que seul le bouton Annuler est affiché, nous pouvons appuyer sur celui-ci et revenir à l'interface pour faire d'autres choses.

### MISE EN GARDE

Cette catégorie est mise en œuvre pour accélérer l'installation d'extensions, mais mal utilisée en installant des extensions pour installer, il peut conduire au dysfonctionnement du lecteur. Il est de la responsabilité de l'utilisateur de l'utiliser correctement.

## Désinstalle des extensions

Cette catégorie nous permettra de désinstaller rapidement les extensions et d'un seul coup.

Nous pouvons choisir dans la liste des extensions que nous avons installées. Nous pouvons sélectionner avec la barre d'espace. Pour aller rapidement dans la liste (Alt+L).

Nous avons également le bouton Sélection (Alt+S) qui remplit la fonction exactement la même chose que dans les catégories précédentes et que je n'expliquerai plus.

Si nous tabulons, nous trouverons le bouton Désinstaller ou touche de raccourci (Alt+D) si nous appuyons dessus et que nous avons une ou plusieurs extensions sélectionnées, nous laissera le focus dans la zone de texte en lecture seule et nous informera de ce qui est fait.

Nous serons également informés par le biais de la barre de progression.

Une fois terminé, nous informera du résultat et, comme dans la catégorie Installateur multiple s'affichera le bouton OK pour nous informer qui devra être redémarrer NVDA ou Annuler pour nous informer  que quelque chose s'est mal passé et le bouton Fermer.

N'oubliez pas que si nous fermons cette catégorie et que nous n'avons pas assisté à la nécessité de redémarrer l'extension, il ne peut pas être utilisé à nouveau tant que NVDA ne redémarre pas.

### MISE EN GARDE

Lors de la désinstallation des extensions une fois que nous appuyons sur le bouton Désinstaller n'a pas de retour en arrière, il est donc convenable de nous assurer que nous savons où obtenir les extensions que nous éliminons au cas où nous voulons les installer comme si cette extension contient des informations dans le répertoire de l'extension elle-même, ces informations seront supprimées.

Ce n'est généralement pas une bonne praxis et NVDA ne recommande pas que les extensions conservent des informations dans le même répertoire de l'extension, mais c'est déjà une décision du programmeur de l'extension.

Par conséquent, je me répète utiliser cette catégorie sous votre responsabilité.

## Active / désactive les extensions

Cette catégorie nous permettra d'activer ou de désactiver en masse nos extensions.

Si nous entrons dans la catégorie, nous tomberons dans la liste des extensions activées, nous pouvons accéder rapidement avec (Alt+L), nous pouvons cocher les extensions que nous voulons désactiver avec la barre d'espace.

Si nous avons des extensions désactivées, nous aurons une deuxième liste avec ces extensions, nous pouvons rapidement nous déplacer entre les listes avec (Alt+L) dans cette liste des extensions désactivées, nous pouvons également cocher celles que nous voulons activer avec la barre d'espace.

Nous pouvons cocher les extensions dans les deux listes en tenant compte du fait que l'action sera effectuée en sens inverse, désactivant les extensions cochées dans la liste des extensions activées comme activant les extensions cochées dans la liste des extensions désactivées.

Cette catégorie a également un bouton Sélection, mais avec une petite différence, lorsque nous appuyons sur celui-ci, il contiendra un sous-menu pour chaque liste afin que nous puissions sélectionner ou désélectionner tout pour la liste que nous choisissons.

Si nous tabulons, nous nous trouverons avec le bouton Traiter ou touche de raccourci (Alt+T), si nous appuyons dessus, nous laissera le focus dans la zone de texte en lecture seule et nous informera de ce qui est fait.

Une fois que l'action se terminera, cela se produira de la même manière que dans les catégories précédentes nous informant et activant les boutons correspondants.

Je vous rappelle que si l'action est satisfaisante et que nous ne redémarrons pas, l'extension ne peut pas être utilisée tant que NVDA n'est pas redémarré.

## Modificateur des manifestes

Dans cette catégorie, nous pouvons modifier le manifeste et ainsi de pouvoir rendre compatible les extensions avec l'API requise par NVDA. Nous pouvons modifier le manifeste au extensions installées ou extensions que nous avons dans un fichier d'extensions NVDA.

Maintenant, selon la dernière politique de NVDA et jusqu'à nouveaux changements, chaque année dans la première version de NVDA, les programmeurs devront modifier la version pour faire correspondre leur manifeste avec la version de NVDA.

Eh bien, il y aura des programmeurs qui le font immédiatement, d'autres qui prennent son temps pour le faire et d'autres qui ne le feront tout simplement pour avoir abandonné leurs extensions ou pour une raison quelconque.

Dans ce dernier cas, nous devrons faire le changement de la propriété lastTestedNVDAVersion à la main et si nous avons de nombreuses extensions, nous devrons perdre du temps, en plus ce n'est pas une tâche facile pour tous les utilisateurs, car il existe de nombreux niveaux d'utilisateurs.

De plus, si nous voulons essayers les versions bêtas et les RC nous devrons modifier ce paramètre dans les manifestes sinon nous ne pouvons pas avoir l'extension installée.

Eh bien, NVDA est un lecteur d'écran en évolution constante, il existe donc plusieurs fois de nombreuses extensions qui sont laissées en cours de route en raison du manque de développement et du fait de ne pas les adapter aux changements de NVDA dans son évolution.

Cela signifie que le changement de la date dans les manifestes résout un problème momentané pour continuer à utiliser ces extensions qui ne sont pas mises à jour ou que le développeur prend du temps pour les mettre à jour. Mais il y aura des extensions qui ne serviront pas seulement à changer le manifeste et nécessitent des changements internes  pour s'adapter aux nouvelles versions, dans ce cas, l'extension sera brisée et reste à contacter avec l'auteur de ladite extension.

Bien je conseille de mettre à jour les extensions présentant les changements dans les manifestes, bien que nous ayons changé avec cet utilitaire la date étant possible que ces extensions apportent hormis l'adaptation du manifeste des autres modifications que le développeur a fait.

Une fois que nous accéderons à cette catégorie, nous tomberons dans la liste qui contiendra toutes les extensions que nous avons installées à côté de sa version API. Nous pouvons accéder rapidement avec (Alt+L), nous pouvons sélectionner les extensions que nous voulons modifier leur manifeste en appuyant dessus et autant que nous le voulons.

Si nous tabulons nous tomberons dans trois zones de liste déroulantes:

* Sélectionner la version Majeure: Cette zone de liste déroulante  doit correspondre à la date de la version que aura NVDA.

* Sélectionner la version Mineure: Ici en la laissant en 1 il suffit, cependant j'ai mis les quatre versions qui sortent annuellement s'il y avait des changements. (N'importe quoi peut arriver)

* Sélectionner une révision: Dans cette zone de liste déroulante en la laissant en 0 il suffit, cependant j'ai mis  jusqu'à 9 aussi au cas où.

Si nous tabulons, nous avons à nouveau le bouton Sélection qui nous permettra de sélectionner ou de désélectionner toutes les extensions de la liste.

Si nous tabulons à nouveau, nous tomberons sur le bouton Traiter ou nous pouvons accéder rapidement avec (Alt+T).

Eh bien, si nous appuyons sur ce bouton, nous afficherons un menu avec les options suivantes:

* Traiter installées, si nous choisissons cette option, le processus de modification du manifeste au extensions que nous avons installées et que nous avons sélectionnées commencera. Elle changera pour celles que nous avons choisi dans les zones de liste déroulante de version majeure, mineure et révision.

* Traiter un fichier d'extension, si nous choisissons cette option, une fenêtre de type: Ouvrir dialogue Nom du fichier s'ouvre, où nous devrons choisir le fichier d'extension que nous voulons modifier le manifeste. Dire  qu'avant, nous devons choisir la version majeure, mineure et révision pour que ces changements prennent effet.

Si nous choisissons de modifier le manifeste dans un fichier et que le processus était satisfaisant, dans le répertoire d'origine de l'extension une autre extension sera générée avec le même nom mais en plus avec un repère comme identifiant  “_gen_modify_manifest” ce sera celui qui contient le manifeste modifié à utiliser.

Avec l'une ou l'autre des deux options, il nous sera laissé le focus dans la zone de texte en lecture seule et nous serons informés de ce qui se passera.

Le comportement sera le même que dans les catégories précédentes avec les boutons OK et Annuler.

N'oubliez pas que si nous choisissons un fichier d'extension avant, nous devons modifier les zones de liste déroulante de version majeure, mineure et révision afin qu'elle soit appliquée au fichier que nous choisissons pour cette configuration au manifeste.

### MISE EN GARDE

L'utilisation de cet utilitaire et ses résultats sont exclusivement sous la responsabilité de l'utilisateur final.

## Documentation des extensions

Dans cette catégorie et vu qu'il y a des gens qui ont du mal à trouver comment lire la documentation des extensions, nous pouvons justement faire ça, consulter la documentation que les auteurs ont écrite pour connaître  le maniement des extensions.

Dans cette catégorie, nous trouverons une liste avec touche de raccourci  (Alt+L) dans laquelle toutes les extensions qui ont une documentation seront affichées étant exclues celles qui pour quelque raison que ce soit n'ont pas de documentation.

Si nous tabulons, nous trouverons un bouton appelé "Ouvrir la documentation de l'extension" ou touche de raccourci (Alt+O), Si nous  appuyons ou appelons ce bouton depuis la liste elle s'ouvrira dans notre navigateur par défaut la documentation de l'extension que nous avons choisi dans la liste.

# Traducteurs et contributeurs:

Si quelqu'un souhaite collaborer avec les traductions, il peut le faire via le dépôt de GitHub de l'extension ou en envoyant un e-mail à xebolax@gmail.com

* Anglais: Dragan Ratkovich (traduction automatique)
* Turc: umut korkmaz
* Français: Rémy Ruiz
* Arabe: Wafiq Taher
* Allemand: Moritz Wolfart
* Russe: Valentin Kupriyanov (communauté russe NVDA.RU)
* Italien: Leonardo Marenda
* Ukrainien: Vova Mobile

# Journal des changements.
## Informations sur les mises à jour:

Cette extension suivra la route de mise à jour suivante:

Seules les versions du type majeure.mineure (par exemple v3.1) sont recensées dans cet historique.

Les versions du type majeure.mineure.x (par exemple v3.1.2)  sont des mises à jour de traductions.

Les modifications de l'extension seront reflétées dans cette section expliquant les nouvelles fonctionnalités.

Le document principal ne sera pas modifié étant une orientation pour l'utilisateur.

L'utilisateur est responsable de la révision de cette section pour être informé des modifications.

## Version 1.3.

* Une erreur a été corrigé lors de la génération des extensions.

La dernière version comprenait le dossier __pycache__ que NVDA génère. Dans cette version, l'extension générée sera égale à celle distribuée par le développeur à l'exclusion du dossier __pycache__ de la branche des répertoires.

## Version 1.2.

* Des erreurs graves ont été corrigés dans la sauvegarde.

## Version 1.1.

* Des erreurs ont été corrigés.

* Ajout de la possibilité de faire et de restaurer des sauvegardes.

Maintenant, nous aurons une nouvelle section appelée Faire / restaurer des sauvegardes.

Cette section affichera dans une liste les options que nous pouvons faire lors d'une sauvegarde.

Les options dans cette version qui peuvent être enregistrées dans une sauvegarde  sont:

* Répertoire Dictionnaires (\speechDicts)
* Répertoire Profils (\profiles)
* Répertoire Bloc-notes du Développeur (\scratchpad)
* Fichier de configuration déclencheurs de profils (profileTriggers.ini)
* Fichier de configuration gestes de commandes (gestures.ini)
* Fichier de configuration NVDA (nvda.ini)

Dans la liste s'affichera uniquement les éléments qui sont présents dans notre copie de NVDA ainsi que les répertoires qui ont du contenu.

Si, par exemple, le Répertoire Profils est vide ne laissera pas faire une sauvegarde.

Nous devrons sélectionner au moins un élément de la liste pour pouvoir faire la sauvegarde.

Si nous tabulons, nous trouverons deux boutons:

* Créer une sauvegarde

Si nous appuyons sur ce bouton, une fenêtre classique d'enregistrement de Windows s'ouvrira en disant que nous mettions le nom de notre sauvegarde et où nous voulons l'enregistrer.

Lorsque nous appuyons sur Enregistrer, la sauvegarde commencera et dans la zone de texte en lecture seule de l'état nous dira le résultat  si tout s'est bien passé ou lorsque des erreurs se produise.

* Restaurer une sauvegarde

Lorsque nous appuyons sur ce bouton, une fenêtre classique de Windows s'ouvrira pour ouvrir un fichier de sauvegarde, nous devrons rechercher où  nous avons enregistré la copie et appuyer sur Ouvrir.

Une fois le fichier ouvert, une fenêtre sera affichée avec le contenu de la sauvegarde, dans cette fenêtre, une liste apparaîtra pour sélectionner les éléments que nous voulons restaurer.

Lorsque nous souhaitons appuyer sur Restaurer et dans la zone de texte en lecture seule de l'état nous informera si la restauration a réussi ou qu'il y a un problème.

MISE EN GARDE:

Lorsque nous restaurons un élément de NVDA, il sera nécessaire de redémarrer NVDA afin que toute action que nous effectuons avec l'extension Utilitaires pour les extensions de NVDA sa conséquence sera de redémarrer NVDA soit si nous appuyons sur OK, Annuler, Fermer, Échap ou Alt+F4.

Si une erreur se produit lors de la restauration de plusieurs éléments alors que l'un est restauré également NVDA redémarrera.

## Version 1.0.

* Version initiale.

Elle a été réécrite à partir de zéro laquelle était l'ancienne extension Empaqueteuse d'extensions avec l'incorporation de nouvelles fonctions.

L'extension change de nom à Utilitaires pour les extensions de NVDA mais il continue de maintenir le nom interne dans lequel NVDA le gère en (addonPackager).

En lançant cette version, l'extension cricricri sera sans maintenance, car cette extension comprend déjà le changement de manifestes.
