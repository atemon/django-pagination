def get_page(self):
    """
    A function which will be monkeypatched onto the request to get the current
    integer representing the current page.
    """

    try:
        self.page = int(self.GET['page']) or int(self.POST['page'])
    except (KeyError, ValueError, TypeError):
        self.page = 1

class PaginationMiddleware(object):
    """
    Inserts a variable representing the current page onto the request object if
    it exists in either **GET** or **POST** portions of the request.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        get_page(request)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_request(self, request):
        request.page = property(get_page)
