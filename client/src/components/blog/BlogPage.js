/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';
import BlogItems from './BlogItems';
import '../../styles/sass/pages/blogpage.css';

const BlogPage = () => {
    return(
		<div className="page" id="page-blog">
			<header className="bp-header cf">
				<h1 className="bp-header__title">Blog &amp; News</h1>
				<p className="info">
					"It's amazing that the amount of news that happens in the world every day always just exactly fits the newspaper." &mdash; Jerry Seinfield
				</p>
			</header>

            {/*Blog items*/}
            <BlogItems/>
		</div>
    )
};

export default BlogPage;
