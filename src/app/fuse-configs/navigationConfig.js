const navigationConfig = [
    {
        'id'      : 'applications',
        'title'   : 'Applications',
        'type'    : 'group',
        'icon'    : 'apps',
        'children': [
            {
                'id'   : 'dashboard',
                'title': 'Dashboard',
                'type' : 'item',
                'icon' : 'dashboard',
                'url'  : '/app/pages/dashboards'
            },
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
                'id'   : 'transactions',
                'title': 'Transactions',
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
            {
                'id'   : 'settings',
                'title': 'Settings',
                'type' : 'item',
                'icon' : 'show_chart',
                'url'  : '/app/pages/subscribes'
            },
        ]
    }
];

export default navigationConfig;

