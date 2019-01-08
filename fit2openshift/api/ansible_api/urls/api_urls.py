# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals

from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .. import api


app_name = "ansible_api"
router = DefaultRouter()

router.register(r'projects', api.ProjectViewSet, 'project')
router.register(r'inventory/hosts', api.HostViewSet, 'host')
router.register(r'inventory/groups', api.GroupViewSet, 'group')
router.register(r'modules', api.AnsibleModuleViewSet, 'ansible-module')

project_router = routers.NestedDefaultRouter(router, r'projects', lookup='project')
<<<<<<< HEAD
project_router.register(r'inventory_data/hosts', api.ProjectHostViewSet, 'project-host')
project_router.register(r'inventory_data/groups', api.ProjectGroupViewSet, 'project-group')
=======
project_router.register(r'inventory/hosts', api.ProjectHostViewSet, 'project-host')
project_router.register(r'inventory/groups', api.ProjectGroupViewSet, 'project-group')
>>>>>>> 9c76263301cfc6cf73a3338535563cc4b44211ce
project_router.register(r'adhoc/executions', api.AdHocExecutionViewSet, 'project-adhoc-execution')
project_router.register(r'adhoc', api.AdHocViewSet, 'project-adhoc')
project_router.register(r'roles', api.ProjectRoleViewSet, 'project-role')
project_router.register(r'playbooks/executions', api.PlaybookExecutionViewSet, 'project-playbook-execution')
project_router.register(r'playbooks', api.ProjectPlaybookViewSet, 'project-playbook')


urlpatterns = [
    path('im/playbooks/', api.IMPlaybookApi.as_view(), name='im-playbook-api'),
    path('im/adhoc/', api.IMAdHocApi.as_view(), name='im-adhoc-api'),
<<<<<<< HEAD
    path('projects/<slug:project_name>/inventory_data/', api.ProjectInventoryApi.as_view(), name='project-inventory_data'),
=======
    path('projects/<slug:project_name>/inventory/', api.ProjectInventoryApi.as_view(), name='project-inventory'),
>>>>>>> 9c76263301cfc6cf73a3338535563cc4b44211ce
]

urlpatterns += router.urls + project_router.urls
