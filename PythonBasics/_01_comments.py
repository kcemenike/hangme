# Comments
# This is a single line comment

'''
This is a multi line
comment. Actually called a documentation string (docstring for short)
'''

""" This is also a
multi line 
comment
"""

# Quiz - what is the difference between the single line and the multi-line comment?

# A multi-line comment IS NOT executed
# A doc string is executed by the interpreter

# -------------------------------- #
# EXAMPLE #


def docStringFunction():
    '''
    This is a multi-line comment
    that is 'saved' by the Python interpreter in a special variable
    '''
    # This is ignored by the intrepreter
    pass


print(docStringFunction.__doc__)
