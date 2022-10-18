import { configureStore } from "@reduxjs/toolkit";
import { usersApi } from "./usersApi";
import { setupListeners } from "@reduxjs/toolkit/query";

// create a Redux store:
export const store = configureStore({
  reducer: {
    [usersApi.reducerPath]: usersApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(usersApi.middleware),
});

// export default store;
setupListeners(store.dispatch);
