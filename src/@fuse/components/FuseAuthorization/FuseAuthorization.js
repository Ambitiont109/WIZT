import React, {Component} from 'react';
import {matchRoutes} from 'react-router-config';
import {withRouter} from 'react-router-dom';
import {connect} from 'react-redux';
import AppContext from 'app/AppContext';

class FuseAuthorization extends Component {

    constructor(props, context)
    {
        super(props);
        const {routes} = context;
        this.state = {
            login:false,
            accessGranted: true,
        };
    }

    componentDidMount()
    {
        this.redirectRoute(this.props);
    }

    componentDidUpdate()
    {
        this.redirectRoute(this.props);
    }

    static getDerivedStateFromProps(props, state)
    {
        const {location, user, login} = props;
        return {
            login:login.success,
        };
    }

    shouldComponentUpdate(nextProps, nextState)
    {
        return nextState.login !== this.state.login;
    }

    redirectRoute(props)
    {
        const {location, user, history, login} = props;
        const {pathname, state} = location;
        /*
        User is guest
        Redirect to Login Page
        */
        if ( login.success === false )
        {
            history.push({
                pathname: '/app/pages/auth/login',
                state   : {redirectUrl: pathname}
            });
        }
        /*
        User is member
        User must be on unAuthorized page or just logged in
        Redirect to dashboard or redirectUrl
        */
        else
        {
            const redirectUrl =  '/';
            history.push({
                pathname: redirectUrl
            });
        }
    }

    render()
    {
        const {children} = this.props;
        const {accessGranted} = this.state;
        return accessGranted ? <React.Fragment>{children}</React.Fragment> : null;
    }
}

function mapStateToProps({fuse, auth})
{
    return {
        user: auth.user,
        login: auth.login
    }
}

FuseAuthorization.contextType = AppContext;

export default withRouter(connect(mapStateToProps)(FuseAuthorization));
