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
               'from should_dsl import should\n'+\
               'from dia_bldd_modules.statemachine_generator.StateMachine import MyStateMachine\n\n'+\
               self._load_fluidity() + '\n\n'+\
               'class FluidityTest(unittest.TestCase):\n\n'+\
               '\tdef setUp(self):\n'+\
               '\t\tself.machine = MyStateMachine()\n\n'

    def create_initial_state_test(self):
        initial_state = self.sm._get_initial_state()
        phrase = 'def test_it_has_an_initial_state(self):\n'+\
                 '\tself.machine.initial_state |should| equal_to("{ini_state}")\n'.format(ini_state=initial_state)+\
                 '\tself.machine.current_state |should| equal_to("{ini_state}")\n'.format(ini_state=initial_state)
        return phrase

    def create_states_test(self):
        states = self.sm._get_states()
        states_name = []
        for state in states:
            states_name.append(state["state"])
        phrase = 'def test_it_defines_states_using_method_calls(self):\n'+\
                 '\tself.machine |should| have(3).states\n'+\
                 '\tself.machine.states() |should| include_all_of({states_list})'.format(states_list=states_name)
        return phrase