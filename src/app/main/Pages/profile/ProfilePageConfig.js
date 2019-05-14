import {FuseLoadable} from '@fuse';

export const ProfilePageConfig = {
    settings: {
        layout: {
            style : 'layout1',
            config: {
                mode   : 'fullwidth',
                navbar : {
                    display : true,
                    folded  : false,
                    position: 'left'
                },
            }
        }
    },
    routes  : [
        {
            path     : '/app/pages/profile',
            component: FuseLoadable({
                loader: () => import('./ProfilePage')
            })
        }
    ]
};
