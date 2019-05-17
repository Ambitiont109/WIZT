import React from 'react';
import {Redirect} from 'react-router-dom';
import {FuseLoadable} from '@fuse';

export const TransactionAppConfig = {
    settings: {
        layout: {
            config: {
                footer:{
                    display: false
                }
            }
        }
    },
    routes  : [
        {
            path     : '/app/pages/transaction',
            component: FuseLoadable({
                loader: () => import('./ContactsApp')
            })
        },
        {
            path     : '/apps/contacts',
            component: () => <Redirect to="/app/pages/transaction"/>
        }
    ]
};
