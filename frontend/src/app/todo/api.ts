import { apiClient } from "@/shared/api/api-client";
import { Todo } from "./types";

export async function getTodos(): Promise<Todo[]> {
  const { data } = await apiClient.get("/todos");
  return data;
}

export async function deleteTodo(id: number): Promise<void> {
  await apiClient.delete(`/todos/${id}`);
}

export async function createTodo(text: string): Promise<Todo> {
  const { data } = await apiClient.post("/todos", { text });
  return data;
}

export async function updateTodo(
  id: number,
  update: Partial<Todo>
): Promise<Todo> {
  const { data } = await apiClient.patch(`/todos/${id}`, update);
  return data;
}
