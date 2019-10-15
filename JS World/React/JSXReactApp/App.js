import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class App extends Component{

    constructor() {
        super();
        let r = Math.random() * 100
        let r1 = Math.random() * 100
        let r2 = Math.random() * 100
        this.state = {
            data: [
                {
                    "id":r,
                    "name":"Foo",
                    "age":"20"
                },
                {
                    "id":r1,
                    "name":"Bar",
                    "age":"30"
                },
                {
                    "id":r2,
                    "name":"Baz",
                    "age":"40"
                }
            ],
            letter: "e"
        }
        this.setStateHandler = this.setStateHandler.bind(this);
        this.changeHeaderColour = this.changeHeaderColour.bind(this);
        this.updateLetter = this.updateLetter.bind(this);
        this.textPickerFn = this.textPickerFn.bind(this);
    }

    setStateHandler() {
        let r = Math.random() * 100
        let newItem = {
            "id": r,
            "name": "Foo",
            "age": "20"
        }
        var oldArray = this.state.data.slice();
        oldArray.push(newItem);
        this.setState({data: oldArray})
    };

    changeHeaderColour() {
        function getRandomColor() {
            var letters = '0123456789ABCDEF';
            var color = '#';
            for (var i = 0; i < 6; i++) {
                color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
        }
        var heading = document.getElementById('heading');
        ReactDOM.findDOMNode(heading).style.color = getRandomColor();
    };

    updateLetter(e) {
        this.setState({letter: e.target.value});
    }

    textPickerFn(e) {
        this.setState({letter: e.target.innerHTML});
    };

    render(){
        return(
            <div>
                <Header/>
                <button onClick = {this.setStateHandler}>Add Row</button>
                <button onClick = {this.changeHeaderColour}>Change Header Colour</button>
                <br/>
                <p>Whatever you will input will be tripled</p>
                <input type = "text" value={this.state.letter} onChange={this.updateLetter} />
                <br/>
                <h4>Tripler fn with param "{this.state.letter}" returns back</h4>
                <h4 id='triple-letter-answer'>{this.props.tripler(this.state.letter)}</h4>
                <table>
                    <tbody>
                    {this.state.data.map((person, i) => <TableRow key={i} data={person} fn={this.textPickerFn} />)}
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
            <h1 id='heading' style = {myStyle}>
                {this.props.headerProp}
            </h1>
        );
    }
}

class TableRow extends React.Component {
    render() {
        return (
            <tr>
                <td>{this.props.data.id + this.props.data.id}</td>
                <td>{this.props.data.name}</td>
                <td onClick={this.props.fn}>{this.props.data.age}</td>
            </tr>
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
