
import { apiClient } from "./axios";

export const authApi = {
  login: async (credentials: any) => {
    const response = await apiClient.post("/auth/login", credentials);
    return response.data;
  },
  register: async (userData: any) => {
    const response = await apiClient.post("/auth/register", userData);
    return response.data;
  },
  getProfile: async () => {
    const response = await apiClient.get("/users/me");
    return response.data;
  },
  updateProfile: async (data: any) => {
    const response = await apiClient.put("/users/me", data);
    return response.data;
  }
};

