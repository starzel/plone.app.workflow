class Dummy:
    '''General purpose dummy object'''

    def __init__(self, **kw):
        self.__dict__.update(kw)


class DummyContent(Dummy):
    """Dummy DynamicType object"""

    def getPortalTypeName(self):
        return getattr(self, 'portal_type')


class DummyWorkflowTool(object):
    """A dummy workflow tool for testing adaptation based workflow"""

    def __init__(self, id='portal_workflow'):
        self._chains_by_type = {}

    def setChainForPortalTypes(self, types, chain):
        for ptype in types:
            self._chains_by_type[ptype] = chain

    def getDefaultChainFor(self, context):
        return ('Default Workflow',)
