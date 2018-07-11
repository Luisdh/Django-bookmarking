import React, { Component } from 'react';

import Flag from './Flag.js';

class List extends Component {
  ComponentWillMount() {
    this.props.getBookmarks();
  }

  render() {
    const { bookmarks, getBookmarks } = this.props;

    const pins = bookmarks.map((bookmark, index) => {
      return (
        <Flag
          key={index}
          index={index}
          bookmark={bookmark}
          getBookmarks={getBookmarks}
        />
      );
    });

    return <div>{pins}</div>;
  }
}

export default List;
