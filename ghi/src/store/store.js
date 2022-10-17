import { configureStore } from "@reduxjs/toolkit";
import { usersApi } from "./usersApi";

// create a Redux store:
export const store = configureStore({
  reducer: {
    [usersApi.reducerPath]: usersApi.reducer,
  },
});
