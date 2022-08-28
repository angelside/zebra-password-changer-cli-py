#!/usr/bin/env python
"""
zebra-password-changer-cli-py

Usage: python main.py <IP_ADDRESS> <PASSWORD (4 digit, only numbers)>
"""
import ipaddress
import socket
import sys
import platform

config = {
    'app_title': '== Zebra password changer ==',
    'app_version': '0.1.0',
    'app_file_name': 'main.py',

    'printer_port': 9100,
    'socket_timeout': 3,
    'password_total_char': 4
}


class CliColors:
    """Cli colors
    """
    HEADER = '\033[95m'
    WHITE  = '\33[37m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_version():
    """
    VERSION
        zebra-password-changer v0.1.0 - Python 3.10.6
    """
    print(f"{CliColors.OKCYAN}VERSION{CliColors.ENDC}")
    print(f"    zebra-password-changer v{config['app_version']} - Python {platform.python_version()}")
    sys.exit(0)


def print_help():
    """
    == Zebra password changer ==

    USAGE
        python main.py <IP_ADDRESS> <PASSWORD>
        python main.py [command]

    COMMANDS
        help     show CLI help
        version  show CLI version

    DESCRIPTION
        CLI tool that allows changing Zebra printers password
    """
    print(f"{CliColors.OKCYAN}USAGE{CliColors.ENDC}")
    print("    python main.py <IP_ADDRESS> <PASSWORD>")
    print("    python main.py [command]")
    print("")

    print(f"{CliColors.OKCYAN}COMMANDS{CliColors.ENDC}")
    print("    help", f"    {CliColors.WHITE}show CLI help{CliColors.ENDC}")
    print("    version", f" {CliColors.WHITE}show CLI version{CliColors.ENDC}")
    print("")

    print(f"{CliColors.OKCYAN}DESCRIPTION{CliColors.ENDC}")
    print("    CLI tool that allows changing Zebra printers password")

    sys.exit(0)


def error_msg(msg, exit=False):
    """Print error message

    Args:
        msg (str): message
        exit (bool, optional): exit from app, defaults to False.
    """
    print(f"{CliColors.FAIL}[ERROR]{CliColors.ENDC} {msg}")
    if exit:
        sys.exit(0)


def usage_help_msg():
    print(f"{CliColors.WARNING}use 'python main.py help' for help{CliColors.ENDC}")


def check_arguments(argument_list):
    """Check arguments

    Args:
        argument_list (list): arguments
    """

    # No any argument -> error & exit
    if not argument_list:
        error_msg("There is no any argument!\n")
        print_help()

    # Argument is "help" -> show help & exit
    if argument_list[0] == "help":
        print_help()

    # Argument is "version" -> show version & exit
    if argument_list[0] == "version":
        print_version()

    # Not have 2 argument -> error & exit
    if len(argument_list) != 2:
        error_msg("Wrong command or argument!\n")
        usage_help_msg()
        sys.exit(0)


def validate_ip_address(ip_address):
    # Validate ip address
    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        # invalid ip adress
        return False
    else:
        return True


def validate_password(input_password, total_char):
    """Validate password

    Args:
        input_password (str): password
    """
    # total_char (from config) and only numbers
    if not input_password.isdigit() or len(input_password) != total_char:
        # invalid password
        return False
    else:
        return True


def check_ip_and_password(input_ip_address, input_password):
    valid_ip_address = validate_ip_address(input_ip_address)
    valid_password   = validate_password(input_password, config['password_total_char'])

    if not valid_ip_address and not valid_password:
        error_msg("IP adress is invalid!")
        error_msg(f"Password is invalid! Please enter a {config['password_total_char']} digit number.")
        usage_help_msg()
        sys.exit(0)
    elif not valid_ip_address:
        error_msg("IP adress is invalid!")
        sys.exit(0)
    elif not valid_password:
        error_msg(f"Password is invalid! Please enter a {config['password_total_char']} digit number.")
        sys.exit(0)


def socket_request(ip_address, port, timeout, zpl_code):
    """Socket request

    Args:
        ip_address (str): IP address
        port (int): Port
        timeout (int): Timeout
        zpl_code (str): ZPL code to send
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((ip_address, port))
            sock.send(zpl_code)
            print(f"\r{CliColors.OKGREEN}[OK]{CliColors.ENDC} {CliColors.OKBLUE}{ip_address}{CliColors.ENDC} : password has been changed.")
        except TimeoutError:
            error_msg(f"Request timed out while connecting to remote host {ip_address}", True)
        finally:
            sock.close()


def main():
    """ Main function
    """

    # Check arguments
    full_cmd_arguments = sys.argv           # Get full command-line arguments
    argument_list = full_cmd_arguments[1:]  # Keep all but the first
    check_arguments(argument_list)

    # Continue only if argument check is passed

    input_ip_address = argument_list[0]
    input_password   = argument_list[1]
    check_ip_and_password(input_ip_address, input_password)

    # Continue only if ip address and password both are valid

    # Prepare the password change zpl code from input_password
    fmt_zpl_code = f"^XA^KP{input_password}^JUS^XZ".encode()

    # Send the password change request
    socket_request(
        ip_address=input_ip_address,
        port=config['printer_port'],
        timeout=config['socket_timeout'],
        zpl_code=fmt_zpl_code
    )


if __name__ == '__main__':
    print(f"{CliColors.HEADER}{config['app_title']}{CliColors.ENDC}", "\n")

    main()
