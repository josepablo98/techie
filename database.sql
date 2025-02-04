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
    theme VARCHAR(50),
    language VARCHAR(50),
    detailLevel VARCHAR(50),
    autoSaveChats BOOLEAN,
    FOREIGN KEY (userId) REFERENCES user(id)
);

-- Creación de la tabla chat
CREATE TABLE chat (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT UNIQUE, -- Relación 1:N con user
    date DATETIME,
    messages JSON,
    FOREIGN KEY (userId) REFERENCES user(id)
);

-- Creación de la tabla admin
CREATE TABLE admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT UNIQUE, -- Relación 1:1 con user
    FOREIGN KEY (userId) REFERENCES user(id)
);

-- Creación de la tabla log
CREATE TABLE log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    adminId INT UNIQUE, -- Relación 1:N con admin
    date DATETIME,
    type VARCHAR(255),
    description TEXT,
    FOREIGN KEY (adminId) REFERENCES admin(id)
);