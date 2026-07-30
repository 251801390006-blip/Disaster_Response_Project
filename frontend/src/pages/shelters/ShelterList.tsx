
import React, { useEffect } from "react";
import { useShelterStore } from "../../store/slices/shelterSlice";
import { shelterApi } from "../../api/shelterApi";
import { Link } from "react-router-dom";

export const ShelterList = () => {
  const { shelters, setShelters, loading, setLoading, setError, error } = useShelterStore();

  useEffect(() => {
    const fetchShelters = async () => {
      setLoading(true);
      try {
        const data = await shelterApi.getAll();
        setShelters(data);
      } catch (err: any) {
        setError(err.message || "Failed to fetch shelters");
      } finally {
        setLoading(false);
      }
    };
    fetchShelters();
  }, [setLoading, setShelters, setError]);

  return (
    <div className="p-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Shelters</h1>
        <Link to="/shelters/new" className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Add Shelter</Link>
      </div>
      
      {/* Search and Filter Placeholders */}
      <div className="bg-white p-4 rounded shadow mb-6 flex gap-4">
        <input type="text" placeholder="Search shelters..." className="border p-2 rounded w-full max-w-sm" />
        <select className="border p-2 rounded"><option>All Zones</option></select>
        <select className="border p-2 rounded"><option>All Statuses</option></select>
      </div>

      {loading ? (
        <p>Loading shelters...</p>
      ) : error ? (
        <p className="text-red-500">{error}</p>
      ) : shelters.length === 0 ? (
        <div className="text-center p-12 bg-white rounded shadow text-gray-500">No shelters found.</div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {shelters.map(shelter => (
            <div key={shelter.id} className="bg-white p-6 rounded shadow hover:shadow-md transition">
              <h3 className="text-xl font-bold">{shelter.name}</h3>
              <p className="text-sm text-gray-500 mb-2">{shelter.code} | {shelter.zone}</p>
              <div className="flex justify-between mt-4">
                <span className={`px-2 py-1 rounded text-xs font-bold ${shelter.status === "Open" ? "bg-green-100 text-green-800" : "bg-red-100 text-red-800"}`}>
                  {shelter.status}
                </span>
                <span className="text-sm">Cap: {shelter.max_capacity}</span>
              </div>
              <Link to={`/shelters/${shelter.id}`} className="mt-4 block text-center text-blue-600 border border-blue-600 rounded py-1 hover:bg-blue-50">View Details</Link>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

