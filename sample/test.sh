#!/bin/bash
#\033[0;32m - Sets the text color to green
#\033[0m - Resets the text color back to default
#The -e flag enables the interpretation of backslash escapes in echo
#To see the color, run the script in a terminal
echo -e "\033[0;32mHello Green World\033[0m"
echo -e "\033[0;35mHello Purple World\033[0m"
