#!/usr/bin/env python

import subprocess

def create_resource_group():
    print('Create stub')

def execute_az_command(command):
    to_be_executed = "az" + " " + command + " --output json"
    print('Executing command:\n' + to_be_executed)
    subprocess.run(to_be_executed.split(' '))

def main():
    resource_group = "data-factory"
    execute_az_command("group exists --name " + resource_group)
    print('main')

main()
