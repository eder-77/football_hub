import { useState, useEffect } from 'react'

function App() {
  const [tournaments, setTournaments] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null) // 👈 Track connection errors

  useEffect(() => {
    // Make sure this matches your exact Django URL address!
    fetch('http://127.0.0.1:8000/api/tournaments/') 
      .then(response => {
        if (!response.ok) {
          // If Django returns a 404 or 500 error, catch it here
          throw new Error(`Server responded with status ${response.status}. URL mismatch?`);
        }
        return response.json()
      })
      .then(data => {
        setTournaments(data)
        setLoading(false)
      })
      .catch(err => {
        console.error('Error fetching tournaments:', err)
        setError(err.message) // 👈 Display the exact network failure message
        setLoading(false)
      })
  }, [])

  return (
    <div style={{ padding: '30px', fontFamily: 'Arial, sans-serif', maxWidth: '800px', margin: '0 auto' }}>
      <header style={{ borderBottom: '2px solid #eee', paddingBottom: '10px', marginBottom: '20px' }}>
        <h1>🏆 Football Hub Dashboard</h1>
      </header>

      <h2>Active Tournaments</h2>
      
      {loading ? (
        <p>Connecting to backend data server...</p>
      ) : error ? (
        // 🚨 This will tell us EXACTLY what broke!
        <div style={{ padding: '20px', backgroundColor: '#ffdada', color: '#c0392b', borderRadius: '8px', border: '1px solid #ebccd1' }}>
          <h3 style={{ margin: '0 0 10px 0' }}>❌ Connection Error Detected</h3>
          <p><strong>Details:</strong> {error}</p>
          <p style={{ fontSize: '14px', marginTop: '15px', color: '#333' }}>
            <strong>Quick Check:</strong> Open your Django endpoint directly by clicking here: <a href="http://127.0.0.1:8000/api/tournaments/" target="_blank" rel="noreferrer">http://127.0.0.1:8000/api/tournaments/</a>. Do you see your tournament data inside brackets <code>[]</code>, or a webpage error?
          </p>
        </div>
      ) : tournaments.length === 0 ? (
        <p style={{ color: '#666' }}>No rooms created yet. Go to your API dashboard to submit one!</p>
      ) : (
        <div style={{ display: 'grid', gap: '15px', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))' }}>
          {tournaments.map(tournament => (
            <div key={tournament.id} style={{ border: '1px solid #ddd', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)' }}>
              <h3 style={{ margin: '0 0 10px 0', color: '#2c3e50' }}>{tournament.name}</h3>
              <p style={{ margin: 0, color: '#7f8c8d' }}>
                <strong>Format:</strong> {tournament.format}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default App