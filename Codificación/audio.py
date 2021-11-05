import pyglet
import time

sound = pyglet.media.load("sound.wav")
left_sound=pyglet.media.load("left.wav")
right_sound=pyglet.media.load("right.wav")

sound.play()
time.sleep(1)
left_sound.play()
left_sound.play()
time.sleep(1)
right_sound.play()
time.sleep(1)
