wt_sr = {'tour-de-france': {1: 120, 2: 50, 3: 25, 4: 15, 5: 5},
         'giro-d-italia': {1: 100, 2: 40, 3: 20, 4: 12, 5: 4},
         'vuelta-a-espana': {1: 100, 2: 40, 3: 20, 4: 12, 5: 4},
         'tour-down-under': {1: 60, 2: 25, 3: 10},
         'paris-nice': {1: 60, 2: 25, 3: 10},
         'tirreno-adriatico': {1: 60, 2: 25, 3: 10},
         'tour-de-romandie': {1: 60, 2: 25, 3: 10},
         'dauphine': {1: 60, 2: 25, 3: 10},
         'tour-de-suisse': {1: 60, 2: 25, 3: 10},
         'volta-a-catalunya': {1: 50, 2: 20, 3: 8},
         'itzulia-basque-country': {1: 50, 2: 20, 3: 8},
         'tour-de-pologne': {1: 50, 2: 20, 3: 8},
         'benelux-tour': {1: 50, 2: 20, 3: 8},
         'uae-tour': {1: 40, 2: 15, 3: 6},
         'tour-of-guangxi': {1: 40, 2: 15, 3: 6}
         }

nonwt_sr = {'2.Pro': {1: 20, 2: 10, 3: 5},
            '1.Pro': {1: 20, 2: 10, 3: 5},
            '1.HC': {1: 20, 2: 10, 3: 5},
            '2.HC': {1: 20, 2: 10, 3: 5},
            '2.1': {1: 14, 2: 5, 3: 3},
            '2.2': {1: 7, 2: 3, 3: 1}
            }

wt_gcjersey = {'tour-de-france': {1: 25},
               'giro-d-italia': {1: 20},
               'vuelta-a-espana': {1: 20},
               'tour-down-under': {1: 10},
               'paris-nice': {1: 10},
               'tirreno-adriatico': {1: 10},
               'tour-de-romandie': {1: 10},
               'dauphine': {1: 10},
               'tour-de-suisse': {1: 10},
               'volta-a-catalunya': {1: 8},
               'itzulia-basque-country': {1: 8},
               'tour-de-pologne': {1: 8},
               'benelux-tour': {1: 8},
               'uae-tour': {1: 8},
               'tour-of-guangxi': {1: 8}
               }

nonwt_gcjersey = {'2.Pro': {1: 5},
                  '1.Pro': {1: 5},
                  '1.HC': {1: 5},
                  '2.HC': {1: 5},
                  '2.1': {1: 3},
                  '2.2': {1: 1}
                  }

ranks = list(range(1, 61))
tdf = [1000, 800, 675, 575, 475, 400, 325, 275, 225, 175, 150, 125, 105, 85, 75, 70, 65, 60, 55, 50, 40, 40, 40, 40, 40,
       30, 30, 30, 30, 30, 25, 25,
       25, 25, 25, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 15, 15, 15, 15, 15, 10, 10, 10, 10, 10]
giro = [850, 680, 575, 460, 380, 320, 260, 220, 180, 140, 120, 100, 84, 68, 60, 56, 52, 48, 44, 40, 32, 32, 32, 32, 32,
        24, 24, 24, 24, 24, 20, 20, 20,
        20, 20, 20, 20, 20, 20, 20, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 12, 12, 12, 12, 12, 8, 8, 8, 8, 8]
downunder = [500, 400, 325, 275, 225, 175, 150, 125, 100, 85, 70, 60, 50, 40, 35, 30, 30, 30, 30, 30, 20, 20, 20, 20,
             20, 20, 20, 20, 20, 20,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 3, 3, 3, 3,
             3]
catalunya = [400, 320, 260, 220, 180, 140, 120, 100, 80, 68, 56, 48, 40, 32, 28, 24, 24, 24, 24, 24, 16, 16, 16, 16, 16,
             16, 16, 16, 16, 16,
             8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2]
