# Let's learn to create our own modules and packages

# Now, we understand how to install external packages - let's make our own
# Modules are just .py scripts that you call in another .py script
# Oackages are a collectio of modules.
# Let's create some examples.

from my_module import my_func

my_func()

from MyMainPackage import some_main_script
from MyMainPackage.MySubPackage import some_sub_script

some_main_script.main_script_func()

some_sub_script.sub_script_func()