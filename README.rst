Converts a Dia statemachine to a Fluidity statemachine.

Basic usage::
```from dia_statemachine_generator.sm_generator import SMGenerator 
sm = SMGenerator()
sm.load_data(dia.diagrams()[0].data) #index represents an opened diagram on Dia
sm.generate()
```