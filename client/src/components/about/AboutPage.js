/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';
import Timeline from './Timeline';


const AboutPage = () =>{
    return(
		<div className="page" id="page-about">
			<header className="bp-header cf">
				<h1 className="bp-header__title">About Us</h1>
				<p className="bp-header__desc">What we do and why we do it.</p>
				<p className="info">
					"When people ask me why I don't eat meat or any other animal products, I say, 'Because they are unhealthy and they are the product of a violent and inhumane industry.'" &mdash;
				</p>
			</header>
            { /*Time line*/ }
            <Timeline/>
		</div>
    )
};

export default AboutPage;