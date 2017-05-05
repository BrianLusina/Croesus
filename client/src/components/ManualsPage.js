/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';

const ManualPage = () => {
    return (
		<div className="page" id="page-manuals">
			<header className="bp-header cf">
				<h1 className="bp-header__title">Manuals</h1>
				<p className="bp-header__desc">Based on Ilya Kostin's Dribbble shot <a href="https://dribbble.com/shots/2286042-Stacked-navigation">Stacked navigation</a></p>
				<p className="info">
					"When you adopt a vegan diet we make a connection, you don't go back, it is not a diet, it is a lifestyle." &mdash; Freelee Frugivore
				</p>
			</header>
			<img className="poster" src="{{ url_for('static', filename='images/2.jpg') }}" alt="img02" />
		</div>        
    )
};

export default ManualPage