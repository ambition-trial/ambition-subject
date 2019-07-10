# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages
from os.path import join, abspath, dirname, normpath

with open(join(dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(join(dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()

tests_require = ["edc_test_utils"]
with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    for line in f:
        tests_require.append(line.strip())

# allow setup.py to be run from any path
os.chdir(normpath(join(abspath(__file__), os.pardir)))

setup(
    name='ambition-subject',
    version=VERSION,
    author=u'Erik van Widenfelt',
    author_email='ew2789@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/ambition-trial/ambition-subject',
    license='GPL license, see LICENSE',
    description='Subject/Participant models for ambition/edc.',
    long_description=README,
    zip_safe=False,
    keywords='django ambition',
    install_requires=[
        'ambition_permissions',
        'ambition-rando',
        'ambition-prn',
        'ambition-ae',
        'ambition-labs',
        'ambition-lists',
        'ambition-metadata-rules',
        'ambition-reference',
        'ambition-sites',
        'ambition-screening',
        'ambition_form_validators',
        'ambition-visit-schedule',
        'django-collect-offline',
        'django-collect-offline-files',
        'edc-action-item',
        'edc-data-manager',
        'edc-appointment',
        'edc-consent',
        'edc-form-describer',
        'edc-form-label',
        'edc_model_admin',
        'edc_notification',
        'edc-offstudy',
        'edc-reportable',
        'edc-subject-dashboard',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires=">=3.7",
    tests_require=tests_require,
    test_suite='runtests.main',
)
