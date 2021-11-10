# Avancée / Planning du cours de MIF08 (Compilation)
_Année 2021-2022_

* Matthieu Moy, Université Lyon 1, LIP https://matthieu-moy.fr/

<!-- 
## Organisation du cours en hybride

L'organisation de l'UE en « mode COVID » est la suivante :

* Pour chaque créneau, les instructions détaillées se trouvent ci-dessous.

* Tous les CM sont à distance

* Les TD et TP sont faits en hybride, certains étudiants et enseignants à distance, d'autres en présentiel. Pour chaque créneau, vous trouverez une case sur TOMUSS indiquant la salle (si vous êtes en présentiel) ou « à distance » si vous êtes à distance. La répartition présentiel/distanciel est faite dans la mesure du possible en suivant les couleurs jAune/Bleu de TOMUSS. Pour les TP/TD à distance, rendez-vous sur le canal correspondant de chat-info (les enseignants utiliseront parfois d'autres outils, par exemple pour une explication ponctuelle en visio, mais posteront le lien vers les outils utilisés dans le canal de chat-info).

* Les groupes B et E sont parfois affectés à des salles de TD pour les TP. Venez avec votre ordinateur personnel pour ces séances.
-->

## Communication et nouvelles du cours

* [NEWS.md](NEWS.md) contient les nouvelles du cours (envoyées par email également).
<!-- 
## Organisation du cours à distance

* Tous les enseignements passent à distance pendant le mois de novembre (au moins) -->

* Pour rejoindre les canaux de discussions sur chat-info, cliquez sur les liens suivants :
    - [compil-2021](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2Fynpajp) pour les discussions générales sur le cours. Vous pouvez utiliser ce canal pour discuter entre vous et pour poser des questions aux enseignants. Nous ouvrirons plus de canaux si nécessaire. Merci d'utiliser le canal commun et non les messages directs ou le mail pour poser vos questions, comme ça tout le monde en profite.

## Intervenants

* Groupe A : Matthieu Moy (+ Guillaume Bouchard pour les TPs)
* Groupe B : Elise Jeanneau (+ Gabriel Radanne pour les TPs)
* Groupe C : Gregoire Pichon (+ Nicolas Louvet pour les TPs)
* Groupe D : Joris Picot (+ Hugo Thievenaz pour les TPs)

## Vidéos des CM

Toutes les vidéos sont disponibles dès maintenant :

