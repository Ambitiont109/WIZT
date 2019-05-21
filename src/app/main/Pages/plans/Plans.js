import React, {Component} from 'react';
import {withStyles} from '@material-ui/core/styles';
import {FusePageSimple, FuseAnimate} from '@fuse';
import {Icon, Typography, IconButton} from '@material-ui/core';
import MediaCard from './cards/MediaCard';

const styles = theme => ({
    layoutRoot: {}
});

class Example extends Component {

    constructor(props) {
        super(props);
        this.state = {
            header_content:"",
            body_content:"",
            footer_content:"",
            cards:[
                {
                    index:1,
                    header_content:"Billed Monthly",
                    body_content:"10 Labels",
                    footer_content:"USD 70(Save 45%)",
                },
                {
                    index:2,
                    header_content:"Billed Monthly",
                    body_content:"10 Labels",
                    footer_content:"USD 70(Save 46%)",
                },
                {
                    index:3,
                    header_content:"Billed Monthly",
                    body_content:"10 Labels",
                    footer_content:"USD 70(Save 47%)",
                },
            ]
        }
    }

    render()
    {
        const {classes} = this.props;
        return (
            <FusePageSimple
                classes={{
                    root: classes.layoutRoot
                }}
                header={
                    <div className="flex items-center" style={{marginLeft: 20}}>
                        <FuseAnimate animation="transition.expandIn" delay={300}>
                            <Icon className="text-32 mr-12">assessment</Icon>
                        </FuseAnimate>
                        <FuseAnimate animation="transition.slideLeftIn" delay={300}>
                            <Typography variant="h6" className="hidden sm:flex">Plans</Typography>
                        </FuseAnimate>
                    </div>
                }
               content={
                    <div className="p-24">
                        <div style={{display:"flex", flexFlow: "row wrap", justifyContent:"space-evenly"}}>
                            {this.state.cards.map((cards, index) => (
                                <MediaCard 
                                    key={cards.index}
                                    header_content={cards.header_content} 
                                    footer_content={cards.footer_content} 
                                    content={cards.body_content} 
                                />
                            ))}
                        </div>
                    </div>
                }
            />
        )
    }
}

export default withStyles(styles, {withTheme: true})(Example);