from z3c.form.error import ErrorViewTemplateFactory

from collective.z3cform.bootstrap.templates import template_path

# Create the bootstrap error view template
StandardErrorViewTemplate = ErrorViewTemplateFactory(
    template_path('error.pt'),
    'text/html',
    )
