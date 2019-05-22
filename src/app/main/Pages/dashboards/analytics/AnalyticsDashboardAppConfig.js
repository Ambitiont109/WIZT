import {FuseLoadable} from '@fuse';
import {authRoles} from 'app/auth';

export const AnalyticsDashboardAppConfig = {
    settings: {
        layout: {
            config: {
                footer:{
                    display: false,
                }
            }
        }
    },
    // auth    : authRoles.onlyGuest,
    routes  : [
        {
            path     : '/app/pages/dashboards',
            component: FuseLoadable({
                loader: () => import('./AnalyticsDashboardApp')
            })
        }
    ]
};
