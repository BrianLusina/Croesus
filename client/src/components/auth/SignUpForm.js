/**
 * @author lusinabrian on 20/05/17.
 * @notes: SignUp Form component
 */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Dialog from 'material-ui/Dialog';
import FlatButton from 'material-ui/FlatButton';
import TextField from 'material-ui/TextField';
// import EmailIcon from 'material-ui/svg-icons/communication/email';
// import LockIcon from 'material-ui/svg-icons/action/lock-open';
// import AssistantIcon from 'material-ui/svg-icons/image/assistant-photo';
// import {red500, yellow500, blue500} from 'material-ui/styles/colors';

/**
 * Sign up form modal
 * This will enable user to sign up
 * Sends data over api to server
 * */
export default class SignUpForm extends Component{
    constructor(){
        super();
        this.state = {
            modalOpen:false
        };

        this.handleModalClose = this.handleModalClose.bind(this);
    }

    /**
     * Component will receive props
     * @param {Object} nextProps Props received from parent container
     * */
    componentWillReceiveProps(nextProps){
        this.setState({
            modalOpen:nextProps.openSignUpModal
        });
    }

    /**
     * Render to DOM
     * */
    render(){
        const actions = [
            <FlatButton
                label="Cancel"
                primary={true}
                onTouchTap={this.handleModalClose}
            />,
            <FlatButton
                label="Create Account"
                primary={true}
                onTouchTap={this.handleModalClose}
            />,
        ];

        return(
            <Dialog
                title="Sign up"
                actions={actions}
                modal={true}
                open={this.state.modalOpen}>
                <div id="cd-signup">
                    <TextField
                        id="signup-username"
                        hintText="Username"
                        floatingLabelText="Username"
                        fullWidth={true}
                        type="text"
                    />

                    <TextField
                        hintText="Email"
                        floatingLabelText="Email"
                        fullWidth={true}
                        type="email"
                    />

                    <TextField
                        hintText="Password"
                        floatingLabelText="Password"
                        fullWidth={true}
                        type="password"
                    />

                    <TextField
                        hintText="Retype Password"
                        floatingLabelText="Retype Password"
                        fullWidth={true}
                        type="password"
                    />
                </div>

{/*
                         <p className="fieldset">
                             <input type="checkbox" id="accept-terms"/>
                             <label htmlFor="accept-terms">I agree to the
                                 <a href="#0">Terms</a>
                             </label>
                         </p>
*/}

            </Dialog>
        )
    }

    /**
     * Handle closing of modal dialog
     * */
    handleModalClose(){
        this.setState({
            modalOpen:false
        });
    }
}

// required prop types
SignUpForm.propTypes = {
    openSignUpModal: PropTypes.bool.isRequired
};