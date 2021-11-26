# to chicken

def to_chicken(text:str):
    code = ""
    characters = '\n !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    for character in text:
        chicken_amount = characters.index(character)
        chickens = " fried chicken" * chicken_amount
        code += '\n' + chickens[1:]
    return "\n".join(code.split('\n')[1:])

in_file = input("input file: ")
out_file = input("output file: ")

in_data_file = open(in_file, "r")
out_data_file = open(out_file, "w")

in_data = in_data_file.read()
out_data_file.write(to_chicken(in_data))

in_data_file.close()
out_data_file.close()

