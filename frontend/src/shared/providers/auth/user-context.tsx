import { createContext } from "react";
import { UserProviderType } from "@/shared/types/user.type";

export const UserContext = createContext<UserProviderType>({
  user: undefined,
});
