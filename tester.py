from the4 import check_commands
from test_data import *
import time
# CENG111 THE4 Tester by Burak Akkaya

def prettify(Tree, space=0, prt=True):
    # def prettify/ created by Ilker Kosaroglu
    if prt:
        print '\033[93m' + Tree[1].lower() + '\033[0m', "*", " " * space * 3, Tree[0]
    if not Tree:
        return space
    for node in Tree[2:]:
        prettify(node, space + 1, prt)


test_no = 1
error = 0
while test_no < 26:
    test_fs = "FS" + "%03d" % test_no
    test_c = "C" + "%03d" % test_no
    test_r = "R" + "%03d" % test_no
    if check_commands(vars()[test_fs], vars()[test_c]) != vars()[test_r]:
        print "-" * 30 + "%03d" % test_no + "-" * 30
        print '\033[93m' + test_fs + " >" + '\033[0m'
        prettify(vars()[test_fs])
        print '\033[93m' + test_c + " >" + '\033[0m', vars()[test_c][0]
        for x in vars()[test_c][1:]:
            print " " * 7 + x
        print '\033[93m' + "Result >" + '\033[0m', check_commands(vars()[test_fs], vars()[test_c])
        print '\033[93m' + "Ex.Result >" + '\033[0m', vars()[test_r]
        error += 1
    test_no += 1
print "-" * 63 + "\n", test_no-1, "test cases applied.\n" + "Test completed with", error, "failures."
