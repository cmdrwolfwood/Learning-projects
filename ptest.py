# TODO
# take in raw input of numbers
# set if statement of < or > than alpha value
# set alpha value as 1st input, then compare ptest value against it, THEN print
# whether the null hypothesis can be negated or can't be
import math

def pvalue():
    alpha = input('Input your alpha value:')
    # this provides an input screen to enter p-values determined statistically from research data
    alpha = float(alpha)
    # this turns the input into a float value for comparison on the next few lines
    if alpha > 0.05:
        print('P-value is greater than 0.05 indicating the null hypothesis can be rejected')
    # these lines compare the entered input against the 95% confidence value thats industry standard
    elif alpha < 0.05:
        print('P-value is less than 0.05 indicating high confidence and that the null hypothesis cant be rejected')


print(pvalue)
print('Always publish your P-value with any paper, any ambiguity can be critiqued and considered.')
#starting the program with pvalue, allowing input to be entered, then states that 2nd print line for consideration
#each time its published/used as a program

pvalue()