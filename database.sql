-- Creación de la tabla user
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    lastPasswordResetRequest DATETIME,
    passwordResetToken VARCHAR(255),
    passwordResetTokenExpires DATETIME,
    passwordResetTokenUsed BOOLEAN,
    passwordHistory JSON,
    isVerified BOOLEAN DEFAULT FALSE,
    verifiedExpires DATETIME,
    verifiedToken VARCHAR(255),
    lastVerifiedRequest DATETIME,
    createdAt TIMESTAMP DEFAULT NOW()
);

-- Creación de la tabla settings
CREATE TABLE settings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT UNIQUE, -- Relación 1:1 con user
    theme VARCHAR(50) DEFAULT "light",
    language VARCHAR(50) DEFAULT "es",
    detailLevel VARCHAR(50) DEFAULT "simplified",
    autoSaveChats BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (userId) REFERENCES user(id)
);

-- Creación de la tabla chat
CREATE TABLE chat (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT, -- Relación 1:N con user
    title VARCHAR(255),
    date DATETIME,
    lastDate DATETIME,
    messages JSON,
    FOREIGN KEY (userId) REFERENCES user(id)
);