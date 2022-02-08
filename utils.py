# import modules
import time

# save variables seperately, to ensure no variables are used externally.
class module_data:
    tests = 0

# a function that tests whether two values are equal, returning a customizable log with a toggleable exception.
def test(value, expected, show_value=False, raise_exception=False, log=True):
    module_data.tests += 1 # increment the amount of tests done by 1
    if value == expected: # the value is expected
        if not show_value: # if it doesn't have to show the value
            a = f'🗸 Test {str(module_data.tests)} Passed.'
        else: # if it has to show the value
            a = f'🗸 Test {str(module_data.tests)} Passed with value {str(value)} as expected.'
    else: # the value is not expected
        if not show_value: # if it doesn't have to show the value
            a = f'✘ Test {str(module_data.tests)} Failed.'
        else: # if it has to show the value
            a = f'✘ Test {str(module_data.tests)} Failed with value {str(value)} instead of {str(expected)}.'
        if raise_exception: # if an exception should be raised
            raise ValueError(a)
    if log: # if a log should be displayed
        print(a)
    return value == expected # return whether the test passed

# two functions that count the time elapsed between the them
class timing: # create a seperate class for timing
    t = time.time() # initialize t
    def start(): # when the timer starts
        timing.t = time.time() # save the current time
    def stop(log=True, digits=2): # when the timer stops
        if log: # if a log should be displayed
            print(f"⏱  {round(time.time() - timing.t, digits)} seconds passed.") # print the elapsed time rounded to .00 seconds
        return time.time() - timing.t # return the elapsed time