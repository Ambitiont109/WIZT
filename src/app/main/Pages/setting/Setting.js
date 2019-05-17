import React, {Component} from 'react';
import {withStyles} from '@material-ui/core/styles';
import {FusePageSimple, DemoContent} from '@fuse';
// import Form from './Form';
import Form from './Form1';
// import InteractiveGrid from './InteractiveGrid';

const styles = theme => ({
    layoutRoot: {}
});

class Setting extends Component {

    render()
    {
        const {classes} = this.props;
        return (
            <FusePageSimple
                classes={{
                    root: classes.layoutRoot
                }}
                header={
                    <div className="p-24"><h4>Setting</h4></div>
                }
                content={
                    <div className="p-24">
                       
                        <Form />
                    </div>
                }
            />
        )
    }
}

export default withStyles(styles, {withTheme: true})(Setting);