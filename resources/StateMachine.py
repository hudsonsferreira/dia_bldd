from fluidity import StateMachine, state, transition
class MyStateMachine(StateMachine):

	initial_state = 'White Sheep'

	state('White Sheep', enter='entry1', exit='exit1')
	state('Black Sheep', enter='entry2')
	state('Grey Sheep')

	transition(from_='White Sheep', event='make_black', to='Black Sheep', guard='guard1', action='action1')
	transition(from_='Black Sheep', event='make_grey', to='Grey Sheep', action='action2')
	transition(from_='Grey Sheep', event='make_white', to='White Sheep')

	def entry1(self): pass
	def exit1(self): pass
	def entry2(self): pass
	def guard1(self): return True
	def action1(self): pass
	def action2(self): pass