import React from 'react';
import { render } from 'react-dom';
import './styles/index.css';
import routes from './routes';
import { HashRouter } from 'react-router-dom';

/**
 * Entry point into the application
 * Router keeps UI and URL in sync and ensures that the props are passed
 * Provider makes the store available to the component hierarchy
 * That way, the components below the hierarchy can access the store’s state with connect method call.
*/

render(
    <HashRouter>
        {routes}
    </HashRouter>,
    document.getElementById('root')
);
