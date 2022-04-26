from os import popen
from itertools import combinations
path = str(__file__)
path_to_exe = path[:-12] + "cmake-build-debug\\"
path_to_tests = path[:-7] + 'etc'
print("path to exe: ", path_to_exe)
print("path to tests: ", path_to_tests)
flags = ['']
for comb in (combinations("123", r=i) for i in range(1, 4)):
    for flag in comb:
        flags.append(''.join(flag))
print("Testing:")
errors = {}
for flag in flags:
    print("Mode:", flag)
    for test in "abcdef":
        cmd = f"{path_to_exe}comm.exe {'' if flag == '' else '-' + flag} {path_to_tests}\\{test}.txt {path_to_tests}\\{test}.txt_2"
        out = popen(cmd).read()
        if out != open(f"{path_to_tests}\\{test}.txt.eta{'' if flag == '' else '.' + flag}", 'r').read():
            if flag in errors:
                errors[flag].append(test)
            else:
                errors[flag] = [test]
            print("Error on test:", test)
if not errors:
    print("All tests passed!!!")
