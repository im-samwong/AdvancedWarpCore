import { create } from 'zustand';

const useStore = create((set) => ({
  isSurvivor: true,
  toggleClass: () => set((state) => ({ isSurvivor: !state.isSurvivor })),
}));

export default useStore;
