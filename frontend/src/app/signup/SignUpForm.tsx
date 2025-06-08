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
  Group,
  Anchor,
} from "@mantine/core";
import { useForm } from "@mantine/form";
import { useRouter } from "next/navigation";
import { apiClient } from "@/shared/api/api-client";
import Link from "next/link";

export default function SignUpForm() {
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const form = useForm({
    initialValues: {
      username: "",
      password: "",
      firstName: "",
      lastName: "",
    },
  });

  const handleSubmit = async (values: typeof form.values) => {
    setLoading(true);
    try {
      await apiClient.post("/auth/register", values);
      router.push("/login");
    } catch (error: any | unknown) {
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
          Sign Up
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

            <TextInput
              required
              label="First name"
              placeholder="First name"
              {...form.getInputProps("firstName")}
            />

            <TextInput
              required
              label="Last name"
              placeholder="Last name"
              {...form.getInputProps("lastName")}
            />

            <Button type="submit" fullWidth loading={loading}>
              Sign Up
            </Button>
            <Group justify="center">
              <Text size="sm" c="dimmed">
                Don't have an account?{" "}
                <Anchor component={Link} href="/signup" size="sm">
                  Sign up
                </Anchor>
              </Text>
            </Group>
          </Stack>
        </form>
      </Paper>
    </div>
  );
}
