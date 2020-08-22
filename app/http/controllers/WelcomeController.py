"""Welcome The User To Masonite."""

from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller
from app.inertia.InertiaResponse import InertiaResponse


class WelcomeController(Controller):
    """Controller For Welcoming The User."""

    def show(self, view: View, request: Request):
        """Show the welcome page.

        Arguments:
            view {masonite.view.View} -- The Masonite view class.
            request {masonite.request.Request} -- The Masonite request class.

        Returns:
            masonite.view.View -- The Masonite view class.
        """
        return view.render('welcome')

    def inertia(self, view: InertiaResponse):
        return view.render('Index')

    def helloworld(self, view: InertiaResponse):
        return view.render('HelloWorld', {'first_name': 'Sam'})