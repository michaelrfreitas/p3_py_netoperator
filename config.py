""" This module to create a config script importing devices module """

import os
import re
from pathlib import Path
from devices import ConfSwitchL3
from devices import ConfSwitchL2
from devices import ConfRouter


class ConfQuestionsSWL2(ConfSwitchL2):
    """ Class to provide the question for configuration Switch L2 devices """

    def __repr__(self):
        return f'''
        ---
        Hostname: {self.hostname}
        Username: {self.username}
        Password: {self.password}
        Manager VLAN ID: {self.manager_vlan}
        Manager IP address: {self.manager_ip}
        Manager Subnet Mask: {self.manager_mask}
        Primary VLAN ID: {self.primary_vlan}
        Default Gateway: {self.default_gateway}
        ---
        '''

    def printer_full(self, vendor):
        """
        Function to printer in screen full config for Switch L2
        """
        if vendor == '1':
            base_path_temp = Path('assets/templates/c_sw_cisco_l2.txt')
        else:
            base_path_temp = Path('assets/templates/c_sw_datacom_l2.txt')

        reading_file = open(base_path_temp, "r", encoding='UTF-8')

        find_conf = ("${hostname}", "${username}", "${password}",
                     "${manager_vlan}", "${manager_ip}", "${manager_mask}",
                     "${primary_vlan}", "${default_gateway}")
        repl_conf = (self.hostname, self.username, self.password,
                     self.manager_vlan, self.manager_ip,
                     self.manager_mask, self.primary_vlan,
                     self.default_gateway)

        for line in reading_file:
            for find, repl in zip(find_conf, repl_conf):
                line = line.replace(find, repl)
            print(line, end="")
        reading_file.close()

    def questions(self):
        """
        Function to provide questions regarding Switch L2
        """
        # Loop to keep code running while validate false
        while True:
            self.hostname = input('What is the hostname? (SW-HOST-01): ')
            if validate_text(self.hostname):
                break
        while True:
            self.username = input('What is the username? (local-admin): ')
            if validate_text(self.username):
                break
        while True:
            self.password = input(
                'What is the password? (Minimun 8 characteres): ')
            if validate_pwd(self.password):
                break
        while True:
            self.manager_vlan = input(
                'What is the manager VLAN ID? (1-4094): ')
            if validate_vlan(self.manager_vlan):
                break
        while True:
            self.manager_ip = input(
                'What is the manager IP address? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.manager_ip):
                break
        while True:
            self.manager_mask = input(
                'What is the manager subnet mask? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.manager_mask):
                break
        while True:
            self.primary_vlan = input(
                'What is the primary VLAN ID? (1-4094): ')
            if validate_vlan(self.primary_vlan):
                break
        while True:
            self.default_gateway = input(
                'What is the default gateway? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.default_gateway):
                break


class ConfQuestionsSWL3(ConfSwitchL3):
    """ Class to provide the question for configuration Switch L3 devices """

    def __repr__(self):
        return f'''
        ---
        Hostname: {self.hostname}
        Username: {self.username}
        Password: {self.password}
        Manager VLAN ID: {self.manager_vlan}
        Manager IP address: {self.manager_ip}
        Manager Subnet Mask: {self.manager_mask}
        Primary Interface VLAN ID: {self.primary_int_vlan}
        Primary Interface IP address: {self.primary_int_ip}
        Primary Interface Subnet Mask: {self.primary_int_mask}
        Default Gateway: {self.default_gateway}
        ---
        '''

    def printer_full(self, vendor):
        """
        Function to printer in screen full config for Switch L3
        """
        if vendor == '1':
            base_path_temp = Path('assets/templates/c_sw_cisco_l3.txt')
        else:
            base_path_temp = Path('assets/templates/c_sw_datacom_l3.txt')

        reading_file = open(base_path_temp, "r", encoding='UTF-8')

        find_conf = ("${hostname}", "${username}", "${password}",
                     "${manager_vlan}", "${manager_ip}", "${manager_mask}",
                     "${primary_int_vlan}", "${primary_int_ip}",
                     "${primary_int_mask}", "${default_gateway}")
        repl_conf = (self.hostname, self.username, self.password,
                     self.manager_vlan, self.manager_ip,
                     self.manager_mask, self.primary_int_vlan,
                     self.primary_int_ip, self.primary_int_mask,
                     self.default_gateway)

        for line in reading_file:
            for find, repl in zip(find_conf, repl_conf):
                line = line.replace(find, repl)
            print(line, end="")
        reading_file.close()

    def questions(self):
        """
        Function to provide questions regarding Switch L3
        """
        # Loop to keep code running while validate false
        while True:
            self.hostname = input('What is the hostname? (SW-HOST-01): ')
            if validate_text(self.hostname):
                break
        while True:
            self.username = input('What is the username? (local-admin): ')
            if validate_text(self.username):
                break
        while True:
            self.password = input(
                'What is the password? (Minimun 8 characteres): ')
            if validate_pwd(self.password):
                break
        while True:
            self.manager_vlan = input(
                'What is the manager VLAN ID? (1-4094): ')
            if validate_vlan(self.manager_vlan):
                break
        while True:
            self.manager_ip = input(
                'What is the manager IP address? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.manager_ip):
                break
        while True:
            self.manager_mask = input(
                'What is the manager subnet mask? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.manager_mask):
                break
        while True:
            self.primary_int_vlan = input(
                'What is the primary interface VLAN ID? (1-4094): ')
            if validate_vlan(self.primary_int_vlan):
                break
        while True:
            self.primary_int_ip = input(
                'What is the primary interface IP address? ' +
                '(XXX.XXX.XXX.XXX): ')
            if validate_ip(self.primary_int_ip):
                break
        while True:
            self.primary_int_mask = input(
                'What is the primary interface subnet mask? ' +
                '(XXX.XXX.XXX.XXX): ')
            if validate_ip(self.primary_int_mask):
                break
        while True:
            self.default_gateway = input(
                'What is the default gateway? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.default_gateway):
                break


class ConfQuestionsRouter(ConfRouter):
    """ Class to provide the question for configuration Router devices """

    def __repr__(self):
        return f'''
        ---
        Hostname: {self.hostname}
        Username: {self.username}
        Password: {self.password}
        IP Interface Inside: {self.interface_ip_inside}
        Mask Interface Inside: {self.interface_mask_inside}
        IP Interface Outside: {self.interface_ip_outside}
        Mask Interface Outside: {self.interface_mask_outside}
        Default IP: {self.default_ip}
        ---
        '''

    def printer_full(self, vendor):
        """
        Function to printer in screen full config for Router
        """
        if vendor == '1':
            base_path_temp = Path('assets/templates/c_rt_cisco.txt')
        else:
            base_path_temp = Path('assets/templates/c_rt_datacom.txt')

        reading_file = open(base_path_temp, "r", encoding='UTF-8')

        find_conf = ("${hostname}", "${username}", "${password}",
                     "${interface_ip_inside}", "${interface_mask_inside}",
                     "${interface_ip_outside}", "${interface_mask_outside}",
                     "${default_ip}")
        repl_conf = (self.hostname, self.username, self.password,
                     self.interface_ip_inside, self.interface_mask_inside,
                     self.interface_ip_outside, self.interface_mask_outside,
                     self.default_ip)

        for line in reading_file:
            for find, repl in zip(find_conf, repl_conf):
                line = line.replace(find, repl)
            print(line, end="")
        reading_file.close()

    def questions(self):
        """
        Function to provide questions regarding Router
        """
        # Loop to keep code running while validate false
        while True:
            self.hostname = input('What is the hostname? (RT-HOST-01): ')
            if validate_text(self.hostname):
                break
        while True:
            self.username = input('What is the username? (local-admin): ')
            if validate_text(self.username):
                break
        while True:
            self.password = input(
                'What is the password? (Minimun 8 characteres): ')
            if validate_pwd(self.password):
                break
        while True:
            self.interface_ip_inside = input(
                'What is the IP address for inside? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.interface_ip_inside):
                break
        while True:
            self.interface_mask_inside = input(
                'What is the subnet mask for inside? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.interface_mask_inside):
                break
        while True:
            self.interface_ip_outside = input(
                'What is the IP address for outside? ' +
                '(XXX.XXX.XXX.XXX): ')
            if validate_ip(self.interface_ip_outside):
                break
        while True:
            self.interface_mask_outside = input(
                'What is the subnet mask for outside? ' +
                '(XXX.XXX.XXX.XXX): ')
            if validate_ip(self.interface_mask_outside):
                break
        while True:
            self.default_ip = input(
                'What is the default IP routing? (XXX.XXX.XXX.XXX): ')
            if validate_ip(self.default_ip):
                break


def validate_vlan(answer):
    """
    Validate function to check the answer for VLANs
    """
    try:
        # Convert answer to integer
        num = int(answer)
        # Check if received the specific numbers
        if num < 1 or num > 4094:
            clear_terminal()
            print(
                f'''
            --------------- WARNING ---------------
            This VLAN {answer} is incorrect,
            please, be sure to type it correctly
            VLAN ID should be between 1 - 4094
            --------------- WARNING ---------------
            '''
            )
            return False
    except ValueError:
        # Check if it received a integer number if not receive a message
        clear_terminal()
        print(
            f'''
            --------------- WARNING ---------------
            This VLAN {answer} is incorrect,
            please, be sure to type it correctly
            VLAN ID should be between 1 - 4094
            --------------- WARNING ---------------
            '''
        )
        return False
    # Return true if didn't have error
    return True


def validate_ip(answer):
    """
    Validate function to check the answer for IPs
    """
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)"\
            "{3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    try:
        if not re.search(regex, answer):
            clear_terminal()
            raise ValueError(
                f'''
                --------------- WARNING ---------------
                This IP {answer} is incorrect,
                please, be sure to type it correctly
                --------------- WARNING ---------------
                '''
            )
    except ValueError as err:
        clear_terminal()
        print(f"{err}")
        return False
    return True


def validate_text(answer):
    """
    Validate function to check the answer for texts
    """
    try:
        if len(answer) < 5 or len(answer) > 20:
            raise ValueError(
                f'''
                --------------- WARNING ---------------
                This text {answer} is incorrect,
                please, be sure to type it correctly
                minimum 5 and maximum 20 characters
                --------------- WARNING ---------------
                '''
            )
    except ValueError as err:
        clear_terminal()
        print(f"{err}")
        return False
    return True


def validate_pwd(answer):
    """
    Validate function to check the answer for password
    """
    try:
        if len(answer) < 8:
            raise ValueError(
                f'''
                --------------- WARNING ---------------
                This password {answer} is incorrect,
                please, be sure to type it correctly
                minimum 8 characters
                --------------- WARNING ---------------
                '''
            )
    except ValueError as err:
        clear_terminal()
        print(f"{err}")
        return False
    return True


def clear_terminal():
    """
    Clear terminal with os.system
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')
