# Faça um programa em Python que abra e roproduza o audio de um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('flow.mp3')
pygame.mixer.music.play()
input()
