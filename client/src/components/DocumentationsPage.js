/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';

const Documentation = () => {
    return(
        <div className="page" id="page-docu">
			<header className="bp-header cf">
				<h1 className="bp-header__title">Documentation</h1>
				<p className="bp-header__desc">Based on Ilya Kostin's Dribbble shot <a href="https://dribbble.com/shots/2286042-Stacked-navigation">Stacked navigation</a></p>
				<p className="info">
					"We cannot have peace among men whose hearts find delight in killing any living creature." &mdash; Rachel Carson
				</p>
			</header>
			<img className="poster" src="{{ url_for('static', filename='images/6.jpg') }}" alt="img06" />
		</div>
    )
};

export default Documentation;
