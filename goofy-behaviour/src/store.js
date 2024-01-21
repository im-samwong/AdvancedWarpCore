import { create } from "zustand";

export const convertRankNum = {
  'I': 3,
  'II': 2,
  'III': 1,
  'IV': 0,
};

export const convertRankName = {
  'Ash': 2,
  'Bronze': 5,
  'Silver': 9,
  'Gold': 13,
  'Iridescent': 18
};

export const convertModelType = {
  'More Killers': '0',
  'More Survivors': '1',
  'Adapted': '2'
}

export const convertPlayer = {
  true: 'Survivor',
  false: 'Killer'
}

const useStore = create((set) => ({
  // State variables
  time: "12:00:00",
  day: "Mon",
  rankName: "Ash",
  rankNum: "I",
  modelType: "More Killers",
  server: "us-west-2",
  partySize: "1",
  isSurvivor: true,
  displayStain: false,
  joiningGameState: false,
  estimatedTime: 0,

  // Functions to update state variables
  setTime: (newTime) => set(() => ({ time: newTime })),
  setDay: (newDay) => set(() => ({ day: newDay })),
  setRankName: (newRankName) => set(() => ({ rankName: newRankName })),
  setRankNum: (newRankNum) => set(() => ({ rankNum: newRankNum })),
  setModelType: (newModelType) => set(() => ({ modelType: newModelType })),
  setServer: (newServer) => set(() => ({ server: newServer })),
  setPartySize: (newPartySize) => set(() => ({ partySize: newPartySize })),
  setJoiningGameState: (newJoiningGameState) => set(() => ({ joiningGameState: newJoiningGameState })),
  setEstimatedTime: (newEstimatedTime) => set(() => ({ estimatedTime: newEstimatedTime })),
  toggleClass: () => {
    set((state) => ({ isSurvivor: !state.isSurvivor }));
    set((state) => ({ displayStain: !state.displayStain }));
    setTimeout(() => {
      set((state) => ({ displayStain: !state.displayStain }));
    }, 200);
  },
  setDisplayStain: () => set((state) => ({ displayStain: !state.displayStain })),
}));

export default useStore;
