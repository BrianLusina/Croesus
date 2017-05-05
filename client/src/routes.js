/**
 * Created by lusinabrian on 05/05/17.
 */
import React from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom'
import App from './containers/App';
import DocumentationPage from './components/DocumentationsPage';
import HomePage from './components/HomePage';
import ManualPage from './components/ManualsPage';

/**
 * Maps components to different routes in the application
 * The parent component(App) maps other routes and serves as the entry point
 * to other components.
 * Route maps HomePage to default route
 */

export default (
    <App>
        <div className="pages-stack">
            <Route component={HomePage} />
            <Route component={DocumentationPage} />
            <Route component={ManualPage}/>
        </div>
    </App>
)