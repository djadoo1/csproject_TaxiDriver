import pygame

#needed to capitalize class names
class Taxi:
	def __init__(self, start_x = 250, color='yellow'):
		#self.xcoor = xcoor
		#self.ycoor = ycoor
		self.start_x = start_x
		self.color = color
		#pygame.Rect(xcoor, ycoor, width, height)
		self.shape = pygame.Rect(self.start_x,460, 10, 40)

	def moveLeft(self, left_x = -100):
		self.left_x = left_x
		'''
		if self.start_x != 150:
			self.start_x -= 100
			'''
		print("moving left:", self.shape.x, " ", self.shape.y)
		if self.shape.x != 150:
			self.shape = self.shape.move(left_x, 0)

	def moveRight(self, right_x = 100):
		'''
		#self.start_x = 250
		if self.start_x != 350:
			self.start_x += 100
			'''
		print("moving right:", self.shape.x, " ", self.shape.y)
		if self.shape.x != 350:
			self.shape = self.shape.move(right_x, 0)

	def __str__(self):
		mystr = ''
		mystr += 'Coordinates: ' + str(self.xcoor) + ', ' + str(self.ycoor) + '\n'
		mystr += 'Color: ' + self.color
		return mystr

#we need to integrate the spawning logic into this, might have to change it some
class Obstacle:
	def __init__(self, speed=10, color='gray'):
		self.color = color

		self.shape = pygame.Rect(xcoor,ycoor, 10, 10)
		self.speed = speed

	def move(self, speed):
		while self.ycoor >= 0:
			self.ycoor -= speed

	#def place():

	def __str__(self):
		mystr = ''
		mystr += 'Coordinates: ' + str(self.xcoor) + ', ' + str(self.ycoor) + '\n'
		mystr += 'Color: ' + self.color + '\n'
		mystr += 'Speed: ' + str(self.speed)
		return mystr
