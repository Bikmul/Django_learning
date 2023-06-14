import sys 
import os
import re
import settings

def main():
    if(len(sys.argv) != 2):
        return print("wrong number of arguments")
    path = sys.argv[1]
    regex = re.compile(".*\.template")
    if not regex.match(path):
        return print("wrong name of argument")
    if not os.path.isfile(path):
        return print("can't find a file")
    f = open(path, "r")
    template = "".join(f.readlines())
    f.close()
    file =template.format(name = settings.name, surname = settings.surname, age = settings.age, profession = settings.profession, title = settings.title)    
    regex = re.compile("(\.template)")
    path = "".join([path[:regex.search(path).start()], ".html"]) 
    f = open(path, "w")
    f.write(file)
    f.close()


if __name__ == '__main__':
    main()