# TODO be more verbose in explanation of can/can't reject null hypotheses
# TODO add error messages for non-numerical entries, looping back to beginning
# of function for re-entry
# TODO add entries for null and alt hypothesis to later write out what can/can't
# be rejected. This makes the program more explanatory.


def ptest():

    alpha = input('Input your desired alpha or level of significance:')
    pvalue = input('Input your p-value:')
    if pvalue > alpha:
        print('P-value is greater than your Alpha value indicating the null '
              'hypothesis can be rejected')
    elif pvalue < alpha:
        print('P-value is less than your Alpha value indicating high confidence'
              ' and that the null hypothesis cant be rejected')
    elif pvalue == alpha:
        print('The level of significance and p-value are equal. This implies '
              'an ambiguous statistical result.')


print('Always publish your P-value with any paper, any ambiguity can be '
      'critiqued and considered.')
# states that print line for consideration each time its used

ptest()
# runs the function
