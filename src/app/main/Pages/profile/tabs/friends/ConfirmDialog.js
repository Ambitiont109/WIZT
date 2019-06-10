import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import {bindActionCreators} from 'redux';
import * as Actions from './store/actions';
import {connect} from 'react-redux';
import axios from "axios";
import requestConfig from "../../../../config/requestConfig";


class ConfirmDialog extends React.Component {
  state = {
    open: false,
  };

  handleClickOpen = () => {
    this.setState({ open: true });
  };

  handleClose = () => {

    this.setState({ open: false });
  };

  removeContact = (item_id) => {
    console.log(item_id)
    let user_id = localStorage.getItem("item_id")
    console.log(item_id)
    axios.delete(requestConfig.baseUrl+"/admin/users/"+user_id+"/friends/"+item_id+"/").then((res)=>this.ReturnMainPage());
  };

  ReturnMainPage = () => {
    const {history, page} = this.props;
    history.push(
      {
        pathname: "/app/pages/profile",
        page : page
      }
    )
    this.props.closeConfirmDialog()
  }

  render() {
    const { closeConfirmDialog, confirmDialog } = this.props;
    return (
      
      <Dialog
        open={confirmDialog.props.open} // added by myself
        onClose={this.handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Permanently delete?"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Please note that it will delete all the user data.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={()=>{  // added by myself
            // closeConfirmDialog();
            this.removeContact(confirmDialog.user_id);
          }} color="primary">
            Agree
          </Button>
          <Button onClick={() =>{ // added by myself
            closeConfirmDialog();
          }} color="primary" autoFocus>
            Disagree
          </Button>
        </DialogActions>
      </Dialog>
      
    );
  }
}
/** The under part added by myself */
function mapDispatchToProps(dispatch)
{
    return bindActionCreators({
        closeEditContactDialog: Actions.closeEditContactDialog,
        closeNewContactDialog : Actions.closeNewContactDialog,
        addContact            : Actions.addContact,
        updateContact         : Actions.updateContact,
        removeContact         : Actions.removeContact,
        closeConfirmDialog    : Actions.closeConfirmDialog,
    }, dispatch);
}

function mapStateToProps({friendsApp})
{
    return {
      confirmDialog: friendsApp.contacts.confirmDialog,
      page: friendsApp.contacts.page
    }
}


export default connect(mapStateToProps, mapDispatchToProps)(ConfirmDialog);
