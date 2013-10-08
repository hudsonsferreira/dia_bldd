Converts a Dia statemachine to a Fluidity statemachine.

Basic usage::

    from dia_statemachine_generator.sm_generator import SMGenerator 
    sm = SMGenerator()
    sm.load_data(dia.diagrams()[0].data) #index represents an opened diagram on Dia
    sm.create_fluidity()

Then, you must get a Fluidity StateMachine::
    
    from fluidity import StateMachine, state, transition
    class MyStateMachine(StateMachine):

		initial_state = 'Carneirinho Branco'

		state('Carneirinho Branco', enter='teste_entrada1', exit='teste_saida1')
		state('Carneirinho Preto', enter='teste_entrada2')
		state('Carneirinho Cinza')

		transition(from_='Carneirinho Branco', event='ficar preto', to='Carneirinho Preto', guard='abc')
		transition(from_='Carneirinho Preto', event='ficar cinza', to='Carneirinho Cinza')
		transition(from_='Carneirinho Cinza', event='ficar branco', to='Carneirinho Branco')