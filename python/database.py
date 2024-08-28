import json
from errors import UsernameAlreadyExistsError


class Database:
    def selectAllUsers(self) -> list:
        with open("./database/users.json", "r", encoding="utf-8") as file:
            data = file.read()
            users = json.loads(data) or []
            return users

    
    def selectUser(self, username: str) -> dict | None:
        users = self.selectAllUsers()
        [user] = list(filter(lambda user: user['username'] == username, users)) or [None]
        
        return user

    
    def login (self, username: str, password: str) -> dict | None:
        users = self.selectAllUsers()
        [user] = list(filter(lambda user: user['username'] == username and user['password'] == password, users)) or [None]
        return user


    def register (self, name: str, surname: str, username: str, password: str):
        foundUser = self.selectUser(username)

        print(foundUser)

        if foundUser:
            raise UsernameAlreadyExistsError("Username band qilingan!")

        USERS = self.selectAllUsers()
        new_users = {
            "id": USERS[-1]['id'] + 1,
            "name": name,
            "surname": surname,
            "username": username,
            "password": password,
        }
        USERS.append(new_users)
        with open("./database/users.json", "w") as file:
            file.write(json.dumps(USERS, indent=4))
    
        return new_users


    def selectAllPosts(self) -> list:
        with open("./database/posts.json", "r", encoding="utf-8") as file:
            data = file.read()
            posts = json.loads(data) or []
            return posts


    def selectUserPosts(self, user_id: int) -> list:
        with open("./database/posts.json", "r", encoding="utf-8") as file:
            data = file.read()
            posts = json.loads(data) or []
            filteredPosts = list(filter(lambda p: p["user_id"] == user_id, posts))
            return filteredPosts
        

    def addPost(self, user_id: int, post_text: str) -> None:
        allPosts = self.selectAllPosts()
        ID = allPosts[-1]["id"] + 1

        allPosts.append({
            "id": ID,
            "user_id": user_id,
            "text": post_text
        })

        with open("./database/posts.json", "w") as file:
            data = json.dumps(allPosts, indent=4)
            file.write(data)