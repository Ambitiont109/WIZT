import React, {Component} from 'react';
import { Avatar, Icon, IconButton, ListItemIcon, ListItemText, Menu, MenuItem, MenuList, Typography} from '@material-ui/core';
import {FuseUtils, FuseAnimate} from '@fuse';
import {connect} from 'react-redux';
import {withRouter} from 'react-router-dom';
import {bindActionCreators} from 'redux';
import ReactTable from "react-table";
import * as Actions from './store/actions';
import ChipsArray from './chips/ChipsArray';

class ContactsList extends Component {

    constructor() {
        super();
        this.state = {
          data: [],
          pages: null,
          loading: true,
          prev: 0,
        };
    }
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

    fetchData = (state, instance) => {
        //Running when changes occure on table.
        // Request the data however you want.  Here, we'll use our mocked service we created earlier
        var params = {
            page: ""
        }

        if(state.page === 0){
            params = {
                page: 1
            }
            this.props.getContacts(params);
        }
        else{
            params = {
                page:state.page+1,
            }
            this.props.getContacts(params)
        }
    } 

    avatar = (row) => {
        if(row.value) {
            var jsObjects = row.value;
            var result = jsObjects.filter(obj => {
                    return obj.is_cover === true
                })
            let results = result.map(a => a.url);
            return  <Avatar  alt={row.original.name} src={results[0]} style={{borderRadius:0}} />
        }
    }
    dateFormat = (date) => {
        var d = new Date(date);
        d = (d.getMonth()+1)+'/'+d.getDate()+'/'+d.getFullYear()+' '+(d.getHours() > 12 ? d.getHours() - 12 : d.getHours())+':'+d.getMinutes()+' '+(d.getHours() >= 12 ? "PM" : "AM");
        return <div>{d}</div>
    }

    render()
    {
        const { contacts, page, user, searchText, selectedContactIds, selectAllContacts, deSelectAllContacts, toggleInSelectedContacts, openEditContactDialog, removeContacts, removeContact, confirmDialog } = this.props;
        const data = this.getFilteredArray(contacts, searchText);
        const {selectedContactsMenu} = this.state;
        if(page)
        {
            var pageNum = page.page-1;
        }
        else
        {
            var pageNum = 0;
        }

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
                                    console.log(rowInfo.original)
                                    openEditContactDialog(rowInfo.original);
                                }
                            }
                        }
                    }}
                    data={data}
                    columns={[
                        {
                            Header    : "No",
                            headerClassName: 'h-68 text-16 font-bold',
                            accessor  : "no",
                            filterable: false,
                            Cell      : row => (
                                    <span>{ row.index + 1 + 10*pageNum }</span>
                                ),
                            width      : 64,
                            className : "font-bold justify-center"
                        },
                        {
                            Header    : "",
                            headerClassName: 'h-68 text-16 font-bold',
                            accessor  : "images",
                            filterable: false,
                            sortable  : false,
                            width     : 64, 
                            className: "justify-center",
                            Cell      : row => (
                                this.avatar(row)
                            ),
                        },
                        {
                            Header    : "Name",
                            headerClassName: 'h-68 text-16 font-bold',
                            accessor  : "name",
                            filterable: false,
                            sortable  : false,
                            width     : 250, 
                            className : "font-bold "
                        },
                        {
                            Header    : "Location",
                            headerClassName: 'h-68 text-16 font-bold',
                            accessor  : "location",
                            filterable: false,
                            sortable  : false,
                        },
                        {
                            Header    : "Tags",
                            headerClassName: 'h-68 text-16 font-bold',
                            accessor  : "tags",
                            Cell      : row => (
                                <ChipsArray data={row.value} isEdit={false} />
                            ),
                            filterable: false,
                            sortable  : false,
                        },
                        {
                            Header    : "Created_by",
                            headerClassName: 'h-68 text-16 font-bold',
                            accessor  : "id",
                            filterable: false,
                            sortable  : false,
                        },
                        {
                            Header    : "Created_at",
                            headerClassName: 'h-68 text-16 font-bold',
                            accessor  : "created_at",
                            Cell      : row => (
                                this.dateFormat(row.value)
                            ),
                            filterable: false,
                            sortable  : false,
                        },
                        {
                            Header: "",
                            width : 128,
                            className: "justify-center",
                            Cell  : row => (
                                <div className="flex items-center">
                                    <IconButton
                                        onClick={(ev) => {
                                            ev.stopPropagation();
                                             //removeContact(row.original.id);
                                            confirmDialog(row.original.id);
                                        }}
                                    >
                                        <Icon>delete</Icon>
                                    </IconButton>
                                </div>
                            )
                        }
                    ]}
                    pages={30}
                    manual
                    onFetchData={this.fetchData}
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
        setContactsUnstarred    : Actions.setContactsUnstarred,
        confirmDialog           : Actions.confirmDialog,    
    }, dispatch);
}

function mapStateToProps({contactsApp})
{
    return {
        contacts          : contactsApp.contacts.entities,
        page              : contactsApp.contacts.page,
        selectedContactIds: contactsApp.contacts.selectedContactIds,
        searchText        : contactsApp.contacts.searchText,
        user              : contactsApp.user
    }
}

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(ContactsList));
