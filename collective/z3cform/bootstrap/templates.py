from os.path import join, dirname

from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile

from z3c.form.interfaces import ISubForm

from plone.app.z3cform.templates import RenderWidget as RenderWidgetBase
from plone.z3cform.templates import FormTemplateFactory

try:
    from collective.z3cform.datagridfield.datagridfield import DataGridFieldObjectSubForm
    HAS_DATAGRIDFIELD = True
except ImportError:
    HAS_DATAGRIDFIELD = False

from collective.z3cform.bootstrap.interfaces import IBootstrapLayer

# This is needed for the factories below, because the classes are instantiated
# in a different context. So the full path to the template needs to be given.
template_path = lambda p: join(dirname(__file__), 'templates', p)

class RenderWidget(RenderWidgetBase):

    template = ViewPageTemplateFile('templates/widget.pt')
    subform_template = ViewPageTemplateFile('templates/subform_widget.pt')

    def subform(self):
        """ Test if this widget is part of a form that provides ISubForm."""
        form = hasattr(self.context, 'form') and self.context.form

        if not form:
            return False

        if HAS_DATAGRIDFIELD:
            # don't use the subform template for datagridfield subforms
            if isinstance(form, DataGridFieldObjectSubForm):
                return False

        return ISubForm.providedBy(form)

    # RenderWidgetBase derives from ViewMixinForTemplates which overrides __call__
    # to not call render. So we have to override __call__ directly instead of render.
    def __call__(self):

        if self.subform():
            return self.subform_template()
        else:
            return self.template()


subform_factory = FormTemplateFactory(
    template_path('subform.pt'),
    form=ISubForm,
    request=IBootstrapLayer,
    )
