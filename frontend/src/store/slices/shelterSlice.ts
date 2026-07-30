
import { create } from "zustand";

interface ShelterState {
  shelters: any[];
  selectedShelter: any | null;
  loading: boolean;
  error: string | null;
  filters: any;
  setShelters: (shelters: any[]) => void;
  setSelectedShelter: (shelter: any) => void;
  setFilters: (filters: any) => void;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
}

export const useShelterStore = create<ShelterState>((set) => ({
  shelters: [],
  selectedShelter: null,
  loading: false,
  error: null,
  filters: {},
  setShelters: (shelters) => set({ shelters }),
  setSelectedShelter: (selectedShelter) => set({ selectedShelter }),
  setFilters: (filters) => set({ filters }),
  setLoading: (loading) => set({ loading }),
  setError: (error) => set({ error })
}));

