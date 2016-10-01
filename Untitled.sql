SELECT * FROM users LEFT JOIN friendship ON users.id = friendship.user_id WHERE users.id = 4
LEFT JOIN users ON friendship.friend_id = users.id 