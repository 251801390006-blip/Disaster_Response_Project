
import { apiClient } from "./axios";

export const shelterApi = {
  getAll: async (params?: any) => {
    const response = await apiClient.get("/shelters", { params });
    return response.data;
  },
  getById: async (id: string) => {
    const response = await apiClient.get(`/shelters/${id}`);
    return response.data;
  },
  create: async (data: any) => {
    const response = await apiClient.post("/shelters", data);
    return response.data;
  },
  update: async (id: string, data: any) => {
    const response = await apiClient.put(`/shelters/${id}`, data);
    return response.data;
  },
  delete: async (id: string) => {
    const response = await apiClient.delete(`/shelters/${id}`);
    return response.data;
  },
  uploadImage: async (id: string, file: File) => {
    const formData = new FormData();
    formData.append("file", file);
    const response = await apiClient.post(`/shelters/${id}/images`, formData, {
      headers: { "Content-Type": "multipart/form-data" }
    });
    return response.data;
  }
};

