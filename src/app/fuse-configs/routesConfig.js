import React from 'react';
import {Redirect} from 'react-router-dom';
import {FuseUtils} from '@fuse/index';
import {ExampleConfig} from 'app/main/example/ExampleConfig';
import {PagesConfig} from 'app/main/Pages/PagesConfig';

const routeConfigs = [
    ExampleConfig,
    ...PagesConfig
];

 const routes = [
    ...FuseUtils.generateRoutesFromConfigs(routeConfigs),
    {
        path     : '/',
        component: () => <Redirect to="/app/pages/dashboards"/>
    }
];

 export default routes;
