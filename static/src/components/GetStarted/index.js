import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import Paper from 'material-ui/Paper';

/* component styles */
import { styles } from './styles.scss';

const style = {
  height: 300,
  width: 600,
  margin: 20,
  textAlign: 'center',
  display: 'inline-block',
};

export const GetStarted = () =>
    <section className={`${styles}`}>
        <Paper style={style} className="col">
            <h1>Transfer </h1>
            <div className="body">
                Switch a refill from your pharmacy to Capsule. <br/> Just give us your info and we'll do all the work.
            </div>
            <div className="sm-pb0 sm-pt3 ">
                <div className="btn btn-primary center btn--mobile-fw bg-red">
                    Help Me
                </div>
            </div>
        </Paper>
        <Paper style={style} className="col">
            <h1>Help Her</h1>
            <div className="body">
                Just tell your doctor to e-prescribe to:
            </div>
            <div className="sm-pb0 sm-pt3">
                <div className="btn btn-primary center btn--mobile-fw bg-red">
                    Learn more
                </div>
            </div>
        </Paper>
    </section>;