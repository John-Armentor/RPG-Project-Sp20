#Author:    John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 03 04
#Modified:      2020 03 04
#Course:    CSC425 - Software Engineering II
#Prof:      Dr. A. Louise Perkins

# A class that stores functions inside of it and allows the functions
# to be executed else where.  Serves as a way to put functions
# into objects

class FunctionPackager():

    def __init__(self, function_name, function_arguments):
        """Initialize attributes for a packaged function."""
        self.function_name = function_name
        self.function_arguments = function_arguments
        
    def execute_function(self):
        """executes the function."""
        return self.function_name(*self.function_arguments)