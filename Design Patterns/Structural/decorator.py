from functools import wraps


def make_blink(function):
    """Defines the decorator"""

    # This makes the decorator transparent in terms of its name and docs
    @wraps(function)
    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


@make_blink
def hello_world():
    """Original function!"""

    return "Hello, World!"


# Check the result of decorating

print(hello_world())
