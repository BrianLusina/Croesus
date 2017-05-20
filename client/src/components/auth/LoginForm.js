/**
 * @author lusinabrian on 20/05/17.
 * @notes: Login Form modal
 */
import React, { Component } from 'react';

export default class LoginForm extends Component{
    render(){
        return(
            <div id="cd-login"> <!-- log in htmlForm -->
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
                <!-- <a href="#0" className="cd-close-form">Close</a> -->
            </div>
        )
    }
}