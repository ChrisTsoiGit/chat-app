import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { processResult } from "immer/dist/internal";

// Define a service using a base URL and expected endpoints:
export const usersApi = createApi({
  reducerPath: "users",
  baseQuery: process.env.REACT_APP_API_HOST,
  endpoints: (builder) => ({
    getUsers: builder.query({
      query: () => "/api/users/",
      //  query: (id) => "/api/users/" + id,
    }),
  }),
});

// Export hooks for usage in functional components, which are
// auto-generated based on the defined endpoints:
export const { useGetUsersQuery } = usersApi;
// export const { useGetUserByIdQuery } = userApi;
