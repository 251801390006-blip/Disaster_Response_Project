
import React from "react";
import { useAuthStore } from "../../store/slices/authSlice";
import { useNavigate } from "react-router-dom";

export const Profile = () => {
  const { user, logout } = useAuthStore();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <div className="p-8 max-w-2xl mx-auto">
      <div className="bg-white p-6 rounded-lg shadow-md">
        <h1 className="text-3xl font-bold mb-4">User Profile</h1>
        <div className="mb-4">
          <p className="text-gray-600"><strong>Name:</strong> {user?.full_name}</p>
          <p className="text-gray-600"><strong>Email:</strong> {user?.email}</p>
          <p className="text-gray-600"><strong>Role:</strong> <span className="uppercase font-semibold text-blue-600">{user?.role}</span></p>
        </div>
        <button onClick={handleLogout} className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">
          Logout
        </button>
      </div>
    </div>
  );
};

