class Handler:
    """Abstract Handler"""

    def __init__(self, successor):
        # define who is the next handler
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)  # if handled, stop here

        # Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass")


class ConcreteHandler1(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print("request {} handled in handler 1".format(request))
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print("End of chain, no handler for {}".format(request))
        return True


class Client:
    """Class using handlers"""

    def __init__(self):
        # Create handlers and use them in a sequence you want
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


# Create a client
client_object = Client()
# Create requests
requests = [1, 2, 4, 5, 8, 9, 12, 45]
client_object.delegate(requests)
