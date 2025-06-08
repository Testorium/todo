"use client";

import React, { useEffect, useState } from "react";
import PageLoader from "@/shared/components/page-loader";
import { UserContext } from "./user-context";
import { UserType } from "@/shared/types/user.type";
import { apiClient } from "@/shared/api/api-client";
import { useRouter } from "next/navigation";

const UserProfile = ({ children }: { children: React.ReactNode }) => {
  const [user, setUser] = useState<UserType | undefined>(undefined);
  const [loading, setLoading] = useState(true);

  const router = useRouter();

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const { data } = await apiClient.get("/users/me");
        setUser(data);
      } catch (error) {
        router.replace("/login");
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, []);

  if (loading) return <PageLoader />;

  return (
    <UserContext.Provider value={{ user }}>{children}</UserContext.Provider>
  );
};

export default UserProfile;
