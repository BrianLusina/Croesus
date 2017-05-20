/**
 * @author lusinabrian on 20/05/17.
 * @notes: Reset password form
 */

import React, { Component } from 'react';

export default class ResetForm extends Component{
    render(){
        return(
            <form className="cd-form">
                <p className="fieldset">
                    <label className="image-replace cd-email" htmlFor="reset-email">E-mail</label>
                    <input className="full-width has-padding has-border"
                           id="reset-email" type="email" placeholder="E-mail"/>
                        <span className="cd-error-message">Error message here!</span>
                </p>
                <p className="fieldset">
                    <input className="full-width has-padding" type="submit"
                           value="Reset password"/>
                </p>
            </form>
        )
    }
}
