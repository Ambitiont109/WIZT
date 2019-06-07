import React, {Component} from 'react';
import {withStyles} from '@material-ui/core';
import {FusePageSimple} from '@fuse';
import {bindActionCreators} from 'redux';
import {withRouter} from 'react-router-dom';
import {connect} from 'react-redux';
import withReducer from 'app/store/withReducer';
import _ from '@lodash';
import FriendsList from './FriendsList';
import EditDialog from './EditDialog';
import * as Actions from './store/actions';
import reducer from './store/reducers';

const styles = theme => ({
    addButton: {
        position: 'absolute',
        right   : 12,
        bottom  : 12,
        zIndex  : 99
    }
});

class FriendsApp extends Component {

    componentDidMount()
    {
        var item_id = localStorage.getItem('item_id')
        this.props.getContacts(item_id);
        this.props.getUserData();
    }

    componentDidUpdate(prevProps, prevState)
    {
        if ( !_.isEqual(this.props.location, prevProps.location) )
        {
            this.props.getContacts(this.props.match.params);
        }
    }

    render()
    {
        // const {classes, openNewContactDialog} = this.props;

        return (
            <React.Fragment>
                <FusePageSimple
                    classes={{
                        contentCardWrapper: "p-16 sm:p-24 pb-80",
                        leftSidebar       : "w-256 border-0",
                        header            : "min-h-72 h-72 sm:h-136 sm:min-h-136"
                    }}
                    content={
                        <FriendsList/>
                    }
                    sidebarInner
                    onRef={instance => {
                        this.pageLayout = instance;
                    }}
                    innerScroll
                />
                <EditDialog/>
            </React.Fragment>
        )
    };
}

function mapDispatchToProps(dispatch)
{
    return bindActionCreators({
        getContacts         : Actions.getContacts,
        getUserData         : Actions.getUserData,
        openNewContactDialog: Actions.openNewContactDialog
    }, dispatch);
}

function mapStateToProps({friendsApp})
{
    return {
        contacts          : friendsApp.contacts.entities,
        selectedContactIds: friendsApp.contacts.selectedContactIds,
        searchText        : friendsApp.contacts.searchText,
        user              : friendsApp.user
    }
}

export default withReducer('friendsApp', reducer)(withStyles(styles, {withTheme: true})(withRouter(connect(mapStateToProps, mapDispatchToProps)(FriendsApp))));
