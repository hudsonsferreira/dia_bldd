Generates unit tests

Basic usage::

    from dia_bldd_modules.spec_generator.spec_generator import SepcGenerator 
    sg = SpecGenerator(dia.diagrams()[0].data)#index represents an opened diagram on Dia
    sg.create_initial_state_test()

Then, you must get the tests::
    
    initial_state |should_not| be_empty
    initial_state |should| be(1)
    initial_state |should| equal_to("White Sheep")
