#!/usr/bin/env python3

import subprocess, json, argparse

class print_indicator:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_with_indication(print_indicator, message):
    print(f'{print_indicator}{message}')

def create_resource_group(resource_group):
    execute_az_command(f'group create -l australiaeast -n {resource_group}')

def create_state_container():
    print_with_indication(print_indicator.OK_GREEN,'Create subcontainer')

def execute_az_command(command):
    to_be_executed = f"az {command} --output json"
    print_with_indication(print_indicator.WARNING, f'Executing command:\n{to_be_executed}')
    output = subprocess.run(to_be_executed.split(' '), capture_output=True, text=True)
    return output.stdout

def does_resource_group_exist(resource_group):
    az_output = execute_az_command("group exists --name " + resource_group)
    return az_output == "true\n"

def parse_arguments():
    parser = argparse.ArgumentParser("Ensure resource group is created")
    parser.add_argument('--resource-group-name', '-rg',
                        type=str,
                        help="Resource Group Name",
                        required=True)
    return parser.parse_args()

def main():
    arguments = parse_arguments()
    resource_group = arguments.resource_group_names
    green_colour = "\033[92m"
    resource_group_exists = does_resource_group_exist(resource_group)
    if resource_group_exists:
        print_with_indication(print_indicator.OK_BLUE, f"resource group '{resource_group}' already created. Will not attempt to create it again.")
    else:
        print_with_indication(print_indicator.OK_BLUE, f"{green_colour}resource group '{resource_group}' does not exists. Will attempt to create it.")
        create_resource_group(resource_group)

main()
