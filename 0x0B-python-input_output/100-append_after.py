#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r") as f:
        a_file = []
        lines = len(f.readlines())
        f.seek(0)
        for t in range(lines):
            a_line = f.readline()
            a_file.append(a_line)
            if search_string in a_line:
                a_file.append(new_string)
    with open(filename, "w") as f:
        f.writelines(a_file)
