**Description de l'ensemble de données**
    application_{train|test}.csv

        Il s'agit de la table principale, divisée en deux fichiers pour Train (avec TARGET) et Test (sans TARGET).
        Données statiques pour toutes les demandes. Une ligne représente un prêt dans notre échantillon de données.

    bureau.csv
        Tous les crédits antérieurs des clients fournis par d'autres institutions financières qui ont été signalés au Bureau de crédit (pour les clients qui ont un prêt dans notre échantillon).
        Pour chaque prêt de notre échantillon, il y a autant de lignes que le nombre de crédits que le client avait au Bureau de crédit avant la date de la demande.

    bureau_balance.csv
        Soldes mensuels des crédits antérieurs au Bureau de crédit.
        Ce tableau comporte une ligne pour chaque mois d'historique de chaque crédit précédent signalé au Bureau de crédit, c'est-à-dire que le tableau comporte (#prêts dans l'échantillon * # de crédits précédents relatifs * # de mois où nous avons un historique observable pour les crédits précédents) lignes.

    POS_CASH_balance.csv
        Instantanés mensuels du solde des prêts POS (points de vente) et des prêts en espèces précédents que le demandeur avait avec Home Credit.
        Ce tableau comporte une ligne pour chaque mois d'historique de chaque crédit précédent dans le domaine du crédit immobilier (crédit à la consommation et prêts en espèces) lié aux prêts de notre échantillon - c'est-à-dire que le tableau comporte (#prêts dans l'échantillon * # de crédits précédents relatifs * # de mois au cours desquels nous avons un historique observable pour les crédits précédents) lignes.

    solde_de_la_carte_de_crédit.csv
        Instantanés du solde mensuel des cartes de crédit précédentes que le demandeur possède auprès de Home Credit.
        Ce tableau comporte une ligne pour chaque mois d'historique de chaque crédit précédent dans le domaine du crédit immobilier (crédit à la consommation et prêts en espèces) lié aux prêts de notre échantillon - c'est-à-dire que le tableau comporte (#prêts dans l'échantillon * # de cartes de crédit précédentes relatives * # de mois où nous avons un historique observable pour la carte de crédit précédente) lignes.

    application_précédente.csv
        Toutes les demandes précédentes de prêts immobiliers des clients ayant des prêts dans notre échantillon.
        Il y a une ligne pour chaque demande précédente liée à des prêts dans notre échantillon de données.

    versements_paiements.csv
        Historique de remboursement des crédits précédemment déboursés en Crédit Immobilier liés aux prêts de notre échantillon.
        Il y a a) une ligne pour chaque paiement effectué plus b) une ligne pour chaque paiement manqué.
        Une ligne équivaut à un paiement d'un versement OU un versement correspondant à un paiement d'un crédit Home Credit antérieur lié aux prêts de notre échantillon.

    AccueilCredit_columns_description.csv
        Ce fichier contient les descriptions des colonnes des différents fichiers de données.