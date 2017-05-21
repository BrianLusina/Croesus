/**
 * @author lusinabrian on 20/05/17.
 * @notes: SignUp Form component
 */
import React, { Component } from 'react';
import PropTypes from 'prop-types';

export default class SignUpForm extends Component{
    constructor(){
        super();
        this.state = {
            modalOpen:false
        };

        this.handleModalClose = this.handleModalClose.bind(this);
    }

    render(){
        return(
            <div id="cd-signup">
                <form className="cd-form">
                    <p className="fieldset">
                        <label className="image-replace cd-username"
                               htmlFor="signup-username">Username
                        </label>
                        <input className="full-width has-padding has-border" id="signup-username" type="text" placeholder="Username"/>
                        <span className="cd-error-message">Error message here!</span>
                    </p>

                    <p className="fieldset">
                        <label className="image-replace cd-email" htmlFor="signup-email">
                            E-mail
                        </label>
                        <input className="full-width has-padding has-border" id="signup-email"
                               type="email" placeholder="E-mail"/>
                        <span className="cd-error-message">Error message here!</span>
                    </p>

                    <p className="fieldset">
                        <label className="image-replace cd-password" htmlFor="signup-password">
                            Password
                        </label>
                        <input className="full-width has-padding has-border" id="signup-password" type="text"  placeholder="Password"/>
                        <a href="#0" className="hide-password">Hide</a>
                        <span className="cd-error-message">Error message here!</span>
                    </p>

                    <p className="fieldset">
                        <input type="checkbox" id="accept-terms"/>
                        <label htmlFor="accept-terms">I agree to the
                            <a href="#0">Terms</a>
                        </label>
                    </p>

                    <p className="fieldset">
                        <input className="full-width has-padding" type="submit" value="Create account"/>
                    </p>
                </form>
            </div>
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
SignUpForm.propTypes = {
    openSignUpModal: PropTypes.bool.isRequired
};