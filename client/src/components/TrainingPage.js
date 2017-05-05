/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';


const TrainingPage = () => {
    return(
		<div className="page" id="page-training">
			<header className="bp-header cf">
				<h1 className="bp-header__title">Training &amp; Learning Center</h1>
				<p className="bp-header__desc">Based on Ilya Kostin's Dribbble shot <a href="https://dribbble.com/shots/2286042-Stacked-navigation">Stacked navigation</a></p>
				<p className="info">
					"The moment I began to understand what was going on with the treatment of animals, it led me more and more in the way of the path I am [on] now, which is a complete vegan." &mdash; Bryan Adams
				</p>
			</header>
			<img className="poster" src="{{ url_for('static', filename='images/5.jpg') }}" alt="img05" />
		</div>
    );
};

export default TrainingPage;