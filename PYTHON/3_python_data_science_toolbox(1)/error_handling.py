#%%
# use try...except
# print out error as 
def sqrt(x):
    """Returns the square root of a number."""
    try:
        return x ** 0.5
    except TypeError:
        print('x must be an int or float')

sqrt('hello')
# %%
# put condition of x > 0
def sqrt(x):
    """Returns the square root of a number."""
    if x < 0:
        raise ValueError('x must be non-negative')
    try:
        return x ** 0.5
    except TypeError:
        prinnt('x must be an int or float')

sqrt(-2)
# %%
# add error sign to shout_echo function:
# add raise for value of echo > 0
def shout_echo(word1, echo = 1):
    """Concatenate echo copies of word1 and !!!."""
    # Initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ''
    # Add try-except
    if echo < 0:
        raise ValueError("echo must equal or greater than 0")
    try:
        echo_word = word1 * echo
        shout_words = echo_word + "!!!"

    except TypeError:
        print("word1 must be a string and echo must be an int")
    return shout_words

shout_echo("tuandeptrai",5)

# %%
