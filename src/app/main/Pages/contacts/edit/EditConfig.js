import Edit from './Edit';

export const EditConfig = {
    settings: {
        layout: {
            style : 'layout1',
            config: {
                navbar : {
                    display : true, // ture/false
                    folded  : true,
                    position: 'left'
                },
            }
        }
    },
    routes  : [
        {
            path     : '/app/pages/users/edit',
            component: Edit
        }
    ]
};