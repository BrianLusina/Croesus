/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';

const SoftwarePage = () => {
    return(
		<div className="page" id="page-software">
			<header className="bp-header cf">
				<h1 className="bp-header__title">Software &amp; Downloads</h1>
				<p className="bp-header__desc">Based on Ilya Kostin's Dribbble shot
                    <a href="https://dribbble.com/shots/2286042-Stacked-navigation">Stacked navigation</a></p>
				<p className="info">
					"I decided to pick the diet that I thought would maximize my chances of long-term survival." &mdash; Al Gore
				</p>
			</header>
			<img className="poster" src="{{ url_for('static', filename='images/3.jpg') }}" alt="img03" />
		</div>
    )
};

export default SoftwarePage;