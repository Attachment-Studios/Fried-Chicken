# main.py
import tkinter
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile

def execute():
    try:
        print("---------------------------------")
        file = askopenfile(mode="r")
        code = file.read()
        file.close()
        characters = '\n !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'
        if code.lower().replace('fried chicken', '').replace(' ', '').replace('\n', '') == "":
            real_code = ""
            for line in code.split('\n'):
                chicken_amount = line.lower().count("fried chicken")
                if chicken_amount >= len(characters):
                    print("Chicken was MUTATED!!!")
                else:
                    character = characters[chicken_amount]
                real_code += str(character)
            try:
                cells_execute(real_code)
            except:
                print("Chicken was OVERFRIED!!!")
        else:
            print("Chicken had BIRD FLU!!!")
    except:
        print("Please input a valid file path...")

# cells
def cells_execute(__codeline__:str):
	codeline = str(__codeline__)
	for __________ in range(1):
		code = []
		iterated_code = "0skip "
		push_to_next_line = ":"
		for character in codeline:
			if character == push_to_next_line:
				code.append(iterated_code)
				iterated_code = "0skip "
			else:
				if iterated_code == "0skip ":
					iterated_code = ""
				iterated_code = iterated_code + character
		skip_lines = []
		variables_name = []
		variables_value = []
		for cell in code:
			if " < " in cell:
				variable_name = ""
				for character in cell.replace("nomenclate ", ""):
					if character == " ":
						break
					else:
						variable_name = variable_name + character
				variable_value = cell.replace("nomenclate ", "")
				variable_value = variable_value.replace(variable_name, "")
				variable_value = variable_value.replace(" < ", "")
				if "nomenclate " in cell:
					variables_name.append(variable_name)
					variables_value.append("")
				variables_value[variables_name.index(variable_name)] = variable_value
				skip_lines.append(int(code.index(cell)))
		line = -1
		while line < len(code) - 1:
			line += 1
			pure_command = str(code[line])
			command = pure_command
			skip_this_line = False
			if code.index(pure_command) in skip_lines:
				skip_this_line = True
				skip_lines.remove(code.index(pure_command))
			for name in variables_name:
				if " " + name in command and not skip_this_line:
					if "endocytosis " not in command and "grow " not in command and "exosmosis " not in command and "multinucleate " not in command and "mitosis " not in command and "meiosis " not in command and "fuse " not in command:
						command = command.replace(" " + name, " " + str(variables_value[variables_name.index(name)]))
			cell_contains_error = False
			if not(skip_this_line):
				if "exocytosis " in command:
					output = command.replace("exocytosis ", "")
					print(output)
				elif "endocytosis " in command:
					variable_name = command.replace("endocytosis ", "")
					if variable_name in variables_name:
						variables_value[variables_name.index(variable_name)] = input()
					else:
						cell_contains_error = True
				elif "skip " in command:
					skip_amount = (command.replace("skip ", ""))
					try:
						for after_index in range(1, int(skip_amount)+1):
							index = code.index(pure_command) + after_index
							skip_lines.append(index)
					except:
						cell_contains_error = True
				elif "regulate ^ " in command:
					try:
						cell_number = int(command.replace("regulate ^ ", ""))
						line = cell_number - 2
						if line < -1:
							line = -1
					except:
						cell_contains_error = True
				elif ">" in command or ">" == command:
					break
				elif "eject " in command:
					try:
						variable_name = command.replace("eject ", "")
						temporary_iterator = ""
						for character in variable_name:
							if character == ",":
								break
							else:
								temporary_iterator = temporary_iterator + character
						variable_name = temporary_iterator
						add_value = command.replace("eject ", "")
						add_value = add_value.replace(variable_name + ",", "")
						try:
							variables_value[variables_name.index(variable_name)] = int(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] -= int(add_value)
						except:
							variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] = variables_value[variables_name.index(variable_name)].replace(str(add_value), "")
					except:
						cell_contains_error = True
				elif "mitosis " in command:
					try:
						variable_name = command.replace("mitosis ", "")
						temporary_iterator = ""
						for character in variable_name:
							if character == ",":
								break
							else:
								temporary_iterator = temporary_iterator + character
						variable_name = temporary_iterator
						add_value = command.replace("mitosis ", "")
						add_value = add_value.replace(variable_name + ",", "")
						try:
							variables_value[variables_name.index(variable_name)] = int(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] /= int(add_value)
						except:
							variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] = variables_value[variables_name.index(variable_name)].replace(str(add_value), "")
					except:
						cell_contains_error = True
				elif "grow " in command:
					try:
						variable_name = command.replace("grow ", "")
						temporary_iterator = ""
						for character in variable_name:
							if character == ",":
								break
							else:
								temporary_iterator = temporary_iterator + character
						variable_name = temporary_iterator
						add_value = command.replace("grow ", "")
						add_value = add_value.replace(variable_name + ",", "")
						try:
							variables_value[variables_name.index(variable_name)] = int(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] += int(add_value)
						except:
							variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] += str(add_value)
					except:
						cell_contains_error = True
				elif "multinucleate " in command:
					try:
						variable_name = command.replace("multinucleate ", "")
						temporary_iterator = ""
						for character in variable_name:
							if character == ",":
								break
							else:
								temporary_iterator = temporary_iterator + character
						variable_name = temporary_iterator
						add_value = command.replace("multinucleate ", "")
						add_value = add_value.replace(variable_name + ",", "")
						try:
							variables_value[variables_name.index(variable_name)] = int(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] *= int(add_value)
						except:
							variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] += str(add_value)
					except:
						cell_contains_error = True
				elif "fuse " in command:
					try:
						variable_name = command.replace("fuse ", "")
						temporary_iterator = ""
						for character in variable_name:
							if character == ",":
								break
							else:
								temporary_iterator = temporary_iterator + character
						variable_name = temporary_iterator
						add_value = command.replace("fuse ", "")
						add_value = add_value.replace(variable_name + ",", "")
						try:
							variables_value[variables_name.index(variable_name)] = float(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] *= float(add_value)
						except:
							variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] += str(add_value)
					except:
						cell_contains_error = True
				elif "meiosis " in command:
					try:
						variable_name = command.replace("meiosis ", "")
						temporary_iterator = ""
						for character in variable_name:
							if character == ",":
								break
							else:
								temporary_iterator = temporary_iterator + character
						variable_name = temporary_iterator
						add_value = command.replace("meiosis ", "")
						add_value = add_value.replace(variable_name + ",", "")
						try:
							variables_value[variables_name.index(variable_name)] = float(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] /= float(add_value)
						except:
							variables_value[variables_name.index(variable_name)] = str(variables_value[variables_name.index(variable_name)])
							variables_value[variables_name.index(variable_name)] = variables_value[variables_name.index(variable_name)].replace(str(add_value), "")
					except:
						cell_contains_error = True
				else:
					cell_contains_error = True
				if cell_contains_error:
					print("Error in cell::" + str(code.index(pure_command) + 1) + "::" + pure_command)
					break


win = tkinter.Tk()
win.title("Fried Chicken")
win.configure(padx=20, pady=20)
btn1 = tkinter.Button(text="Browse Code File And Run In Console", command=execute)
btn1.pack()

win.mainloop()

