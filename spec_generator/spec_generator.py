from dia_bldd_modules.statemachine_generator.sm_generator import SMGenerator

class SpecGenerator():

    def __init__(self, data):
        self.data = data
        self.sm = SMGenerator()
        self.sm.load_data(data)

    def _header(self):
        return 'import unittest\n'+\
               'from should_dsl import should\n'+\
               'from dia_bldd_modules.statemachine_generator.StateMachine import MyStateMachine\n\n'+\
               'class FluidityTest(unittest.TestCase):\n\n'+\
               '\tdef setUp(self):\n'+\
               '\t\tself.machine = MyStateMachine()\n'

    def create_initial_state_test(self):
        initial_state = self.sm._get_initial_state()
        phrase = '\n\tdef test_it_has_an_initial_state(self):\n'+\
                 '\t\tself.machine.initial_state |should| equal_to("{ini_state}")\n'.format(ini_state=initial_state)+\
                 '\t\tself.machine.current_state |should| equal_to("{ini_state}")\n'.format(ini_state=initial_state)
        return phrase

    def create_states_test(self):
        states = self.sm._get_states()
        states_name = []
        for state in states:
            states_name.append(state["state"])
        phrase = '\n\tdef test_it_defines_states_using_method_calls(self):\n'+\
                 '\t\tself.machine |should| have({total}).states\n'.format(total=len(states_name))+\
                 '\t\tself.machine.states() |should| include_all_of({states_list})'
        phrase.format(states_list=states_name)
        return phrase

    def create_transition_respond_test(self):
        transitions = self.sm._get_transitions()
        transitions_name = []
        phrase = '\n\n\tdef test_its_declaration_creates_a_method_with_its_name(self):\n'
        for transition in transitions:
            phrase += '\t\tself.machine |should| respond_to("{transition_name}")\n'
            phrase.format(transition_name=transition["event"])
        return phrase

    def create_action_test(self):
        transitions = self.sm._get_transitions()
        phrase = '\n\tdef test_it_changes_machine_state(self):\n' +\
                 '\t\tself.machine.current_state |should| equal_to("{source}")\n'.format(source=transitions[0]["from"])
        for transition in transitions:
            phrase += '\t\tself.machine.{event_name}()\n'.format(event_name=transition["event"])+\
                      '\t\tself.machine.current_state |should| equal_to("{target}")\n'.format(target=transition["to"])
        return phrase

    def generate_content(self):
        content = self._header()
        content += self.create_initial_state_test()
        content += self.create_states_test()
        content += self.create_transition_respond_test()
        content += self.create_action_test()
        return content

    def create_test_file(self):
        content = self.generate_content()
        with open('TestStateMachine.py', 'w') as test_file:
            test_file.write(content)