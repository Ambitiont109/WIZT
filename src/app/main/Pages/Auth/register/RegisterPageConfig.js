import {FuseLoadable} from '@fuse';
import {authRoles} from 'app/auth';
export const RegisterPageConfig = {
    settings: {
        layout: {
            style : 'layout1',
            config: {
                navbar : {
                    display : false, // ture/false
                    folded  : true,
                    position: 'left'
                },
                toolbar: {
                    display : false,
                    style   : 'fixed',
                    position: 'below'
                },
                footer : {
                    display : false, 
                    style   : 'fixed',
                    position: 'below'
                },
                mode   : 'fullwidth',
                rightSidePanel: {
                    display: false
                }
            }
        },
        customScrollbars: false,
    },
    //auth    : authRoles.onlyGuest,
    routes  : [
        {
            path     : '/app/pages/auth/register',
            component: FuseLoadable({
                loader: () => import('./RegisterPage')
            })
        }
    ]
};
