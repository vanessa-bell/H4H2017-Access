import React from 'react';
import RaisedButton from 'material-ui/RaisedButton';
import { Link } from 'react-router';
import reachLogo from '../../img/withinreachlogo.png';

/* component styles */
import { styles, hero__title, hero__description, btn, img } from './styles.scss';
// TODO create method for Get Started
export const Home = () =>
    <section className={`${styles}`}>
        <div className="container">
            <div>
                <img height='300' src={reachLogo} className={`${img}`} alt="within reach logo" />

            </div>
            <h5 className={`${hero__description}`}>
                we believe access to birth control <br /> should always be within reach
            </h5>
            <div className="hero__cta">
                <Link to="/find-a-pharmacy">
                    <RaisedButton
                      style={{ marginTop: 50, marginRight: 150}}
                      label="Get Access"
                    />

                </Link>
                <RaisedButton
                  style={{ marginTop: 50 }}
                  label="Help Others"
                />
            </div>
        </div>
    </section>;
