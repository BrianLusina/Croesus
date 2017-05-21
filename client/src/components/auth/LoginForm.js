/**
 * @author lusinabrian on 20/05/17.
 * @notes: Login Form modal
 */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Dialog from 'material-ui/Dialog';
import FlatButton from 'material-ui/FlatButton';


export default class LoginForm extends Component{
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
            modalOpen:nextProps.openLoginModal
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
                title="Login"
                actions={actions}
                modal={true}
                open={this.state.modalOpen}>
                <div id="cd-login">
                    <form className="cd-form">
                        <p className="fieldset">
                            <label className="image-replace cd-email" htmlFor="signin-email">
                                E-mail
                            </label>
                            <input className="full-width has-padding has-border" id="signin-email" type="email" placeholder="E-mail"/>
                            <span className="cd-error-message">Error message here!</span>
                        </p>

                        <p className="fieldset">
                            <label className="image-replace cd-password" htmlFor="signin-password">
                                Password
                            </label>
                            <input className="full-width has-padding has-border" id="signin-password"
                                   type="text"  placeholder="Password"/>
                            <a href="#0" className="hide-password">Hide</a>
                            <span className="cd-error-message">Error message here!</span>
                        </p>

                        <p className="fieldset">
                            <input type="checkbox" id="remember-me" checked/>
                            <label htmlFor="remember-me">Remember me</label>
                        </p>

                        <p className="fieldset">
                            <input className="full-width" type="submit" value="Login"/>
                        </p>
                    </form>
                    <p className="cd-htmlForm-bottom-message">
                        <a href="#0">Forgot your password?</a>
                    </p>
                </div>
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

// required proptypes
LoginForm.propTypes = {
    openLoginModal: PropTypes.bool.isRequired
};