#! /usr/bin/python3


# By Liping Wang    2019-03-29 14:57:43
# for python3 

from __future__ import print_function
import os
import sys
import subprocess
import regex as re
import argparse

nodes = [ 'node{}'.format(i) for i in range(1, 15)]
sep_line = '+-------------------------------+----------------------+----------------------+'


def get_smi(nodes):
    for node in nodes:
        node_info = '+-----------------------------------------------------------------------------+\n'\
                    '|                               {}                                         |\n'\
                    '+-----------------------------------------------------------------------------+'.format(node)
        print(node_info)
        cmd = 'ssh -t {} "nvidia-smi"'.format(node)
        output = subprocess.getoutput(cmd)
        lines = output.split('\n')
        for line in lines:
            if re.search('N/A', line) or re.search('Default', line):
                print(line.strip())

            if re.search('Default', line):
                print (sep_line)
        print ('\n\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cluster-level nvidia-smi')
    parser.add_argument('-n','--node', help='Specify a node in the cluster', type=int)
    args = parser.parse_args()
    if args.node:
        nodes = [ 'node{}'.format(args.node) ]

    get_smi(nodes)



