import React, { Component } from 'react';
import PropTypes from 'prop-types';
import '../styles/App.css';
import Navigation from '../common/Navigation';

class App extends Component {
  render() {
    return (
      <div>
          <Navigation />
          {this.props.children}
          <button className="menu-button">
              <span>Menu</span>
          </button>
      </div>
    );
  }
}

App.propTypes = {
    children: PropTypes.object.isRequired
};

export default App;
