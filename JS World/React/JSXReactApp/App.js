import React, { Component } from 'react';

class App extends Component{
    constructor() {
        super();
        this.state = {
            data: [
                {
                    "id":1,
                    "name":"Foo",
                    "age":"20"
                },
                {
                    "id":2,
                    "name":"Bar",
                    "age":"30"
                },
                {
                    "id":3,
                    "name":"Baz",
                    "age":"40"
                }
            ]
        }
    }
    render(){
        return(
            <div>
                <Header/>
                <h3>Tripler fn with param "e" returns back "{this.props.tripler("e")}"</h3>
                <table>
                    <tbody>
                    {this.state.data.map((person, i) => <TableRow key = {i} data = {person} />)}
                    </tbody>
                </table>
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
            <h1 style = {myStyle}>
                {this.props.headerProp}
            </h1>
        );
    }
}

class TableRow extends React.Component {
    render() {
        return (
            <div>
                <tr>
                    <td>{this.props.data.id + this.props.data.id}</td>
                    <td>{this.props.data.name}</td>
                    <td>{this.props.data.age}</td>
                </tr>
            </div>
        );
    }
}

Header.defaultProps = {
    headerProp: "Header Content is from immutable prop",
}

App.defaultProps = {
    tripler: (e) => {
        return e + e + e
    }
}

export default App;
