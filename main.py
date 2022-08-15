#!/usr/bin/env python
"""
zebra-password-changer-cli-py

Usage: python main.py <IP_ADDRESS> <PASSWORD (4 digit, only numbers)>
"""
import ipaddress
import socket
import sys

config = {
    'script_title': '== Zebra password changer ==',
    'printer_port': 9100,
    'socket_timeout': 3
}


class CliColors:
    """Cli colors
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def exit_with_msg(msg):
    """Exit with message

    Args:
        msg (str): message
    """
    print(f"{CliColors.FAIL}[ERROR]{CliColors.ENDC} {msg}")
    sys.exit(0)


def socket_request(ip_address, password):
    """Socket request

    Args:
        ip_address (str): IP address
        password (str): Password
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(config['socket_timeout'])
        try:
            sock.connect((ip_address, config['printer_port']))
            sock.send(f"^XA^KP{password}^JUS^XZ".encode())
            print(f"\r{CliColors.OKGREEN}[OK]{CliColors.ENDC} {CliColors.OKBLUE}{ip_address}{CliColors.ENDC} : password has been changed.")
        except TimeoutError:
            exit_with_msg(f"Request timed out while connecting to remote host {ip_address}")
        finally:
            sock.close()


def cli_help():
    print(f"{CliColors.OKGREEN}Usage:{CliColors.ENDC} python main.py {CliColors.OKBLUE}<IP_ADDRESS>{CliColors.ENDC} {CliColors.OKBLUE}<PASSWORD (4 digit, only numbers)>{CliColors.ENDC}")


def check_arguments(argument_list):
    """Check arguments

    Args:
        argument_list (list): arguments
    """

    # No any argument -> error & exit
    if not argument_list:
        print("There is no any argument!\n")
        cli_help()
        exit(0)

    # Argument is "help" -> show help & exit
    help_arg_list = ["help", "--help", "-help", "/help"]
    if argument_list[0] in help_arg_list:
        print("zebra-zpl-send-cli-py\n")
        cli_help()
        sys.exit(0)

    # Not have 2 argument -> error & exit
    if len(argument_list) != 2:
        print("There is only one argument!\n")
        cli_help()
        sys.exit(0)


def validate_ip_address(ip_address, password):
    # Validate ip address
    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        print(f"{CliColors.FAIL}[ERROR]{CliColors.ENDC} IP adress is invalid.")
        # We must validate password here too, if ip and password both are invalid. Because of the exception.
        validate_password(password)
        sys.exit(0)


def validate_password(input_password):
    """Validate password

    Args:
        input_password (str): password
    """
    if not input_password.isdigit() or len(input_password) != 4:
        exit_with_msg("Please enter a 4 digit number!")


def main():
    """ Main function
    """
    full_cmd_arguments = sys.argv           # Get full command-line arguments
    argument_list = full_cmd_arguments[1:]  # Keep all but the first
    check_arguments(argument_list)

    # Argument check is passed, lets continue

    input_ip_address = argument_list[0]
    input_password   = argument_list[1]

    validate_ip_address(input_ip_address, input_password)

    validate_password(input_password)

    # Ip address and password are valid
    # Send the password change request
    socket_request(input_ip_address, input_password)


if __name__ == '__main__':
    print(f"{CliColors.HEADER}{config['script_title']}{CliColors.ENDC}", "\n")

    main()
