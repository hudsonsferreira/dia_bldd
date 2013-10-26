from dia_bldd_modules.statemachine_generator.sm_generator import SMGenerator

class SpecGenerator():

    def __init__(self, data):
        self.data = data
        self.sm = SMGenerator()
        self.sm.load_data(data)

    def _load_fluidity(self):
        content = ''
        fluidity = open('/home/hudson/.dia/python/dia_bldd_modules/statemachine_generator/StateMachine.py', 'r')
        for line in fluidity.read():
            content += line
        return content

    def _header(self):
        return 'impot unittest\n'+\
               'from should_dsl import should, should_not\n'+\
               'from fluidity import StateMachine, transition, state\n'
               'from dia_bldd_modules.statemachine_generator.StateMachine import MyStateMachine\n'

    def create_initial_state_test(self):
        initial_state = self.sm._get_initial_state()
        phrase = 'machine = MyStateMachine()\n'+\
                 'machine.initial_state |should| equal_to("{ini_state}")\n'+\
                 'machine.current_state |should| equal_to("{ini_state}")\n'.format(ini_state=initial_state, ini_state=initial_state)
        return phrase

    def create_states_test(self):
        states = self.sm_get_states()
        