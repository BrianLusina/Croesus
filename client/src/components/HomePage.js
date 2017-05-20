/**
 * Created by lusinabrian on 05/05/17.
 */
import React, { Component } from 'react';

export default class HomePage extends Component{
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
                        <a className="bp-nav__item bp-icon bp-icon--prev" href="" data-info="Login">
                            <span>Login</span>
                        </a>

                        <a className="bp-nav__item bp-icon bp-icon--drop" href="" data-info="Sign Up">
                            <span>Sign Up</span>
                        </a>

                        <a className="bp-nav__item bp-icon bp-icon--archive" href="" data-info="About">
                            <span>About</span>
                        </a>
                    </nav>
                </header>

                <img className="poster" src="" alt="img01" />

		</div>
        )
    }

    /**
     * Open login modal
     * @param {Object} e
     * */
    handleOnLoginClick(e){

    }
}