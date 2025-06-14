"""
This type stub file was generated by pyright.
"""

from functools import cache

"""
The main DebugToolbar class that loads and renders the Toolbar.
"""
class DebugToolbar:
    _created = ...
    def __init__(self, request, get_response) -> None:
        ...
    
    @property
    def panels(self): # -> list[Panel]:
        """
        Get a list of all available panels.
        """
        ...
    
    @property
    def enabled_panels(self): # -> list[Panel]:
        """
        Get a list of panels enabled for the current request.
        """
        ...
    
    @property
    def csp_nonce(self): # -> Any | None:
        """
        Look up the Content Security Policy nonce if there is one.

        This is built specifically for django-csp, which may not always
        have a nonce associated with the request.
        """
        ...
    
    def get_panel_by_id(self, panel_id): # -> Panel:
        """
        Get the panel with the given id, which is the class name by default.
        """
        ...
    
    def render_toolbar(self): # -> SafeString:
        """
        Renders the overall Toolbar with panels inside.
        """
        ...
    
    def should_render_panels(self): # -> Literal[False]:
        """Determine whether the panels should be rendered during the request

        If False, the panels will be loaded via Ajax.
        """
        ...
    
    _store = ...
    def store(self): # -> None:
        ...
    
    @classmethod
    def fetch(cls, store_id): # -> None:
        ...
    
    _panel_classes = ...
    @classmethod
    def get_panel_classes(cls): # -> list[Any]:
        ...
    
    _urlpatterns = ...
    @classmethod
    def get_urls(cls): # -> list[URLPattern] | Any:
        ...
    
    @classmethod
    def is_toolbar_request(cls, request): # -> bool | list[str]:
        """
        Determine if the request is for a DebugToolbar view.
        """
        ...
    
    @staticmethod
    @cache
    def get_observe_request(): # -> Any:
        ...
    


def observe_request(request): # -> Literal[True]:
    """
    Determine whether to update the toolbar from a client side request.
    """
    ...

def debug_toolbar_urls(prefix=...): # -> list[Any] | list[URLResolver]:
    """
    Return a URL pattern for serving toolbar in debug mode.

    from django.conf import settings
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        # ... the rest of your URLconf goes here ...
    ] + debug_toolbar_urls()
    """
    ...

