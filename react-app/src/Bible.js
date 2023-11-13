import React, {useState, useEffect} from 'react'

const Bible = () => {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/verse").then(
      res => res.text()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  // Create a function to safely render HTML
  const renderHTML = (html) => ({ __html: html })

  return ( 
    <div>
      {(typeof data === 'undefined') ? (
        <p> Loading ... </p>
      ) : (
        <p dangerouslySetInnerHTML={renderHTML(data)}></p>
      )}
    </div>
  )
};

export default Bible;
