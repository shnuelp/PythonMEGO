class User:
    count = 0

    def __init__(self, username):
        self.username = username
        self.followers = []
        self.following = []
        User.count += 1

    def follow(self, other_user):
        self.following.append(other_user.username)
        other_user.followers.append(self.username)

    def __str__(self):
        return f"User: {self.username}\n" \
               f"Followers: {len(self.followers)}\n" \
               f"Followers: {', '.join(self.followers)}" \
               f"Following: {len(self.following)}\n" \
               f"Following: {', '.join(self.following)}\n"

a = User("vxxc")


b = User("tgtrg")
c = User("Weeeeeeee")
d = User("k")

a.follow(b)
a.follow(c)
b.follow(c)

print(a)  # Printing the formatted user information
print(b)
print(c)