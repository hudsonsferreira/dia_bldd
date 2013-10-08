from fluidity import StateMachine, state, transition
class MyStateMachine(StateMachine):

	initial_state = 'Carneirinho Branco'

	state('Carneirinho Branco', enter='teste_entrada1', exit='teste_saida1')
	state('Carneirinho Preto', enter='teste_entrada2')
	state('Carneirinho Cinza')

	transition(from_='Carneirinho Branco', event='ficar preto', to='Carneirinho Preto', guard='abc')
	transition(from_='Carneirinho Preto', event='ficar cinza', to='Carneirinho Cinza')
	transition(from_='Carneirinho Cinza', event='ficar branco', to='Carneirinho Branco')