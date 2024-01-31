class User:
    count = 0

    def __init__(self, username):
        self.username = username
        self.followers = []
        self.following = []
        User.count += 1

    def follow(self, other_user):
        self.following.append(other_user)
        other_user.followers.append(self)

    def unfollow(self, other_user):
        if other_user not in self.following:
            raise ValueError("User is not already followed.")
        self.following.remove(other_user)
        other_user.followers.remove(self)

    def is_following(self, other_user):
        return other_user in self.following

    def __str__(self):
        followers_list = [follower.username for follower in self.followers]
        following_list = [following.username for following in self.following ]

        return f"User: {self.username}\n" \
               f"Followers: {len(followers_list)} = {' , '.join(followers_list)}\n" \
               f"Following: {len(following_list)} = {' , '.join(following_list)}\n"


a = User("name1")
b = User("name2")
c = User("name3")
d = User("name4")

a.follow(b)
a.follow(c)
b.follow(b)
a.follow(d)
c.follow(a)
d.follow(c)

print(c)
print(a)
print(b)
print(c)
print(d)
