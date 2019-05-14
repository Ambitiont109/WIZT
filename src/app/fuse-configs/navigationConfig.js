const navigationConfig = [
    {
        'id'      : 'applications',
        'title'   : 'Applications',
        'type'    : 'group',
        'icon'    : 'apps',
        'children': [
            // {
            //     'id'   : 'example-component',
            //     'title': 'Example',
            //     'type' : 'item',
            //     'icon' : 'whatshot',
            //     'url'  : '/example'
            // },
            {
                'id'   : 'dashboard',
                'title': 'Dashboard',
                'type' : 'item',
                'icon' : 'dashboard',
                'url'  : '/app/pages/dashboards'
            },
            // {
            //     'id'   : 'users',
            //     'title': 'Users',
            //     'type' : 'item',
            //     'icon' : 'people',
            //     'url'  : '/app/pages/users'
            // },
            {
                id: "users",
                title: "Users",
                type: "item",
                icon: "people",
                url: "/app/pages/users/all"
            },
            {
                'id'   : 'labels',
                'title': 'Labels',
                'type' : 'item',
                'icon' : 'label',
                'url'  : '/app/pages/labels'
            },
            {
                'id'   : 'subscribes',
                'title': 'Subscribes',
                'type' : 'item',
                'icon' : 'payment',
                'url'  : '/app/pages/subscribes'
            },
            {
                'id'   : 'plans',
                'title': 'Plans',
                'type' : 'item',
                'icon' : 'show_chart',
                'url'  : '/app/pages/subscribes'
            },
        ]
    }
];

export default navigationConfig;