[La playlist Youtube MIF08](https://www.youtube.com/playlist?list=PLtjm-n_Ts-J9HSZ9ahpbsC_kTQMzUZQPx)

Le contenu des vidéos (réalisées en 2020) est sensiblement le même que celui des CM présentiels. Il est recommandé de venir en présentiel.

## Infrastructure technique, logiciels à installer

Les TP utilisent la chaîne d'outils RiscV, un peu lourde à installer. Voir [INSTALL.md](INSTALL.md) pour les consignes. À faire avant les TPs si vous voulez travailler sur vos machines personnelles.

Si vous n'arrivez pas à installer les outils sur vos machines, vous pourrez travailler sur les ordinateurs de la fac, et nous fournissons aussi des machines virtuelles pré-installées : [VM.md](VM.md).

## Planning

## Mercredi 15/09/2021

- :book: 14h: Cours 1: Introduction, machine cible (RISCV), lexing :
    - Introduction au cours, à la compilation et à l'architecture cible : [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/capmif_cours01_intro_et_archi.pdf)
    - Lexing (et parsing) : [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/capmif_cours02_lexing_parsing.pdf) <!-- TODO: passer parsing sur CM 1, sinon il manque un bout pour le TD. -->
    - [Vidéo "teaser"](https://youtu.be/ny7HlqyuM9E)
    - [vidéo d'introduction au cours](https://www.youtube.com/watch?v=zGifE8MfPWA)
    - [vidéo sur RISCV](https://youtu.be/ZdElX9e_tAI)
    - [vidéo lexing](https://www.youtube.com/watch?v=UlUTSsOA9Qc)
    - Extrait de la documentation RISCV: [riscv_isa.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/riscv_isa.pdf)
    - chat sur [compil-2021](https://go.rocket.chat/invite?host=chat-info.univ-lyon1.fr&path=invite%2Fynpajp).
    - :100: QCM noté sur TOMUSS, à faire avant dimanche 19/09/2021, 23:59

- :pencil2: 15h45: TD1 : Architecture RISCV, Lexing, Parsing
    - Salles :
        - Groupe A : Nautibus TD1 (Matthieu Moy)
        - Groupe B : Nautibus TD2 (Elise Jeanneau)
        - Groupe C : Nautibus TD3 (Grégoire Pichon)
        - Groupe D : Nautibus TD10 (Joris Picot)
    - [Énoncé du TD1](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/td1.pdf)
    - Rappel, extrait de la documentation RISCV : [riscv_isa.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/riscv_isa.pdf)
    - Lexing et parsing avec ANTLR en 2 slides : [td1-slides.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/td1-slides.pdf)

- :hammer: 17h30: TP1 : Python et RiscV
    - Salles :
        - Groupe A1 : Nautibus TP10 (Matthieu Moy)
        - Groupe A2 : Nautibus TP11 (Guillaume Bouchard)
        - Groupe B1 : Nautibus TP5 (Elise Jeanneau)
        - Groupe B2 : Nautibus TP6 (Gabriel Radanne)
        - Groupe C1 : Nautibus TP1 (Gregoire Pichon)
        - Groupe C2 : Nautibus TP2 (Nicolas Louvet)
        - Groupe D1 : Nautibus TP12 (Joris Picot)
        - Groupe D2 : Nautibus TP13 (Hugo Thievenaz)
    - Énoncé : [TP1 python/archi](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/tp1.pdf)
    - Fichiers du TP1 : [TP01/](TP01/).

## Mercredi 6/10/2021

- :book: 8h: Cours 2: Lexing, Parsing, interprétation
    - Parsing : [deuxième partie des transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/capmif_cours02_lexing_parsing.pdf)
    - [vidéo parsing](https://www.youtube.com/watch?v=y9MrfDzrAmA)
    - [transparents sémantique et interprète](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/capmif_cours03_interpreters.pdf)
    - [vidéo sémantique et interprète](https://youtu.be/8PYhBsgRO6g)

- :100: QCM noté sur TOMUSS, à faire avant lundi 11/10/2021, 23:59.

- :pencil2: 9h45: TD, Arbres abstraits, attributions, types
    - Salles :
        - Groupe A : Nautibus TD 1
        - Groupe B : Nautibus TD 2
        - Groupe C : Nautibus TD 3
        - Groupe D : Nautibus TD 10
    - [Énoncé du TD2](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/td2.pdf)

- :hammer: 14h-17h15: TP2, ANTLR
    - Salles :
        - Groupe A1 : Nautibus TP10
        - Groupe A2 : Nautibus TP11
        - Groupe B1 : Nautibus TP5
        - Groupe B2 : Nautibus TP6
        - Groupe C1 : Nautibus TP1
        - Groupe C2 : Nautibus TP2
        - Groupe D1 : Nautibus TP13
        - Groupe D2 : Nautibus TP12
    - Transparents de présentation : [capmif_labs.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/capmif_labs.pdf)
    - Si besoin : des VM pour vous dépanner en cas de problème sur machine perso : [VM.md](VM.md)
    - Énoncé : [TP2 antlr](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/tp2.pdf)
    - Fichiers du TP2 : [TP02/](TP02/).
    - **Date limite pour le rendu (noté) : mardi 12/10/2021, 23h59.**

## Mercredi 13/10/2021

- :book: Cours 3, Typage : 14h-15h30
    - [transparents typage](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/capmif_cours04_typing.pdf)
    - [vidéo typage](https://youtu.be/2A-hQy_6YlE)
- :100: QCM noté sur TOMUSS, à faire avant dimanche 17/10/2021, 23:59

- :hammer: TP3, interprète MiniC : 15h45-17h15
    - Salles :
        - Groupe A1 : Nautibus TP10
        - Groupe A2 : Nautibus TP11
        - Groupe B1 : Nautibus TP5
        - Groupe B2 : Nautibus TP6
        - Groupe C1 : Nautibus TP9 (Attention, bug de groupe sur ADE)
        - Groupe C2 : Nautibus TP14 (Attention, bug de groupe sur ADE)
        - Groupe D1 : Nautibus TP13
        - Groupe D2 : Nautibus TP12
    - Énoncé : [TP3 frontend, interprète](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/tp3.pdf)
    - Fichiers du TP3 : [TP03/](TP03/) puis [MiniC/](MiniC/).
    - **Date limite de rendu du TP3 : dimanche 7 novembre 2021, 23h59 (vous aurez une séance d'1h30 pour finir le TP le 3/11/2021).**

## Mercredi 3/11/2021

- :hammer: TP3, interprète MiniC (suite) : 14h00-15h30
    - Salles :
        - Groupe A1 : Nautibus TP10
        - Groupe A2 : Nautibus TP11
        - Groupe B1 : Nautibus TP5
        - Groupe B2 : Nautibus TP6
        - Groupe C1 : Nautibus TP7
        - Groupe C2 : Nautibus TP8
        - Groupe D1 : Nautibus TP13
        - Groupe D2 : Nautibus TP12

- :book: Cours 4 : 15h45-17h15
    - génération de code 3 adresses + allocation naive, [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/capmif_cours05_3ad_codegen.pdf), [vidéo](https://youtu.be/m2x7leFnCN4)
    - Représentations intermédiaires, [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/capmif_cours06_irs.pdf), [vidéo 6a](https://youtu.be/dD9bRhLfykM), [vidéo 6b](https://youtu.be/Xico_JTK3XQ).

- :100: QCM noté sur TOMUSS, à faire avant Dimanche 7/11/2021, 23:59.

## Mercredi 10/11/2021

- :pencil2: TD 3 : 14h00-15h30 :
    - Salles :
        - Groupe A : Nautibus TD 1
        - Groupe B : Nautibus TD 2
        - Groupe C : Nautibus TD 3
        - Groupe D : Nautibus TD 10
    - Sujet : [TD3 génération de code](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/td3.pdf)

- :hammer: TP, 15h45-17h15
    - Salles :
        - Groupe A1 : Nautibus TP10
        - Groupe A2 : Nautibus TP11
        - Groupe B1 : Nautibus TP5
        - Groupe B2 : Nautibus TP6
        - Groupe C1 : Nautibus TP7
        - Groupe C2 : Nautibus TP8
        - Groupe D1 : Nautibus TP13
        - Groupe D2 : Nautibus TP12
    - Transparents de présentation : [capmif_labs.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_labs.pdf)
    - Rappel : des VM pour vous dépanner en cas de problème sur machine perso : [VM.md](VM.md)
    - Énoncé : [TP4 génération de code](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2021/tp4.pdf)
    - Fichiers du TP4 : [MiniC/TP04/](MiniC/TP04/).
    - **Date limite pour le rendu (noté) : 17 décembre 2021, 23h59.** Si vous rendez après la deadline mais avant le 2 janvier 2022, 23h59, un malus d'un point sur 20 est appliqué, puis un point de malus par jour de retard supplémentaire. Aucun TP ne sera accepté après le mardi 4 janvier 2022, 23h59.

## Mercredi 1/12/2021

- :hammer: TP 4 (suite), 14h-17h15 : cf. ci-dessus pour les supports et les salles (mêmes que le 10/11)

## Pondération des notes (indicative pour l'instant sauf l'examen final qui sera forcément 50%)
  - QCM : 10% (2% chacun)
  - TP2 parsing et évaluation d'expression : 5%
  - TP3 interprète : 10%
  - TP4 génération de code : 12.5%
  - TP5 allocation de registres : 12.5%
  - Examen final : 50 %

La session 2 remplace la note d'examen final.

# BROUILLON DE PLANNING

```
08/12/2021:
  14:00 -> 15:30 : CM 5 (CM, Matthieu Moy : IR and Register allocations)
  15:45 -> 17:15 : TD 4 (A, Matthieu Moy : Liveness analysis)
  15:45 -> 17:15 : TD 4 (B, Elise Jeanneau : Liveness analysis)
  15:45 -> 17:15 : TD 4 (C, Gregoire Pichon : Liveness analysis)
  15:45 -> 17:15 : TD 4 (D, Joris Picot : Liveness analysis)
  15:45 -> 17:15 : TD 4 (E, Guillaume Bouchard : Liveness analysis)

Deadline TP4 juste avant les vacances de noel

05/01/2022:
  14:00 -> 15:30 : TD 5 (A, Matthieu Moy : Register allocation)
  14:00 -> 15:30 : TD 5 (B, Elise Jeanneau : Register allocation)
  14:00 -> 15:30 : TD 5 (C, Gregoire Pichon : Register allocation)
  14:00 -> 15:30 : TD 5 (D, Joris Picot : Register allocation)
  14:00 -> 15:30 : TD 5 (E, Guillaume Bouchard : Register allocation)
  15:45 -> 17:15 : TP 5 (début) (A1, Matthieu Moy : Smart register allocation)
  15:45 -> 17:15 : TP 5 (début) (B2, Thierry Excoffier : Smart register allocation)
  15:45 -> 17:15 : TP 5 (début) (B1, Elise Jeanneau : Smart register allocation)
  15:45 -> 17:15 : TP 5 (début) (C2, Nicolas Louvet : Smart register allocation)
  15:45 -> 17:15 : TP 5 (début) (C1, Gregoire Pichon : Smart register allocation)
  15:45 -> 17:15 : TP 5 (début) (D2, Joris Picot : Smart register allocation)
  15:45 -> 17:15 : TP 5 (début) (D1, Hugo Thievenaz : Smart register allocation)
  15:45 -> 17:15 : TP 5 (début) (E2, Gabriel Radanne : Smart register allocation)
  15:45 -> 17:15 : TP 5 (début) (E1, Guillaume Bouchard : Smart register allocation)
  15:45 -> 17:15 : TP 5 (début) (A2, Lionel Morel : Smart register allocation)

12/01/2022:
  14:00 -> 15:30 : TP 5 (fin) (A1, Matthieu Moy : Smart register allocation)
  14:00 -> 15:30 : TP 5 (fin) (B2, Thierry Excoffier : Smart register allocation)
  14:00 -> 15:30 : TP 5 (fin) (B1, Elise Jeanneau : Smart register allocation)
  14:00 -> 15:30 : TP 5 (fin) (C2, Nicolas Louvet : Smart register allocation)
  14:00 -> 15:30 : TP 5 (fin) (C1, Gregoire Pichon : Smart register allocation)
  14:00 -> 15:30 : TP 5 (fin) (D2, Joris Picot : Smart register allocation)
  14:00 -> 15:30 : TP 5 (fin) (D1, Hugo Thievenaz : Smart register allocation)
  14:00 -> 15:30 : TP 5 (fin) (E2, Gabriel Radanne : Smart register allocation)
  14:00 -> 15:30 : TP 5 (fin) (E1, Guillaume Bouchard : Smart register allocation)
  14:00 -> 15:30 : TP 5 (fin) (A2, Lionel Morel : Smart register allocation)

Deadline TP5 mercredi 12/1 soir pour éviter les clashs avec les deadlines mif03 (7, 10, 11, 13, 14 janvier selon les groupes).
```

# CI-DESSOUS, LE PLANNING DE L'ANNEE DERNIERE QUI SERA MIS À JOUR AU FUR ET À MESURE

## Jeudi 10/12/2020

- :hammer: TP, 14h-15h30 : fin du TP 4 (cf. ci-dessus pour les supports et liens chat-info).

- :book: Cours 5, allocation de registres
    - Register allocation + data-flow analyses : [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_cours07_regalloc.pdf), [vidéo première partie](https://youtu.be/9902mMgDIK8), [vidéo deuxième partie](https://youtu.be/LknSDccweFw).

- :100: QCM noté sur TOMUSS, à faire avant 23:59 le jour même (10/12)

## Mercredi 6/01/2021
<!-- 
- :mag_right: Contrôle continu (tp) (20 min de composition) une grammaire
    ANTLR -->

Toujours les mêmes groupes et canaux sur chat-info, cf. ci-dessus.

- :pencil2: 14h-15h30 :
    - Énoncé : [TD4 liveness](https://compil-lyon.gitlabpages.inria.fr/mif08-20/td4.pdf)

- :hammer: 15h45-17h15 : TP5
    - Énoncé : [TP5 allocation de registres](https://compil-lyon.gitlabpages.inria.fr/mif08-20/tp5.pdf)
    - Fichiers du TP5 : [MiniC/TP05/](MiniC/TP05/).
    - **Date limite pour le rendu (noté) : dimanche 17/01/2021, 23h59.**

## Mercredi 13/01/2021

- :pencil2: 14h-15h30
    - Énoncé : [TD5 regalloc](https://compil-lyon.gitlabpages.inria.fr/mif08-20/td5.pdf)

- :hammer: 15h45-17h15 : TP5, suite
    - Même sujet et organisation que la semaine d'avant en TP.
<!-- 
### Rendus Tomuss et feedback

- CC de cours : la note arrivera fin de la semaine.

- CC de tp noté : rendu mercredi 15/01 à 14h30. La correction
arrivera avant la fin de la semaine.

- Rendu de l'évaluateur juste après la démo le vendredi 17/01. Une
note "automatique" vous sera rendue durant le week-end.

- Tps de génération de code directe: rendu le mardi 21/01 à 18h - une
correction partielle sera fournie à la même heure. 

- Dernier TP : rendu le dimanche 26 à 23h59.

- Les deux dernières notes de TP vous seront fournies après l'examen. -->

## Annales et consignes pour l'examen

* L'examen Session 1 2020-2021 : [exam_mif08_2020.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-20/exam_mif08_2020.pdf) et les éléments de corrigé : [exam_mif08_2020_corr.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-20/exam_mif08_2020_corr.pdf)

* L'examen 2019-2020 : [mif08_exam1920.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-20/mif08_exam1920.pdf) et les éléments de corrigés : [mif08_exam1920-corr.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-20/mif08_exam1920-corr.pdf).

* L'examen 2018-2019 : [exam_mif08_2018.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-20/exam_mif08_2018.pdf)

* Aide mémoire fourni avec le sujet (sera fourni pour l'examen de janvier 2021): [mif08_sheet20.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-20/mif08_sheet20.pdf)

* [Consignes pour l'examen](https://compil-lyon.gitlabpages.inria.fr/mif08-20/exam_mif08_2020-page1.pdf)

* Examen de session 1 :
    - Pour les étudiants bénéficiant d'un tiers-temps : 8h-10h, salle Nautibus C2.
    - Pour les étudiants ne bénéficiant pas de tiers-temps : 8h15-9h45, Amphis Déambu (place exacte sur TOMUSS)
