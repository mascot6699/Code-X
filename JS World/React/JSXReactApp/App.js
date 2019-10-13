import React, { Component } from 'react';

class App extends Component{
    render(){
        return(
            <div>
                <Header/>
                <Content/>
            </div>
    );
    }
}

class Header extends React.Component {
    render() {
        var myStyle = {
            fontSize: 40,
            color: '#ff891c'
        }
        return (
            <h1 style = {myStyle}>Hello World</h1>
        );
    }
}

class Content extends React.Component {
    render() {
        return (
            <div>
                <h2>Content</h2>
                <p>{1+1} => I can do use javascript expressions</p>
            </div>
        );
    }
}

export default App;
