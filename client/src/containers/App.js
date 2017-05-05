import React, { Component } from 'react';
import '../styles/app.css';
import Navigation from '../common/Navigation';
import DocumentationPage from '../components/DocumentationsPage';
import HomePage from '../components/HomePage';
import ManualPage from '../components/ManualsPage';
import SoftwarePage from '../components/SoftwarePage';
import CustomSettingsPage from '../components/CustomSettingsPage';
import TrainingPage from '../components/TrainingPage';
import AboutPage from '../components/about/AboutPage';
import BlogPage from '../components/blog/BlogPage';
import ContactPage from '../components/contact/ContactPage';

class App extends Component {
  render() {
    return (
      <div>
          <Navigation />
          <div className="pages-stack">
              <HomePage />
              <DocumentationPage />
              <ManualPage />
              <SoftwarePage />
              <CustomSettingsPage />
              <TrainingPage />
              <AboutPage />
              <BlogPage />
              <ContactPage />
          </div>
          <button className="menu-button">
              <span>Menu</span>
          </button>
      </div>
    );
  }
}

export default App;
