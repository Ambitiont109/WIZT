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
            // routes
        };
    }

    componentDidMount()
    {
        if (!this.state.accessGranted)
        {
            this.redirectRoute(this.props);
        }
    }

    componentDidUpdate()
    {
        console.log('DidUpdate')
        this.redirectRoute(this.props);
    }

    static getDerivedStateFromProps(props, state)
    {
        const {location, user, login} = props;
        console.log(login.success)
        // this.redirectPage(this.props);
        return {
            login:login.success,
            
        };
    }

    shouldComponentUpdate(nextProps, nextState)
    {
        console.log('shouldComponentUpdate')
        return nextState.login !== this.state.login;
    }

    redirectRoute(props)
    {
        console.log('this is redirectRoute')
        const {location, user, history, login} = props;
        console.log("login")
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
            const redirectUrl = state && state.redirectUrl ? state.redirectUrl : '/';
            console.log(redirectUrl)

            history.push({
                pathname: redirectUrl
            });
        }
    }

    render()
    {
        console.log('rendering')
        const {children} = this.props;
        const {accessGranted} = this.state;
        // console.info('Fuse Authorization rendered', accessGranted);
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
