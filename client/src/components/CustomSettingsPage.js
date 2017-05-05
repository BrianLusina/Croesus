/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';


const CustomSettingsPage = () => {
    return(
		<div className="page" id="page-custom">
			<header className="bp-header cf">
				<h1 className="bp-header__title">Customization &amp; Settings</h1>
				<p className="bp-header__desc">Based on Ilya Kostin's Dribbble shot
                    <a href="https://dribbble.com/shots/2286042-Stacked-navigation">Stacked navigation</a>
                </p>
				<p className="info">
					"You have to make a conscious decision to change for your own well-being, that of your family and your country." &mdash;Bill Clinton
				</p>
			</header>
			<img className="poster" src="{{ url_for('static', filename='images/4.jpg') }}" alt="img04" />
		</div>
    )
};

export default CustomSettingsPage;