import React from 'react';
import PropTypes, { func } from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import CardHeader from '@material-ui/core/CardHeader';
import Fab from '@material-ui/core/Fab';
import Typography from '@material-ui/core/Typography';
import {FuseAnimate} from '@fuse';
import {Icon, IconButton} from '@material-ui/core';


const styles = {
  card: {
    marginBottom: 20,
    maxWidth: 345,
    backgroundColor:"#303030",
  },
  media: {
    height: 100,
    width: 100,
    margin: 'auto', 
    marginTop:20,
    alignSelf:"center",
  },
  
  color:{
    color:"#fff"
  },
  backgroundColor:{
    backgroundColor:"#3c4252"
  }
};
const edit = () => {
  alert("hang on me");
}

function MediaCard(props) {
  const { classes, header_content, body_content, footer_content} = props;
  
  return (
    <FuseAnimate animation="transition.flipBounceXIn"  duration={300}>
      <Card className={classes.card}>
        <CardHeader 
          title={<div>membership</div>}
          classes={{title:classes.color}}
          // subheader={<div>plans</div>}
          className={classes.backgroundColor}
        />
        <CardActionArea style={{justifyContent:"center"}}>
          <CardMedia
            className={classes.media}
            image="/assets/images/home/house.svg"
            title="Contemplative Reptile"
          />
          <CardContent>
            <Typography  classes={{h6:classes.color}} variant="h6" component="h3" align="center">
              {header_content}
            </Typography>
            <Typography  classes={{h6:classes.color}} variant="h6" component="h3" align="center">
              {body_content}
            </Typography>
            <Typography  classes={{h6:classes.color}} variant="h6" component="h3" align="center">
            {footer_content}
            </Typography>
            <Typography classes={{subtitle1:classes.color}} variant="subtitle1" component="p" align="center">
              Get 10 additional Labels Take up to 100 Photos 
              Customisable Floorplans 
              Reusable Labels Unlimited Tags Billed
            </Typography>
          </CardContent>
        </CardActionArea>
        <CardActions style={{ justifyContent:"flex-end", alignItems: "center", backgroundColor:"#303030"}}>
          {/* <Button  size="small" color="primary" variant="outlined" style={{ color:"#fff", backgroundColor:"#039be5"}}>
            Learn More
          </Button> */}
          <Fab color="secondary" aria-label="Edit" 
            onClick={()=>{
              edit()
            }}
          >
            <Icon>edit_icon</Icon>
          </Fab>
        </CardActions>
      </Card>
    </FuseAnimate>
  );
  
}

MediaCard.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(MediaCard);