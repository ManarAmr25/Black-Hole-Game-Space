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

INSERT INTO user_info(name, password, salt) VALUES("GameAd","password", "salt");

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


CREATE TABLE game_achievements(
    id INT PRIMARY KEY AUTO_INCREMENT,
    description VARCHAR(500) NOT NULL,
    type VARCHAR(50) NOT NULL,
    goal INT
);

CREATE TABLE player_achievements(
	player_name VARCHAR(50),
    achievement_id INT,
    checked BIT NOT NULL DEFAULT 0,
    PRIMARY KEY(player_name, achievement_id), 
    CONSTRAINT x FOREIGN KEY(achievement_id) REFERENCES game_achievements(id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT y FOREIGN KEY(player_name) REFERENCES user_info(name) ON UPDATE CASCADE ON DELETE CASCADE
);


INSERT INTO game_achievements(description, type, goal) VALUES
("reach 5 xp in this level", "xp", 5),
("win 2 times", "wins", 2),
("reach level 2", "level", 2),
("achieve 2 daily challenges", "daily challenge", 2),
("reach 10 xp in this level", "xp", 10);
