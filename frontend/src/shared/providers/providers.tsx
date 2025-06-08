import { createTheme, MantineProvider } from "@mantine/core";
import UserProfile from "./user/user-provider";

const theme = createTheme({});

export default function Providers({ children }: { children: React.ReactNode }) {
  return (
    <UserProfile>
      <MantineProvider theme={theme}>{children}</MantineProvider>;
    </UserProfile>
  );
}
