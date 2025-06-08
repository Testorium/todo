"use client";

import { useState } from "react";
import {
  TextInput,
  PasswordInput,
  Button,
  Text,
  Paper,
  Divider,
  Stack,
} from "@mantine/core";
import { useForm } from "@mantine/form";
import { useRouter } from "next/navigation";
import { apiClient } from "@/shared/api/api-client";

export default function LoginForm() {
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const form = useForm({
    initialValues: {
      username: "",
      password: "",
    },
  });

  const handleSubmit = async (values: typeof form.values) => {
    setLoading(true);
    try {
      const response = await apiClient.post("/auth/login", values);
      router.push("/todo");
    } catch (error: any) {
      console.error("Login error:", error.response?.data || error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        padding: "1rem",
      }}
    >
      <Paper radius="md" p="xl" withBorder shadow="md" w={400}>
        <Text size="lg" fw={500} ta="center" mb="md">
          Login
        </Text>

        <Divider my="lg" />

        <form onSubmit={form.onSubmit(handleSubmit)}>
          <Stack>
            <TextInput
              required
              label="Username"
              placeholder="username"
              {...form.getInputProps("username")}
            />

            <PasswordInput
              required
              label="Password"
              placeholder="Your password"
              {...form.getInputProps("password")}
            />

            <Button type="submit" fullWidth loading={loading}>
              Sign in
            </Button>
          </Stack>
        </form>
      </Paper>
    </div>
  );
}
