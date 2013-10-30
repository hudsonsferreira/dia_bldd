import unittest
from should_dsl import should
from dia_bldd_modules.statemachine_generator.StateMachine import MyStateMachine

class FluidityTest(unittest.TestCase):

	def setUp(self):
		self.machine = MyStateMachine()

	def test_it_has_an_initial_state(self):
		self.machine.initial_state |should| equal_to("White Sheep")
		self.machine.current_state |should| equal_to("White Sheep")

	def test_it_defines_states_using_method_calls(self):
		self.machine |should| have(3).states
		self.machine.states() |should| include_all_of({states_list})

	def test_its_declaration_creates_a_method_with_its_name(self):
		self.machine |should| respond_to("{transition_name}")
		self.machine |should| respond_to("{transition_name}")
		self.machine |should| respond_to("{transition_name}")

	def test_it_changes_machine_state(self):
		self.machine.current_state |should| equal_to("White Sheep")
		self.machine.make_black()
		self.machine.current_state |should| equal_to("Black Sheep")
		self.machine.make_grey()
		self.machine.current_state |should| equal_to("Grey Sheep")
		self.machine.make_white()
		self.machine.current_state |should| equal_to("White Sheep")
