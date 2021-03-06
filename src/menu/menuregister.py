# -*- coding: UTF-8 -*-
import pygame, sys
from pygame.locals import *
from pgu import gui
from twisted.internet import reactor

import global_vars as g
from constants import *

from gui.dialogs import alertMessageDialog

# Font hack
import os
dataPath = os.path.join('..', 'data')
HAPPY_FONT_TIME = pygame.font.Font(dataPath + '/fonts/ConsolaMono-Bold.ttf', 16)

class registerControl(gui.Table):
    def __init__(self, **params):
        gui.Table.__init__(self, **params)
        self.value = gui.Form()
        self.engine = None

        def btnRegister(btn):
            def isLoginLegal(username, password):
                if len(username) > 3 and len(password) > 3:
                    return True
                else:
                    alertMessageDialog(msg='La salutnomo kaj pasvorto devas esti pli longa ol 3 karaktroj', title='Eraro okazis')

            def isStringLegal(string):
                restricted = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ĉĈĝĜĥĤĵĴŝŜŭŬ'

                for i in range(len(string)):
                    if string[i] not in restricted:
                        # todo: msgbox (not valid)
                        alertMessageDialog(msg=u'La nomo nevalidas. Ĝi devas enhavi nur tiujn karaktrojn: [a-z], [ĉĝĥĵŝŭ], kaj [0-9].', title='Eraro okazis')
                        return False

                return True

            def checkPasswords(password1, password2):
                if password1 == password2:
                    return True


            username = self.value.items()[0][1]
            password = self.value.items()[1][1]
            passwordConfirm = self.value.items()[2][1]

            if isLoginLegal(username, password):
                if checkPasswords(password, passwordConfirm):
                    if isStringLegal(username):
                        g.tcpConn.sendNewAccount(username, password)

                else:
                    # todo: msgbox
                    alertMessageDialog(msg='La pasvortoj ne kongruas.', title='Eraro okazis')

        def btnCancel(btn):
            g.gameState = MENU_LOGIN

        self.tr()
        self.td(gui.Spacer(0, 100))
        self.tr()
        self.td(gui.Label('Bonvolu, ne uzas vian ordinaran pasvorton-', color=(255, 255, 255), font=HAPPY_FONT_TIME))
        self.tr()
        self.td(gui.Label('Pasvortoj ne estas ĉifrita nuntempe! :(', color=(255, 255, 255), font=HAPPY_FONT_TIME))
        self.tr()
        self.td(gui.Spacer(0, 5))
        self.tr()
        self.td(gui.Label('Salutnomo:', color=(255, 255, 255), font=HAPPY_FONT_TIME))
        self.tr()
        self.td(gui.Input(name="username", value="Salutnomo", font=HAPPY_FONT_TIME))

        self.tr()
        self.td(gui.Spacer(0, 20))

        self.tr()
        self.td(gui.Label('Pasvorto:', color=(255, 255, 255), font=HAPPY_FONT_TIME))
        self.tr()
        self.td(gui.Password(name="password", value=""), font=HAPPY_FONT_TIME)

        self.tr()
        self.td(gui.Spacer(0, 10))

        self.tr()
        self.td(gui.Label('Konfirmi pasvorto:', color=(255, 255, 255), font=HAPPY_FONT_TIME))
        self.tr()
        self.td(gui.Password(name="passwordConfirm", value=""), font=HAPPY_FONT_TIME)

        self.tr()
        self.td(gui.Spacer(0, 30))


        self.tr()
        btn = gui.Button("Krei", width=120, font=HAPPY_FONT_TIME)
        btn.connect(gui.CLICK, btnRegister, None)
        self.td(btn)

        self.tr()
        self.td(gui.Spacer(0, 5))

        self.tr()
        btn = gui.Button("Rezigni", width=120, font=HAPPY_FONT_TIME)
        btn.connect(gui.CLICK, btnCancel, None)
        self.td(btn)

class menuRegister():
    def __init__(self, surface):
        self.surface = surface
        self.backgroundImage = pygame.image.load(g.dataPath + '/gui/bg_menu.png')

        # GUI
        self.app = gui.App()

        regControl = registerControl()
        regControl.engine = self

        self.c = gui.Container(align=0, valign=0)
        self.c.add(regControl, 0, 0)

        self.app.init(self.c)

    def draw(self):
        # background
        self.surface.blit(self.backgroundImage, (0, 0))
        self.app.paint()

        pygame.display.update()

    def _handleEvents(self, event):
        self.app.event(event)

        if event.type == KEYDOWN and event.key == K_ESCAPE:
            # disconnect and return to login menu
            g.gameEngine.disconnect()
            g.gameState = MENU_LOGIN
