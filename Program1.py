"""
CSCI-UA.0002 Spring 2024
Assignment #9, Program 1
Your name here
"""
# This program implements a prototype of a messaging system
import datetime

# function:   valid_username
# input:      a username (string)
# processing: determines if the username supplied is valid.  for the purpose
#             of this program a valid username is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters or numbers)
#             (3) the last character must be a number
# output:     boolean (True if valid, False if invalid)


# function:   valid_password
# input:      a password (string)
# processing: determines if the password supplied is valid.  for the purpose
#             of this program a valid password is defined as follows:
#             (1) must be 6 characters or longer
#             (2) must not contain any numbers
#	            (3) at least one letter must be lower case and one upper case
# output:     boolean (True if valid, False if invalid)


# function:   username_exists
# input:      a username (string)
# processing: determines if the username exists in the file 'user_info.txt'
# output:     boolean (True if found, False if not found)


# function:   check_password
# input:      a username (string) and a password (string)
# processing: determines if the username / password combination
#             supplied matches one of the user accounts represented
#             in the 'user_info.txt' file
# output:     boolean (True if valid, False if invalid)


# function:   add_user
# input:      a username (string) and a password (string)
# processing: if the user being supplied is not already in the
#             'user_info.txt' file they should be added, along with
#             their password.
# output:     boolean (True if added successfully, False if not)


# function:   send_message
# input:      a sender (string), a recipient (string) and a message (string)
# processing: writes a new line into the specific messages file for the given user
#             with the following information:
#
#             sender|date_and_time|message\n
#
# output:     nothing


# function:   print_messages
# input:      a username (string)
# processing: prints all messages sent to the username in question.
# output:     no return value (simply prints the messages)


# function:   delete_messages
# input:      a username (string)
# processing: erases all data in the messages file for this user
# output:     no return value
