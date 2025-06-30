CREATE TABLE IF NOT EXISTS 'meals' (
   id TEXT PRIMARY KEY,
   name TEXT NOT NULL,
   description TEXT NOT NULL,
   datetime DATETIME NOT NULL,
   is_on_diet INTEGER NOT NULL,
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS 'users' (
   id TEXT PRIMARY KEY,
   name TEXT NOT NULL,
   email TEXT NOT NULL UNIQUE,
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS 'user_meals' (
   id TEXT PRIMARY KEY,
   user_id TEXT NOT NULL,
   meal_id TEXT NOT NULL,
   FOREIGN KEY (user_id) REFERENCES users(id),
   FOREIGN KEY (meal_id) REFERENCES meals(id)
);

CREATE INDEX IF NOT EXISTS idx_meals_datetime ON meals(datetime);

CREATE INDEX IF NOT EXISTS idx_meals_is_on_diet ON meals(is_on_diet);

CREATE INDEX IF NOT EXISTS idx_user_meals_user_id ON user_meals(user_id);

CREATE INDEX IF NOT EXISTS idx_user_meals_meal_id ON user_meals(meal_id);
