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
except:
  print("[ERROR]Invalid Input File Format")