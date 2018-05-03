#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:39:55 2018

@author: rin35130
"""

import pyglet
from pyglet.window.key import MOD_CTRL, A, B, C


window = pyglet.window.Window()



obrazek= pyglet.image.load("rooster.png")
obrazek.anchor_x =obrazek.width // 2
obrazek.anchor_y =obrazek.width // 2
sprite= pyglet.sprite.Sprite(obrazek)


def tiktak(t):
   print(t)
   sprite.x = sprite.x + 10*t
   sprite.y = sprite.y + 10*t

   
   
   
@window.event
def on_draw():
    window.clear()
    sprite.draw()



@window.event
def on_mouse_press(x, y, button, mod):
    if button == 1:
        sprite.x= x
        sprite.y= y
    elif button == 4:
        sprite.rotation += 10
          
    
    
    
@window.event
def on_key_press(sym, mod):
    if sym != A:
         print(sym, mod)
       
pyglet.clock.schedule_interval(tiktak, 2)




pyglet.app.run()
print("Hotovo")