import { createTheme, MantineProvider } from "@mantine/core";
import UserProfile from "./auth/user-provider";

const theme = createTheme({});

export default function Providers({ children }: { children: React.ReactNode }) {
  return (
    <UserProfile>
      <MantineProvider theme={theme}>{children}</MantineProvider>;
    </UserProfile>
  );
}
