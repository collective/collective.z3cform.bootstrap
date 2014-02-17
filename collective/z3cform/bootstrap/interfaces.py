from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from plone.app.z3cform.interfaces import IPloneFormLayer

class IBootstrapLayer(IDefaultBrowserLayer, IPloneFormLayer):
    """Request marker interface to enable bootstrap widgets and templates"""


class IBootstrapObjectMarker(Interface):
    """Marker interface for objects that should set IBootstrapLayer on the
    request when traversed.

    This currently only works together with a __before_publishing_traverse__
    handler on the object."""
