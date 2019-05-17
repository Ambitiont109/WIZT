import React, {Component} from 'react';
import {Avatar, Checkbox, Icon, IconButton, ListItemIcon, ListItemText, Menu, MenuItem, MenuList, Typography} from '@material-ui/core';
import {FuseUtils, FuseAnimate} from '@fuse';
import {connect} from 'react-redux';
import {withRouter} from 'react-router-dom';
import {bindActionCreators} from 'redux';
import ReactTable from "react-table";
import * as Actions from './store/actions';
import ChipsArray from './chips/ChipsArray';

class ContactsList extends Component {

    state = {
        selectedContactsMenu: null
    };

    getFilteredArray = (entities, searchText) => {
        const arr = Object.keys(entities).map((id) => entities[id]);
        if ( searchText.length === 0 )
        {
            return arr;
        }
        return FuseUtils.filterArrayByString(arr, searchText);
    };

    openSelectedContactMenu = (event) => {
        this.setState({selectedContactsMenu: event.currentTarget});
    };

    closeSelectedContactsMenu = () => {
        this.setState({selectedContactsMenu: null});
    };

    render()
    {
        const { contacts, user, searchText, selectedContactIds, selectAllContacts, deSelectAllContacts, toggleInSelectedContacts, openEditContactDialog, removeContacts, removeContact, toggleStarredContact, setContactsUnstarred, setContactsStarred} = this.props;
        const data = this.getFilteredArray(contacts, searchText);
        const {selectedContactsMenu} = this.state;

        if ( !data && data.length === 0 )
        {
            return (
                <div className="flex items-center justify-center h-full">
                    <Typography color="textSecondary" variant="h5">
                        There are no contacts!
                    </Typography>
                </div>
            );
        }

        return (
            <FuseAnimate animation="transition.slideUpIn" delay={300}>
                <ReactTable
                    className="-striped -highlight border-0"
                    getTrProps={(state, rowInfo, column) => {
                        return {
                            className: "cursor-pointer",
                            onClick  : (e, handleOriginal) => {
                                if ( rowInfo )
                                {
                                    openEditContactDialog(rowInfo.original);
                                }
                            }
                        }
                    }}
                    data={data}
                    columns={[
                        // {
                        //     Header   : () => (
                        //         <Checkbox
                        //             onClick={(event) => {
                        //                 event.stopPropagation();
                        //             }}
                        //             onChange={(event) => {
                        //                 event.target.checked ? selectAllContacts() : deSelectAllContacts();
                        //             }}
                        //             checked={selectedContactIds.length === Object.keys(contacts).length && selectedContactIds.length > 0}
                        //             indeterminate={selectedContactIds.length !== Object.keys(contacts).length && selectedContactIds.length > 0}
                        //         />
                        //     ),
                        //     accessor : "",
                        //     Cell     : row => {
                        //         return (<Checkbox
                        //                 onClick={(event) => {
                        //                     event.stopPropagation();
                        //                 }}
                        //                 checked={selectedContactIds.includes(row.value.id)}
                        //                 onChange={() => toggleInSelectedContacts(row.value.id)}
                        //             />
                        //         )
                        //     },
                        //     className: "justify-center",
                        //     sortable : false,
                        //     width    : 64
                        // },
                      
                        {
                            Header    : "No",
                            accessor  : "",
                            filterable: false,
                            Cell      : row => (
                                    <span>{row.index+1}</span>
                                ),
                            width      : 64,
                            className : "font-bold justify-center"
                        },
                        {
                            Header    : "Name",
                            accessor  : "name",
                            filterable: false,
                            width     : 250, 
                            className : "font-bold "
                        },
                        {
                            Header    : "User",
                            accessor  : "company",
                            filterable: false,
                            width     : 250, 
                        },
                        {
                            Header    : "Location",
                            accessor  : "jobTitle",
                            filterable: false
                        },
                        {
                            Header    : "Tags",
                            accessor  : "",
                            Cell      : row => (
                                <ChipsArray />
                            ),
                            filterable: false
                        },
                        // {
                        //     Header    : "Email",
                        //     accessor  : "email",
                        //     filterable: false
                        // },
                        // {
                        //     Header    : "Phone",
                        //     accessor  : "phone",
                        //     filterable: false
                        // },
                        // {
                        //     Header: "",
                        //     width : 128,
                        //     Cell  : row => (
                        //         <div className="flex items-center">
                        //             <IconButton
                        //                 onClick={(ev) => {
                        //                     ev.stopPropagation();
                        //                     toggleStarredContact(row.original.id)
                        //                 }}
                        //             >
                        //                 {user.starred && user.starred.includes(row.original.id) ? (
                        //                     <Icon>star</Icon>
                        //                 ) : (
                        //                     <Icon>star_border</Icon>
                        //                 )}
                        //             </IconButton>
                        //             <IconButton
                        //                 onClick={(ev) => {
                        //                     ev.stopPropagation();
                        //                     removeContact(row.original.id);
                        //                 }}
                        //             >
                        //                 <Icon>delete</Icon>
                        //             </IconButton>
                        //         </div>
                        //     )
                        // }
                    ]}
                    defaultPageSize={10}
                    noDataText="No contacts found"
                />
            </FuseAnimate>
        );
    }
}


function mapDispatchToProps(dispatch)
{
    return bindActionCreators({
        getContacts             : Actions.getContacts,
        getUserData             : Actions.getUserData,
        toggleInSelectedContacts: Actions.toggleInSelectedContacts,
        selectAllContacts       : Actions.selectAllContacts,
        deSelectAllContacts     : Actions.deSelectAllContacts,
        openEditContactDialog   : Actions.openEditContactDialog,
        removeContacts          : Actions.removeContacts,
        removeContact           : Actions.removeContact,
        toggleStarredContact    : Actions.toggleStarredContact,
        toggleStarredContacts   : Actions.toggleStarredContacts,
        setContactsStarred      : Actions.setContactsStarred,
        setContactsUnstarred    : Actions.setContactsUnstarred
    }, dispatch);
}

function mapStateToProps({contactsApp})
{
    return {
        contacts          : contactsApp.contacts.entities,
        selectedContactIds: contactsApp.contacts.selectedContactIds,
        searchText        : contactsApp.contacts.searchText,
        user              : contactsApp.user
    }
}

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(ContactsList));
