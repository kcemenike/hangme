# FUNCTIONS

# When you need to perform a group of actions repetitively, you need a function
# This is the beginning of automation
# So we can have a routine that is as such:
# I wake up in the morning and I:
#   Say a thank you prayer
#   Brush my teeth

# wake_up(time=morning):
#   if time==morning:
#       Say thank you prayer
#       Brush teeth
#   else:
#       do nothing


def wake_up(time="morning"):
    if time == "morning":  # == is the test for equality, = is the assignment operator
        print("Thank you!")
        print("Brush teeth")
    else:
        pass


# wake_up(time="morning")

# wake_up(time="afternoon")
