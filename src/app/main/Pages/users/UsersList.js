import React, {Component} from 'react';
import {Avatar, Icon, IconButton, ListItemIcon, ListItemText, Menu, MenuItem, MenuList, Typography} from '@material-ui/core';
import {FuseUtils, FuseAnimate} from '@fuse';
import {connect} from 'react-redux';
import {withRouter} from 'react-router-dom';
import {bindActionCreators} from 'redux';
import ReactTable from "react-table";
import * as Actions from './store/actions';
import axios from "axios";
import requestConfig from "../../config/requestConfig";

class UsersList extends Component {

    constructor() {
        super();
        this.state = {
            pageSize: "",
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
    onClickEdit = (id, name, imgURL) => {
        localStorage.setItem('item_id', id)
        localStorage.setItem('name', name)
        localStorage.setItem('imgURL', imgURL)
        this.props.history.push('/app/pages/profile')
    }

    fetchData = (state, instance) => {
        //Running when changes occure on table.
        // Request the data however you want.  Here, we'll use our mocked service we created earlier
        console.log(state.page)
        this.setState({
            pageSize: state.pageSize,
        })
        axios.post(requestConfig.baseUrl+"/admin/users/pagination/", {pagination_size: state.pageSize})
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
    };

    dateFormat = (date) => {
        var d = new Date(date);
        d = (d.getMonth()+1)+'/'+d.getDate()+'/'+d.getFullYear()+' '+(d.getHours() > 12 ? d.getHours() - 12 : d.getHours())+':'+d.getMinutes()+' '+(d.getHours() >= 12 ? "PM" : "AM");
        return <div>{d}</div>
    };

    phoneFormat = (data) => {
        if (data) {
            let phone_number = data.slice(0, 1) + data.slice(1, 2) + "-" + data.slice(2, 5) + "-" + data.slice(5, 8) + "-" + data.slice(8);
            return <div>{phone_number}</div>
        }
    }

    render()
    {
        const x = this.state.pageSize;
        const { contacts, user, page, searchText, selectedContactIds, totalPage, removeContacts, setContactsUnstarred, setContactsStarred, confirmDialog} = this.props;
        const data = this.getFilteredArray(contacts, searchText);
        const {selectedContactsMenu} = this.state;
        let pages = Math.floor(totalPage/x);
        const remainder = totalPage % x;
        if(pages && remainder) 
        {
            pages++; 
        }
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
                    data={data}
                    columns={[
                        {
                            Header    : "No",
                            headerClassName: 'h-52 text-16',
                            accessor  : "no",
                            filterable: false,
                            Cell      : row => (
                                    <span>{ row.index + 1 + this.state.pageSize*pageNum }</span>
                                ),
                            width      : 64,
                            className : "justify-center"
                           
                        },
                        {
                            Header   : () => (
                                selectedContactIds.length > 0 && (
                                    <React.Fragment>
                                        <IconButton
                                            aria-owns={selectedContactsMenu ? 'selectedContactsMenu' : null}
                                            aria-haspopup="true"
                                            onClick={this.openSelectedContactMenu}
                                        >
                                            <Icon>more_horiz</Icon>
                                        </IconButton>
                                        <Menu
                                            id="selectedContactsMenu"
                                            anchorEl={selectedContactsMenu}
                                            open={Boolean(selectedContactsMenu)}
                                            onClose={this.closeSelectedContactsMenu}
                                        >
                                            <MenuList>
                                                <MenuItem
                                                    onClick={() => {
                                                        removeContacts(selectedContactIds);
                                                        this.closeSelectedContactsMenu();
                                                    }}
                                                >
                                                    <ListItemIcon>
                                                        <Icon>delete</Icon>
                                                    </ListItemIcon>
                                                    <ListItemText inset primary="Remove"/>
                                                </MenuItem>
                                                <MenuItem
                                                    onClick={() => {
                                                        setContactsStarred(selectedContactIds);
                                                        this.closeSelectedContactsMenu();
                                                    }}
                                                >
                                                    <ListItemIcon>
                                                        <Icon>star</Icon>
                                                    </ListItemIcon>
                                                    <ListItemText inset primary="Starred"/>
                                                </MenuItem>
                                                <MenuItem
                                                    onClick={() => {
                                                        setContactsUnstarred(selectedContactIds);
                                                        this.closeSelectedContactsMenu();
                                                    }}
                                                >
                                                    <ListItemIcon>
                                                        <Icon>star_border</Icon>
                                                    </ListItemIcon>
                                                    <ListItemText inset primary="Unstarred"/>
                                                </MenuItem>

                                            </MenuList>
                                        </Menu>
                                    </React.Fragment>
                                )
                            ),
                            accessor : "picture",
                            Cell     : row => (
                                <Avatar  alt={row.original.name} src={row.value}/>
                            ),
                            className: "justify-center",
                            width    : 64,
                            sortable : false
                        },
                        {
                            Header    : "Name",
                            accessor  : "name",
                            filterable: false,
                            sortable  : false,
                            className : "justify-center"
                        },
                        {
                            Header    : "Email",
                            accessor  : "email",
                            filterable: false,
                            sortable  : false,
                            className : "justify-center"
                        },
                        {
                            Header    : "Phone number",
                            accessor  : "phone_number",
                            Cell      : row => (
                                this.phoneFormat(row.value)
                            ),
                            filterable: false,
                            sortable  : false,
                            className : "justify-center"
                        },
                        {
                            Header    : "Label in use",
                            accessor  : "label_in_use",
                            filterable: false,
                            sortable  : false,
                            className : "justify-center",
                            width     : 94,
                        },
                        {
                            Header    : "Photo in use",
                            accessor  : "photo_in_use",
                            filterable: false,
                            sortable  : false,
                            className : "justify-center",
                            width     : 94,
                        },
                        {
                            Header    : "Total label count",
                            accessor  : "total_label_count",
                            filterable: false,
                            sortable  : false,
                            className : "justify-center",
                            width     : 125,
                        },
                        {
                            Header    : "Friends count",
                            accessor  : "friends_count",
                            filterable: false,
                            sortable  : false,
                            className : "justify-center",
                            width     : 100,
                        },
                        {
                            Header    : "Created at",
                            accessor  : "created_at",
                            filterable: false,
                            sortable  : false,
                            className : "justify-center",
                            Cell      : row => (
                                this.dateFormat(row.value)
                            )
                        },
                        {
                            Header: "",
                            width : 128,
                            Cell  : row => (
                                <div className="flex items-center">
                                    <IconButton
                                        onClick={(ev) => {
                                            ev.stopPropagation();
                                            this.onClickEdit(row.original.id, row.original.name, row.original.picture);
                                        }}
                                    >
                                            <Icon>edit</Icon>
                                    </IconButton>
                                    <IconButton
                                        onClick={(ev) => {
                                            ev.stopPropagation();
                                            confirmDialog(row.original.id);
                                        }}
                                    >
                                        <Icon>delete</Icon>
                                    </IconButton>
                                </div>
                            )
                        }
                    ]}
                    pages={pages}
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

function mapStateToProps({usersApp})
{
    return {
        contacts          : usersApp.contacts.entities,
        totalPage         : usersApp.contacts.totalPage,
        page              : usersApp.contacts.page,
        selectedContactIds: usersApp.contacts.selectedContactIds,
        searchText        : usersApp.contacts.searchText,
        user              : usersApp.user
    }
}

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(UsersList));
