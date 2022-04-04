#!/usr/bin/python3

import sqlite3
import logging
import uuid
import hashlib
import termcolor
import pyfiglet
import getpass
import sys
import time
import random
import tests
import subprocess

logging.basicConfig(filename="errors.log", filemode="w", level=logging.DEBUG)

print_red = lambda x: termcolor.cprint(x, "red")
print_green = lambda x: termcolor.cprint(x, "green")
print_blue = lambda x: termcolor.cprint(x, "blue")
print_yellow = lambda x: termcolor.cprint(x, "yellow")
colored = lambda x, color: termcolor.colored(x, color)

fig = pyfiglet.Figlet(font="standard")

try:
    conn = sqlite3.connect("ErsDb.db")
except Exception as ex:
    logging.error("can't connect to the database, got this message: %s" % ex)

def help():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "--help":
            print("Help docs")
            sys.exit(0)
        else:
            print("Do you mean: --help")
            sys.exit(0)

def hashPassword(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt

def selectByLogin(login):
    try:
        cursor = conn.execute("SELECT LOGIN, PASSWORD FROM USER WHERE LOGIN = '%s'" % login)
        user = cursor.fetchone()
        if user == None:
            return False
        return user
    except Exception as ex:
        logging.error("selectionByLogin failed,got this message : %s" % ex)

def register(login, password):
    try:
        if selectByLogin(login) == False:
            conn.execute("INSERT INTO USER (LOGIN, PASSWORD)\
                            VALUES ('%s', '%s')" % (login, hashPassword(password)))
            conn.commit()
            return True
        else:
            return False
    except Exception as ex:
        logging.error("registration failed,got this message : %s" % ex)

def login(login, password):
    user = selectByLogin(login)
    if user == False:
        return False
    hpassword, salt = user[1].split(":")
    return hpassword == hashlib.sha256(salt.encode() + password.encode()).hexdigest()

def registerCommand():
    login = input(colored("Login: ", "yellow"))
    refill_pass = True
    while refill_pass:
        password = getpass.getpass(colored("Password: ", "yellow"))
        rpassword = getpass.getpass(prompt=colored("Confirm password: ", "yellow"))
        if password == rpassword:
            refill_pass = False
        else:
            print_red("Passwords does not match!")
        if not refill_pass and register(login, password):
            print_green("Congratulation you are registered successfully")
        else:
            if refill_pass == False:
                print_red("User already exist!")

def loginCommand():
    global exam_session
    global user
    user_login = input(colored("Login: ", "yellow"))
    user_password = getpass.getpass(colored("Password: ", "yellow"))
    if login(user_login, user_password):
        print_green("logged successfully")
        exam_session = True
        user = selectByLogin(user_login)
        return True
    else:
        print_red("Entered login or password Incorrect!")
        return False

def examshellCommand():
    global examshell_status
    global start_session
    global part_one
    global part_two
    if exam_session == True:
        examshell_status = True
        start_session = time.time()
        print_green("ExamShell started successfully")
        part_one = subjs[random.choice([0,1])]
        part_two = subjs[random.choice([2,3])]
    else:
        print_red("Please login first!")

def timeCommand():
    if start_session == 0:
        print_red("Examshell session not started yet!")
    else:
        remaining_time = time.strftime('%H:%M:%S', time.gmtime(time.time() - start_session))
        print_green("Examshell started %s ago" % remaining_time)

def grademeCommand():
    global grade
    if exam_session == True and examshell_status == True:
        if grade[0] == 0:
            if part_one == "inter":
                if tests.inter() == True:
                    subprocess.Popen(["python3", "animation.py"])
                    time.sleep(3)
                    subprocess.Popen(["python3", "killAnimation.py"])
                    time.sleep(1)
                    print_green("Current subject 'Inter' validated successfully")
                    grade[0] = 50
                    subprocess.Popen(["rm","a.out"], cwd="rendu/%s" % part_one)
                elif tests.inter() == False:
                    subprocess.Popen(["python3", "animation.py"])
                    time.sleep(3)
                    subprocess.Popen(["python3", "killAnimation.py"])
                    time.sleep(1)
                    print_red("Current Subject 'Inter' Faild passing the tests!")
                    subprocess.Popen(["rm","a.out"], cwd="rendu/%s" % part_one)
                else:
                    subprocess.Popen(["python3", "animation.py"])
                    time.sleep(3)
                    subprocess.Popen(["python3", "killAnimation.py"])
                    time.sleep(1)
                    print_red(tests.inter())
            else:
                if tests.union() == True:
                    subprocess.Popen(["python3", "animation.py"])
                    time.sleep(3)
                    subprocess.Popen(["python3", "killAnimation.py"])
                    time.sleep(1)
                    print_green("Current subject 'Union' validated successfully")
                    grade[0] = 50
                    subprocess.Popen(["rm","a.out"], cwd="rendu/%s" % part_one)
                elif tests.union() == False:
                    print_red("Current Subject 'Union' Faild passing the tests!")
                    subprocess.Popen(["rm","a.out"], cwd="rendu/%s" % part_one)
                else:
                    subprocess.Popen(["python3", "animation.py"])
                    time.sleep(3)
                    subprocess.Popen(["python3", "killAnimation.py"])
                    time.sleep(1)
                    print_red(tests.union())
        else:
            if part_two == "gnl":
                subprocess.Popen(["python3", "animation.py"])
                if tests.gnl() == True:
                    subprocess.Popen(["python3", "killAnimation.py"])
                    time.sleep(1)
                    print_green("Current subject 'Get_next_line' validated successfully")
                    grade[1] = 50
                    time.sleep(5)
                    finishCommand()
                    sys.exit(0)
                else:
                    time.sleep(3)
                    subprocess.Popen(["python3", "killAnimation.py"])
                    print_red("Current Subject 'Get_next_line' Faild passing the tests!")
            else:
                subprocess.Popen(["python3", "animation.py"])
                if tests.ft_printf() == True:
                    subprocess.Popen(["python3", "killAnimation.py"])
                    time.sleep(1)
                    print_green("Current subject 'Ft_printf' validated successfully")
                    grade[1] = 50
                    time.sleep(5)
                    finishCommand()
                    sys.exit(0)
                else:
                    time.sleep(3)
                    subprocess.Popen(["python3", "killAnimation.py"])
                    time.sleep(1)
                    print_red("Current Subject 'Ft_printf' Faild passing the tests!")
    else:
        print_red("Examshell session not started yet!")

def finishCommand():
    if exam_session == True and examshell_status == True:
        if sum(grade) <= 50:
            print_red("Examshell faild with grade: %s" % sum(grade))
        else:
            print_green("Examshell passed successfully with grade: %s" % sum(grade))

def helpCommand():
    pass

def subjCommand():
    if exam_session == True and examshell_status == True:
        file_p1 = open("subjs/" + part_one + ".txt", "r")
        file_p2 = open("subjs/" + part_two + ".txt", "r")
        if grade[0] == 0:
            print_green("Subject: %s" % part_one)
            print_yellow(file_p1.read())
            file_p1.close()
        else:
            print_green("Subject: %s" % part_two)
            print_yellow(file_p2.read())
            file_p2.close()
    else:
        print_red("Examshell session not started yet!")

def updateCommand():
    out = subprocess.check_output(["git", "pull"])
    print(out)
    if out == "Already up to date.\n".encode():
        print_green("you have latest version")
    else:
        print_green("Examshell updated successfully")

def examShell(prompt=colored("$> ", "blue"), exam_title="Exam Shell 02"):
    help()
    run = True
    global exam_session
    global user
    global start_session
    global examshell_status
    global subjs
    global part_one
    global part_two
    global grade
    subjs = ["inter", "union", "ft_printf", "gnl"]
    grade = [0,0]
    part_one = None
    part_two = None
    examshell_status = False
    exam_session = False
    user = "Anonymous"
    start_session = 0
    commands = ["register", "login", "me", "examshell", "time", "grademe", "finish", "help", "subj", "update"]
    print_yellow(fig.renderText("%s" % exam_title))
    while run:
        if examshell_status == True:
            if time.time() - start_session >= 7200:
                print_red("Examshell time expired")
                sys.exit(0)
        try:
            command = input(prompt).strip()
            if command in commands:
                if command == "register":
                    registerCommand()
                if command == "login":
                    loginCommand()
                if command == "finish":
                    finishCommand()
                    run = False
                    exam_session = False
                    examshell_status = False
                    sys.exit(0)
                if command == "me":
                    if exam_session == True and examshell_status == True:
                        print_yellow(user[0])
                        print_green("Current Grade: %s" % str(sum(grade)))
                    elif exam_session == True:
                        print_yellow(user[0])
                    else:
                        print_yellow(user)
                if command == "examshell":
                    if examshell_status == False:
                        examshellCommand()
                    else:
                        print_red("Examshell session alredy started!")
                if command == "time":
                    timeCommand()
                if command == "subj":
                    subjCommand()
                if command == "grademe":
                    grademeCommand()
                if command == "update":
                    updateCommand()
            else:
                print_red("Command not found please use: ./main --help")
        except (KeyboardInterrupt, EOFError):
            print()
            sys.exit(0)

if __name__ == "__main__":
    examShell()
