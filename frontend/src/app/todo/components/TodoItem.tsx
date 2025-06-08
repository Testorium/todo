import {
  Paper,
  Group,
  Checkbox,
  ActionIcon,
  TextInput,
  Text,
  Box,
} from "@mantine/core";
import { IconTrash, IconEdit, IconCheck, IconX } from "@tabler/icons-react";
import { useState } from "react";
import { Todo } from "../types";

interface Props {
  todo: Todo;
  onToggle: (todo: Todo) => void;
  onDelete: (id: number) => void;
  onUpdate: (id: number, text: string) => void;
}

export default function TodoItem({
  todo,
  onToggle,
  onDelete,
  onUpdate,
}: Props) {
  const [isEditing, setIsEditing] = useState(false);
  const [editText, setEditText] = useState(todo.text);

  return (
    <Paper
      p="md"
      withBorder
      radius="sm"
      bg={todo.isCompleted ? "gray.0" : "white"}
    >
      <Group justify="space-between">
        <Group>
          <Checkbox
            checked={todo.isCompleted}
            onChange={() => onToggle(todo)}
            size="md"
          />
          {isEditing ? (
            <TextInput
              value={editText}
              onChange={(e) => setEditText(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  onUpdate(todo.id, editText);
                  setIsEditing(false);
                } else if (e.key === "Escape") {
                  setEditText(todo.text);
                  setIsEditing(false);
                }
              }}
              autoFocus
            />
          ) : (
            <Box>
              <Text
                td={todo.isCompleted ? "line-through" : "none"}
                c={todo.isCompleted ? "dimmed" : "dark"}
                fw={todo.isCompleted ? 400 : 500}
              >
                {todo.text}
              </Text>
            </Box>
          )}
        </Group>
        <Group gap="xs">
          {isEditing ? (
            <>
              <ActionIcon
                color="green"
                variant="light"
                onClick={() => {
                  onUpdate(todo.id, editText);
                  setIsEditing(false);
                }}
              >
                <IconCheck size={16} />
              </ActionIcon>
              <ActionIcon
                color="gray"
                variant="light"
                onClick={() => {
                  setEditText(todo.text);
                  setIsEditing(false);
                }}
              >
                <IconX size={16} />
              </ActionIcon>
            </>
          ) : (
            <>
              <ActionIcon
                color="blue"
                variant="light"
                onClick={() => setIsEditing(true)}
              >
                <IconEdit size={16} />
              </ActionIcon>
              <ActionIcon
                color="red"
                variant="light"
                onClick={() => onDelete(todo.id)}
              >
                <IconTrash size={16} />
              </ActionIcon>
            </>
          )}
        </Group>
      </Group>
    </Paper>
  );
}
