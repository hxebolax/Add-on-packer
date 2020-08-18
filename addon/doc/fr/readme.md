# Empaqueteuse d'extensions

Cette extension provient de la nécessité d'avoir une sauvegarde des extensions installées.

NVDA a une grande collection d'extensions officielles, facile d'obtenir à partir de les dépôts officiels  ou à partir de différents comptes de  Github des auteurs.

Mais en même temps y a également un certain nombre d'extensions non officielles est parfois difficile de savoir où ont été obtenus.

L'idée est venue lorsque un ami   ma demander une extension non officielle et de ne pas avoir à la main l'extension elle fallait l'empaqueter.

Alors que le processus de l'empaquetage d'une extension est facile, mais pas connu par tout le monde il me est apparu que cette fonction serait fantastique que NVDA la puisse avoir.

Eh bien, c'est ce qui rend cette extension,  l'empaquetage automatique de ces extensions que l'utilisateur veut avoir pour pouvoir installer sur une autre copie de NVDA, sur une installation propre de NVDA ou simplement pour le partager.

## Utilisation de l'extension

L'extension est divisée en quatre zones:

* La première contenant une liste de tous nos extensions installées soit activées ou désactivées. Dans cette liste, nous sélectionnons tous les   extensions que nous souhaiterons.
* La deuxième une rangée de boutons pour sélectionner rapidement toutes les extensions ou pour supprimer rapidement tous les sélection que nous avions fait.
* La troisième une zone de texte en lecture seule contenant le répertoire de sortie et un bouton pour sélectionner ce répertoire de sortie.

J'ai mis la zone de texte en lecture seule pour pouvoir examiner facilement à tout moment le répertoire de sortie. J'ai décidé de ne pas mettre l'écriture normale pour éviter certaine pulsation par erreur et que le répertoire puisse être affecté.

* La quatrième une rangée de boutons avec le bouton pour Générer les extensions déjà empaquetées et et un autre pour sortir de l'extension.

### Commandes clavier rapides dans l'extension

* Alt + L: Nous allons placer le focus sur la liste des extensions.
* Alt + S: Nous sélectionnons toutes les  extensions indifféremment si auparavant y avait déjà une de cochée.
* Alt + E: Nous décochons toutes les extensions que nous avions cochées.
* Alt + R: Nous allons ouvrir une fenêtre de sélection du répertoire pour sélectionner le répertoire de sortie.
* Alt + G: Nous démarrons  la génération des extensions que nous avions sélectionnées dans le répertoire de sortie.
* Alt + F o Alt + F4: Nous fermons l'extension.

## Autres informations d'intérêts

* L'extension  nous avertira à tout moment avec un dialogues  d'information sur l'état du déroulement de la manipulation accompli.
* Nous avertira si nous essayons de générer une  extension sans avoir  sélectionnée aucune.
* Nous avertira si nous essayons de générer une  extension sans avoir un répertoire de sortie défini.
* Nous avertira lorsque le processus    est un succès de même  lorsque une erreur se produit.
* Le répertoire de sortie  sera sauvegardé afin qu'il soit spécifié à la prochaine fois que nous utilisons l'extension, ce paramètre est effacé si le répertoire de sortie est supprimé et nous allons sélectionner un autre répertoire existant.
* Pendant la génération des extensions nous serons  averti  par une barre de progression indiquant le pourcentage d'avancement accompli à tout moment.
* Les fichiers résultants ont sur le nom  en plus un repère pour identifier qui ont été générés et ne sont pas d'origine. Ce repère est (gen).

# Note très importante

Mentionnant que les fichiers résultants sont tels que nous les avons dans notre répertoire Addon sans ajouter ni supprimer quoi que ce soit de la part de cette extension.

Cela signifie  que elle inclus toutes les informations de l'extension que nous sélectionnons.

Bien qu'il est pas normal qu'un développeur d'extensions eut inclus des informations sensibles dans le propre répertoire de l'extension.

En fait, ceci est considéré comme une mauvaise pratique il est peu probable au moins que dans les extensions officielles se produisent.

Mais à l'existence des centaines d'extensions non officielles et de diverse nature soyez prévenus que si une extension comprend des informations sensibles dans le propre répertoire de votre extension, ces informations sensibles seront inclus dans le fichier généré.


Nous devons donc considérer cet aspect de la confidentialité et de la sécurité pour savoir si nous devions partager une extension générée si apporte des informations sensibles que nous ne voulons pas partager.

Comme je le mentionne ce qui est presque improbable, mais soyez prévenus et ceci  avec l'utilisation de cette extension Vous accepter  savoir que vous avez été informé et déchargeant  de toute responsabilité à l'auteur de cette extension.
