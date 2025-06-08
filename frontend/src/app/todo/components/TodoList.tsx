"use client";
import { useEffect, useState } from "react";
import { Paper, Stack, Divider } from "@mantine/core";
import PageLoader from "@/shared/components/page-loader";
import { Todo } from "../types";
import { createTodo, deleteTodo, getTodos, updateTodo } from "../api";
import TodoStats from "./TodoStats";
import TodoForm from "./TodoForm";
import TodoItem from "./TodoItem";

export default function TodoList() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTodos = async () => {
      setLoading(true);
      try {
        const data = await getTodos();
        setTodos(data);
      } catch (err) {
        console.error("Failed to fetch todos", err);
      } finally {
        setLoading(false);
      }
    };

    fetchTodos();
  }, []);

  const handleAdd = async (text: string) => {
    try {
      const created = await createTodo(text);
      setTodos((prev) => [...prev, created]);
    } catch (err) {
      console.error("Add failed", err);
    }
  };

  const handleToggle = async (todo: Todo) => {
    try {
      const updated = await updateTodo(todo.id, {
        isCompleted: !todo.isCompleted,
      });
      setTodos((prev) => prev.map((t) => (t.id === updated.id ? updated : t)));
    } catch (err) {
      console.error("Toggle failed", err);
    }
  };

  const handleUpdate = async (id: number, text: string) => {
    try {
      const updated = await updateTodo(id, { text });
      setTodos((prev) => prev.map((t) => (t.id === id ? updated : t)));
    } catch (err) {
      console.error("Update failed", err);
    }
  };

  const handleDelete = async (id: number) => {
    try {
      await deleteTodo(id);
      setTodos((prev) => prev.filter((t) => t.id !== id));
    } catch (err) {
      console.error("Delete failed", err);
    }
  };

  if (loading) return <PageLoader />;

  return (
    <Paper p="lg" withBorder shadow="sm" radius="md">
      <TodoStats todos={todos} />
      <TodoForm onAdd={handleAdd} />
      <Divider my="md" />
      <Stack gap="sm">
        {todos.length === 0 ? (
          <p style={{ textAlign: "center", color: "#999" }}>
            No tasks yet. Add one above!
          </p>
        ) : (
          todos.map((todo) => (
            <TodoItem
              key={todo.id}
              todo={todo}
              onToggle={handleToggle}
              onDelete={handleDelete}
              onUpdate={handleUpdate}
            />
          ))
        )}
      </Stack>
    </Paper>
  );
}
