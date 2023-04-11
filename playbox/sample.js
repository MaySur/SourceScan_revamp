import React, { useEffect, useState } from 'react'

const App = () => {
  const [keyword, setKeyword] = useState("")
  const [data, setData] = useState({ point: [] })
  const [submittedKeyword, setSubmittedKeyword] = useState("")

  const sendData = () =>{
    fetch("/point", {
      method: 'POST',
      body: JSON.stringify({stateVariable: submittedKeyword}),
      headers: {
        'Content-Type': 'application/json'
      }




    })
  }


  useEffect(() =>{
    fetch("/point")
      .then(res => res.json())
      .then(data => {
        setData(data)
        console.log(data)
      })
  }, [])
   const handleSubmit = (event)=>{
    event.preventDefault()
    setSubmittedKeyword(keyword)
   }

  return (
    <div>
      <h1>First</h1>
        <form onSubmit={handleSubmit}>
          <label>Enter the Keyword: 
            <input style={{marginLeft: 10}} type="text" value={keyword} onChange={(e) => setKeyword(e.target.value)}/>
          </label>
            <input type="submit" />
        
        </form>

      <pre>{data.point.map(i => (
        <li key={i['subreddit']}>
        <p> Subreddit: </p>

        </li>
      ))}</pre>
      <h2>Keyword: {submittedKeyword}</h2> 

      
    </div>
  )
  
}

export default App
