#!/usr/bin/env python3
'''Lab 3 Part 2 script for launching system commands'''
# Author ID: asaini85

import subprocess

def free_space():
    p = subprocess.Popen(['df', '-h', '/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()

    if error:
        return "Error running command"
    else:
        result = output.decode('utf-8').strip().split('\n')[-1].split()[3]
        return result

if __name__ == '__main__':
    print(free_space())
