import React from 'react';
import {Redirect} from 'react-router-dom';
import {FuseLoadable} from '@fuse';
import {authRoles} from 'app/auth';

export const ContactsAppConfig = {
    settings: {
        layout: {
            config: {
                footer:{
                    display: false,
                }
            }
        }
    },
    // auth    : authRoles.admin,
    routes  : [
        {
            path     : '/app/pages/users/:id',
            component: FuseLoadable({
                loader: () => import('./ContactsApp')
            })
        },
        {
            path     : '/app/contacts',
            component: () => <Redirect to="/app/pages/users/all"/>
        }
    ]
};
