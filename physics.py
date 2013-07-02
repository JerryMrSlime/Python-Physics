import pygame as py
from pygame.locals import *
import math

class Collision(object):
	def __init__(self):
		pass
	def check(self, obj1, obj2):
		if obj1.x > obj2.x + obj2.width or obj1.y > obj2.y + obj2.height or obj1.x+obj1.width < obj2.x or obj1.y+obj1.height < obj2.y:
			return False
		else:
			return True
	def check_c(self, ball, ball2):
		if math.sqrt((ball2.x - ball.x)**2 + (ball2.y - ball.y)**2) <= 10:
			return True
		else:
			return False
			
class Platform(object):
	def __init__(self):
		self.x, self.y = 320, 280
		self.width, self.height = 80, 20
	def render(self, screen):
		py.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
		
class Ball(object):
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.vx = 0
		self.width, self.height = 5, 5
		self.vy = 0
		self.enable = True
		
	def update(self):
		if self.enable:
			self.vy += 0.2
		else:
			self.vy = 0
		self.x += self.vx
		self.y += self.vy
		
	def render(self, screen):
		py.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), 5)
		
def main():
	py.init()
	screen = py.display.set_mode((800, 600))
	clock = py.time.Clock()
	clear = (0, 0, 0)
	balls =  []
	exit = False
	platf = Platform()
	collision = Collision()
	
	while not exit:
		screen.fill(clear)
		for event in py.event.get():
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				exit = True
			if event.type == MOUSEBUTTONDOWN:
				balls.append(Ball(py.mouse.get_pos()[0], py.mouse.get_pos()[1]))
				
		platf.render(screen)
		updateBalls(balls, screen, collision, platf)
		py.display.update()
		clock.tick(60)
		
	return 0

def updateBalls(balls, screen, collision, rectangle):
	for ball in balls:
		if collision.check(ball, rectangle):
			ball.enable = False
			ball.y = rectangle.y - ball.height
		else:
			ball.enable = True
		if ball.y > 600 or ball.x > 800 or ball.x < 0:
			balls.remove(ball)
		for ball2 in balls:
			if ball != ball2:
				if collision.check_c(ball, ball2):
					if ball.x > ball2.x:
						ball.vx = 3
						ball2.vx = -3
					else:
						ball.vx = -3
						ball2.vx = 3
		ball.update()
		ball.render(screen)

if __name__ == "__main__":
	main()
