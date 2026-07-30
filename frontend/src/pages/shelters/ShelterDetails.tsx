
import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { shelterApi } from "../../api/shelterApi";

export const ShelterDetails = () => {
  const { id } = useParams<{ id: string }>();
  const [shelter, setShelter] = useState<any>(null);

  useEffect(() => {
    if (id) {
      shelterApi.getById(id).then(setShelter).catch(console.error);
    }
  }, [id]);

  if (!shelter) return <div className="p-8">Loading details...</div>;

  return (
    <div className="p-8 max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">{shelter.name}</h1>
        <Link to={`/shelters/${id}/edit`} className="bg-gray-200 px-4 py-2 rounded">Edit</Link>
      </div>
      <div className="bg-white p-6 rounded shadow mb-6">
        <h2 className="text-xl font-semibold mb-4">Capacity Overview</h2>
        <div className="flex justify-between border-b pb-4">
          <div><p className="text-gray-500">Max</p><p className="text-2xl">{shelter.max_capacity}</p></div>
          <div><p className="text-gray-500">Occupied</p><p className="text-2xl">{shelter.current_occupancy}</p></div>
          <div><p className="text-gray-500">Available</p><p className="text-2xl text-green-600">{shelter.available_capacity}</p></div>
        </div>
      </div>
      {/* Cloudinary Gallery Placeholder */}
      <div className="bg-white p-6 rounded shadow">
        <h2 className="text-xl font-semibold mb-4">Gallery</h2>
        <div className="grid grid-cols-4 gap-4">
           {shelter.images?.map((img: any) => (
             <img key={img.id} src={img.url} alt="shelter" className="w-full h-32 object-cover rounded" />
           ))}
        </div>
      </div>
    </div>
  );
};

