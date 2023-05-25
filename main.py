import pygame
import pianoList as pl
from pygame import mixer

pygame.init()
pygame.mixer.set_num_channels(50)

font = pygame.font.Font("assets/DancingScript.ttf", 48)
mediumFont = pygame.font.Font("assets/DancingScript.ttf", 28)
smallFont = pygame.font.Font("assets/DancingScript.ttf", 16)
realSmallFont = pygame.font.Font("assets/DancingScript.ttf", 10)
fps = 60
timer = pygame.time.Clock()
WIDTH = 52 * 35
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
icon = pygame.image.load("assets\icon.png")
pygame.display.set_icon(icon)
whiteSounds = []
blackSounds = []
activeWhites = []
activeBlacks = []
leftOct = 4
rightOct = 5

leftHand = pl.leftHand
rightHand = pl.rightHand
pianoNotes = pl.pianoNotes
whiteNotes = pl.whiteNotes
blackNotes = pl.blackNotes
blackLabels = pl.blackLabels

for i in range(len(whiteNotes)):
    whiteSounds.append(mixer.Sound(f"assets\\notes\\{whiteNotes[i]}.wav"))

for i in range(len(blackNotes)):
    blackSounds.append(mixer.Sound(f"assets\\notes\\{blackNotes[i]}.wav"))

pygame.display.set_caption("Python Piano")


def drawPiano(whites, blacks):
    whiteRects = []
    for i in range(52):
        rect = pygame.draw.rect(screen, "white", [i * 35, HEIGHT - 300, 35, 300], 0, 2)
        whiteRects.append(rect)
        pygame.draw.rect(screen, "black", [i * 35, HEIGHT - 300, 35, 300], 2, 2)
        keyLabel = smallFont.render(whiteNotes[i], True, "black")
        screen.blit(keyLabel, (i * 35 + 3, HEIGHT - 20))
    skipCount = 0
    lastSkip = 2
    skipTrack = 2
    blackRects = []
    for i in range(36):
        rect = pygame.draw.rect(screen, "black", [23 + (i * 35) + (skipCount * 35), HEIGHT - 300, 24, 200], 0, 2)
        for q in range(len(blacks)):
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(screen, "green", [23 + (i * 35) + (skipCount * 35), HEIGHT - 300, 24, 200], 2, 2)
                    blacks[q][1] -= 1

        keyLabel = realSmallFont.render(blackLabels[i], True, "white")
        screen.blit(keyLabel, (25 + (i * 35) + (skipCount * 35), HEIGHT - 120))
        blackRects.append(rect)
        skipTrack += 1
        if lastSkip == 2 and skipTrack == 3:
            lastSkip = 3
            skipTrack = 0
            skipCount += 1
        elif lastSkip == 3 and skipTrack == 2:
            lastSkip = 2
            skipTrack = 0
            skipCount += 1

    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, "green", [j * 35, HEIGHT - 100, 35, 100], 2, 2)
            whites[i][1] -= 1

    return whiteRects, blackRects, whites, blacks


