/**
 * @author lusinabrian on 20/05/17.
 * @notes: Auth container for login and sign up components
 */
import ResetForm from './ResetForm';
import React, { Component } from 'react';
import Dialog from 'material-ui/Dialog';
import FlatButton from 'material-ui/FlatButton';
import PropTypes from 'prop-types';

export default class Auth extends Component{
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
            modalOpen:nextProps.openModal
        });
    }

    render(){
        const actions = [
            <FlatButton
                label="Cancel"
                primary={true}
                onTouchTap={this.handleModalClose}
            />,
            <FlatButton
                label="Submit"
                primary={true}
                disabled={true}
                onTouchTap={this.handleModalClose}
            />,
        ];

        return(
            <Dialog
                title="Dialog With Actions"
                actions={actions}
                modal={true}
                open={this.state.modalOpen}>
                Only actions can close this dialog.
            </Dialog>
        // <div className="cd-user-modal">
        //         <div className="cd-user-modal-container">
        //
        //             <ul className="cd-switcher">
        //                 <li><a href="#0">Sign in</a></li>
        //                 <li><a href="#0">New account</a></li>
        //             </ul>
        //
        //             <LoginForm />
        //
        //             <SignUpForm />
        //
        //             <div id="cd-reset-password">
        //                 <p className="cd-form-message">Lost your password? Please enter your email address. You will receive a link to create a new password.</p>
        //
        //                 <ResetForm />
        //
        //                 <p className="cd-form-bottom-message">
        //                     <a href="#0">Back to log-in</a>
        //                 </p>
        //             </div>
        //             <a href="#0" className="cd-close-form">Close</a>
        //         </div>
        //     </div>
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

// required proptypes
Auth.propTypes = {
  openModal: PropTypes.bool.isRequired
};