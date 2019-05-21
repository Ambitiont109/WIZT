import Setting from './Setting';

export const SettingConfig = {
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
            path     : '/setting',
            component: Setting
        }
    ]
};

