var ReactDOM = require('react-dom');

import React, {Component} from 'react'
import {BrowserRouter, Route, Link, Switch} from 'react-router-dom'
import {format_date} from 'moment'

import axios from 'axios';

class Task extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            task: []
        };
        this.handleSubmitPatch = this.handleSubmitPatch.bind(this);
    }

    loadTask(task_id) {
        fetch(`/api/task/${task_id}/`)
            .then(response => response.json())
            .then(data => {
                this.setState(data)
            });
    }

    componentDidMount() {
        this.loadTask(this.props.match.params['task_id']);
    }

    async handleSubmitPatch(event) {
        event.preventDefault();
        await axios({
            method: 'patch',
            url: '/api/task/' + this.props.match.params['task_id'] + '/',
            data: {is_ready: true},
            headers: {
                responseType: 'json',
            }
        })
        this.setState({is_ready: true});

    }

    render() {
        console.log(this.state);
        const {taskname, tasktext, date, is_imp, is_ready} = this.state;
        return (
            <div className="task">
                <h4>Task: {taskname}</h4>
                <p>Content: {tasktext}</p>
                <p>Started on {date}</p>
                <p>Is it important?{is_imp ? (' Important!'):(' No.')}</p>
                <p>Status: {is_ready ? ('Closed') : ('Opened')} </p>
                {is_ready == false ? (
                    <form onSubmit={this.handleSubmitPatch}>
                        <input type="submit" value="Complete task"/>
                    </form>
                ) : (
                    ''
                )}
                <Link to="/">Back</Link>
            </div>
        );
    }
}

class List extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        console.log(this.props.tasks);
        return (
            <div>
                {this.props.tasks ? (
                    <ul className="content-list">
                        {this.props.tasks.map((task, i) => (
                            <li key={i}>
                                <Link to={`/${task.id}`}>{task.taskname}</Link>
                            </li>
                        ))}
                    </ul>
                ) : (<p>Sorry, tasks are not created.</p>)}

            </div>
        );
    }
}

class AddTaskClass extends React.Component {

    constructor(props) {
        super(props);
        this.state = {taskname: '', tasktext: '', formFields: []};

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    async handleSubmit(event) {
        event.preventDefault();
        let formFields = {taskname: this.state.taskname, tasktext: this.state.tasktext, is_ready: false, is_imp: false};
        await axios({
            method: 'post',
            url: '/api/task/',
            data: formFields,
            headers: {
                responseType: 'json',
            }
        })
        this.setState({taskname: '', tasktext: '', formFields: []});
        await this.loadTasks();
    }

    handleChange(event) {
        const name = event.target.name;

        this.setState({
            [name]: event.target.value
        });
    }

    render() {
        return (
            <div>
                <p>Add new task</p>

                <form onSubmit={this.handleSubmit}>
                    <label>
                        Name:
                        <input type="text" name="taskname" value={this.state.taskname} onChange={this.handleChange}/>
                    </label><br/>
                    <label>
                        Description:
                        <input type="text" name="tasktext" value={this.state.tasktext} onChange={this.handleChange}/>
                    </label><br/>
                    <input type="submit" value="Create task"/>
                </form>
                <Link to={'/'}>Back</Link>

            </div>
        )
    }
}

class IndexPageClass extends React.Component {

    constructor(props) {
        super(props);
        this.state = {tasks: []};
    }

    async loadTasks() {
        console.log('loading tasks');
        this.setState({
            tasks: await fetch("/api/task/").then(response => response.json())
        });
    }

    componentDidMount() {
        this.loadTasks();
    }

    render() {
        return (
            <div>
                <Link to={`/add`}>Add new</Link>
                <div ref="myRef">
                    <List tasks={this.state.tasks}/>
                </div>
            </div>
        );
    }
}


const Main = () => (
    <BrowserRouter>
        <main>
            <Switch>
                <Route exact path='/' component={IndexPageClass}/>
                <Route exact path='/add' component={AddTaskClass}/>
                <Route path='/:task_id' component={Task}/>
            </Switch>
        </main>
    </BrowserRouter>
);


ReactDOM.render(<Main/>, document.getElementById('app'));