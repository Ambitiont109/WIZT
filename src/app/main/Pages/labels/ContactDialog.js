import React, {Component} from 'react';
import {TextField, Button, Dialog, DialogActions, DialogContent, Icon, IconButton, Typography, Toolbar, AppBar, Avatar} from '@material-ui/core';
import {bindActionCreators} from 'redux';
import * as Actions from './store/actions';
import {connect} from 'react-redux';
import _ from '@lodash';
import Stepper from "./Stepper";
import ChipsArray from './chips/ChipsArray';
const newContactState = {
    id      : '',
    name    : '',
    lastName: '',
    avatar  : 'assets/images/avatars/profile.jpg',
    nickname: '',
    company : '',
    jobTitle: '',
    email   : '',
    phone   : '',
    address : '',
    birthday: '',
    notes   : ''
};

class ContactDialog extends Component {

    state = {...newContactState, disableEdit: true };

    componentDidUpdate(prevProps, prevState, snapshot)
    {   
        /**
         * After Dialog Open
         */
        if ( !prevProps.contactDialog.props.open && this.props.contactDialog.props.open )
        {
            /**
             * Dialog type: 'edit'
             * Update State
             */
            if ( this.props.contactDialog.type === 'edit' &&
                this.props.contactDialog.data &&
                !_.isEqual(this.props.contactDialog.data, prevState) )
            {
                this.setState({...this.props.contactDialog.data, disableEdit: true});
            }

            /**
             * Dialog type: 'new'
             * Update State
             */
            if ( this.props.contactDialog.type === 'new' &&
                !_.isEqual(newContactState, prevState) )
            {
                this.setState({...newContactState});
            }
        }
    }

    handleChange = (event) => {
        this.setState(_.set({...this.state}, event.target.name, event.target.type === 'checkbox' ? event.target.checked : event.target.value));
    };

    closeComposeDialog = () => {
        this.props.contactDialog.type === 'edit' ? this.props.closeEditContactDialog() : this.props.closeNewContactDialog();
    };

    canBeSubmitted()
    {
        const {name} = this.state;
        return (
            name.length > 0
        );
    }

    edit = () => {
        this.setState({
            disableEdit: false
        })
    }

    render()
    {
        const {contactDialog, addContact, updateContact, removeContact} = this.props;
  
        return (
            <Dialog
                classes={{
                    paper: "m-24"
                }}
                {...contactDialog.props}
                onClose={this.closeComposeDialog}
                fullWidth
                maxWidth="xs"
            >
                 <AppBar position="static" elevation={1}>
                    <div className="flex flex-col items-center justify-center pb-20 pt-16">
                        {contactDialog.type === 'edit' && (
                            <Typography variant="h6" color="inherit" className="pt-8">
                                {this.state.name}
                            </Typography>
                        )}
                    </div>
                </AppBar>
                {/* this is the part for stepper */}
                <Stepper images={this.state.images} /> 

                <DialogContent classes={{root: "p-24"}}>
                    <div className="flex">
                        <TextField
                            disabled = {this.state.disableEdit}
                            className="mb-24"
                            label="Name"
                            autoFocus
                            id="name"
                            name="name"
                            value={this.state.name}
                            // onChange={this.handleChange}
                            variant="outlined"
                            required
                            fullWidth
                        />
                    </div>

                    <div className="flex">
                        <TextField
                            disabled = {this.state.disableEdit}
                            className="mb-24"
                            label="Created by"
                            id="created_by"
                            name="created_by"
                            value={this.state.id}
                            // onChange={this.handleChange}
                            variant="outlined"
                            fullWidth
                        />
                    </div>
                    <div className="flex">
                        <TextField
                            disabled = {this.state.disableEdit}
                            className="mb-24"
                            label="Address"
                            id="address"
                            name="address"
                            value={this.state.location}
                            // onChange={this.handleChange}
                            variant="outlined"
                            fullWidth
                        />
                    </div>
                    <div className="flex">
                        <fieldset style={{border:"1px solid #c4c4c4", borderRadius: 4, width:312
                        }} >
                            <legend style={{color:"#757575", marginLeft: 10, fontSize: 12
                        }}>Tags</legend>
                            <div>
                                <ChipsArray data={this.state.tags} isEdit={true} />
                            </div>
                            
                        </fieldset>
                    </div>
                </DialogContent>

                {contactDialog.type === 'new' ? (
                    <DialogActions className="justify-between pl-16">
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={() => {
                                addContact(this.state);
                                this.closeComposeDialog();
                            }}
                            disabled={!this.canBeSubmitted()}
                        >
                            Add
                        </Button>
                    </DialogActions>
                ) : (
                    <DialogActions className="justify-between pl-16">
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={() => {
                                this.edit();
                                // updateContact(this.state);
                                // this.closeComposeDialog();
                            }}
                            disabled={!this.canBeSubmitted()}
                        >
                            {this.state.disableEdit? "Edit" : "Save"}
                        </Button>
                        <IconButton
                            onClick={() => {
                                removeContact(this.state.id);
                                this.closeComposeDialog();
                            }}
                        >
                            <Icon>delete</Icon>
                        </IconButton>
                    </DialogActions>
                )}
            </Dialog>
        );
    }
}


function mapDispatchToProps(dispatch)
{
    return bindActionCreators({
        closeEditContactDialog: Actions.closeEditContactDialog,
        closeNewContactDialog : Actions.closeNewContactDialog,
        addContact            : Actions.addContact,
        updateContact         : Actions.updateContact,
        removeContact         : Actions.removeContact
    }, dispatch);
}

function mapStateToProps({contactsApp})
{
    return {
        contactDialog: contactsApp.contacts.contactDialog
    }
}


export default connect(mapStateToProps, mapDispatchToProps)(ContactDialog);
