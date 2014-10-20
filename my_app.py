from module_one import supporting_file

supporting_file.my_supporting_function()

# Import just the function directly
from module_one.supporting_file import my_supporting_function

# Can you import from a folder without __init__.py?
from folder import random_script

# Add an empty file in the folder 'folder' called __init__.py to continue
# On the terminal this looks like:
# touch folder/__init__.py

from module_two.module_three import sub_module_file
sub_module_file.sub_module_function()

# Can you figure out what's going on here?
from module_one import my_first_function
my_first_function()

# Can you make this work?
# Hint: Look at module_two/__init__.py
# The imports cascade up!
from module_two import my_other_function

my_other_function()
