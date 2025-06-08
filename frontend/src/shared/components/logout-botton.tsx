"use client";

import { apiClient } from "@/shared/api/api-client";
import { Button, Paper } from "@mantine/core";
import { useRouter } from "next/navigation";
import useUser from "../hooks/use-user.hook";

export default function LogoutButton() {
  const { user } = useUser();
  const router = useRouter();

  const handleLogout = async () => {
    try {
      await apiClient.post("/auth/logout");
      router.replace("/login");
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  return (
    <Paper radius="md" p="lg" withBorder shadow="sm">
      <Button
        size="compact-sm"
        variant="filled"
        color="indigo"
        onClick={handleLogout}
      >
        Logout, {user?.firstName}
      </Button>
    </Paper>
  );
}
