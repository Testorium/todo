"use client";

import { useContext } from "react";
import { UserContext } from "@/shared/providers/user/user-context";

export default function useUser() {
  return useContext(UserContext);
}
