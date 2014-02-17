from os.path import join, dirname

from z3c.form.interfaces import ISubForm

from plone.z3cform.templates import FormTemplateFactory

from collective.z3cform.bootstrap.interfaces import IBootstrapLayer

# This is needed for the factories below, because the classes are instantiated
# in a different context. So the full path to the template needs to be given.
template_path = lambda p: join(dirname(__file__), 'templates', p)

subform_factory = FormTemplateFactory(
    template_path('subform.pt'),
    form=ISubForm,
    request=IBootstrapLayer,
    )
