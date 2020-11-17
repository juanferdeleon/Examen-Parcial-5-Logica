'''
        Examen Parcial 5

Creado por:

    Juan Fernando De Leon       17822
    Diego Estrada               18
    Andree Toledo               18

'''

import sys

pr = sys.stdout.write

class MachineTapeException(Exception):
	""" Turing Exception Exception """
	def __init__(self, value):
		Exception.__init__(self)
		self.value = value
	def __str__(self):
		return self.value

class TuringErrorException(Exception):
	""" Turing Exception Exception """
	def __str__(self):
		return "Reject"

class TuringAcceptException(Exception):
	""" Turing Accept Exception """
	def __str__(self):
		return "Accept"

class MachineTape:
	def __init__(self, initialString=[], initialPos=0, blank="_"):
		self.tape = []
		self.pos = initialPos
		self.blank = blank
		self.initialString = initialString
		if len(initialString) > 0:
		    for ch in initialString:
			    self.tape.append(ch)
		else:
		    self.tape.append(blank)

	def reinit(self):
		self.__init__(self.initialString)

	def move(self, check_char, changeto_char, direction):
		""" Only R, L directions are supported """
		if check_char != self.tape[self.pos]:
			raise MachineTapeException ("Tape head doesn't match head character")
		
		# at this point the head is over the same character we are looking for
		#  change the head character to the new character
		self.tape[self.pos] = changeto_char
		
		if direction == "L":
			self.move_left()
		elif direction == "R":
			self.move_right()
		else: raise MachineTapeException ("Direction is invalid")
	
	def read(self):
		""" return the character over the head """
		return self.tape[self.pos]
	
	def move_left(self):
		if self.pos <= 0: 
			self.tape.insert(-1, self.blank)
			self.pos = 0
		else:
			self.pos += -1

	def move_right(self):
		self.pos += 1
		if self.pos >= len(self.tape): self.tape.append(self.blank)
	
	def show(self):
		""" print the tape """
		for ch in self.tape:
			pr(ch)
		pr("\n"); pr(" "*self.pos + "^"); pr("\n")

class TuringMachine:
	def __init__(self, initialString, finalStates=[], blank="_"):
		self.blank = blank
		self.tape = MachineTape(initialString)
		self.fstates = finalStates
		self.program = {}
		self.initState = 0
		self.state = self.initState
		self.lenStr = len(initialString)
	
	def reinit(self):
		self.state = self.initState
		self.tape.reinit()
	
	def addTransition(self, state, char_in, dest_state, char_out, movement):
		if not self.program.has_key(state):
			self.program[state] = {}

		tup = (dest_state, char_out, movement)
		self.program[state][char_in] = tup

	def step(self):
		if self.lenStr == 0 and self.state in self.fstates: raise TuringAcceptException
		if self.state in self.fstates: raise TuringAcceptException 
		if self.state not in self.program.keys(): raise TuringErrorException
		
		head = self.tape.read()
		if head not in self.program[self.state].keys(): raise TuringErrorException

		# execute transition
		(dest_state, char_out, movement) = self.program[self.state][head]
		self.state = dest_state
		try:
			self.tape.move(head, char_out, movement)
		except MachineTapeException, s:
			print s

	def execute(self):
		try:
			while 1:
				m.tape.show()
				m.step()
		except (TuringErrorException, TuringAcceptException), s:
			print s

def initTuringMachine(initialString):
    '''Set transitions of Turing Machine'''

    m = TuringMachine(initialString, [5])

    '''q0'''
    # 0 -> _, R
    m.addTransition(0, '0', 1, '_', 'R')
    # _ -> R
    m.addTransition(0, '_', 7, '_', 'R')
    # x -> R
    m.addTransition(0, 'x', 6, 'x', 'R')

    '''q1'''
    # 0 -> x, R
    m.addTransition(1, '0', 2, 'x', 'R')
    # x -> R
    m.addTransition(1, 'x', 1, 'x', 'R')
    # _ -> R
    m.addTransition(1, '_', 5, '_', 'R')

    '''q2'''
    # 0 -> R
    m.addTransition(2, '0', 3, '0', 'R')
    # x -> R
    m.addTransition(2, 'x', 2, 'x', 'R')
    # _ -> R
    m.addTransition(2, '_', 4, '_', 'L')

    '''q3'''
    # 0 -> x, R
    m.addTransition(3, '0', 2, 'x', 'R')
    # x -> R
    m.addTransition(3, 'x', 3, 'x', 'R')
    # _ -> R
    m.addTransition(3, '_', 6, '_', 'R')

    '''q4'''
    # 0 -> R
    m.addTransition(4, '0', 4, '0', 'L')
    # x -> R
    m.addTransition(4, 'x', 4, 'x', 'L')
    # _ -> R
    m.addTransition(4, '_', 1, '_', 'R')

    '''q7'''
    # _ -> R
    m.addTransition(7, '_', 7, '_', 'R')
    # x -> R
    m.addTransition(7, 'x', 7, 'x', 'R')
    # 0 -> R
    m.addTransition(7, '0', 7, '0', 'R')

    return m



if __name__ == "__main__":
    '''Main'''

    f = open("accepted_input_final.txt", "r")
    print("Reading file...")
    
    initialString = f.readline()
    
    # Turing Machine 1 (Accept)
    m = initTuringMachine(initialString)

    # run the TM
    m.execute()

    # f = open("rejected_input_final.txt", "r")
    # print("Reading file...")
    
    # initialString = f.readline()

    # # Turing Machine 2 (Reject)
    # m = initTuringMachine(initialString)

    # # run the TM
    # m.execute()

    # f = open("loop_input_final.txt", "r")
    # print("Reading file...")
    
    # initialString = f.readline()

    # # # Turing Machine 2 (Infinite Loop)
    # m = initTuringMachine(initialString)

    # # # run the TM
    # m.execute()