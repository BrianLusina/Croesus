/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';
import {Route, IndexRoute} from 'react-router';
import App from './containers/App';
import HomePage from './components/HomePage';

/* Maps components to different routes in the application
The parent component(App) maps other routes and serves as the entry point
to other components.
IndexRoute maps HomePage to default route
 */

export default (
    <Route path="/" component={App}>
        <IndexRoute component={HomePage}/>
        <Route path="" component={}/>
    </Route>
)