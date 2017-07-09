import React from 'react';

/* components */
import { Home } from '../../components/Home';
import { GetStarted } from '../../components/GetStarted';
import { DidYouKnow } from '../../components/DidYouKnow';

export const HomeContainer = () =>
    <section>
        <Home />
        <DidYouKnow />
        <GetStarted />
    </section>
