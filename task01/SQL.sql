Отримати всі завдання певного користувача
SELECT * 
FROM tasks 
WHERE user_id = X;

Вибрати завдання за певним статусом
SELECT * 
FROM tasks 
WHERE status_id = X;

Оновити статус конкретного завданн
UPDATE tasks 
SET status_id = X 
WHERE id = X;

Отримати список користувачів, які не мають жодного завдання
SELECT users.* 
FROM users 
LEFT JOIN tasks ON users.id = tasks.user_id 
WHERE tasks.id IS NULL;

Додати нове завдання для конкретного користувача
INSERT INTO tasks (title, description, status_id, user_id) 
VALUES (A, B, C, D);

Отримати всі завдання, які ще не завершено
SELECT * 
FROM tasks 
WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

Видалити конкретне завдання
DELETE FROM tasks 
WHERE id = X;

Знайти користувачів з певною електронною поштою
SELECT * 
FROM users 
WHERE email LIKE X;

"Оновити ім'я користувача"
UPDATE users 
SET name = X 
WHERE id = X;

Отримати кількість завдань для кожного статусу
SELECT status.name, COUNT(tasks.id) AS task_count
FROM status
LEFT JOIN tasks ON status.id = tasks.status_id
GROUP BY status.name;

Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
SELECT tasks.* 
FROM tasks 
JOIN users ON tasks.user_id = users.id 
WHERE users.email LIKE '%@gmail.com';

Отримати список завдань, що не мають опису
SELECT * 
FROM tasks 
WHERE description IS NULL OR description = '';

Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
SELECT users.name, tasks.title
FROM users
JOIN tasks ON users.id = tasks.user_id
JOIN status ON tasks.status_id = status.id
WHERE status.name = 'in progress';

Отримати користувачів та кількість їхніх завдань
SELECT users.name, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.name;
