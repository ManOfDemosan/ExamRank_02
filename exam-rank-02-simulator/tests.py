#!/usr/bin/python3
import subprocess

def compile(c_file):
    try:
        out = subprocess.check_output(["gcc", c_file], cwd="rendu/%s" % c_file.split(".")[0])
        if out == "".encode():
            return True
        return False
    except Exception:
        return False

def inter():
    if compile("inter.c") == True:
        test1 = subprocess.check_output(["./a.out", "padinton", "paqefwtdjetyiytjneytjoeyjnejeyj"] , cwd="rendu/inter")
        test2 = subprocess.check_output(["./a.out", "ddf6vewg64f", "gtwthgdwthdwfteewhrtag6h4ffdhsd"] , cwd="rendu/inter")
        test3 = subprocess.check_output(["./a.out", "nothing", "This sentence hides nothing"] , cwd="rendu/inter")
        test4 = subprocess.check_output(["./a.out"] , cwd="rendu/inter")

        if test1 == "padinto\n".encode() and test2 == "df6ewg4\n".encode() and test3 == "nothig\n".encode() and test4 == "\n".encode():
            return True
        else:
            return False
    else:
        return "something went wrong compiling your code!"

def union():
    if compile("union.c") == True:
        test1 = subprocess.check_output(["./a.out", "zpadinton", "paqefwtdjetyiytjneytjoeyjnejeyj"] , cwd="rendu/union")
        test2 = subprocess.check_output(["./a.out", "ddf6vewg64f", "gtwthgdwthdwfteewhrtag6h4ffdhsd"] , cwd="rendu/union")
        test3 = subprocess.check_output(["./a.out", "rien", "cette phrase ne cache rien"] , cwd="rendu/union")
        test4 = subprocess.check_output(["./a.out"] , cwd="rendu/union")
        test5 = subprocess.check_output(["./a.out", "rien"] , cwd="rendu/union")

        if test1 == "zpadintoqefwjy\n".encode() and test2 == "df6vewg4thras\n".encode() and test3 == "rienct phas\n".encode() and test4 == "\n".encode() and test5 == "\n".encode():
            return True
        else:
            return False
    else:
        return "something went wrong compiling your code!"

def ft_printf():
    try:
        subprocess.Popen(["make","fclean"], cwd="helper")
        out = subprocess.check_output(["make","m"], cwd="printfTester")
        fl = open("printfTester/diffTrace", "wb")
        fl.write(out)
        fl.close()
    except Exception:
        return False
    try:
        diff = subprocess.check_output(["diff" ,"diffTrace", "pfCorrTrace"], cwd="printfTester")
    except Exception:
        return False
    dl = subprocess.check_output(["rm", "diffTrace"], cwd="printfTester")
    if diff == "".encode():
        return True
    return False

def gnl():
    try:
        out = subprocess.check_output(["make","m"], cwd="gnlTester")
        fl = open("gnlTester/diffTrace", "wb")
        fl.write(out)
        fl.close()
    except Exception:
        return False
    try:
        diff = subprocess.check_output(["diff" ,"diffTrace", "gnlCorrTrace"], cwd="gnlTester")
    except Exception:
        return False
    dl = subprocess.check_output(["rm", "diffTrace"], cwd="gnlTester")
    if diff == "".encode():
        return True
    return False
