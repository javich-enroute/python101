# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def sets ():
    set = {"a","b","c","a","b","c","a","b","c","a","b","c","a","b","c"}
    for s in set:
        print(s)


def diccionarios():
    ejemplo_dicccionario = {
        "str": "esto es un string",
        "float" : 1.540,
        "int" : 1,
        "str": "otra cosa"
    }

    for llave,valor in ejemplo_dicccionario.items():
     print(f"{llave}={valor}")




def iterate():
    x = "otra cosa"
    for y in range(0, 6, 2):
        print(y)
    print("------------------")

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)



def printint():
    x = 1
    f = 1.001


def printstr():
    s = ''
    x = "asdf"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('lo que yo quiera {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Javich')
    sets()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
