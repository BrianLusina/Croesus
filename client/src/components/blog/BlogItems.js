/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';

const BlogItems = () => {
    return(
        <div>
            <ul className="cd-items cd-container">
                <li className="cd-item">
                    <img src="{{ url_for('static', filename='images/blogs/item-1.jpg' )}}" alt="Item Preview"/>
                        <a href="#0" className="cd-trigger">Read More</a>
                </li>
                <li className="cd-item">
                    <img src="{{ url_for('static', filename='images/blogs/item-1.jpg' )}}" alt="Item Preview"/>
                    <a href="#0" className="cd-trigger">Read More</a>
                </li>
                <li className="cd-item">
                    <img src="{{ url_for('static', filename='images/blogs/item-1.jpg' )}}" alt="Item Preview"/>
                    <a href="#0" className="cd-trigger">Read More</a>
                </li>
            </ul>

            <div className="cd-quick-view">
                <div className="cd-slider-wrapper">
                    <ul className="cd-slider">
                        <li className="selected">
                            <img src="{{ url_for('static', filename='images/blogs/item-1.jpg' )}}" alt="Product 1"/>
                        </li>

                        <li>
                            <img src="{{ url_for('static', filename='images/blogs/item-2.jpg' )}}" alt="Product 2"/>
                        </li>

                        <li>
                            <img src="{{ url_for('static', filename='images/blogs/item-3.jpg' )}}" alt="Product 3"/>
                        </li>
                    </ul>

                    <ul className="cd-slider-navigation">
                        <li><a className="cd-next" href="#0">Prev</a></li>
                        <li><a className="cd-prev" href="#0">Next</a></li>
                    </ul>
                </div>

                <div className="cd-item-info">
                    <h2>News Title</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officia, omnis illo iste ratione. Numquam eveniet quo, ullam itaque expedita impedit. Eveniet, asperiores amet iste repellendus similique reiciendis, maxime laborum praesentium.</p>

                    <ul className="cd-item-action">
                        <li><button className="learn-more">Learn More</button></li>
                    </ul>
                </div>
                <a href="#0" className="cd-close">Close</a>
            </div>
        </div>
    );
};

export default BlogItems;