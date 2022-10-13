import React from "react";
import { render } from "react-dom";
import App from './App';

import { createRoot } from 'react-dom/client';

const container = document.getElementById('app');

const root = createRoot(container);

// App.addUrl();

root.render(<App tab="home" />);