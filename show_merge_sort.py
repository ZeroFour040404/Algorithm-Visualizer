
import pygame as py
import time 
import numpy as np


class ShowMergeSort():
    def __init__(self, list):
        self.list = list
        self.bar_width = 700 / len(self.list)
        self.max_value = max(list)
        self.sound_step = 0
        self.draw_step = 0
        py.init()
        self.screen = py.display.set_mode((800, 600))
        py.display.set_caption('Merge Sort Algorithm')
        self.clock = py.time.Clock()
        py.mixer.init(frequency = 44100)
        
    def play_tone(self, freq, duration = 0.02, volume = 0.3):
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = np.sin(2 * np.pi * freq * t)
        
        mono = (wave * 32767 * volume).astype(np.int16)
        stereo = np.column_stack((mono, mono))
        sound = py.sndarray.make_sound(stereo)
        sound.play()
        
    def draw(self, active = -1):
        self.screen.fill((0, 0, 0))
        
        for i, value in enumerate(self.list):
            x = int(i * self.bar_width)
            h = int(value / self.max_value * 500)
            y = 580 - h
            
            color = (255, 255, 255) if i == active else (0, 255, 0)
            py.draw.rect(self.screen, color, (50 + x, y, self.bar_width, h))
        
        py.display.flip()
        py.event.pump()
        
    def value_to_freq(self, value):
        return 200 + (value / self.max_value) * 1800
        
        
    def merge_sort(self, left, right):
        if left < right:
            mid = (left + right)//2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)
            
    def merge(self, left, mid, right):
        l = self.list[left:mid + 1]
        r = self.list[mid + 1: right + 1]
        
        i = j = 0
        k = left
        
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                self.list[k] = l[i]
                freq = self.value_to_freq(l[i])
                i += 1
            else:
                self.list[k] = r[j]
                freq = self.value_to_freq(r[j])
                j += 1
            if self.sound_step % 3 == 0:
                self.play_tone(freq)
            self.sound_step += 1
            if self.draw_step % 2 == 0:
                self.draw(k)
            self.draw_step += 1
            self.clock.tick(240)
            k += 1
                
        while i < len(l):
            self.list[k] = l[i]
            if self.sound_step % 3 == 0:
                self.play_tone(self.value_to_freq(l[i]))
            self.sound_step += 1
            if self.draw_step % 2 == 0:
                self.draw(k)
            self.draw_step += 1
            self.clock.tick(240)
            i += 1
            k += 1
            
        while j < len(r):
            self.list[k] = r[j]
            if self.sound_step % 3 == 0:
                self.play_tone(self.value_to_freq(r[j]))
            self.sound_step += 1
            if self.draw_step % 2 == 0:
                self.draw(k)
            self.draw_step += 1
            self.clock.tick(240)
            j += 1
            k += 1
            
    def sort(self):
        self.draw()
        self.merge_sort(0, len(self.list) - 1)
        self.play_tone(900, 0.4)
        
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()


if __name__ == '__main__':
    import random
    
    arr = [random.randint(1, 1000) for i in range(500)]
    vis = ShowMergeSort(arr)
    vis.sort()