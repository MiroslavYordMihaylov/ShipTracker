import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <main style={{ textAlign: 'center', padding: '4rem 2rem' }}>
        <h1>Welcome</h1>
        <p>
          Edit <code>src/App.jsx</code> and save to test changes.
        </p>
        <button
          type="button"
          onClick={() => setCount((count) => count + 1)}
          style={{ marginTop: '1rem', padding: '0.6rem 1.2rem', cursor: 'pointer' }}
        >
          Count is {count}
        </button>
      </main>
    </>
  )
}

export default App
