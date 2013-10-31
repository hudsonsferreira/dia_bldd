class SMGenerator():

    def __init__(self):
        self.header = "from fluidity import StateMachine, state, transition\nclass MyStateMachine(StateMachine):"
        self.data = None

    def load_data(self, data):
        self.data = data
        if self.data == None:
            raise ValueError("Invalid data!")
    
    def _get_states(self):
        states = []
        for layer in self.data.layers:
            for obj in layer.objects:
                if obj.type.name == "UML - State":
                    states.append({'state':obj.properties["text"].value.text.strip(),
                                   'enter':obj.properties["entry_action"].value,
                                   'exit':obj.properties["exit_action"].value
                                  })
        return states

    def _get_transitions(self):
        transitions = []
        for layer in self.data.layers:
            for obj in layer.objects:
                if obj.type.name == "UML - Transition":
                    source = obj.handles[0].connected_to.object
                    target = obj.handles[1].connected_to.object
                    if source.type.name == "UML - State" and target.type.name == "UML - State":
                        transitions.append({'from':source.properties["text"].value.text.strip(), 
                                            'event':obj.properties["trigger"].value, 
                                            'to':target.properties["text"].value.text.strip(),
                                            'action':obj.properties["action"].value, 
                                            'guard':obj.properties["guard"].value
                                           })           
        return transitions              

    def _get_initial_state(self):
        for layer in self.data.layers:
            for obj in layer.objects:
                if obj.type.name == "UML - Transition":
                    source = obj.handles[0].connected_to.object
                    target = obj.handles[1].connected_to.object
                    if source.type.name == "UML - State Term" and target.type.name == "UML - State":
                        return target.properties["text"].value.text.strip()

    def _generate_state(self):
        initial_state = self._get_initial_state()
        states = self._get_states()
        state_content = ""
        state_content += "\n\n\tinitial_state = '"+initial_state+"'\n"

        for state in states:
            state_content += "\n\tstate('"+state["state"]
            if state["enter"] != "":
                state_content += "', enter='"+state["enter"]
            if state["exit"] != "":
                state_content += "', exit='"+state["exit"]
            state_content +="')"
        state_content += "\n"
        return state_content

    def _generate_transition(self):
        transitions = self._get_transitions()
        transition_content = ""
        
        for transition in transitions:
            transition_content += "\n\ttransition(from_='"+transition["from"]+"', event='"+transition["event"]+"', to='"+transition["to"]
            if transition["guard"] != "":
                transition_content += "', guard='"+transition["guard"]
            if transition["action"] != "":
                transition_content += "', action='"+transition["action"]
            transition_content +="')"
        transition_content += "\n"
        return transition_content


    def _generate_fluidity_methods(self):
        states = self._get_states()
        transitions = self._get_transitions()
        methods_content = ""
        phrase = "\n\tdef {word}(self): pass"
        for state in states:
            if state["enter"] != "":
                methods_content += phrase.format(word=state["enter"])
            if state["exit"] != "":
                methods_content += phrase.format(word=state["exit"])
        for transition in transitions:
            if transition["guard"] != "":
                methods_content += phrase.format(word=transition["guard"])
            if transition["action"] != "":
                methods_content += phrase.format(word=transition["action"])
        return methods_content


    def _generate_statemachine(self):
        content = self.header
        content += self._generate_state()
        content += self._generate_transition()
        content += self._generate_fluidity_methods()
        return content

    def create_fluidity(self):
        content = self._generate_statemachine()
        with open('StateMachine.py', 'w') as fluidity:
            fluidity.write(content)