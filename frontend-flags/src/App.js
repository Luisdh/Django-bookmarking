import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import axios from 'axios';
import url from './urls.js';

import List from './components/List.js';

class App extends Component {
  constructor() {
    super();
    this.state = {
      showFlag: false,
      bookmarks: [],
      flag: {}
    };
  }

  getBookmarks = () => {
    axios
      .get('/api/Bookmark')
      .then(res => this.setState({ bookmarks: res.data }))
      .catch(err => console.log('err getting data', err.response.data));
  };

  getFlag = id => {
    axios
      .get(url(`Bookmark/${id}`))
      .then(res => this.setState({ flag: res.data, showFlag: true }))
      .catch(err => console.log(err.response.data));
  };
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <List
          getBookmarks={this.getBookmarks}
          bookmarks={this.state.bookmarks}
        />
      </div>
    );
  }
}

export default App;
