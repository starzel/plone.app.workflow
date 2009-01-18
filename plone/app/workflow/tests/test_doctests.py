from unittest import TestSuite
from zope.testing.doctestunit import DocTestSuite

from plone.app.workflow.tests.base import WorkflowFunctionalTestCase

def test_suite():
    suites = (
        DocTestSuite('plone.app.workflow.workflowchain'),
        )

    return TestSuite(suites)
