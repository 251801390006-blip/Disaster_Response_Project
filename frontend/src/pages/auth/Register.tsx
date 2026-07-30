
import React, { useState } from "react";

export const Register = () => {
  const [role, setRole] = useState("citizen"); // or volunteer
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Register for SafeHarbor AI</h1>
      <div className="flex gap-4 mb-4">
        <button onClick={() => setRole("citizen")} className={`px-4 py-2 rounded ${role === "citizen" ? "bg-blue-600 text-white" : "bg-gray-200"}`}>Citizen</button>
        <button onClick={() => setRole("volunteer")} className={`px-4 py-2 rounded ${role === "volunteer" ? "bg-blue-600 text-white" : "bg-gray-200"}`}>Volunteer</button>
      </div>
      <form className="max-w-md">
        {/* Registration fields based on role */}
      </form>
    </div>
  );
};

