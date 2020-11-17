import time

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

f = open("loop_input.txt", "r")
print("Reading file...")

items = list(range(0, 20))
l = len(items)

printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    time.sleep(0.1)
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)


string = f.readline()
length = len(string) + 2
tape = ['B']*length
i = 1
tapehead = 1

with open('loop_output.txt', 'a+') as the_file:
    the_file.write("Expression: " + str(string) + '\n')

def action(input_char, replace_with, move, new_state):
    global tapehead, state
    if tape[tapehead] == input_char:
        tape[tapehead] = replace_with
        state = new_state
        if move == 'L':
            tapehead -= 1
        else:
            tapehead += 1
        return True
    return False

for s in string: #loop to place string in tape
    tape[i] = s
    i += 1

state = 0
#assigning characters to variable so that don't have to use characters each time
a, b, X, Z, U, V, R, L, B = 'a', 'b', 'X', 'Z', 'U', 'V', 'R', 'L', 'B' 
oldtapehead = -1
accept = False
while(oldtapehead != tapehead): #if tapehead not moving that means terminate Turing machine
    oldtapehead = tapehead
    #print(tape , "with tapehead at index", tapehead, "on state" , state)
    with open('loop_output.txt', 'a+') as the_file:
        the_file.write(str(tape) + " with tapehead at index " + str(tapehead) + " on state " + str(state) + '\n')
    if state == 0:
        if action(a, X, R, 1) or action(B, B, R, 10) or action(Z, Z, R, 7) or action(b, U, R, 4):
            pass
        
    elif state == 1:
        if action(a, a, R, 1) or action(b, b, R, 2) or action(B, B, L, 11):
            pass
        
    elif state == 2:
        if action(b, b, R, 2) or action(Z, Z, R, 2) or action(a, Z, L, 3):
            pass
            
    elif state == 3:
        if action(b, b, L, 3) or action(Z, Z, L, 3) or action(a, a, L, 3) or action(X, X, R, 0):
            pass
    
    elif state == 4:
        if action(b, b, R, 4) or action(Z, Z, R, 5) or action(B, B, L, 15):
            pass
        
    elif state == 5:
        if action(Z, Z, R, 5) or action(V, V, R, 5) or action(b, V, L, 6):
            pass
            
    elif state == 6:
        if action(Z, Z, L, 6) or action(V, V, L, 6) or action(b, b, L, 6) or action(U, U, R, 0):
            pass
            
    elif state == 7:
        if action(Z, Z, R, 7) or action(V, V, R, 8):
            pass
            
    elif state == 8:
        if action(V, V, R, 8) or action(B, B, R, 9):
            pass
        
    elif state == 11:
        if action(a, a, L, 11) or action(X, X, R, 12):
            pass
        
    elif state == 12:
        if action(a, Z, R, 13):
            pass
        
    elif state == 13:
        if action(a, X, R, 12) or action(B, B, R, 14):
            pass
            
    elif state == 15:
        if action(b, b, L, 15) or action(U, U, R, 16):
            pass
            
    elif state == 16:
        if action(b, V, R, 17):
            pass
            
    elif state == 17:
        if action(b, U, R, 16) or action(B, B, R, 18):
            pass
            
    else:
        accept = True
        
            
if accept:
    with open('loop_output.txt', 'a+') as the_file:
        the_file.write("String accepted on state " + str(state) + '\n')
else:
    with open('loop_output.txt', 'a+') as the_file:
        the_file.write("String not accepted on state " + str(state) + '\n')

print("Program finished successfully, thanks for using...")