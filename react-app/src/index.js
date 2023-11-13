import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Bible from './Bible';
import Word from './Word';
import Poem from './Poem';
import VOO from './VOO';
import AMZN from './AMZN';
import AMD from './AMD';
import SQQQ from './sQQQ';
import QQQ from './QQQ';
import TSLA from './TSLA';
import DateTimeDisplay from './DateTimeDisplay';

const poem = ReactDOM.createRoot(document.getElementById('poem_otd'));
poem.render(
  <React.StrictMode>
    <Poem />
  </React.StrictMode>
);

const bible = ReactDOM.createRoot(document.getElementById('bible_verse_otd'));
bible.render(
  <React.StrictMode>
    <Bible />
  </React.StrictMode>
);

const word = ReactDOM.createRoot(document.getElementById('word_otd'));
word.render(
  <React.StrictMode>
    <Word />
  </React.StrictMode>
);

const voo1 = ReactDOM.createRoot(document.getElementById('VOO'));
voo1.render(
  <React.StrictMode>
    <VOO />
  </React.StrictMode>
);

const amzn1 = ReactDOM.createRoot(document.getElementById('AMZN'));
amzn1.render(
  <React.StrictMode>
    <AMZN />
  </React.StrictMode>
);

const amd1 = ReactDOM.createRoot(document.getElementById('AMD'));
amd1.render(
  <React.StrictMode>
    <AMD />
  </React.StrictMode>
);

const TSLA1 = ReactDOM.createRoot(document.getElementById('TSLA'));
TSLA1.render(
  <React.StrictMode>
    <TSLA />
  </React.StrictMode>
);

const sQQQ1 = ReactDOM.createRoot(document.getElementById('sQQQ'));
sQQQ1.render(
  <React.StrictMode>
    <SQQQ />
  </React.StrictMode>
);

const QQQ1 = ReactDOM.createRoot(document.getElementById('QQQ'));
QQQ1.render(
  <React.StrictMode>
    <QQQ />
  </React.StrictMode>
);

const dateTime = ReactDOM.createRoot(document.getElementById('dateTimeDisplay'));
dateTime.render(
  <React.StrictMode>
    <DateTimeDisplay />
  </React.StrictMode>
);
