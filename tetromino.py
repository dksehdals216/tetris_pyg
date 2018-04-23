

#clean up imports
import pygame as pg


class Tetromino(object):

	# Defines Tetrominos: L, I, O, S, T, Z, rev_L shapes.
	# Blocks of the actual tetris game, 

	def __init__(self, name, direction, x_pos, y_pos, state):

		self.name = name
		self.direction = direction
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.state = state

	#redefine
	# Need name of tetromino to get the actual png file
	@property
	def attribute_name(self):
		return self.__name

	#redefine
	@property
	def attribute_direction(self):
		return self.__direction

	#redefine
	@property
	def attribute_x(self):
		return self._name

	#redefine
	@property
	def attribute_y(self):
		return self._name

	#redefine
	@property
	def attribute_state(self):
		return self.__state

	#redefine
	@ch_name.setter
	def ch_name(self, name):
