import { Group, Text, Badge } from "@mantine/core";
import { Todo } from "../types";

export default function TodoStats({ todos }: { todos: Todo[] }) {
  const completed = todos.filter((t) => t.isCompleted).length;
  return (
    <Group justify="space-between" mb="lg">
      <Text size="xl" fw={600}>
        My Tasks
      </Text>
      <Badge variant="light" size="lg">
        {completed}/{todos.length} completed
      </Badge>
    </Group>
  );
}
