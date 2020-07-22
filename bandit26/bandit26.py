USERNAME = 'bandit26'
PASSWORD = '5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z'

# this is the continuation from the last challenge, bandit25 -> bandit26

# make sure to make the terminal window as small as possible before logging in as bandit26
# this is to prevent the completion of 'more' program
# because 'more' depends on the screen size, if the screen is too small to contain the content of the 
# file, then more will not show everything immediately
# instead, it will wait for user interaction

# next, we can type 'v' to get into an editor while we are still in 'more'
# the editor is set in environment variable EDITOR or VISUAL
# reference: https://man7.org/linux/man-pages/man1/more.1.html

# NOTE: press 'esc' to change to command mode in 'vi'
# :set shell=/bin/bash to set the shell to /bin/bash
# :shell to get the shell

# after gaining access to the shell,
# there is a SUID program, bandit27-do, which we can use to read the password for bandit27
# ./bandit27-do cat /etc/bandit_pass/bandit27
password = '3ba3118a22e93127a4ed485be72ef5ea'
print(f'bandit27 password: {password}')