uae = [300, 250, 215, 175, 120, 115, 95, 75, 60, 50, 40, 35, 30, 25, 20, 20, 20, 20, 20, 20, 12, 12, 12, 12, 12, 12, 12,
       12, 12, 12, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
       5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
pro = [200, 150, 125, 100, 85, 70, 60, 50, 40, 35, 30, 25, 20, 15, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
       5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
c1 = [125, 85, 70, 60, 50, 40, 35, 30, 25, 20, 15, 10, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
c2 = [40, 30, 25, 20, 15, 10, 5, 3, 3, 3]
wcrr = [600, 475, 400, 325, 275, 225, 175, 150, 125, 100, 85, 70, 60, 50, 40, 35, 30, 30, 30, 30, 30, 20, 20, 20, 20,
        20, 20, 20, 20, 20, 20, 10, 10, 10, 10,
        10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3]
wcitt = [300, 250, 200, 150, 125, 100, 85, 70, 60, 50, 40, 30, 25, 20, 15, 10, 5, 5, 5, 5]
ncrr = [100, 75, 60, 50, 40, 30, 20, 10, 5, 3, 3, 1, 1, 1, 1]
ncitt = [50, 30, 20, 15, 10, 5, 3, 3, 1, 1]
ecrr = [250, 200, 150, 125, 100, 90, 80, 70, 60, 50, 40, 35, 30, 25, 20, 15, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
        3, 3, 3, 3, 3, 1, 1, 1, 1, 1]
ecitt = [70, 55, 40, 30, 25, 20, 15, 10, 5, 3]


wt_nonsr = {
    'tour-de-france': dict(zip(ranks, tdf)),
    'giro-d-italia': dict(zip(ranks, giro)),
    'vuelta-a-espana': dict(zip(ranks, giro)),
    'tour-down-under': dict(zip(ranks, downunder)),
    'paris-nice': dict(zip(ranks, downunder)),
    'tirreno-adriatico': dict(zip(ranks, downunder)),
    'tour-de-romandie': dict(zip(ranks, downunder)),
    'dauphine': dict(zip(ranks, downunder)),
    'tour-de-suisse': dict(zip(ranks, downunder)),
    'volta-a-catalunya': dict(zip(ranks, catalunya)),
    'itzulia-basque-country': dict(zip(ranks, catalunya)),
    'tour-de-pologne': dict(zip(ranks, catalunya)),
    'benelux-tour': dict(zip(ranks, catalunya)),
    'uae-tour': dict(zip(ranks, uae)),
    'tour-of-guangxi': dict(zip(ranks, uae)),
    'liege-bastogne-liege': dict(zip(ranks, downunder)),
    'paris-roubaix': dict(zip(ranks, downunder)),
    'ronde-van-vlaanderen': dict(zip(ranks, downunder)),
    'milano-sanremo': dict(zip(ranks, downunder)),
    'il-lombardia': dict(zip(ranks, downunder)),
    'gent-wevelgem': dict(zip(ranks, downunder)),
    'amstel-gold-race': dict(zip(ranks, downunder)),
    'gp-quebec': dict(zip(ranks, downunder)),
    'gp-montreal': dict(zip(ranks, downunder)),
    'e3-harelbeke': dict(zip(ranks, catalunya)),
    'la-fleche-wallone': dict(zip(ranks, catalunya)),
    'san-sebastian': dict(zip(ranks, catalunya)),
    'cyclassics-hamburg': dict(zip(ranks, catalunya)),
    'bretagne-classic': dict(zip(ranks, catalunya)),
    'great-ocean-race': dict(zip(ranks, uae)),
    'omloop-het-nieuwsblad': dict(zip(ranks, uae)),
    'strade-bianche': dict(zip(ranks, uae)),
    'oxyclean-classic-brugge-de-panne': dict(zip(ranks, uae)),
    'dwars-door-vlaanderen': dict(zip(ranks, uae)),
    'Eschborn-Frankfurt': dict(zip(ranks, uae)),
    'world-championship-itt': dict(zip(ranks, wcitt)),
    'world-championship': dict(zip(ranks, wcrr)),
    'olympic-games-itt': dict(zip(ranks, wcitt)),
    'olympic-games': dict(zip(ranks, wcrr)),
    'uec-road-european-championships': dict(zip(ranks, ecrr)),
    'uec-road-european-championships-itt': dict(zip(ranks, ecitt))
}

nonwt_nonsr = {
    '2.Pro': dict(zip(ranks, pro)),
    '1.Pro': dict(zip(ranks, pro)),
    '1.HC': dict(zip(ranks, pro)),
    '2.HC': dict(zip(ranks, pro)),
    '1.1': dict(zip(ranks, c1)),
    '1.2': dict(zip(ranks, c2)),
    '2.1': dict(zip(ranks, c1)),
    '2.2': dict(zip(ranks, c2)),
    'NC': dict(zip(ranks, ncrr)),
    'NC_ITT': dict(zip(ranks, ncitt))
}