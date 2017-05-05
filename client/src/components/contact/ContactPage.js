/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';
import ContactForm from './ContactForm';
import Map from './Map';


const ContactPage = () =>{
    return(
        <div className="page" id="page-contact">
			<header className="bp-header cf">
				<h1 className="bp-header__title">Contact</h1>
				<p className="bp-header__desc">Send us an email and we will get right back.</p>
				<p className="info">
					"My belief is that communication is the best way to create strong relationships." &mdash; Jada Pinkett Smith
				</p>
			</header>
            <main id="contact-form-map-container">
                <ContactForm/>

                {/* Custom map*/}
                <Map/>
            </main>
		</div>        
    )
};

export default ContactPage;