def drawHands(rightOct, leftOct, rightHand, leftHand):
    # left hand
    pygame.draw.rect(screen, "dark green", [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, "black", [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 4, 4)
    text = smallFont.render(leftHand[0], True, "white")
    screen.blit(text, ((leftOct * 245) - 165, HEIGHT - 55))
    text = smallFont.render(leftHand[2], True, "white")
    screen.blit(text, ((leftOct * 245) - 130, HEIGHT - 55))
    text = smallFont.render(leftHand[4], True, "white")
    screen.blit(text, ((leftOct * 245) - 95, HEIGHT - 55))
    text = smallFont.render(leftHand[5], True, "white")
    screen.blit(text, ((leftOct * 245) - 60, HEIGHT - 55))
    text = smallFont.render(leftHand[7], True, "white")
    screen.blit(text, ((leftOct * 245) - 25, HEIGHT - 55))
    text = smallFont.render(leftHand[9], True, "white")
    screen.blit(text, ((leftOct * 245) + 10, HEIGHT - 55))
    text = smallFont.render(leftHand[11], True, "white")
    screen.blit(text, ((leftOct * 245) + 45, HEIGHT - 55))
    text = smallFont.render(leftHand[1], True, "black")
    screen.blit(text, ((leftOct * 245) - 148, HEIGHT - 55))
    text = smallFont.render(leftHand[3], True, "black")
    screen.blit(text, ((leftOct * 245) - 113, HEIGHT - 55))
    text = smallFont.render(leftHand[6], True, "black")
    screen.blit(text, ((leftOct * 245) - 43, HEIGHT - 55))
    text = smallFont.render(leftHand[8], True, "black")
    screen.blit(text, ((leftOct * 245) - 8, HEIGHT - 55))
    text = smallFont.render(leftHand[10], True, "black")
    screen.blit(text, ((leftOct * 245) + 27, HEIGHT - 55))
    # right hand
    pygame.draw.rect(screen, "dark green", [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, "black", [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 4, 4)
    text = smallFont.render(rightHand[0], True, "white")
    screen.blit(text, ((rightOct * 245) - 165, HEIGHT - 55))
    text = smallFont.render(rightHand[2], True, "white")
    screen.blit(text, ((rightOct * 245) - 130, HEIGHT - 55))
    text = smallFont.render(rightHand[4], True, "white")
    screen.blit(text, ((rightOct * 245) - 95, HEIGHT - 55))
    text = smallFont.render(rightHand[5], True, "white")
    screen.blit(text, ((rightOct * 245) - 60, HEIGHT - 55))
    text = smallFont.render(rightHand[7], True, "white")
    screen.blit(text, ((rightOct * 245) - 25, HEIGHT - 55))
    text = smallFont.render(rightHand[9], True, "white")
    screen.blit(text, ((rightOct * 245) + 10, HEIGHT - 55))
    text = smallFont.render(rightHand[11], True, "white")
    screen.blit(text, ((rightOct * 245) + 45, HEIGHT - 55))
    text = smallFont.render(rightHand[1], True, "black")
    screen.blit(text, ((rightOct * 245) - 148, HEIGHT - 55))
    text = smallFont.render(rightHand[3], True, "black")
    screen.blit(text, ((rightOct * 245) - 113, HEIGHT - 55))
    text = smallFont.render(rightHand[6], True, "black")
    screen.blit(text, ((rightOct * 245) - 43, HEIGHT - 55))
    text = smallFont.render(rightHand[8], True, "black")
    screen.blit(text, ((rightOct * 245) - 8, HEIGHT - 55))
    text = smallFont.render(rightHand[10], True, "black")
    screen.blit(text, ((rightOct * 245) + 27, HEIGHT - 55))


def drawTitleBar():
    instructionText = mediumFont.render("Left/Right Arrows Change Left Hand", True, "black")
    screen.blit(instructionText, (WIDTH - 500, 10))
    instructionText2 = mediumFont.render("Up/Down Arrows Change Right Hand", True, "black")
    screen.blit(instructionText2, (WIDTH - 500, 50))
    titleText = font.render("Python Piano!", True, "white")
    screen.blit(titleText, (498, 18))
    titleText = font.render("Python Piano!", True, "black")
    screen.blit(titleText, (500, 20))


run = True
while run:
    leftDict = {"Z": f"C{leftOct}",
                 "S": f"C#{leftOct}",
                 "X": f"D{leftOct}",
                 "D": f"D#{leftOct}",
                 "C": f"E{leftOct}",
                 "V": f"F{leftOct}",
                 "G": f"F#{leftOct}",
                 "B": f"G{leftOct}",
                 "H": f"G#{leftOct}",
                 "N": f"A{leftOct}",
                 "J": f"A#{leftOct}",
                 "M": f"B{leftOct}"}

    rightDict = {"R": f"C{rightOct}",
                  "5": f"C#{rightOct}",
                  "T": f"D{rightOct}",
                  "6": f"D#{rightOct}",
                  "Y": f"E{rightOct}",
                  "U": f"F{rightOct}",
                  "8": f"F#{rightOct}",
                  "I": f"G{rightOct}",
                  "9": f"G#{rightOct}",
                  "O": f"A{rightOct}",
                  "0": f"A#{rightOct}",
                  "P": f"B{rightOct}"}
    timer.tick(fps)
    screen.fill("brown")
    whiteKeys, blackKeys, activeWhites, activeBlacks = drawPiano(activeWhites, activeBlacks)
    drawHands(rightOct, leftOct, rightHand, leftHand)
    drawTitleBar()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            blackKey = False
            for i in range(len(blackKeys)):
                if blackKeys[i].collidepoint(event.pos):
                    blackSounds[i].play(0, 1000)
                    blackKey = True
                    activeBlacks.append([i, 30])
            for i in range(len(whiteKeys)):
                if whiteKeys[i].collidepoint(event.pos) and not blackKey:
                    whiteSounds[i].play(0, 3000)
                    activeWhites.append([i, 30])
        if event.type == pygame.TEXTINPUT:
            if event.text.upper() in leftDict:
                if leftDict[event.text.upper()][1] == "#":
                    index = blackLabels.index(leftDict[event.text.upper()])
                    blackSounds[index].play(0, 1000)
                    activeBlacks.append([index, 30])
                else:
                    index = whiteNotes.index(leftDict[event.text.upper()])
                    whiteSounds[index].play(0, 1000)
                    activeWhites.append([index, 30])
            if event.text.upper() in rightDict:
                if rightDict[event.text.upper()][1] == "#":
                    index = blackLabels.index(rightDict[event.text.upper()])
                    blackSounds[index].play(0, 1000)
                    activeBlacks.append([index, 30])
                else:
                    index = whiteNotes.index(rightDict[event.text.upper()])
                    whiteSounds[index].play(0, 1000)
                    activeWhites.append([index, 30])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if rightOct < 8:
                    rightOct += 1
            if event.key == pygame.K_DOWN:
                if rightOct > 0:
                    rightOct -= 1
            if event.key == pygame.K_RIGHT:
                if leftOct < 8:
                    leftOct += 1
            if event.key == pygame.K_LEFT:
                if leftOct > 0:
                    leftOct -= 1

    pygame.display.flip()
pygame.quit()
