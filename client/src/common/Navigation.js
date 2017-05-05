/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';
import { Link } from 'react-router-dom';

/**
 * Stateless Component responsible for presentation
 * This will be used to display a header, so the business logic will be handled by the
 * containers.
 * */

const navigationItems = [
    {name:"Home"},
    {name:"Documentation"},
    {name:"Manuals"},
    {name:"Software"},
    {name:"Customization &amp; Settings"},
    {name:"Training"},
    {name:"About Us"},
    {name:"Blog & News"},
    {name:"Contact"},
];

const socialMediaLinks = [
    {classes:"fa fa-twitter", socialName:"Twitter", socialLink:""},
    {classes:"fa fa-linkedin", socialName:"LinkedIn", socialLink:""},
    {classes:"fa fa-facebook", socialName:"Facebook", socialLink:""},
];

const Navigation = () =>(
    	<nav className="pages-nav">
            {
                navigationItems.map((item, indx) => {
                    return (
                        <div key={indx} className="pages-nav__item">
                            <Link to="home" className="link link--page">{item.name}</Link>
                        </div>
                    );
                })
            }
	    	<div className="pages-nav__item pages-nav__item--social">
                {
                    socialMediaLinks.map((item, indx)=>{
                        return(
                            <a key={indx} className="link link--social link--faded"
                               href={item.socialLink}>
                                <i className={item.classes}></i>
                                <span className="text-hidden">{item.socialName}</span>
                            </a>
                        );
                    })
                }
            </div>
        </nav>
);

export default Navigation;
