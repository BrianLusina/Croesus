/**
 * Created by lusinabrian on 05/05/17.
 * Home page of application
 */
import React, { Component } from 'react';
import LoginForm from './auth/LoginForm';
import SignUpForm from './auth/SignUpForm';


export default class HomePage extends Component{

    constructor(){
        super();
        this.state = {
            openLoginModal:false,
            openSignUpModal:false
        };

        this.handleOnLoginClick = this.handleOnLoginClick.bind(this);
        this.handleOnSignUpClicked = this.handleOnSignUpClicked.bind(this);
        this.handleOnAboutClicked = this.handleOnAboutClicked.bind(this);
    }

    render(){
        return(
            <div className="page" id="page-home">
                <header className="bp-header cf">
                    <span className="bp-header__present">
                        Arco
                        <span className="bp-tooltip bp-icon bp-icon--about" data-content="All you will ever need to track your financial information"></span>
                    </span>

                    <h1 className="bp-header__title">Financial Market Tracker</h1>
                    <p className="bp-header__desc">Sifts through the market, so you don't have to.</p>
                    <nav className="bp-nav">
                        <a className="bp-nav__item bp-icon bp-icon--prev"
                           onClick={this.handleOnLoginClick} data-info="Login">
                            <span>Login</span>
                        </a>

                        <a className="bp-nav__item bp-icon bp-icon--drop"
                           onClick={this.handleOnSignUpClicked} data-info="Sign Up">
                            <span>Sign Up</span>
                        </a>

                        <a className="bp-nav__item bp-icon bp-icon--archive"
                           onClick={this.handleOnAboutClicked} data-info="About">
                            <span>About</span>
                        </a>
                    </nav>
                </header>
                <img className="poster" src="" alt="img01" />

                <LoginForm openLoginModal={this.state.openLoginModal}/>
                <SignUpForm openSignUpModal={this.state.openSignUpModal}/>
            </div>
        )
    }

    /**
     * Handle login click event
     * @param {Object} e event object
     * */
    handleOnLoginClick(e){
        e.preventDefault();
        this.setState({
            openLoginModal:true,
            openSignUpModal:false
        });
    }

    /**
     * Handle sign up click event
     * @param {Object} e event object*/
    handleOnSignUpClicked(e){
        e.preventDefault();
        this.setState({
            openSignUpModal:true,
            openLoginModal:false
        })
    }

    //todo: open about modal
    /**
     * Handle About click event
     * @param {object} e event object
     * */
    handleOnAboutClicked(e){
        e.preventDefault();

    }
}