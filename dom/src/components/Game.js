import React, { Component } from 'react'
const API_ROOT = 'http://localhost:5000'
const HEADERS = {
  'Content-Type': 'application/json',
  Accept: 'application/json',
}
const Board = ({rows})=> {
  return (
    <table>
      <tbody>
        { rows.map((row, idx )=> <Row key={idx} row={row} />) }
      </tbody>
    </table>
  )
}

const Row = ({row}) => {
  return (
    <tr className='row'>
      { row.map((cell, idx)=> <Cell key={idx} cell={cell} />) }
    </tr>
  )
}

const Cell = ({cell}) => {
  let aliveClass = cell === 1 ? 'alive' : ''
  return (
    <td className={`box ${aliveClass}`}></td>
  )
}

class Game extends Component {
  constructor(props) {
    super(props);
    this.maxIterations = 1000
    this.state = {
      iteration: 1,
      cells: [[]],
    }
  }

  componentDidMount() {
    fetch(`${API_ROOT}/new`)
      .then(res => res.json())
      .then(cells => this.setState({ cells: cells }))
  }

  componentDidUpdate(){
    if(this.state.iteration < this.maxIterations){
      setTimeout(()=> {
        this.tick()
      }, 100)
    }
  }

  tick() {
    fetch(`${API_ROOT}/next`,{
      method: 'POST',
      headers: HEADERS,
      body: JSON.stringify({ board: this.state.cells })
    }).then(res => res.json())
      .then(data => this.setState(prevState =>
        ({cells: data, iteration: prevState.iteration += 1}))
      )
  }

  render() {
    return (
      <div>
        <div className='flex justify-between mb-4'>
          <div>
            <h1 className='text-blue-800 text-lg'>Conway's Game of Life</h1>
            <p>Displaying iteration {this.state.iteration} of {this.maxIterations}</p>
          </div>
          <button className='p-1 bg-blue-100 border border-solid-blue-100' onClick={()=> window.location.reload()}>Restart</button>
        </div>
        <Board rows={this.state.cells} />
      </div>
    )
  }
}

export default Game
