from fluidity import StateMachine, state, transition
class MyStateMachine(StateMachine):

	initial_state = 'White Sheep'

	state('White Sheep', enter='entry1', exit='exit1')
	state('Black Sheep', enter='entry2')
	state('Grey Sheep')

	transition(from_='White Sheep', event='make black', to='Black Sheep', guard='guard1', action='action1')
	transition(from_='Black Sheep', event='make grey', to='Grey Sheep', action='action2')
	transition(from_='Grey Sheep', event='make white', to='White Sheep')