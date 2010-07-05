"""
Do a Python test on the app.

:Test-Layer: python
"""
#!/home/jelle/projects_active/bioport/virtualenv_python2.4/bin/python

import unittest
import sys
import os

sys.path.append('..')
sys.path.append('../..')
from bioport.admin import Sources, Source, Edit
from bioport.app import Bioport
from zope.publisher.browser import TestRequest
import bioport_repository


class SimpleSampleTest(unittest.TestCase):
    "Test the Sample application"

    def setUp(self):
        grokapp = Bioport()
        
        admin = grokapp['admin']
#        admin.SVN_REPOSITORY = None-
#        admin.SVN_REPOSITORY_LOCAL_COPY = None
        admin.DB_CONNECTION = 'mysql://root@localhost/bioport_test'
        self.app = grokapp
        self.admin = admin
        self.repo = repo = self.admin.repository(user=None)
        self.repo.db.metadata.drop_all()
        repo.db.metadata.create_all()
        url = os.path.join(os.path.dirname(bioport_repository.__file__), 
                         'tests', 'data','knaw', 'list.xml')
        src = bioport_repository.source.Source(id='knaw', url=url) 
        repo.add_source(src)
        
    def tearDown(self):
        self.repo.db.metadata.drop_all()
        
    def test_sources(self):
        request = TestRequest()
        sources = Sources(self.admin, request)
        source = Source(self.admin, request)
        knaw_source = self.repo.get_source('knaw')
        source.update(source_id='knaw')
        sources.update(action='update_source', source_id='knaw')
    
    def test_persoon(self):
        request = TestRequest()
        
    def test_edit(self):
        request = TestRequest()
        edit = Edit(self.admin, request)
        edit.reset_database
        

