-- Exercise 1 (done for you):
SELECT * 
FROM users;



-- Exercise 2 (done for you):
SELECT id, first_name, last_name 
FROM users;



-- Exercise 3
SELECT id, first_name, last_name 
FROM users 
ORDER BY last_name;



-- Exercise 4
SELECT id, user_id, image_url 
FROM posts 
WHERE user_id=26;



-- Exercise 5
SELECT id, user_id, image_url
FROM posts
WHERE user_id=12 OR user_id=26;



-- Exercise 6
SELECT COUNT(*)
FROM posts;



-- Exercise 7
SELECT COUNT(*) 
FROM comments
GROUP BY user_id;

--incorrect, couldn't figure out why it wouldn't order



-- Exercise 8
SELECT posts.id, posts.image_url, posts.user_id 
FROM posts 
INNER JOIN users
ON posts.user_id = users.id
WHERE posts.id=26 OR posts.id=12;

--incorrect, missing columns??



-- Exercise 9
SELECT posts.pub_date, posts.id 
FROM posts 
INNER JOIN following
ON posts.id=26 OR posts.id=12
ORDER BY posts.id ASC;



-- Exercise 10

--optional skip (sorry)


-- Exercise 11
INSERT INTO bookmarks
VALUES (501,26,219), (502,26,220), (503,26,221);



-- Exercise 12
DELETE FROM bookmarks
where id > 500;



-- Exercise 13
UPDATE users
SET email = 'cyoung2022@gmail.com'
WHERE users.id = 26;



-- Exercise 14
