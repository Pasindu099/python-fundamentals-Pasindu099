-- Drop table if it already exists (for safety)
DROP TABLE IF EXISTS users;

-- Create a 'users' table
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  full_name VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
);

-- Insert some sample data
INSERT INTO users (username, email, full_name)
VALUES
  ('alice', 'alice@example.com', 'Alice Anderson'),
  ('bob', 'bob@example.com', 'Bob Brown'),
  ('charlie', 'charlie@example.com', 'Charlie Clark');
