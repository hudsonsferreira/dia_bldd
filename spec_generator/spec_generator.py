from dia_bldd_modules.statemachine_generator.sm_generator import SMGenerator

class SpecGenerator():

    def __init__(self, data):
        self.data = data
        self.sm = SMGenerator()
        self.sm.load_data(data)

    def _header(self):
        return 'impot unittest\n'+\
               'from should_dsl import should, should_not\n'+\
               'from dia_bldd_modules.statemachine_generator.StateMachine import MyStateMachine\n'

    def create_initial_state_test(self):
        initial_state = self.sm._get_initial_state()
        phrase = 'initial_state |should_not| be_empty\n'+\
                 'initial_state |should| be(1)\n'+\
                 'initial_state |should| equal_to("{ini_state}")'.format(ini_state=initial_state)
        return phrase