import React, { useEffect, useState } from 'react'

const App = () => {
  const [data, setData] = useState({ point: [] })

  useEffect(() =>{
    fetch("/point")
      .then(res => res.json())
      .then(data => {
        setData(data)
        console.log(data)
      })
  }, [])

  return (
    <div>
      <h1>First</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre> 

      
    </div>
  )
  
}

export default App
