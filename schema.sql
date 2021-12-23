CREATE USER 'GameAd'@'localhost' IDENTIFIED BY 'password';
CREATE DATABASE BlackHole;
GRANT ALL PRIVILEGES ON BlackHole. * TO 'GameAd'@'localhost';
FLUSH PRIVILEGES;
USE BlackHole;

CREATE TABLE user_info(
    name VARCHAR(50) PRIMARY KEY , 
    password VARCHAR(64) NOT NULL,
    salt VARCHAR(64) NOT NULL,
    gender BIT NOT NULL DEFAULT 0,
    avatar VARCHAR(100),
    level INT NOT NULL DEFAULT 1,
    xp BIGINT NOT NULL DEFAULT 0,
    weekly_xp BIGINT NOT NULL DEFAULT 0,
    wins BIGINT NOT NULL DEFAULT 0,
    games BIGINT NOT NULL DEFAULT 0,
    daily_ch BIGINT NOT NULL DEFAULT 0
);

INSERT INTO user_info(name, password) VALUES("GameAd","password");

CREATE TABLE quotes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    quote VARCHAR(200) NOT NULL
);

INSERT INTO quotes(quote) VALUES
("Shine in your own way"),
("Work hard .. Play harder"),
("Without hustle, talent will only carry you so far."),
("No win without will"),
("The harder you have to try, the more points you deserve!"),
("Welcome back , we are very happy to see you");

