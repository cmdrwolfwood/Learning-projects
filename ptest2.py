# TODO make the alpha 0.05 a changeable variable by user
# TODO give a 'close to' range for alpha variable that implies ambiguity in
# final determination
# TODO be more verbose in explanation of can/can't reject null hypotheses
# TODO add elif statement for input that isn't capable of being made a float
# TODO add statements for if the input value equals the alpha value exactly


def pvalue():

    alpha = input('Input your alpha value:')
    # this provides an input screen to enter p-values determined statistically
    # from research data
    alpha = float(alpha)
    # this turns the input into a float value for comparison
    if alpha > 0.05:
        print('P-value is greater than 0.05 indicating the null hypothesis can '
              'be rejected')
    # these lines compare the entered input against the 95% confidence value
    # thats industry standard
    elif alpha < 0.05:
        print('P-value is less than 0.05 indicating high confidence and that '
              'the null hypothesis cant be rejected')


print('Always publish your P-value with any paper, any ambiguity can be '
      'critiqued and considered.')
# states that print line for consideration each time its used

pvalue()
# runs the function
