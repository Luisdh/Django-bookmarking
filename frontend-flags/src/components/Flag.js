import React, { Component } from 'react';

class Flag extends Component {
  render() {
    const { getBookmarks, flag } = this.props;

    return (
      <div>
        <div>{flag.title}</div>
      </div>
    );
  }
}

export default Flag;
