from zope.interface import alsoProvides

from collective.z3cform.bootstrap.interfaces import IBootstrapLayer


def set_bootstrap_layer(request):
    """Set the IBootstrapLayer on the request. Useful if you don't want to
    enable the bootstrap layer for your whole site."""
    alsoProvides(request, IBootstrapLayer)


def before_traversal_event_handler(obj, event):
    set_bootstrap_layer(event.request)
