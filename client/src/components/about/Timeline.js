/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';

const Timeline = () => {
    return(
        <section className="cd-horizontal-timeline">
            <div className="timeline">
		<div className="events-wrapper">
			<div className="events">
				<ol>
					<li><a href="#0" data-date="1/10/2016" className="selected">1 Oct, 2016</a></li>
					<li><a href="#0" data-date="15/10/2016">15 Oct, 2016</a></li>
					<li><a href="#0" data-date="30/10/2016">30 Oct, 2016</a></li>
					<li><a href="#0" data-date="13/11/2016">13 Nov, 2016</a></li>
					<li><a href="#0" data-date="25/11/2016">25 Nov, 2016</a></li>
					<li><a href="#0" data-date="5/12/2016">5 Dec, 2016</a></li>
					<li><a href="#0" data-date="18/12/2016">18 Dec, 2016</a></li>
					<li><a href="#0" data-date="27/12/2016">27 Dec, 2016</a></li>
					<li><a href="#0" data-date="10/1/2017">10 Jan, 2017</a></li>
					<li><a href="#0" data-date="29/1/2017">29 Jan, 2017</a></li>
					<li><a href="#0" data-date="02/02/2017">3 Feb, 2017</a></li>
				</ol>

				<span className="filling-line" aria-hidden="true"></span>
			</div> <!-- .events -->
		</div> <!-- .events-wrapper -->

		<ul className="cd-timeline-navigation">
			<li><a href="#0" className="prev inactive">Prev</a></li>
			<li><a href="#0" className="next">Next</a></li>
		</ul> <!-- .cd-timeline-navigation -->
	</div> <!-- .timeline -->

            <div className="events-content">
                <ol>
                    <li className="selected" data-date="1/10/2016">
                        <h2>Genesis</h2>
                        <em>October 1st, 2016</em>
                        <p>
                            Inception of Arco is born. The idea is formulated to advance financial sector. Provide smart solutions and grow investor knowledge by teaching a machine to learn past investor behavioral patterns. Inspired by open-sourcing of Tensorflow.
                        </p>
                    </li>

                    <li data-date="15/10/2016">
                        <h2>Event title here</h2>
                        <em>October 15th, 2016</em>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum praesentium officia, fugit recusandae ipsa, quia velit nulla adipisci? Consequuntur aspernatur at, eaque hic repellendus sit dicta consequatur quae, ut harum ipsam molestias maxime non nisi reiciendis eligendi! Doloremque quia pariatur harum ea amet quibusdam quisquam, quae, temporibus dolores porro doloribus.
                        </p>
                    </li>

                    <li data-date="30/10/2016">
                        <h2>Event title here</h2>
                        <em>October 30th, 2016</em>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum praesentium officia, fugit recusandae ipsa, quia velit nulla adipisci? Consequuntur aspernatur at, eaque hic repellendus sit dicta consequatur quae, ut harum ipsam molestias maxime non nisi reiciendis eligendi! Doloremque quia pariatur harum ea amet quibusdam quisquam, quae, temporibus dolores porro doloribus.
                        </p>
                    </li>

                    <li data-date="13/11/2016">
                        <h2>Event title here</h2>
                        <em>November 13th, 2016</em>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum praesentium officia, fugit recusandae ipsa, quia velit nulla adipisci? Consequuntur aspernatur at, eaque hic repellendus sit dicta consequatur quae, ut harum ipsam molestias maxime non nisi reiciendis eligendi! Doloremque quia pariatur harum ea amet quibusdam quisquam, quae, temporibus dolores porro doloribus.
                        </p>
                    </li>

                    <li data-date="25/11/2016">
                        <h2>Event title here</h2>
                        <em>November 25th, 2016</em>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum praesentium officia, fugit recusandae ipsa, quia velit nulla adipisci? Consequuntur aspernatur at, eaque hic repellendus sit dicta consequatur quae, ut harum ipsam molestias maxime non nisi reiciendis eligendi! Doloremque quia pariatur harum ea amet quibusdam quisquam, quae, temporibus dolores porro doloribus.
                        </p>
                    </li>

                    <li data-date="5/12/2016">
                        <h2>Event title here</h2>
                        <em>December 5th, 2016</em>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum praesentium officia, fugit recusandae ipsa, quia velit nulla adipisci? Consequuntur aspernatur at, eaque hic repellendus sit dicta consequatur quae, ut harum ipsam molestias maxime non nisi reiciendis eligendi! Doloremque quia pariatur harum ea amet quibusdam quisquam, quae, temporibus dolores porro doloribus.
                        </p>
                    </li>

                    <li data-date="18/12/2016">
                        <h2>Event title here</h2>
                        <em>December 18th, 2016</em>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum praesentium officia, fugit recusandae ipsa, quia velit nulla adipisci? Consequuntur aspernatur at, eaque hic repellendus sit dicta consequatur quae, ut harum ipsam molestias maxime non nisi reiciendis eligendi! Doloremque quia pariatur harum ea amet quibusdam quisquam, quae, temporibus dolores porro doloribus.
                        </p>
                    </li>

                    <li data-date="27/12/2016">
                        <h2>Event title here</h2>
                        <em>December 27th, 2016</em>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum praesentium officia, fugit recusandae ipsa, quia velit nulla adipisci? Consequuntur aspernatur at, eaque hic repellendus sit dicta consequatur quae, ut harum ipsam molestias maxime non nisi reiciendis eligendi! Doloremque quia pariatur harum ea amet quibusdam quisquam, quae, temporibus dolores porro doloribus.
                        </p>
                    </li>
        		</ol>
            </div> <!-- .events-content -->
        </section>
    )
};


export default Timeline;