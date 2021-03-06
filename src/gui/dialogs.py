# -*- coding: UTF-8 -*-
from pgu import gui
import global_vars as g
from constants import *

# Font hack
import pygame
from pygame.locals import *
import os
dataPath = os.path.join('..', 'data')
HAPPY_FONT_TIME = pygame.font.Font(dataPath + '/fonts/ConsolaMono-Bold.ttf', 16)

def alertMessageDialog(msg='', title=''):
    # show an alert message
    if title is '':
        title = gui.Label(u'Averta mesaĝo', font=HAPPY_FONT_TIME)
    else:
        title = gui.Label(title, font=HAPPY_FONT_TIME)

    mainTable = gui.Table()

    mainTable.tr()
    mainTable.td(gui.Spacer(10, 10))

    mainTable.tr()
    mainTable.td(gui.Label(msg, font=HAPPY_FONT_TIME))

    mainTable.tr()
    mainTable.td(gui.Spacer(10, 20))

    d = gui.Dialog(title, mainTable)

    # handle alert messages differently on some alerts
    if msg == 'Via konto estas kreinta!':
        def btnAccountCreated(btn):
            g.gameEngine.setState(MENU_LOGIN)
            d.close()

        btn = gui.Button('Konfirmi', width=120)
        btn.connect(gui.CLICK, btnAccountCreated, None)

    else:
        # simple close button
        def btnOk(btn):
            d.close()

        btn = gui.Button('Konfirmi', width=120)
        btn.connect(gui.CLICK, btnOk, None)

    # add button to alert message
    mainTable.tr()
    mainTable.td(btn)

    # show the message
    d.open()
