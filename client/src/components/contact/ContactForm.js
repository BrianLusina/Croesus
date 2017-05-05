/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';


const ContactForm = () => {
    return (
        <section id="contact-form-container">
            <form id="contact_form" className="cd-form floating-labels" method="post">
                <fieldset>
                    <div className="icon">
                        <label className="cd-label" htmlFor="cd-name">Name</label>
                        <input className="user" type="text" name="cd-name" id="cd-name" required/>
                    </div>

                    <div className="icon">
                        <label className="cd-label" htmlFor="cd-company">Company</label>
                        <input className="company" type="text" name="cd-company" id="cd-company"/>
                    </div>

                    <div className="icon">
                        <label className="cd-label" htmlFor="cd-email">Email</label>
                        <input className="email error" type="email" name="cd-email" id="cd-email" required/>
                    </div>
        		</fieldset>

                <fieldset>
                    <div className="icon">
                        <label className="cd-label" htmlFor="cd-textarea">Project description</label>
                        <textarea className="message" name="cd-textarea" id="cd-textarea" required></textarea>
                    </div>
                    <div>
                        <input type="submit" value="Send Message"/>
                    </div>
                </fieldset>
            </form>
        </section>
    )
};

export default ContactForm;
