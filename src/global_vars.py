#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import pygame
from pygame.locals import *

from constants import TARGET_TYPE_NONE

pygame.init()

# connection
gameEngine = None
soundEngine = None

tcpConn = None
connector = None

# player variables
myIndex = None
expToNextLvl = 0
target = None
targetType = TARGET_TYPE_NONE

# gameloop
inGame = False
isLogging = True
gameState = 0
connectionStatus = ""

canMoveNow = True

editor = None

# input
inpDIR_UP = False
inpDIR_DOWN = False
inpDIR_LEFT = False
inpDIR_RIGHT = False
inpSHIFT = False
inpCTRL = False

# spell hotkeys
SPELLBOOK_HOTKEYS =         {pygame.K_1: None, 
                             pygame.K_2: None,
                             pygame.K_3: None,
                             pygame.K_4: None,
                             pygame.K_5: None,
                             pygame.K_6: None,
                             pygame.K_7: None,
                             pygame.K_8: None,
                             pygame.K_9: None}

SPELLBOOK_HOTKEYS_STRINGS = {pygame.K_1: '1', 
                             pygame.K_2: '2',
                             pygame.K_3: '3',
                             pygame.K_4: '4',
                             pygame.K_5: '5',
                             pygame.K_6: '6',
                             pygame.K_7: '7',
                             pygame.K_8: '8',
                             pygame.K_9: '9'}
HOTKEY_1 = None
HOTKEY_2 = None
HOTKEY_3 = None
HOTKYE_4 = None


# used for improved looping
highIndex = 0
playersOnMapHighIndex = 0
playersOnMap = []
npcHighIndex = 0

# used for draggin picture boxes
sOffsetX = 0
sOffestY = 0

# freeze controls when getting map
gettingMap = False

# mouse position (and tile position)
cursorX = 0
cursorY = 0
cursorXTile = 0
cursorYTile = 0

# maximum classes
maxClasses = 3

# path for data files
dataPath = os.path.join('..', 'data')

# --------------------

# general
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# sdl
screenSurface = None

gameSurface = pygame.Surface((480, 352))
bgSurface = None

guiSurface = pygame.Surface((800, 600))

dirtyRects = []

# surfaces
gameSurfaceXOffset = 0
gameSurfaceYOffset = 0

guiSurfaceXOffset = 0
guiSurfaceYOffset = 0

clock = pygame.time.Clock()

# fonts
''' change these to customize the in-game fonts '''
systemFont = pygame.font.Font(dataPath + '/fonts/ConsolaMono-Bold.ttf', 16)
nameFont = pygame.font.Font(dataPath + '/fonts/ConsolaMono-Bold.ttf', 12)
chatFont = pygame.font.Font(dataPath + '/fonts/ConsolaMono-Bold.ttf', 12)
charSelFont = pygame.font.Font(dataPath + '/fonts/ConsolaMono-Bold.ttf', 18)
tooltipFont = pygame.font.Font(dataPath + '/fonts/ConsolaMono-Bold.ttf', 12)

# check if text is to be drawn
boolFPS = False
boolLoc = False

# tiles
tileDimension = 32

# map
mapNames = []
