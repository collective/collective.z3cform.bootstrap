from z3c.form.form import Form

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class ModalForm(Form):

    template = ViewPageTemplateFile('templates/modal.pt')
