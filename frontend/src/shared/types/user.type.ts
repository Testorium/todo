export type UserType = {
  id: number;
  username: string;
  firstName: string;
  lastName: string;
};

export type UserProviderType = {
  user: UserType | undefined;
};
