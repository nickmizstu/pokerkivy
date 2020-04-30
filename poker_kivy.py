import itertools
from kivy.properties import StringProperty
import itertools
import csv
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
import pandas as pd


dfn = pd.read_csv('pro.csv')
dataf = dfn.round(5)


Window.size = (450, 300)


carddeck = ['02c', '02d', '02h', '02s',
            '03c', '03d', '03h', '03s',
            '04c', '04d', '04h', '04s',
            '05c', '05d', '05h', '05s',
            '06c', '06d', '06h', '06s',
            '07c', '07d', '07h', '07s',
            '08c', '08d', '08h', '08s',
            '09c', '09d', '09h', '09s',
            '10c', '10d', '10h', '10s',
            '11c', '11d', '11h', '11s',
            '12c', '12d', '12h', '12s',
            '13c', '13d', '13h', '13s',
            '14c', '14d', '14h', '14s']
all_hand_list = []
for i in itertools.combinations(carddeck, 2):
    all_hand_list.append(list(i))

defultpro = [0.03108, 0.16807, 2.59610, 3.02549,
             4.61938, 4.82987, 23.49554, 43.82255, 17.41192]

b1p, b1n, b2p, b2n, b3p, b3n, b4p, b4n, b5p, b5n = '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'
h1p, h1n, h2p, h2n = '0', '0', '0', '0'
valuedic = {'C': 'c', 'D': 'd', 'H': 'h', 'S': 's',
            'A': '14', '2': '02', '3': '03', '4': '04',
            '5': '05', '6': '06', '7': '07', '8': '08',
            '9': '09', '10': '10', 'J': '11', 'Q': '12',
            'K': '13', '0': '0', '-': '0'}


def hand_point(hands, plop, turn, rever):
    all_cards = list(hands + plop + turn + rever)
    all_cards.sort()
    points = {1}
    for tc in itertools.combinations(all_cards, 5):
        c = list(tc)
        c.sort()
        c1, c2, c3, c4, c5 = c
        c1m, c1p = int(c1[:-1]), c1[-1]
        c2m, c2p = int(c2[:-1]), c2[-1]
        c3m, c3p = int(c3[:-1]), c3[-1]
        c4m, c4p = int(c4[:-1]), c4[-1]
        c5m, c5p = int(c5[:-1]), c5[-1]

        if c1m + 4 == c2m + 3 == c3m + 2 == c4m + 1 == c5m and c1p == c2p == c3p == c4p == c5p:
            points.add(9)
            break
        elif c1m + 12 == c2m + 11 == c3m + 10 == c4m + 9 == c5m and c1p == c2p == c3p == c4p == c5p:
            points.add(9)
            break
        elif c2m == c3m == c4m == c5m or c1m == c2m == c3m == c4m:
            points.add(8)
        elif c1m == c2m == c3m and c4m == c5m:
            points.add(7)
        elif c1m == c2m and c3m == c4m == c5m:
            points.add(7)
        elif c1p == c2p == c3p == c4p == c5p:
            points.add(6)
        elif c1m + 4 == c2m + 3 == c3m + 2 == c4m + 1 == c5m or c1m + 12 == c2m + 11 == c3m + 10 == c4m + 9 == c5m:
            points.add(5)
        elif c3m == c4m == c5m or c2m == c3m == c4m or c1m == c2m == c3m:
            points.add(4)
        elif c4m == c5m and c2m == c3m or c4m == c5m and c1m == c2m or c3m == c4m and c1m == c2m:
            points.add(3)
        elif c4m == c5m or c3m == c4m or c2m == c3m or c1m == c2m:
            points.add(2)
        else:
            pass
    return max(points)


class PokerApp(App):
    def __init__(self, **kwargs):
        super(PokerApp, self).__init__(**kwargs)

    def built(self):
        return PokerSheet()


