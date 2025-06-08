import { Group, TextInput, Button } from "@mantine/core";
import { IconPlus } from "@tabler/icons-react";
import { useState } from "react";

export default function TodoForm({ onAdd }: { onAdd: (text: string) => void }) {
  const [newTodo, setNewTodo] = useState("");

  const handleAdd = () => {
    if (!newTodo.trim()) return;
    onAdd(newTodo);
    setNewTodo("");
  };

  return (
    <Group mb="lg">
      <TextInput
        placeholder="Add a new task..."
        value={newTodo}
        onChange={(e) => setNewTodo(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleAdd()}
        style={{ flex: 1 }}
      />
      <Button onClick={handleAdd} leftSection={<IconPlus size={16} />}>
        Add
      </Button>
    </Group>
  );
}
