/**
 * Entry point into the application
 * Router keeps UI and URL in sync and ensures that the props are passed
 * Provider makes the store available to the component hierarchy
 * That way, the components below the hierarchy can access the store’s state with connect
 * method call.
*/

import React from 'react';
import { render } from 'react-dom';
import './styles/index.css';
import App from './containers/App';
import configureStore from './store/configureStore';
import { Provider } from 'react-redux';

// initialize store
const store = configureStore();

// render the application to the DOM
render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root')
);
