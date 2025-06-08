"use client";

import { useContext } from "react";
import { UserContext } from "@/shared/providers/auth/user-context";

export default function useUser() {
  return useContext(UserContext);
}
