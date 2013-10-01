from should_dsl import should, should_not
from DiaModule.sm_generator import SMGenerator
import unittest

class SMGeneratorSpec(unittest.TestCase):

	def setUp(self):
		self.sm_generator = SMGenerator()

	def test_if_statemachine_was_generated(self):
		repr(self.sm_generator) |should| equal_to("class Statemachine(StateMachine):")

if __name__ == '__main__':
	unittest.main()