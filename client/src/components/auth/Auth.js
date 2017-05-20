/**
 * @author lusinabrian on 20/05/17.
 * @notes: Auth container for login and sign up components
 */
import LoginForm from 'LoginForm';
import SignUpForm from 'SignUpForm';
import ResetForm from 'ResetForm';
import React, { Component } from 'react';

export default class Auth extends Component{
    render(){
        return(
            <div className="cd-user-modal">
                <div className="cd-user-modal-container">

                    <ul className="cd-switcher">
                        <li><a href="#0">Sign in</a></li>
                        <li><a href="#0">New account</a></li>
                    </ul>

                    <LoginForm />

                    <SignUpForm />

                    <div id="cd-reset-password">
                        <p className="cd-form-message">Lost your password? Please enter your email address. You will receive a link to create a new password.</p>

                        <ResetForm />

                        <p className="cd-form-bottom-message">
                            <a href="#0">Back to log-in</a>
                        </p>
                    </div>
                    <a href="#0" className="cd-close-form">Close</a>
                </div>
            </div>
        )
    }
}