class BoardSheet(FloatLayout):
    defui = StringProperty()
    defui = '-'

    def __init__(self, **kwargs):
        super(BoardSheet, self).__init__(**kwargs)

    def board1p(self, value):
        print(("{} was chosen!!!").format(value))
        global b1p
        b1p = value

    def board1n(self, value):
        print(("{} was chosen").format(value))
        global b1n
        b1n = value

    def board2p(self, value):
        print(("{} was chosen").format(value))
        global b2p
        b2p = value

    def board2n(self, value):
        print(("{} was chosen").format(value))
        global b2n
        b2n = value

    def board3p(self, value):
        print(("{} was chosen").format(value))
        global b3p
        b3p = value

    def board3n(self, value):
        print(("{} was chosen").format(value))
        global b3n
        b3n = value

    def board4p(self, value):
        print(("{} was chosen").format(value))
        global b4p
        b4p = value

    def board4n(self, value):
        print(("{} was chosen").format(value))
        global b4n
        b4n = value

    def board5p(self, value):
        print(("{} was chosen").format(value))
        global b5p
        b5p = value

    def board5n(self, value):
        print(("{} was chosen").format(value))
        global b5n
        b5n = value


class HandSheet(FloatLayout):
    defui = StringProperty()
    defui = '-'

    def hand1p(self, value):
        print(("{} was chosen").format(value))
        global h1p
        h1p = value

    def hand1n(self, value):
        print(("{} was chosen").format(value))
        global h1n
        h1n = value

    def hand2p(self, value):
        print(("{} was chosen").format(value))
        global h2p
        h2p = value

    def hand2n(self, value):
        print(("{} was chosen").format(value))
        global h2n
        h2n = value


