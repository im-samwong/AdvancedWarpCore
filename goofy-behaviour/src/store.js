import { create } from "zustand";

const useStore = create((set) => ({
  // State variables
  time: "",
  day: "Mon",
  rankName: "Ash",
  rankNum: "1",
  modelType: "1",
  server: "us-west-2",
  partySize: "1",
  isSurvivor: true,
  displayStain: false,

  // Functions to update state variables
  setTime: (newTime) => set(() => ({ time: newTime })),
  setDay: (newDay) => set(() => ({ day: newDay })),
  setRankName: (newRankName) => set(() => ({ rankName: newRankName })),
  setRankNum: (newRankNum) => set(() => ({ rankNum: newRankNum })),
  setModelType: (newModelType) => set(() => ({ modelType: newModelType })),
  setServer: (newServer) => set(() => ({ server: newServer })),
  setPartySize: (newPartySize) => set(() => ({ partySize: newPartySize })),
  toggleClass: () => {
    set((state) => ({ isSurvivor: !state.isSurvivor }));
    set((state) => ({ displayStain: !state.displayStain }));
    setTimeout(() => {
      set((state) => ({ displayStain: !state.displayStain }));
    }, 200); // 500 milliseconds = 0.5 seconds
  },
  setDisplayStain: () => set((state) => ({ displayStain: !state.displayStain })),

}));

export default useStore;
