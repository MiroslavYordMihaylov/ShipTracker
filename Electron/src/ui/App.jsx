import './App.css'
import "leaflet/dist/leaflet.css"
import { MapContainer, TileLayer } from 'react-leaflet'


function App() {

  const cartoApiKey = import.meta.env.VITE_CARTO_API_KEY 

  return (
    <MapContainer 
      center={[51.505, -0.09]} 
      zoom={3} 
      scrollWheelZoom={true}
      style={{ height: "100vh", width: "100%" }}
    >
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
        url={`https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png?key=${cartoApiKey}`}
      />

    </MapContainer>
  );
}

export default App