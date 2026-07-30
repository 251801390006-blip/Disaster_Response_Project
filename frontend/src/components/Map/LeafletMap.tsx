
import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";

// Fix Leaflet default marker icon issue in React
delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png",
  iconUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png",
  shadowUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png",
});

interface MarkerData {
  id: string;
  latitude: number;
  longitude: number;
  title: string;
  description?: string;
  type?: "shelter" | "volunteer" | "disaster";
}

interface MapProps {
  markers?: MarkerData[];
  center?: [number, number];
  zoom?: number;
  height?: string;
  showGPS?: boolean;
}

const LocationMarker = () => {
  const [position, setPosition] = useState<L.LatLng | null>(null);
  const map = useMap();

  useEffect(() => {
    map.locate().on("locationfound", function (e) {
      setPosition(e.latlng);
      map.flyTo(e.latlng, map.getZoom());
    });
  }, [map]);

  return position === null ? null : (
    <Marker position={position}>
      <Popup>You are here</Popup>
    </Marker>
  );
};

export const LeafletMap: React.FC<MapProps> = ({ 
  markers = [], 
  center = [17.6868, 83.2185], // Default GVMC Visakhapatnam coordinates
  zoom = 12, 
  height = "400px",
  showGPS = false
}) => {
  return (
    <MapContainer center={center} zoom={zoom} style={{ height, width: "100%", zIndex: 1, borderRadius: "0.5rem" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; <a href=`"https://www.openstreetmap.org/copyright`">OpenStreetMap</a> contributors"
      />
      
      {showGPS && <LocationMarker />}
      
      {markers.map((marker) => (
        <Marker key={marker.id} position={[marker.latitude, marker.longitude]}>
          <Popup>
            <div className="text-sm">
              <strong className="block mb-1">{marker.title}</strong>
              {marker.description && <span className="text-gray-600">{marker.description}</span>}
            </div>
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