class PokerSheet(BoxLayout):
    sfpro = StringProperty()
    fkpro = StringProperty()
    fhpro = StringProperty()
    flpro = StringProperty()
    stpro = StringProperty()
    tkpro = StringProperty()
    tppro = StringProperty()
    oppro = StringProperty()
    hcpro = StringProperty()
    defui = StringProperty()

    def __init__(self, **kwargs):
        super(PokerSheet, self).__init__(**kwargs)
        self.sfpro = str(defultpro[0])+'%'
        self.fkpro = str(defultpro[1])+'%'
        self.fhpro = str(defultpro[2])+'%'
        self.flpro = str(defultpro[3])+'%'
        self.stpro = str(defultpro[4])+'%'
        self.tkpro = str(defultpro[5])+'%'
        self.tppro = str(defultpro[6])+'%'
        self.oppro = str(defultpro[7])+'%'
        self.hcpro = str(defultpro[8])+'%'

        self.sfcl = [1, 1, .7, 1]
        self.fkcl = [1, 1, .6, 1]
        self.fhcl = [1, 1, .5, 1]
        self.flcl = [1, 1, .4, 1]
        self.stcl = [1, 1, .3, 1]
        self.tkcl = [1, 1, .1, 1]
        self.tpcl = [1, 1, 1, 1]
        self.opcl = [1, 1, 1, 1]
        self.hccl = [1, 1, 1, 1]

    def execute_clicked(self):
        b1 = valuedic[b1n]+valuedic[b1p]
        b2 = valuedic[b2n]+valuedic[b2p]
        b3 = valuedic[b3n]+valuedic[b3p]
        plop_card = [b1, b2, b3]
        b4 = valuedic[b4n]+valuedic[b4p]
        turn_card = [b4]
        b5 = valuedic[b5n]+valuedic[b5p]
        river_card = [b5]
        boardlist = [b1, b2, b3, b4, b5]
        boardlist.sort()

        h1 = valuedic[h1n]+valuedic[h1p]
        h2 = valuedic[h2n]+valuedic[h2p]
        handlist = [h1, h2]
        handlist.sort()
        print('The board is '+str(boardlist))
        print('The hand is ' + str(handlist))

        try:
            if all([i != '0' for i in [h1p, h1n, h2p, h2n, b1p, b1n, b2p, b2n, b3p, b3n, b4p, b4n, b5p, b5n]]):
                poi = hand_point(handlist, plop_card, turn_card, river_card)
                if poi == 9:
                    self.sfpro = '100%'
                    self.fkpro = '0%'
                    self.fhpro = '0%'
                    self.flpro = '0%'
                    self.stpro = '0%'
                    self.tkpro = '0%'
                    self.tppro = '0%'
                    self.oppro = '0%'
                    self.hcpro = '0%'

                if poi == 8:
                    self.sfpro = '0%'
                    self.fkpro = '100%'
                    self.fhpro = '0%'
                    self.flpro = '0%'
                    self.stpro = '0%'
                    self.tkpro = '0%'
                    self.tppro = '0%'
                    self.oppro = '0%'
                    self.hcpro = '0%'

                if poi == 7:
                    self.sfpro = '0%'
                    self.fkpro = '0%'
                    self.fhpro = '100%'
                    self.flpro = '0%'
                    self.stpro = '0%'
                    self.tkpro = '0%'
                    self.tppro = '0%'
                    self.oppro = '0%'
                    self.hcpro = '0%'

                if poi == 6:
                    self.sfpro = '0%'
                    self.fkpro = '0%'
                    self.fhpro = '0%'
                    self.flpro = '100%'
                    self.stpro = '0%'
                    self.tkpro = '0%'
                    self.tppro = '0%'
                    self.oppro = '0%'
                    self.hcpro = '0%'

                if poi == 5:
                    self.sfpro = '0%'
                    self.fkpro = '0%'
                    self.fhpro = '0%'
                    self.flpro = '0%'
                    self.stpro = '100%'
                    self.tkpro = '0%'
                    self.tppro = '0%'
                    self.oppro = '0%'
                    self.hcpro = '0%'

                if poi == 4:
                    self.sfpro = '0%'
                    self.fkpro = '0%'
                    self.fhpro = '0%'
                    self.flpro = '0%'
                    self.stpro = '0%'
                    self.tkpro = '100%'
                    self.tppro = '0%'
                    self.oppro = '0%'
                    self.hcpro = '0%'

                if poi == 3:
                    self.sfpro = '0%'
                    self.fkpro = '0%'
                    self.fhpro = '0%'
                    self.flpro = '0%'
                    self.stpro = '0%'
                    self.tkpro = '0%'
                    self.tppro = '100%'
                    self.oppro = '0%'
                    self.hcpro = '0%'

                if poi == 2:
                    self.sfpro = '0%'
                    self.fkpro = '0%'
                    self.fhpro = '0%'
                    self.flpro = '0%'
                    self.stpro = '0%'
                    self.tkpro = '0%'
                    self.tppro = '0%'
                    self.oppro = '100%'
                    self.hcpro = '0%'

                if poi == 1:
                    self.sfpro = '0%'
                    self.fkpro = '0%'
                    self.fhpro = '0%'
                    self.flpro = '0%'
                    self.stpro = '0%'
                    self.tkpro = '0%'
                    self.tppro = '0%'
                    self.oppro = '0%'
                    self.hcpro = '100%'

            elif all([i != '0' for i in [h1p, h1n, h2p, h2n, b1p, b1n, b2p, b2n, b3p, b3n, b4p, b4n]]):
                card_left = carddeck[:]
                river_point = []
                for drop in [h1, h2, b1, b2, b3, b4]:
                    card_left.remove(drop)
                for river in card_left:
                    rivp = hand_point(handlist, plop_card,
                                      turn_card, list(river))
                    river_point.append(rivp)
                lennum = len(river_point)
                self.sfpro = str(round(river_point.count(9)/lennum*100)) + '%'
                self.fkpro = str(round(river_point.count(8)/lennum*100)) + '%'
                self.fhpro = str(round(river_point.count(7)/lennum*100)) + '%'
                self.flpro = str(round(river_point.count(6)/lennum*100)) + '%'
                self.stpro = str(round(river_point.count(5)/lennum*100)) + '%'
                self.tkpro = str(round(river_point.count(4)/lennum*100)) + '%'
                self.tppro = str(round(river_point.count(3)/lennum*100)) + '%'
                self.oppro = str(round(river_point.count(2)/lennum*100)) + '%'
                self.hcpro = str(round(river_point.count(1)/lennum*100)) + '%'

            elif all([i != '0' for i in [h1p, h1n, h2p, h2n, b1p, b1n, b2p, b2n, b3p, b3n, ]]):
                card_left = carddeck[:]
                river_point = []
                for drop in [h1, h2, b1, b2, b3]:
                    card_left.remove(drop)
                for river in itertools.combinations(card_left, 2):
                    rivp = hand_point(handlist, plop_card,
                                      list(river[0]), list(river[1]))
                    river_point.append(rivp)
                lennum = len(river_point)
                self.sfpro = str(round(river_point.count(9)/lennum*100)) + '%'
                self.fkpro = str(round(river_point.count(8)/lennum*100)) + '%'
                self.fhpro = str(round(river_point.count(7)/lennum*100)) + '%'
                self.flpro = str(round(river_point.count(6)/lennum*100)) + '%'
                self.stpro = str(round(river_point.count(5)/lennum*100)) + '%'
                self.tkpro = str(round(river_point.count(4)/lennum*100)) + '%'
                self.tppro = str(round(river_point.count(3)/lennum*100)) + '%'
                self.oppro = str(round(river_point.count(2)/lennum*100)) + '%'
                self.hcpro = str(round(river_point.count(1)/lennum*100)) + '%'

            elif all([i != '0' for i in [h1p, h1n, h2p, h2n, ]]):
                ind = all_hand_list.index(handlist)
                listfornow = dataf.loc[ind]

                print(ind)
                print(listfornow)
                self.sfpro = str(listfornow[1])+'%'
                self.fkpro = str(listfornow[2])+'%'
                self.fhpro = str(listfornow[3])+'%'
                self.flpro = str(listfornow[4])+'%'
                self.stpro = str(listfornow[5])+'%'
                self.tkpro = str(listfornow[6])+'%'
                self.tppro = str(listfornow[7])+'%'
                self.oppro = str(listfornow[8])+'%'
                self.hcpro = str(listfornow[9])+'%'
                
        except ValueError:
            self.sfpro = 'E'
            self.fkpro = 'R'
            self.fhpro = 'R'
            self.flpro = 'O'
            self.stpro = 'R'
            self.tkpro = '!'
            self.tppro = '!'
            self.oppro = '!'
            self.hcpro = '!'
            print('ValueError')



    def cls_clicked(self):
        self.bsdef.bonep.text = '-'
        self.bsdef.bonen.text = '-'
        self.bsdef.btwop.text = '-'
        self.bsdef.btwon.text = '-'
        self.bsdef.bthreep.text = '-'
        self.bsdef.bthreen.text = '-'
        self.bsdef.bfourp.text = '-'
        self.bsdef.bfourn.text = '-'
        self.bsdef.bfivep.text = '-'
        self.bsdef.bfiven.text = '-'
        self.bsdef.bfivep.text = '-'
        self.bsdef.bfiven.text = '-'

        self.hsdef.honep.text = '-'
        self.hsdef.honen.text = '-'
        self.hsdef.htwop.text = '-'
        self.hsdef.htwon.text = '-'
        self.sfpro = str(defultpro[0])+'%'
        self.fkpro = str(defultpro[1])+'%'
        self.fhpro = str(defultpro[2])+'%'
        self.flpro = str(defultpro[3])+'%'
        self.stpro = str(defultpro[4])+'%'
        self.tkpro = str(defultpro[5])+'%'
        self.tppro = str(defultpro[6])+'%'
        self.oppro = str(defultpro[7])+'%'
        self.hcpro = str(defultpro[8])+'%'

        print('cls')


if __name__ == '__main__':
    PokerApp().run()
