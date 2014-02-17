from zope.component import adapts

from z3c.form.button import ButtonAction as ButtonActionBase
from z3c.form.interfaces import IButton

from collective.z3cform.bootstrap.interfaces import IBootstrapLayer

class ButtonAction(ButtonActionBase):
    adapts(IBootstrapLayer, IButton)

    def update(self):
        super(ButtonAction, self).update()
        self.addClass('btn btn-primary')
