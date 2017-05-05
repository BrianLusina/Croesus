import React, { Component, PropTypes } from 'react';
import '../styles/App.css';
import Navigation from '../common/Navigation';

class App extends Component {
  render() {
    return (
      <div className="App">
          <Navigation />
          {this.props.children}
      </div>
    );
  }
}

App.propTypes = {
    children: PropTypes.object.isRequired
};

export default App;
