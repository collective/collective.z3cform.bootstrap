from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.z3cform.bootstrap',
      version=version,
      description="Twitter Bootstrap widgets and templates for z3c.form",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Gaudenz Steinlin',
      author_email='gaudenz.steinlin@cirrax.com',
      url="'https://github.com/collective/collective.z3cform.bootstrap'",
      license='GPL v3+',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.z3cform'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.z3cform',
      ],
      extras_require={
        'datetime': [
            'collective.z3cform.datetimewidget',
            ],
        },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
