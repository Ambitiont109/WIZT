import React, {Component} from 'react';
import { AppBar, Card, CardContent, Icon, Toolbar, Typography} from '@material-ui/core';
import {FuseAnimateGroup} from '@fuse';
import axios from 'axios';

class AboutTab extends Component {

    state = {
        general: null,
        work   : null,
        contact: null,
        groups : null,
        friends: null
    };

    componentDidMount()
    {
        axios.get('/api/profile/about').then(res => {
            this.setState(res.data);
        });
    }

    render()
    {
        const {general, work, contact, groups, friends} = this.state;

        return (
            <div className="md:flex" >

                <div className="flex flex-col flex-1 md:pr-32">
                    <FuseAnimateGroup
                        enter={{
                            animation: "transition.slideUpBigIn"
                        }}
                    >
                        {general && (
                            <Card className="w-full mb-16">
                                <AppBar position="static" elevation={0}>
                                    <Toolbar className="pl-16 pr-8">
                                        <Typography variant="subtitle1" color="inherit" className="flex-1">
                                            General Information
                                        </Typography>
                                    </Toolbar>
                                </AppBar>

                                <CardContent>
                                    <div className="mb-24">
                                        <Typography className="font-bold mb-4 text-15">Gender</Typography>
                                        <Typography>{general.gender}</Typography>
                                    </div>

                                    <div className="mb-24">
                                        <Typography className="font-bold mb-4 text-15">Birthday</Typography>
                                        <Typography>{general.birthday}</Typography>
                                    </div>

                                    <div className="mb-24">
                                        <Typography className="font-bold mb-4 text-15">Locations</Typography>

                                        {general.locations.map((location) => (
                                            <div className="flex items-center" key={location}>
                                                <Typography>{location}</Typography>
                                                <Icon className="text-16 ml-4" color="action">location_on</Icon>
                                            </div>
                                        ))}
                                    </div>

                                    <div className="mb-24">
                                        <Typography className="font-bold mb-4 text-15">About Me</Typography>
                                        <Typography>{general.about}</Typography>
                                    </div>

                                </CardContent>
                            </Card>
                        )}

                       
                        
                    </FuseAnimateGroup>
                </div>
                <div className="flex flex-col md:w-512">
                    <FuseAnimateGroup
                        enter={{
                            animation: "transition.slideUpBigIn"
                        }}
                    >
                         {work && (
                            <Card className="w-full mb-16">
                                <AppBar position="static" elevation={0}>
                                    <Toolbar className="pl-16 pr-8">
                                        <Typography variant="subtitle1" color="inherit" className="flex-1">
                                            Subscription
                                        </Typography>
                                    </Toolbar>
                                </AppBar>

                                <CardContent>
                                    <div className="mb-24">
                                        <Typography className="font-bold mb-4 text-15">Occupation</Typography>
                                        <Typography>{work.occupation}</Typography>
                                    </div>

                                    <div className="mb-24">
                                        <Typography className="font-bold mb-4 text-15">Skills</Typography>
                                        <Typography>{work.skills}</Typography>
                                    </div>

                                    <div className="mb-24">
                                        <Typography className="font-bold mb-4 text-15">Jobs</Typography>
                                        <table className="">
                                            <tbody>
                                                {work.jobs.map((job) => (
                                                    <tr key={job.company}>
                                                        <td className="pr-16">
                                                            <Typography>{job.company}</Typography>
                                                        </td>
                                                        <td>
                                                            <Typography color="textSecondary">{job.date}</Typography>
                                                        </td>
                                                    </tr>
                                                ))}
                                            </tbody>
                                        </table>
                                    </div>
                                </CardContent>
                            </Card>
                        )}

                    </FuseAnimateGroup>
                </div>
            </div>
        );
    }
}

export default AboutTab;
