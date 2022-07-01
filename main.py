#from sys import stdin
import fileinput

try:
  l=[]
  '''f1=stdin.read().split("\n")
  for i in f1:
    if(i!=""):
      l.append(i+"\n")
    else:
      l.append("\n")'''
  with fileinput.input(files = 'test.txt') as f1:
    for i in f1:
      if(i!=""):
        l.append(i+"\n")
      else:
        l.append("\n")
  xx=len(l)-1
  while(True):
    if(l[xx]=="\n"):
      l=l[:xx]
      xx=xx-1
    else:
      break
  opcode = {"add": ("10000", "RRR"),"sub": ("10001", 'RRR'),"mov": ("10010", 'R$', "10011", 'RR'),"ld": ("10100", "Rm"),
              "st": ("10101", "Rm"),"mul": ("10110", "RRR"),"div": ("10111", "RR"),"rs": ("11000", "R$"),
              "ls": ("11001", "R$"),"xor": ("11010", "RRR"),"or": ("11011", "RRR"),"and": ("11100", "RRR"),
              "not": ("11101", "RR"),"cmp": ("11110", "RR"),"jmp": ("11111", "m"),"jlt": ("01100", "m"),
              "jgt": ("01101", "m"),"je": ("01111", "m"),"hlt": ("01010", "F")}
  registers = {"R0": "000","R1": "001","R2": "010","R3": "011","R4": "100","R5": "101","R6": "110","FLAGS": "111"}
  var_dict = {}  # Stores the variable name with the memory address allocated to the variable
  label_dict  = {} #Stores the variable name with the memory address allocated to the label
  instruction_count = 0
  line_count=1
  l2 = []
  out=[]
  error=False
  def _8bit(n):  # Function to convert a binary number to 8 bit binary number
      x = bin(n)[2:]
      num = 8 - len(x)
      return "0" * num + x
  def inst_to_bin(instruction_list):
      global line_count
      global error
      binary_instruction = ""
      # getting opcode
      if instruction_list[0] in opcode.keys():
          if instruction_list[0] != "mov":
              binary_instruction = binary_instruction + opcode[instruction_list[0]][0]
          else:
              if instruction_list[2][0] == "$":
                  binary_instruction += opcode[instruction_list[0]][0]
              else:
                  binary_instruction += opcode[instruction_list[0]][2]
          if instruction_list[0] != "mov": # getting type and values accordingly
              if opcode[instruction_list[0]][1] == "RRR":  # type A
                if len(instruction_list) == 4 and instruction_list[1] in registers.keys() and instruction_list[2] in registers.keys() and instruction_list[3] in registers.keys():
                  
                  if registers[instruction_list[1]] != "111" and registers[instruction_list[2]] != "111" and registers[instruction_list[3]] != "111":
                    binary_instruction = binary_instruction + "00" + registers[instruction_list[1]] + registers[instruction_list[2]] + registers[instruction_list[3]]
                    out.append(binary_instruction)
                  else:
                    error = True
                    print("[ERROR] Illegal use of FLAGS register at line "+str(line_count))
                else: 
                  error =  True
                  print("[ERROR] Invalid Syntax at line "+str(line_count))
              elif opcode[instruction_list[0]][1] == "Rm":  # type D
                if len(instruction_list) == 3 and instruction_list[1] in registers.keys():  
                  if registers[instruction_list[1]] != "111":
                    if instruction_list[2] in var_dict.keys():
                      binary_instruction = binary_instruction + registers[instruction_list[1]] + var_dict[instruction_list[2]]
                      out.append(binary_instruction)
                    elif instruction_list[2] in label_dict.keys():
                      error = True
                      print("[ERROR] Label Misused as Variable at line "+str(line_count))
                    else:
                      error = True
                      print("[ERROR] Use of undefined variable at line "+str(line_count))
                  else:
                    error = True
                    print("[ERROR] Illegal use of FLAGS register at line "+str(line_count)) 
                else:
                  error = True
                  print("[ERROR] Invalid Syntax at line "+str(line_count))    
except:
  print("[ERROR]Invalid Input File Format")