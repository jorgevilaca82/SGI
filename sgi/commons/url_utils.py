from django.urls import include, path

LIST_OPERATION = 'list'
CREATE_OPERATION = 'create'
DETAIL_OPERATION = 'detail'
UPDATE_OPERATION = 'update'
DELETE_OPERATION = 'delete'


def crud(base_path, views_module, *args, **kwargs):

    url_prefix = kwargs.get('url_prefix', base_path)

    def url_name_for(operation):
        return '{0}-{1}'.format(url_prefix, operation)

    default_only_operations = [
        LIST_OPERATION,
        CREATE_OPERATION,
        DETAIL_OPERATION,
        UPDATE_OPERATION,
        DELETE_OPERATION
    ]

    only = kwargs.get('only', default_only_operations)

    ops_dict = {
        LIST_OPERATION: path('',
                             views_module.ListView.as_view(),
                             name=url_name_for(LIST_OPERATION)),

        CREATE_OPERATION: path('create',
                               views_module.CreateView.as_view(),
                               name=url_name_for(CREATE_OPERATION)),

        DETAIL_OPERATION: path('<int:pk>/',
                               views_module.DetailView.as_view(),
                               name=url_name_for(DETAIL_OPERATION)),

        UPDATE_OPERATION: path('<int:pk>/edit',
                               views_module.UpdateView.as_view(),
                               name=url_name_for(UPDATE_OPERATION)),

        DELETE_OPERATION: path('<int:pk>/del',
                               views_module.DeleteView.as_view(),
                               name=url_name_for(DELETE_OPERATION)),
    }

    ops_list = [ops_dict[o] for o in only]

    paths = path(base_path + '/', include(ops_list))

    del(ops_dict)
    return paths
